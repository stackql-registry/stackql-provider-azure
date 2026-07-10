--- 
title: web_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps
  - web
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

Creates, updates, deletes, gets or lists a <code>web_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="web_apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.web_apps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_instance_process_module_slot"
    values={[
        { label: 'get_instance_process_module_slot', value: 'get_instance_process_module_slot' },
        { label: 'list_slot_differences_slot', value: 'list_slot_differences_slot' },
        { label: 'list_instance_process_threads_slot', value: 'list_instance_process_threads_slot' },
        { label: 'get_hybrid_connection_slot', value: 'get_hybrid_connection_slot' },
        { label: 'get_vnet_connection_gateway_slot', value: 'get_vnet_connection_gateway_slot' },
        { label: 'get_instance_process_module', value: 'get_instance_process_module' },
        { label: 'get_process_module_slot', value: 'get_process_module_slot' },
        { label: 'get_triggered_web_job_history_slot', value: 'get_triggered_web_job_history_slot' },
        { label: 'list_slot_differences_from_production', value: 'list_slot_differences_from_production' },
        { label: 'list_backup_status_secrets_slot', value: 'list_backup_status_secrets_slot' },
        { label: 'list_deployment_log_slot', value: 'list_deployment_log_slot' },
        { label: 'list_function_keys_slot', value: 'list_function_keys_slot' },
        { label: 'list_instance_process_threads', value: 'list_instance_process_threads' },
        { label: 'list_instance_processes_slot', value: 'list_instance_processes_slot' },
        { label: 'list_process_threads_slot', value: 'list_process_threads_slot' },
        { label: 'list_network_features_slot', value: 'list_network_features_slot' },
        { label: 'list_triggered_web_job_history_slot', value: 'list_triggered_web_job_history_slot' },
        { label: 'get_network_trace_operation_slot', value: 'get_network_trace_operation_slot' },
        { label: 'get_private_endpoint_connection_slot', value: 'get_private_endpoint_connection_slot' },
        { label: 'get_hybrid_connection', value: 'get_hybrid_connection' },
        { label: 'get_vnet_connection_slot', value: 'get_vnet_connection_slot' },
        { label: 'get_vnet_connection_gateway', value: 'get_vnet_connection_gateway' },
        { label: 'get_app_setting_key_vault_reference_slot', value: 'get_app_setting_key_vault_reference_slot' },
        { label: 'get_site_connection_string_key_vault_reference_slot', value: 'get_site_connection_string_key_vault_reference_slot' },
        { label: 'get_configuration_snapshot_slot', value: 'get_configuration_snapshot_slot' },
        { label: 'get_slot_site_deployment_status_slot', value: 'get_slot_site_deployment_status_slot' },
        { label: 'get_domain_ownership_identifier_slot', value: 'get_domain_ownership_identifier_slot' },
        { label: 'get_host_name_binding_slot', value: 'get_host_name_binding_slot' },
        { label: 'get_relay_service_connection_slot', value: 'get_relay_service_connection_slot' },
        { label: 'get_process_module', value: 'get_process_module' },
        { label: 'get_premier_add_on_slot', value: 'get_premier_add_on_slot' },
        { label: 'get_public_certificate_slot', value: 'get_public_certificate_slot' },
        { label: 'get_site_container_slot', value: 'get_site_container_slot' },
        { label: 'get_site_extension_slot', value: 'get_site_extension_slot' },
        { label: 'get_triggered_web_job_history', value: 'get_triggered_web_job_history' },
        { label: 'get_instance_workflow_slot', value: 'get_instance_workflow_slot' },
        { label: 'list_application_settings_slot', value: 'list_application_settings_slot' },
        { label: 'list_backup_status_secrets', value: 'list_backup_status_secrets' },
        { label: 'list_deployment_log', value: 'list_deployment_log' },
        { label: 'list_function_keys', value: 'list_function_keys' },
        { label: 'list_instance_processes', value: 'list_instance_processes' },
        { label: 'list_process_threads', value: 'list_process_threads' },
        { label: 'list_network_features', value: 'list_network_features' },
        { label: 'list_triggered_web_job_history', value: 'list_triggered_web_job_history' },
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'get_vnet_connection', value: 'get_vnet_connection' },
        { label: 'get_network_trace_operation', value: 'get_network_trace_operation' },
        { label: 'get_app_setting_key_vault_reference', value: 'get_app_setting_key_vault_reference' },
        { label: 'get_site_connection_string_key_vault_reference', value: 'get_site_connection_string_key_vault_reference' },
        { label: 'get_configuration_snapshot', value: 'get_configuration_snapshot' },
        { label: 'get_production_site_deployment_status', value: 'get_production_site_deployment_status' },
        { label: 'get_domain_ownership_identifier', value: 'get_domain_ownership_identifier' },
        { label: 'get_host_name_binding', value: 'get_host_name_binding' },
        { label: 'get_relay_service_connection', value: 'get_relay_service_connection' },
        { label: 'get_premier_add_on', value: 'get_premier_add_on' },
        { label: 'get_public_certificate', value: 'get_public_certificate' },
        { label: 'get_site_container', value: 'get_site_container' },
        { label: 'get_site_extension', value: 'get_site_extension' },
        { label: 'get_workflow', value: 'get_workflow' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_instance_process_module_slot">

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
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>File name.</td>
</tr>
<tr>
    <td><CopyableCode code="base_address" /></td>
    <td><code>string</code></td>
    <td>Base address. Used as module identifier in ARM resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="file_description" /></td>
    <td><code>string</code></td>
    <td>File description.</td>
</tr>
<tr>
    <td><CopyableCode code="file_path" /></td>
    <td><code>string</code></td>
    <td>File path.</td>
</tr>
<tr>
    <td><CopyableCode code="file_version" /></td>
    <td><code>string</code></td>
    <td>File version.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="is_debug" /></td>
    <td><code>boolean</code></td>
    <td>Is debug?.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Module language (locale).</td>
</tr>
<tr>
    <td><CopyableCode code="module_memory_size" /></td>
    <td><code>integer</code></td>
    <td>Module memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Product name.</td>
</tr>
<tr>
    <td><CopyableCode code="product_version" /></td>
    <td><code>string</code></td>
    <td>Product version.</td>
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
<TabItem value="list_slot_differences_slot">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the setting difference.</td>
</tr>
<tr>
    <td><CopyableCode code="diffRule" /></td>
    <td><code>string</code></td>
    <td>Rule that describes how to process the setting difference during a slot swap.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level of the difference: Information, Warning or Error.</td>
</tr>
<tr>
    <td><CopyableCode code="settingName" /></td>
    <td><code>string</code></td>
    <td>Name of the setting.</td>
</tr>
<tr>
    <td><CopyableCode code="settingType" /></td>
    <td><code>string</code></td>
    <td>The type of the setting: General, AppSetting or ConnectionString.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="valueInCurrentSlot" /></td>
    <td><code>string</code></td>
    <td>Value of the setting in the current slot.</td>
</tr>
<tr>
    <td><CopyableCode code="valueInTargetSlot" /></td>
    <td><code>string</code></td>
    <td>Value of the setting in the target slot.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_instance_process_threads_slot">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="base_priority" /></td>
    <td><code>integer</code></td>
    <td>Base priority.</td>
</tr>
<tr>
    <td><CopyableCode code="current_priority" /></td>
    <td><code>integer</code></td>
    <td>Current thread priority.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>integer</code></td>
    <td>Site extension ID.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="priority_level" /></td>
    <td><code>string</code></td>
    <td>Thread priority level.</td>
</tr>
<tr>
    <td><CopyableCode code="process" /></td>
    <td><code>string</code></td>
    <td>Process URI.</td>
</tr>
<tr>
    <td><CopyableCode code="start_address" /></td>
    <td><code>string</code></td>
    <td>Start address.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Thread state.</td>
</tr>
<tr>
    <td><CopyableCode code="total_processor_time" /></td>
    <td><code>string</code></td>
    <td>Total processor time.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="user_processor_time" /></td>
    <td><code>string</code></td>
    <td>User processor time.</td>
</tr>
<tr>
    <td><CopyableCode code="wait_reason" /></td>
    <td><code>string</code></td>
    <td>Wait reason.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_hybrid_connection_slot">

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
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname of the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port of the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="relayArmUri" /></td>
    <td><code>string</code></td>
    <td>The ARM URI to the Service Bus relay.</td>
</tr>
<tr>
    <td><CopyableCode code="relayName" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus relay.</td>
</tr>
<tr>
    <td><CopyableCode code="sendKeyName" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus key which has Send permissions. This is used to authenticate to Service Bus.</td>
</tr>
<tr>
    <td><CopyableCode code="sendKeyValue" /></td>
    <td><code>string</code></td>
    <td>The value of the Service Bus key. This is used to authenticate to Service Bus. In ARM this key will not be returned normally, use the POST /listKeys API instead.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusNamespace" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusSuffix" /></td>
    <td><code>string</code></td>
    <td>The suffix for the service bus endpoint. By default this is .servicebus.windows.net.</td>
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
<TabItem value="get_vnet_connection_gateway_slot">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<tr>
    <td><CopyableCode code="vnetName" /></td>
    <td><code>string</code></td>
    <td>The Virtual Network name.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnPackageUri" /></td>
    <td><code>string</code></td>
    <td>The URI where the VPN package can be downloaded. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_instance_process_module">

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
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>File name.</td>
</tr>
<tr>
    <td><CopyableCode code="base_address" /></td>
    <td><code>string</code></td>
    <td>Base address. Used as module identifier in ARM resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="file_description" /></td>
    <td><code>string</code></td>
    <td>File description.</td>
</tr>
<tr>
    <td><CopyableCode code="file_path" /></td>
    <td><code>string</code></td>
    <td>File path.</td>
</tr>
<tr>
    <td><CopyableCode code="file_version" /></td>
    <td><code>string</code></td>
    <td>File version.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="is_debug" /></td>
    <td><code>boolean</code></td>
    <td>Is debug?.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Module language (locale).</td>
</tr>
<tr>
    <td><CopyableCode code="module_memory_size" /></td>
    <td><code>integer</code></td>
    <td>Module memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Product name.</td>
</tr>
<tr>
    <td><CopyableCode code="product_version" /></td>
    <td><code>string</code></td>
    <td>Product version.</td>
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
<TabItem value="get_process_module_slot">

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
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>File name.</td>
</tr>
<tr>
    <td><CopyableCode code="base_address" /></td>
    <td><code>string</code></td>
    <td>Base address. Used as module identifier in ARM resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="file_description" /></td>
    <td><code>string</code></td>
    <td>File description.</td>
</tr>
<tr>
    <td><CopyableCode code="file_path" /></td>
    <td><code>string</code></td>
    <td>File path.</td>
</tr>
<tr>
    <td><CopyableCode code="file_version" /></td>
    <td><code>string</code></td>
    <td>File version.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="is_debug" /></td>
    <td><code>boolean</code></td>
    <td>Is debug?.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Module language (locale).</td>
</tr>
<tr>
    <td><CopyableCode code="module_memory_size" /></td>
    <td><code>integer</code></td>
    <td>Module memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Product name.</td>
</tr>
<tr>
    <td><CopyableCode code="product_version" /></td>
    <td><code>string</code></td>
    <td>Product version.</td>
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
<TabItem value="get_triggered_web_job_history_slot">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="runs" /></td>
    <td><code>array</code></td>
    <td>List of triggered web job runs.</td>
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
<TabItem value="list_slot_differences_from_production">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the setting difference.</td>
</tr>
<tr>
    <td><CopyableCode code="diffRule" /></td>
    <td><code>string</code></td>
    <td>Rule that describes how to process the setting difference during a slot swap.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level of the difference: Information, Warning or Error.</td>
</tr>
<tr>
    <td><CopyableCode code="settingName" /></td>
    <td><code>string</code></td>
    <td>Name of the setting.</td>
</tr>
<tr>
    <td><CopyableCode code="settingType" /></td>
    <td><code>string</code></td>
    <td>The type of the setting: General, AppSetting or ConnectionString.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="valueInCurrentSlot" /></td>
    <td><code>string</code></td>
    <td>Value of the setting in the current slot.</td>
</tr>
<tr>
    <td><CopyableCode code="valueInTargetSlot" /></td>
    <td><code>string</code></td>
    <td>Value of the setting in the target slot.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_backup_status_secrets_slot">

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
    <td><CopyableCode code="blobName" /></td>
    <td><code>string</code></td>
    <td>Name of the blob which contains data for this backup.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Unique correlation identifier. Please use this along with the timestamp while communicating with Azure support.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the backup creation.</td>
</tr>
<tr>
    <td><CopyableCode code="databases" /></td>
    <td><code>array</code></td>
    <td>List of databases included in the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="finishedTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this backup finished.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRestoreTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of a last restore operation which used this backup.</td>
</tr>
<tr>
    <td><CopyableCode code="log" /></td>
    <td><code>string</code></td>
    <td>Details regarding this backup. Might contain an error message.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduled" /></td>
    <td><code>boolean</code></td>
    <td>True if this backup has been created due to a schedule being triggered.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Size of the backup in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Backup status. Known values are: "InProgress", "Failed", "Succeeded", "TimedOut", "Created", "Skipped", "PartiallySucceeded", "DeleteInProgress", "DeleteFailed", and "Deleted". (InProgress, Failed, Succeeded, TimedOut, Created, Skipped, PartiallySucceeded, DeleteInProgress, DeleteFailed, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountUrl" /></td>
    <td><code>string</code></td>
    <td>SAS URL for the storage account container which contains this backup.</td>
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
<tr>
    <td><CopyableCode code="websiteSizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Size of the original web app which has been backed up.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_deployment_log_slot">

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
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>True if deployment is currently active, false if completed and null if not started.</td>
</tr>
<tr>
    <td><CopyableCode code="author" /></td>
    <td><code>string</code></td>
    <td>Who authored the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="author_email" /></td>
    <td><code>string</code></td>
    <td>Author email.</td>
</tr>
<tr>
    <td><CopyableCode code="deployer" /></td>
    <td><code>string</code></td>
    <td>Who performed the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>string</code></td>
    <td>Details on deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="end_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Details about deployment status.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>integer</code></td>
    <td>Deployment status.</td>
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
<TabItem value="list_function_keys_slot">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_instance_process_threads">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="base_priority" /></td>
    <td><code>integer</code></td>
    <td>Base priority.</td>
</tr>
<tr>
    <td><CopyableCode code="current_priority" /></td>
    <td><code>integer</code></td>
    <td>Current thread priority.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>integer</code></td>
    <td>Site extension ID.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="priority_level" /></td>
    <td><code>string</code></td>
    <td>Thread priority level.</td>
</tr>
<tr>
    <td><CopyableCode code="process" /></td>
    <td><code>string</code></td>
    <td>Process URI.</td>
</tr>
<tr>
    <td><CopyableCode code="start_address" /></td>
    <td><code>string</code></td>
    <td>Start address.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Thread state.</td>
</tr>
<tr>
    <td><CopyableCode code="total_processor_time" /></td>
    <td><code>string</code></td>
    <td>Total processor time.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="user_processor_time" /></td>
    <td><code>string</code></td>
    <td>User processor time.</td>
</tr>
<tr>
    <td><CopyableCode code="wait_reason" /></td>
    <td><code>string</code></td>
    <td>Wait reason.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_instance_processes_slot">

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
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>Deployment name.</td>
</tr>
<tr>
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>File name of this process.</td>
</tr>
<tr>
    <td><CopyableCode code="user_name" /></td>
    <td><code>string</code></td>
    <td>User name.</td>
</tr>
<tr>
    <td><CopyableCode code="children" /></td>
    <td><code>array</code></td>
    <td>Child process list.</td>
</tr>
<tr>
    <td><CopyableCode code="command_line" /></td>
    <td><code>string</code></td>
    <td>Command line.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of process.</td>
</tr>
<tr>
    <td><CopyableCode code="environment_variables" /></td>
    <td><code>object</code></td>
    <td>List of environment variables.</td>
</tr>
<tr>
    <td><CopyableCode code="handle_count" /></td>
    <td><code>integer</code></td>
    <td>Handle count.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>integer</code></td>
    <td>ARM Identifier for deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="iis_profile_timeout_in_seconds" /></td>
    <td><code>number</code></td>
    <td>IIS Profile timeout (seconds).</td>
</tr>
<tr>
    <td><CopyableCode code="is_iis_profile_running" /></td>
    <td><code>boolean</code></td>
    <td>Is the IIS Profile running?.</td>
</tr>
<tr>
    <td><CopyableCode code="is_profile_running" /></td>
    <td><code>boolean</code></td>
    <td>Is profile running?.</td>
</tr>
<tr>
    <td><CopyableCode code="is_scm_site" /></td>
    <td><code>boolean</code></td>
    <td>Is this the SCM site?.</td>
</tr>
<tr>
    <td><CopyableCode code="is_webjob" /></td>
    <td><code>boolean</code></td>
    <td>Is this a Web Job?.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="minidump" /></td>
    <td><code>string</code></td>
    <td>Minidump URI.</td>
</tr>
<tr>
    <td><CopyableCode code="module_count" /></td>
    <td><code>integer</code></td>
    <td>Module count.</td>
</tr>
<tr>
    <td><CopyableCode code="modules" /></td>
    <td><code>array</code></td>
    <td>List of modules.</td>
</tr>
<tr>
    <td><CopyableCode code="non_paged_system_memory" /></td>
    <td><code>integer</code></td>
    <td>Non-paged system memory.</td>
</tr>
<tr>
    <td><CopyableCode code="open_file_handles" /></td>
    <td><code>array</code></td>
    <td>List of open files.</td>
</tr>
<tr>
    <td><CopyableCode code="paged_memory" /></td>
    <td><code>integer</code></td>
    <td>Paged memory.</td>
</tr>
<tr>
    <td><CopyableCode code="paged_system_memory" /></td>
    <td><code>integer</code></td>
    <td>Paged system memory.</td>
</tr>
<tr>
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Parent process.</td>
</tr>
<tr>
    <td><CopyableCode code="peak_paged_memory" /></td>
    <td><code>integer</code></td>
    <td>Peak paged memory.</td>
</tr>
<tr>
    <td><CopyableCode code="peak_virtual_memory" /></td>
    <td><code>integer</code></td>
    <td>Peak virtual memory usage.</td>
</tr>
<tr>
    <td><CopyableCode code="peak_working_set" /></td>
    <td><code>integer</code></td>
    <td>Peak working set.</td>
</tr>
<tr>
    <td><CopyableCode code="private_memory" /></td>
    <td><code>integer</code></td>
    <td>Private memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="privileged_cpu_time" /></td>
    <td><code>string</code></td>
    <td>Privileged CPU time.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thread_count" /></td>
    <td><code>integer</code></td>
    <td>Thread count.</td>
</tr>
<tr>
    <td><CopyableCode code="threads" /></td>
    <td><code>array</code></td>
    <td>Thread list.</td>
</tr>
<tr>
    <td><CopyableCode code="time_stamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time stamp.</td>
</tr>
<tr>
    <td><CopyableCode code="total_cpu_time" /></td>
    <td><code>string</code></td>
    <td>Total CPU time.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="user_cpu_time" /></td>
    <td><code>string</code></td>
    <td>User CPU time.</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_memory" /></td>
    <td><code>integer</code></td>
    <td>Virtual memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="working_set" /></td>
    <td><code>integer</code></td>
    <td>Working set.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_process_threads_slot">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="base_priority" /></td>
    <td><code>integer</code></td>
    <td>Base priority.</td>
</tr>
<tr>
    <td><CopyableCode code="current_priority" /></td>
    <td><code>integer</code></td>
    <td>Current thread priority.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>integer</code></td>
    <td>Site extension ID.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="priority_level" /></td>
    <td><code>string</code></td>
    <td>Thread priority level.</td>
</tr>
<tr>
    <td><CopyableCode code="process" /></td>
    <td><code>string</code></td>
    <td>Process URI.</td>
</tr>
<tr>
    <td><CopyableCode code="start_address" /></td>
    <td><code>string</code></td>
    <td>Start address.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Thread state.</td>
</tr>
<tr>
    <td><CopyableCode code="total_processor_time" /></td>
    <td><code>string</code></td>
    <td>Total processor time.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="user_processor_time" /></td>
    <td><code>string</code></td>
    <td>User processor time.</td>
</tr>
<tr>
    <td><CopyableCode code="wait_reason" /></td>
    <td><code>string</code></td>
    <td>Wait reason.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_network_features_slot">

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
    <td><CopyableCode code="hybridConnections" /></td>
    <td><code>array</code></td>
    <td>The Hybrid Connections summary view.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridConnectionsV2" /></td>
    <td><code>array</code></td>
    <td>The Hybrid Connection V2 (Service Bus) view.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<tr>
    <td><CopyableCode code="virtualNetworkConnection" /></td>
    <td><code>object</code></td>
    <td>The Virtual Network summary view.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkName" /></td>
    <td><code>string</code></td>
    <td>The Virtual Network name.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_triggered_web_job_history_slot">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="runs" /></td>
    <td><code>array</code></td>
    <td>List of triggered web job runs.</td>
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
<TabItem value="get_network_trace_operation_slot">

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
    <td>Detailed message of a network trace operation, e.g. error message in case of failure.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Local file path for the captured network trace file.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of the network trace operation, same as Operation.Status (InProgress/Succeeded/Failed).</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_private_endpoint_connection_slot">

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
    <td><CopyableCode code="ipAddresses" /></td>
    <td><code>array</code></td>
    <td>Private IPAddresses mapped to the remote private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>PrivateEndpoint of a remote private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>The state of a private link connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>:vartype provisioning_state: str</td>
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
<TabItem value="get_hybrid_connection">

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
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>The hostname of the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port of the endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="relayArmUri" /></td>
    <td><code>string</code></td>
    <td>The ARM URI to the Service Bus relay.</td>
</tr>
<tr>
    <td><CopyableCode code="relayName" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus relay.</td>
</tr>
<tr>
    <td><CopyableCode code="sendKeyName" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus key which has Send permissions. This is used to authenticate to Service Bus.</td>
</tr>
<tr>
    <td><CopyableCode code="sendKeyValue" /></td>
    <td><code>string</code></td>
    <td>The value of the Service Bus key. This is used to authenticate to Service Bus. In ARM this key will not be returned normally, use the POST /listKeys API instead.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusNamespace" /></td>
    <td><code>string</code></td>
    <td>The name of the Service Bus namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceBusSuffix" /></td>
    <td><code>string</code></td>
    <td>The suffix for the service bus endpoint. By default this is .servicebus.windows.net.</td>
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
<TabItem value="get_vnet_connection_slot">

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
    <td><CopyableCode code="certBlob" /></td>
    <td><code>string</code></td>
    <td>A certificate file (.cer) blob containing the public key of the private key used to authenticate a \nPoint-To-Site VPN connection.</td>
</tr>
<tr>
    <td><CopyableCode code="certThumbprint" /></td>
    <td><code>string</code></td>
    <td>The client certificate thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServers" /></td>
    <td><code>string</code></td>
    <td>DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="isSwift" /></td>
    <td><code>boolean</code></td>
    <td>Flag that is used to denote if this is VNET injection.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resyncRequired" /></td>
    <td><code>boolean</code></td>
    <td>true if a resync is required; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>The routes that this Virtual Network connection uses.</td>
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
<tr>
    <td><CopyableCode code="vnetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Virtual Network's resource ID.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_vnet_connection_gateway">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<tr>
    <td><CopyableCode code="vnetName" /></td>
    <td><code>string</code></td>
    <td>The Virtual Network name.</td>
</tr>
<tr>
    <td><CopyableCode code="vpnPackageUri" /></td>
    <td><code>string</code></td>
    <td>The URI where the VPN package can be downloaded. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_app_setting_key_vault_reference_slot">

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
    <td><CopyableCode code="activeVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype active_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>string</code></td>
    <td>:vartype details: str</td>
</tr>
<tr>
    <td><CopyableCode code="identityType" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="reference" /></td>
    <td><code>string</code></td>
    <td>:vartype reference: str</td>
</tr>
<tr>
    <td><CopyableCode code="secretName" /></td>
    <td><code>string</code></td>
    <td>:vartype secret_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="secretVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype secret_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Default value is "KeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Initialized", "Resolved", "InvalidSyntax", "MSINotEnabled", "VaultNotFound", "SecretNotFound", "SecretVersionNotFound", "AccessToKeyVaultDenied", "OtherReasons", "FetchTimedOut", and "UnauthorizedClient". (Initialized, Resolved, InvalidSyntax, MSINotEnabled, VaultNotFound, SecretNotFound, SecretVersionNotFound, AccessToKeyVaultDenied, OtherReasons, FetchTimedOut, UnauthorizedClient)</td>
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
<tr>
    <td><CopyableCode code="vaultName" /></td>
    <td><code>string</code></td>
    <td>:vartype vault_name: str</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_site_connection_string_key_vault_reference_slot">

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
    <td><CopyableCode code="activeVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype active_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>string</code></td>
    <td>:vartype details: str</td>
</tr>
<tr>
    <td><CopyableCode code="identityType" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="reference" /></td>
    <td><code>string</code></td>
    <td>:vartype reference: str</td>
</tr>
<tr>
    <td><CopyableCode code="secretName" /></td>
    <td><code>string</code></td>
    <td>:vartype secret_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="secretVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype secret_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Default value is "KeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Initialized", "Resolved", "InvalidSyntax", "MSINotEnabled", "VaultNotFound", "SecretNotFound", "SecretVersionNotFound", "AccessToKeyVaultDenied", "OtherReasons", "FetchTimedOut", and "UnauthorizedClient". (Initialized, Resolved, InvalidSyntax, MSINotEnabled, VaultNotFound, SecretNotFound, SecretVersionNotFound, AccessToKeyVaultDenied, OtherReasons, FetchTimedOut, UnauthorizedClient)</td>
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
<tr>
    <td><CopyableCode code="vaultName" /></td>
    <td><code>string</code></td>
    <td>:vartype vault_name: str</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_configuration_snapshot_slot">

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
    <td><CopyableCode code="acrUseManagedIdentityCreds" /></td>
    <td><code>boolean</code></td>
    <td>Flag to use Managed Identity Creds for ACR pull.</td>
</tr>
<tr>
    <td><CopyableCode code="acrUserManagedIdentityID" /></td>
    <td><code>string</code></td>
    <td>If using user managed identity, the user managed identity ClientId.</td>
</tr>
<tr>
    <td><CopyableCode code="alwaysOn" /></td>
    <td><code>boolean</code></td>
    <td>true if Always On is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="apiDefinition" /></td>
    <td><code>object</code></td>
    <td>Information about the formal API definition for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="apiManagementConfig" /></td>
    <td><code>object</code></td>
    <td>Azure API management settings linked to the app.</td>
</tr>
<tr>
    <td><CopyableCode code="appCommandLine" /></td>
    <td><code>string</code></td>
    <td>App command line to launch.</td>
</tr>
<tr>
    <td><CopyableCode code="appSettings" /></td>
    <td><code>array</code></td>
    <td>Application settings. This property is not returned in response to normal create and read requests since it may contain sensitive information.</td>
</tr>
<tr>
    <td><CopyableCode code="autoHealEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if Auto Heal is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="autoHealRules" /></td>
    <td><code>object</code></td>
    <td>Auto Heal rules.</td>
</tr>
<tr>
    <td><CopyableCode code="autoSwapSlotName" /></td>
    <td><code>string</code></td>
    <td>Auto-swap slot name.</td>
</tr>
<tr>
    <td><CopyableCode code="azureStorageAccounts" /></td>
    <td><code>object</code></td>
    <td>List of Azure Storage Accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStrings" /></td>
    <td><code>array</code></td>
    <td>Connection strings. This property is not returned in response to normal create and read requests since it may contain sensitive information.</td>
</tr>
<tr>
    <td><CopyableCode code="cors" /></td>
    <td><code>object</code></td>
    <td>Cross-Origin Resource Sharing (CORS) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDocuments" /></td>
    <td><code>array</code></td>
    <td>Default documents.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedErrorLoggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if detailed error logging is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="documentRoot" /></td>
    <td><code>string</code></td>
    <td>Document root.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticWebAppScaleLimit" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of workers that a site can scale out to. This setting only applies to apps in plans where ElasticScaleEnabled is true.</td>
</tr>
<tr>
    <td><CopyableCode code="experiments" /></td>
    <td><code>object</code></td>
    <td>This is work around for polymorphic types.</td>
</tr>
<tr>
    <td><CopyableCode code="ftpsState" /></td>
    <td><code>string</code></td>
    <td>State of FTP / FTPS service. Known values are: "AllAllowed", "FtpsOnly", and "Disabled". (AllAllowed, FtpsOnly, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppScaleLimit" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of workers that a site can scale out to. This setting only applies to the Consumption and Elastic Premium Plans.</td>
</tr>
<tr>
    <td><CopyableCode code="functionsRuntimeScaleMonitoringEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether functions runtime scale monitoring is enabled. When enabled, the ScaleController will not monitor event sources directly, but will instead call to the runtime to get scale status.</td>
</tr>
<tr>
    <td><CopyableCode code="handlerMappings" /></td>
    <td><code>array</code></td>
    <td>Handler mappings.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckPath" /></td>
    <td><code>string</code></td>
    <td>Health check path.</td>
</tr>
<tr>
    <td><CopyableCode code="http20Enabled" /></td>
    <td><code>boolean</code></td>
    <td>Http20Enabled: configures a web site to allow clients to connect over http2.0.</td>
</tr>
<tr>
    <td><CopyableCode code="http20ProxyFlag" /></td>
    <td><code>integer</code></td>
    <td>Http20ProxyFlag: Configures a website to allow http2.0 to pass be proxied all the way to the app. 0 = disabled, 1 = pass through all http2 traffic, 2 = pass through gRPC only.</td>
</tr>
<tr>
    <td><CopyableCode code="httpLoggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if HTTP logging is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="ipSecurityRestrictions" /></td>
    <td><code>array</code></td>
    <td>IP security restrictions for main.</td>
</tr>
<tr>
    <td><CopyableCode code="ipSecurityRestrictionsDefaultAction" /></td>
    <td><code>string</code></td>
    <td>Default action for main access restriction if no rules are matched. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="javaContainer" /></td>
    <td><code>string</code></td>
    <td>Java container.</td>
</tr>
<tr>
    <td><CopyableCode code="javaContainerVersion" /></td>
    <td><code>string</code></td>
    <td>Java container version.</td>
</tr>
<tr>
    <td><CopyableCode code="javaVersion" /></td>
    <td><code>string</code></td>
    <td>Java version.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReferenceIdentity" /></td>
    <td><code>string</code></td>
    <td>Identity to use for Key Vault Reference authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="limits" /></td>
    <td><code>object</code></td>
    <td>Site limits.</td>
</tr>
<tr>
    <td><CopyableCode code="linuxFxVersion" /></td>
    <td><code>string</code></td>
    <td>Linux App Framework and version.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancing" /></td>
    <td><code>string</code></td>
    <td>Site load balancing. Known values are: "WeightedRoundRobin", "LeastRequests", "LeastResponseTime", "WeightedTotalTraffic", "RequestHash", "PerSiteRoundRobin", and "LeastRequestsWithTieBreaker". (WeightedRoundRobin, LeastRequests, LeastResponseTime, WeightedTotalTraffic, RequestHash, PerSiteRoundRobin, LeastRequestsWithTieBreaker)</td>
</tr>
<tr>
    <td><CopyableCode code="localMySqlEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable local MySQL; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="logsDirectorySizeLimit" /></td>
    <td><code>integer</code></td>
    <td>HTTP logs directory size limit.</td>
</tr>
<tr>
    <td><CopyableCode code="machineKey" /></td>
    <td><code>object</code></td>
    <td>Site MachineKey.</td>
</tr>
<tr>
    <td><CopyableCode code="managedPipelineMode" /></td>
    <td><code>string</code></td>
    <td>Managed pipeline mode. Known values are: "Integrated" and "Classic". (Integrated, Classic)</td>
</tr>
<tr>
    <td><CopyableCode code="managedServiceIdentityId" /></td>
    <td><code>integer</code></td>
    <td>Managed Service Identity Id.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>Application metadata. This property cannot be retrieved, since it may contain secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="minTlsCipherSuite" /></td>
    <td><code>string</code></td>
    <td>The minimum strength TLS cipher suite allowed for an application. Known values are: "TLS_AES_256_GCM_SHA384", "TLS_AES_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA", "TLS_RSA_WITH_AES_256_GCM_SHA384", "TLS_RSA_WITH_AES_128_GCM_SHA256", "TLS_RSA_WITH_AES_256_CBC_SHA256", "TLS_RSA_WITH_AES_128_CBC_SHA256", "TLS_RSA_WITH_AES_256_CBC_SHA", and "TLS_RSA_WITH_AES_128_CBC_SHA". (TLS_AES_256_GCM_SHA384, TLS_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA)</td>
</tr>
<tr>
    <td><CopyableCode code="minTlsVersion" /></td>
    <td><code>string</code></td>
    <td>MinTlsVersion: configures the minimum version of TLS required for SSL requests. Known values are: "1.0", "1.1", "1.2", and "1.3". (1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="minimumElasticInstanceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of minimum instance count for a site This setting only applies to the Elastic Plans.</td>
</tr>
<tr>
    <td><CopyableCode code="netFrameworkVersion" /></td>
    <td><code>string</code></td>
    <td>.NET Framework version.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeVersion" /></td>
    <td><code>string</code></td>
    <td>Version of Node.js.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>Number of workers.</td>
</tr>
<tr>
    <td><CopyableCode code="phpVersion" /></td>
    <td><code>string</code></td>
    <td>Version of PHP.</td>
</tr>
<tr>
    <td><CopyableCode code="powerShellVersion" /></td>
    <td><code>string</code></td>
    <td>Version of PowerShell.</td>
</tr>
<tr>
    <td><CopyableCode code="preWarmedInstanceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of preWarmed instances. This setting only applies to the Consumption and Elastic Plans.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to allow or block all public traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="publishingUsername" /></td>
    <td><code>string</code></td>
    <td>Publishing user name.</td>
</tr>
<tr>
    <td><CopyableCode code="push" /></td>
    <td><code>object</code></td>
    <td>Push endpoint settings.</td>
</tr>
<tr>
    <td><CopyableCode code="pythonVersion" /></td>
    <td><code>string</code></td>
    <td>Version of Python.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteDebuggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if remote debugging is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteDebuggingVersion" /></td>
    <td><code>string</code></td>
    <td>Remote debugging version.</td>
</tr>
<tr>
    <td><CopyableCode code="requestTracingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if request tracing is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="requestTracingExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Request tracing expiration time.</td>
</tr>
<tr>
    <td><CopyableCode code="scmIpSecurityRestrictions" /></td>
    <td><code>array</code></td>
    <td>IP security restrictions for scm.</td>
</tr>
<tr>
    <td><CopyableCode code="scmIpSecurityRestrictionsDefaultAction" /></td>
    <td><code>string</code></td>
    <td>Default action for scm access restriction if no rules are matched. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="scmIpSecurityRestrictionsUseMain" /></td>
    <td><code>boolean</code></td>
    <td>IP security restrictions for scm to use main.</td>
</tr>
<tr>
    <td><CopyableCode code="scmMinTlsVersion" /></td>
    <td><code>string</code></td>
    <td>ScmMinTlsVersion: configures the minimum version of TLS required for SSL requests for SCM site. Known values are: "1.0", "1.1", "1.2", and "1.3". (1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="scmType" /></td>
    <td><code>string</code></td>
    <td>SCM type. Known values are: "None", "Dropbox", "Tfs", "LocalGit", "GitHub", "CodePlexGit", "CodePlexHg", "BitbucketGit", "BitbucketHg", "ExternalGit", "ExternalHg", "OneDrive", "VSO", and "VSTSRM". (None, Dropbox, Tfs, LocalGit, GitHub, CodePlexGit, CodePlexHg, BitbucketGit, BitbucketHg, ExternalGit, ExternalHg, OneDrive, VSO, VSTSRM)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tracingOptions" /></td>
    <td><code>string</code></td>
    <td>Tracing options.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="use32BitWorkerProcess" /></td>
    <td><code>boolean</code></td>
    <td>true to use 32-bit worker process; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplications" /></td>
    <td><code>array</code></td>
    <td>Virtual applications.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetName" /></td>
    <td><code>string</code></td>
    <td>Virtual Network name.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetPrivatePortsCount" /></td>
    <td><code>integer</code></td>
    <td>The number of private ports assigned to this app. These will be assigned dynamically on runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetRouteAllEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Virtual Network Route All enabled. This causes all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied.</td>
</tr>
<tr>
    <td><CopyableCode code="webSocketsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if WebSocket is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="websiteTimeZone" /></td>
    <td><code>string</code></td>
    <td>Sets the time zone a site uses for generating timestamps. Compatible with Linux and Windows App Service. Setting the WEBSITE_TIME_ZONE app setting takes precedence over this config. For Linux, expects tz database values `https://www.iana.org/time-zones `_ (for a quick reference see `https://en.wikipedia.org/wiki/List_of_tz_database_time_zones `_). For Windows, expects one of the time zones listed under HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones.</td>
</tr>
<tr>
    <td><CopyableCode code="windowsFxVersion" /></td>
    <td><code>string</code></td>
    <td>Xenon App Framework and version.</td>
</tr>
<tr>
    <td><CopyableCode code="xManagedServiceIdentityId" /></td>
    <td><code>integer</code></td>
    <td>Explicit Managed Service Identity Id.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_slot_site_deployment_status_slot">

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
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation id.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>List of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="failedInstancesLogs" /></td>
    <td><code>array</code></td>
    <td>List of URLs pointing to logs for instances which failed to provision.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInstancesFailed" /></td>
    <td><code>integer</code></td>
    <td>Number of site instances failed to provision.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInstancesInProgress" /></td>
    <td><code>integer</code></td>
    <td>Number of site instances currently being provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInstancesSuccessful" /></td>
    <td><code>integer</code></td>
    <td>Number of site instances provisioned successfully.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Deployment build status. Known values are: "TimedOut", "RuntimeFailed", "BuildAborted", "BuildFailed", "BuildRequestReceived", "BuildPending", "BuildInProgress", "BuildSuccessful", "PostBuildRestartRequired", "StartPolling", "StartPollingWithRestart", "RuntimeStarting", and "RuntimeSuccessful". (TimedOut, RuntimeFailed, BuildAborted, BuildFailed, BuildRequestReceived, BuildPending, BuildInProgress, BuildSuccessful, PostBuildRestartRequired, StartPolling, StartPollingWithRestart, RuntimeStarting, RuntimeSuccessful)</td>
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
<TabItem value="get_domain_ownership_identifier_slot">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<TabItem value="get_host_name_binding_slot">

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
    <td><CopyableCode code="azureResourceName" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="azureResourceType" /></td>
    <td><code>string</code></td>
    <td>Azure resource type. Known values are: "Website" and "TrafficManager". (Website, TrafficManager)</td>
</tr>
<tr>
    <td><CopyableCode code="customHostNameDnsRecordType" /></td>
    <td><code>string</code></td>
    <td>Custom DNS record type. Known values are: "CName" and "A". (CName, A)</td>
</tr>
<tr>
    <td><CopyableCode code="domainId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified ARM domain resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNameType" /></td>
    <td><code>string</code></td>
    <td>Hostname type. Known values are: "Verified" and "Managed". (Verified, Managed)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>App Service app name.</td>
</tr>
<tr>
    <td><CopyableCode code="sslState" /></td>
    <td><code>string</code></td>
    <td>SSL type. Known values are: "Disabled", "SniEnabled", and "IpBasedEnabled". (Disabled, SniEnabled, IpBasedEnabled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>SSL certificate thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualIP" /></td>
    <td><code>string</code></td>
    <td>Virtual IP address assigned to the hostname if IP based SSL is enabled.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_relay_service_connection_slot">

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
    <td><CopyableCode code="biztalkUri" /></td>
    <td><code>string</code></td>
    <td>:vartype biztalk_uri: str</td>
</tr>
<tr>
    <td><CopyableCode code="entityConnectionString" /></td>
    <td><code>string</code></td>
    <td>:vartype entity_connection_string: str</td>
</tr>
<tr>
    <td><CopyableCode code="entityName" /></td>
    <td><code>string</code></td>
    <td>:vartype entity_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>:vartype hostname: str</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>:vartype port: int</td>
</tr>
<tr>
    <td><CopyableCode code="resourceConnectionString" /></td>
    <td><code>string</code></td>
    <td>:vartype resource_connection_string: str</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>:vartype resource_type: str</td>
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
<TabItem value="get_process_module">

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
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>File name.</td>
</tr>
<tr>
    <td><CopyableCode code="base_address" /></td>
    <td><code>string</code></td>
    <td>Base address. Used as module identifier in ARM resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="file_description" /></td>
    <td><code>string</code></td>
    <td>File description.</td>
</tr>
<tr>
    <td><CopyableCode code="file_path" /></td>
    <td><code>string</code></td>
    <td>File path.</td>
</tr>
<tr>
    <td><CopyableCode code="file_version" /></td>
    <td><code>string</code></td>
    <td>File version.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="is_debug" /></td>
    <td><code>boolean</code></td>
    <td>Is debug?.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>Module language (locale).</td>
</tr>
<tr>
    <td><CopyableCode code="module_memory_size" /></td>
    <td><code>integer</code></td>
    <td>Module memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Product name.</td>
</tr>
<tr>
    <td><CopyableCode code="product_version" /></td>
    <td><code>string</code></td>
    <td>Product version.</td>
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
<TabItem value="get_premier_add_on_slot">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceOffer" /></td>
    <td><code>string</code></td>
    <td>Premier add on Marketplace offer.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplacePublisher" /></td>
    <td><code>string</code></td>
    <td>Premier add on Marketplace publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Premier add on Product.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Premier add on SKU.</td>
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
<tr>
    <td><CopyableCode code="vendor" /></td>
    <td><code>string</code></td>
    <td>Premier add on Vendor.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_public_certificate_slot">

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
    <td><CopyableCode code="blob" /></td>
    <td><code>string (byte)</code></td>
    <td>Public Certificate byte array.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicCertificateLocation" /></td>
    <td><code>string</code></td>
    <td>Public Certificate Location. Known values are: "CurrentUserMy", "LocalMachineMy", and "Unknown". (CurrentUserMy, LocalMachineMy, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>Certificate Thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_site_container_slot">

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
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>Auth Type. Known values are: "Anonymous", "UserCredentials", "SystemIdentity", and "UserAssigned". (Anonymous, UserCredentials, SystemIdentity, UserAssigned)</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Created Time.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentVariables" /></td>
    <td><code>array</code></td>
    <td>List of environment variables.</td>
</tr>
<tr>
    <td><CopyableCode code="image" /></td>
    <td><code>string</code></td>
    <td>Image Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="inheritAppSettingsAndConnectionStrings" /></td>
    <td><code>boolean</code></td>
    <td>true if all AppSettings and ConnectionStrings have to be passed to the container as environment variables; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="isMain" /></td>
    <td><code>boolean</code></td>
    <td>true if the container is the main site container; false otherwise. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Modified Time.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordSecret" /></td>
    <td><code>string</code></td>
    <td>Password Secret.</td>
</tr>
<tr>
    <td><CopyableCode code="startUpCommand" /></td>
    <td><code>string</code></td>
    <td>StartUp Command.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetPort" /></td>
    <td><code>string</code></td>
    <td>Target Port.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userManagedIdentityClientId" /></td>
    <td><code>string</code></td>
    <td>UserManagedIdentity ClientId.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>User Name.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeMounts" /></td>
    <td><code>array</code></td>
    <td>List of volume mounts.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_site_extension_slot">

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
    <td><CopyableCode code="extension_id" /></td>
    <td><code>string</code></td>
    <td>Site extension ID.</td>
</tr>
<tr>
    <td><CopyableCode code="authors" /></td>
    <td><code>array</code></td>
    <td>List of authors.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Site Extension comment.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description.</td>
</tr>
<tr>
    <td><CopyableCode code="download_count" /></td>
    <td><code>integer</code></td>
    <td>Count of downloads.</td>
</tr>
<tr>
    <td><CopyableCode code="extension_type" /></td>
    <td><code>string</code></td>
    <td>Site extension type. Known values are: "Gallery" and "WebRoot". (Gallery, WebRoot)</td>
</tr>
<tr>
    <td><CopyableCode code="extension_url" /></td>
    <td><code>string</code></td>
    <td>Extension URL.</td>
</tr>
<tr>
    <td><CopyableCode code="feed_url" /></td>
    <td><code>string</code></td>
    <td>Feed URL.</td>
</tr>
<tr>
    <td><CopyableCode code="icon_url" /></td>
    <td><code>string</code></td>
    <td>Icon URL.</td>
</tr>
<tr>
    <td><CopyableCode code="installed_date_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Installed timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="installer_command_line_params" /></td>
    <td><code>string</code></td>
    <td>Installer command line parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="license_url" /></td>
    <td><code>string</code></td>
    <td>License URL.</td>
</tr>
<tr>
    <td><CopyableCode code="local_is_latest_version" /></td>
    <td><code>boolean</code></td>
    <td>true if the local version is the latest version; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="local_path" /></td>
    <td><code>string</code></td>
    <td>Local path.</td>
</tr>
<tr>
    <td><CopyableCode code="project_url" /></td>
    <td><code>string</code></td>
    <td>Project URL.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="published_date_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Published timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>Summary description.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>:vartype title: str</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version information.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_triggered_web_job_history">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="runs" /></td>
    <td><code>array</code></td>
    <td>List of triggered web job runs.</td>
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
<TabItem value="get_instance_workflow_slot">

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
    <td><CopyableCode code="files" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the files.</td>
</tr>
<tr>
    <td><CopyableCode code="flowState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the state of the workflow. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended". (NotSpecified, Completed, Enabled, Disabled, Deleted, Suspended)</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Gets or sets workflow health.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The resource kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
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
<TabItem value="list_application_settings_slot">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_backup_status_secrets">

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
    <td><CopyableCode code="blobName" /></td>
    <td><code>string</code></td>
    <td>Name of the blob which contains data for this backup.</td>
</tr>
<tr>
    <td><CopyableCode code="correlationId" /></td>
    <td><code>string</code></td>
    <td>Unique correlation identifier. Please use this along with the timestamp while communicating with Azure support.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of the backup creation.</td>
</tr>
<tr>
    <td><CopyableCode code="databases" /></td>
    <td><code>array</code></td>
    <td>List of databases included in the backup.</td>
</tr>
<tr>
    <td><CopyableCode code="finishedTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when this backup finished.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRestoreTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp of a last restore operation which used this backup.</td>
</tr>
<tr>
    <td><CopyableCode code="log" /></td>
    <td><code>string</code></td>
    <td>Details regarding this backup. Might contain an error message.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduled" /></td>
    <td><code>boolean</code></td>
    <td>True if this backup has been created due to a schedule being triggered.</td>
</tr>
<tr>
    <td><CopyableCode code="sizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Size of the backup in bytes.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Backup status. Known values are: "InProgress", "Failed", "Succeeded", "TimedOut", "Created", "Skipped", "PartiallySucceeded", "DeleteInProgress", "DeleteFailed", and "Deleted". (InProgress, Failed, Succeeded, TimedOut, Created, Skipped, PartiallySucceeded, DeleteInProgress, DeleteFailed, Deleted)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountUrl" /></td>
    <td><code>string</code></td>
    <td>SAS URL for the storage account container which contains this backup.</td>
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
<tr>
    <td><CopyableCode code="websiteSizeInBytes" /></td>
    <td><code>integer</code></td>
    <td>Size of the original web app which has been backed up.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_deployment_log">

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
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>True if deployment is currently active, false if completed and null if not started.</td>
</tr>
<tr>
    <td><CopyableCode code="author" /></td>
    <td><code>string</code></td>
    <td>Who authored the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="author_email" /></td>
    <td><code>string</code></td>
    <td>Author email.</td>
</tr>
<tr>
    <td><CopyableCode code="deployer" /></td>
    <td><code>string</code></td>
    <td>Who performed the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>string</code></td>
    <td>Details on deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="end_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>End time.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Details about deployment status.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>integer</code></td>
    <td>Deployment status.</td>
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
<TabItem value="list_function_keys">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_instance_processes">

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
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>Deployment name.</td>
</tr>
<tr>
    <td><CopyableCode code="file_name" /></td>
    <td><code>string</code></td>
    <td>File name of this process.</td>
</tr>
<tr>
    <td><CopyableCode code="user_name" /></td>
    <td><code>string</code></td>
    <td>User name.</td>
</tr>
<tr>
    <td><CopyableCode code="children" /></td>
    <td><code>array</code></td>
    <td>Child process list.</td>
</tr>
<tr>
    <td><CopyableCode code="command_line" /></td>
    <td><code>string</code></td>
    <td>Command line.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of process.</td>
</tr>
<tr>
    <td><CopyableCode code="environment_variables" /></td>
    <td><code>object</code></td>
    <td>List of environment variables.</td>
</tr>
<tr>
    <td><CopyableCode code="handle_count" /></td>
    <td><code>integer</code></td>
    <td>Handle count.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>integer</code></td>
    <td>ARM Identifier for deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="iis_profile_timeout_in_seconds" /></td>
    <td><code>number</code></td>
    <td>IIS Profile timeout (seconds).</td>
</tr>
<tr>
    <td><CopyableCode code="is_iis_profile_running" /></td>
    <td><code>boolean</code></td>
    <td>Is the IIS Profile running?.</td>
</tr>
<tr>
    <td><CopyableCode code="is_profile_running" /></td>
    <td><code>boolean</code></td>
    <td>Is profile running?.</td>
</tr>
<tr>
    <td><CopyableCode code="is_scm_site" /></td>
    <td><code>boolean</code></td>
    <td>Is this the SCM site?.</td>
</tr>
<tr>
    <td><CopyableCode code="is_webjob" /></td>
    <td><code>boolean</code></td>
    <td>Is this a Web Job?.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="minidump" /></td>
    <td><code>string</code></td>
    <td>Minidump URI.</td>
</tr>
<tr>
    <td><CopyableCode code="module_count" /></td>
    <td><code>integer</code></td>
    <td>Module count.</td>
</tr>
<tr>
    <td><CopyableCode code="modules" /></td>
    <td><code>array</code></td>
    <td>List of modules.</td>
</tr>
<tr>
    <td><CopyableCode code="non_paged_system_memory" /></td>
    <td><code>integer</code></td>
    <td>Non-paged system memory.</td>
</tr>
<tr>
    <td><CopyableCode code="open_file_handles" /></td>
    <td><code>array</code></td>
    <td>List of open files.</td>
</tr>
<tr>
    <td><CopyableCode code="paged_memory" /></td>
    <td><code>integer</code></td>
    <td>Paged memory.</td>
</tr>
<tr>
    <td><CopyableCode code="paged_system_memory" /></td>
    <td><code>integer</code></td>
    <td>Paged system memory.</td>
</tr>
<tr>
    <td><CopyableCode code="parent" /></td>
    <td><code>string</code></td>
    <td>Parent process.</td>
</tr>
<tr>
    <td><CopyableCode code="peak_paged_memory" /></td>
    <td><code>integer</code></td>
    <td>Peak paged memory.</td>
</tr>
<tr>
    <td><CopyableCode code="peak_virtual_memory" /></td>
    <td><code>integer</code></td>
    <td>Peak virtual memory usage.</td>
</tr>
<tr>
    <td><CopyableCode code="peak_working_set" /></td>
    <td><code>integer</code></td>
    <td>Peak working set.</td>
</tr>
<tr>
    <td><CopyableCode code="private_memory" /></td>
    <td><code>integer</code></td>
    <td>Private memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="privileged_cpu_time" /></td>
    <td><code>string</code></td>
    <td>Privileged CPU time.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thread_count" /></td>
    <td><code>integer</code></td>
    <td>Thread count.</td>
</tr>
<tr>
    <td><CopyableCode code="threads" /></td>
    <td><code>array</code></td>
    <td>Thread list.</td>
</tr>
<tr>
    <td><CopyableCode code="time_stamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time stamp.</td>
</tr>
<tr>
    <td><CopyableCode code="total_cpu_time" /></td>
    <td><code>string</code></td>
    <td>Total CPU time.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="user_cpu_time" /></td>
    <td><code>string</code></td>
    <td>User CPU time.</td>
</tr>
<tr>
    <td><CopyableCode code="virtual_memory" /></td>
    <td><code>integer</code></td>
    <td>Virtual memory size.</td>
</tr>
<tr>
    <td><CopyableCode code="working_set" /></td>
    <td><code>integer</code></td>
    <td>Working set.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_process_threads">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="base_priority" /></td>
    <td><code>integer</code></td>
    <td>Base priority.</td>
</tr>
<tr>
    <td><CopyableCode code="current_priority" /></td>
    <td><code>integer</code></td>
    <td>Current thread priority.</td>
</tr>
<tr>
    <td><CopyableCode code="href" /></td>
    <td><code>string</code></td>
    <td>HRef URI.</td>
</tr>
<tr>
    <td><CopyableCode code="identifier" /></td>
    <td><code>integer</code></td>
    <td>Site extension ID.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="priority_level" /></td>
    <td><code>string</code></td>
    <td>Thread priority level.</td>
</tr>
<tr>
    <td><CopyableCode code="process" /></td>
    <td><code>string</code></td>
    <td>Process URI.</td>
</tr>
<tr>
    <td><CopyableCode code="start_address" /></td>
    <td><code>string</code></td>
    <td>Start address.</td>
</tr>
<tr>
    <td><CopyableCode code="start_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Thread state.</td>
</tr>
<tr>
    <td><CopyableCode code="total_processor_time" /></td>
    <td><code>string</code></td>
    <td>Total processor time.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="user_processor_time" /></td>
    <td><code>string</code></td>
    <td>User processor time.</td>
</tr>
<tr>
    <td><CopyableCode code="wait_reason" /></td>
    <td><code>string</code></td>
    <td>Wait reason.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_network_features">

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
    <td><CopyableCode code="hybridConnections" /></td>
    <td><code>array</code></td>
    <td>The Hybrid Connections summary view.</td>
</tr>
<tr>
    <td><CopyableCode code="hybridConnectionsV2" /></td>
    <td><code>array</code></td>
    <td>The Hybrid Connection V2 (Service Bus) view.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<tr>
    <td><CopyableCode code="virtualNetworkConnection" /></td>
    <td><code>object</code></td>
    <td>The Virtual Network summary view.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkName" /></td>
    <td><code>string</code></td>
    <td>The Virtual Network name.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_triggered_web_job_history">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="runs" /></td>
    <td><code>array</code></td>
    <td>List of triggered web job runs.</td>
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
<TabItem value="get_private_endpoint_connection">

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
    <td><CopyableCode code="ipAddresses" /></td>
    <td><code>array</code></td>
    <td>Private IPAddresses mapped to the remote private endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpoint" /></td>
    <td><code>object</code></td>
    <td>PrivateEndpoint of a remote private endpoint connection.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkServiceConnectionState" /></td>
    <td><code>object</code></td>
    <td>The state of a private link connection.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>:vartype provisioning_state: str</td>
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
<TabItem value="get_vnet_connection">

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
    <td><CopyableCode code="certBlob" /></td>
    <td><code>string</code></td>
    <td>A certificate file (.cer) blob containing the public key of the private key used to authenticate a \nPoint-To-Site VPN connection.</td>
</tr>
<tr>
    <td><CopyableCode code="certThumbprint" /></td>
    <td><code>string</code></td>
    <td>The client certificate thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsServers" /></td>
    <td><code>string</code></td>
    <td>DNS servers to be used by this Virtual Network. This should be a comma-separated list of IP addresses.</td>
</tr>
<tr>
    <td><CopyableCode code="isSwift" /></td>
    <td><code>boolean</code></td>
    <td>Flag that is used to denote if this is VNET injection.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="resyncRequired" /></td>
    <td><code>boolean</code></td>
    <td>true if a resync is required; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="routes" /></td>
    <td><code>array</code></td>
    <td>The routes that this Virtual Network connection uses.</td>
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
<tr>
    <td><CopyableCode code="vnetResourceId" /></td>
    <td><code>string</code></td>
    <td>The Virtual Network's resource ID.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_network_trace_operation">

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
    <td>Detailed message of a network trace operation, e.g. error message in case of failure.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>Local file path for the captured network trace file.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of the network trace operation, same as Operation.Status (InProgress/Succeeded/Failed).</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_app_setting_key_vault_reference">

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
    <td><CopyableCode code="activeVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype active_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>string</code></td>
    <td>:vartype details: str</td>
</tr>
<tr>
    <td><CopyableCode code="identityType" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="reference" /></td>
    <td><code>string</code></td>
    <td>:vartype reference: str</td>
</tr>
<tr>
    <td><CopyableCode code="secretName" /></td>
    <td><code>string</code></td>
    <td>:vartype secret_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="secretVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype secret_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Default value is "KeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Initialized", "Resolved", "InvalidSyntax", "MSINotEnabled", "VaultNotFound", "SecretNotFound", "SecretVersionNotFound", "AccessToKeyVaultDenied", "OtherReasons", "FetchTimedOut", and "UnauthorizedClient". (Initialized, Resolved, InvalidSyntax, MSINotEnabled, VaultNotFound, SecretNotFound, SecretVersionNotFound, AccessToKeyVaultDenied, OtherReasons, FetchTimedOut, UnauthorizedClient)</td>
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
<tr>
    <td><CopyableCode code="vaultName" /></td>
    <td><code>string</code></td>
    <td>:vartype vault_name: str</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_site_connection_string_key_vault_reference">

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
    <td><CopyableCode code="activeVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype active_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="details" /></td>
    <td><code>string</code></td>
    <td>:vartype details: str</td>
</tr>
<tr>
    <td><CopyableCode code="identityType" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="reference" /></td>
    <td><code>string</code></td>
    <td>:vartype reference: str</td>
</tr>
<tr>
    <td><CopyableCode code="secretName" /></td>
    <td><code>string</code></td>
    <td>:vartype secret_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="secretVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype secret_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>Default value is "KeyVault".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Initialized", "Resolved", "InvalidSyntax", "MSINotEnabled", "VaultNotFound", "SecretNotFound", "SecretVersionNotFound", "AccessToKeyVaultDenied", "OtherReasons", "FetchTimedOut", and "UnauthorizedClient". (Initialized, Resolved, InvalidSyntax, MSINotEnabled, VaultNotFound, SecretNotFound, SecretVersionNotFound, AccessToKeyVaultDenied, OtherReasons, FetchTimedOut, UnauthorizedClient)</td>
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
<tr>
    <td><CopyableCode code="vaultName" /></td>
    <td><code>string</code></td>
    <td>:vartype vault_name: str</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_configuration_snapshot">

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
    <td><CopyableCode code="acrUseManagedIdentityCreds" /></td>
    <td><code>boolean</code></td>
    <td>Flag to use Managed Identity Creds for ACR pull.</td>
</tr>
<tr>
    <td><CopyableCode code="acrUserManagedIdentityID" /></td>
    <td><code>string</code></td>
    <td>If using user managed identity, the user managed identity ClientId.</td>
</tr>
<tr>
    <td><CopyableCode code="alwaysOn" /></td>
    <td><code>boolean</code></td>
    <td>true if Always On is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="apiDefinition" /></td>
    <td><code>object</code></td>
    <td>Information about the formal API definition for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="apiManagementConfig" /></td>
    <td><code>object</code></td>
    <td>Azure API management settings linked to the app.</td>
</tr>
<tr>
    <td><CopyableCode code="appCommandLine" /></td>
    <td><code>string</code></td>
    <td>App command line to launch.</td>
</tr>
<tr>
    <td><CopyableCode code="appSettings" /></td>
    <td><code>array</code></td>
    <td>Application settings. This property is not returned in response to normal create and read requests since it may contain sensitive information.</td>
</tr>
<tr>
    <td><CopyableCode code="autoHealEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if Auto Heal is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="autoHealRules" /></td>
    <td><code>object</code></td>
    <td>Auto Heal rules.</td>
</tr>
<tr>
    <td><CopyableCode code="autoSwapSlotName" /></td>
    <td><code>string</code></td>
    <td>Auto-swap slot name.</td>
</tr>
<tr>
    <td><CopyableCode code="azureStorageAccounts" /></td>
    <td><code>object</code></td>
    <td>List of Azure Storage Accounts.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStrings" /></td>
    <td><code>array</code></td>
    <td>Connection strings. This property is not returned in response to normal create and read requests since it may contain sensitive information.</td>
</tr>
<tr>
    <td><CopyableCode code="cors" /></td>
    <td><code>object</code></td>
    <td>Cross-Origin Resource Sharing (CORS) settings.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDocuments" /></td>
    <td><code>array</code></td>
    <td>Default documents.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedErrorLoggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if detailed error logging is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="documentRoot" /></td>
    <td><code>string</code></td>
    <td>Document root.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticWebAppScaleLimit" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of workers that a site can scale out to. This setting only applies to apps in plans where ElasticScaleEnabled is true.</td>
</tr>
<tr>
    <td><CopyableCode code="experiments" /></td>
    <td><code>object</code></td>
    <td>This is work around for polymorphic types.</td>
</tr>
<tr>
    <td><CopyableCode code="ftpsState" /></td>
    <td><code>string</code></td>
    <td>State of FTP / FTPS service. Known values are: "AllAllowed", "FtpsOnly", and "Disabled". (AllAllowed, FtpsOnly, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppScaleLimit" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of workers that a site can scale out to. This setting only applies to the Consumption and Elastic Premium Plans.</td>
</tr>
<tr>
    <td><CopyableCode code="functionsRuntimeScaleMonitoringEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets a value indicating whether functions runtime scale monitoring is enabled. When enabled, the ScaleController will not monitor event sources directly, but will instead call to the runtime to get scale status.</td>
</tr>
<tr>
    <td><CopyableCode code="handlerMappings" /></td>
    <td><code>array</code></td>
    <td>Handler mappings.</td>
</tr>
<tr>
    <td><CopyableCode code="healthCheckPath" /></td>
    <td><code>string</code></td>
    <td>Health check path.</td>
</tr>
<tr>
    <td><CopyableCode code="http20Enabled" /></td>
    <td><code>boolean</code></td>
    <td>Http20Enabled: configures a web site to allow clients to connect over http2.0.</td>
</tr>
<tr>
    <td><CopyableCode code="http20ProxyFlag" /></td>
    <td><code>integer</code></td>
    <td>Http20ProxyFlag: Configures a website to allow http2.0 to pass be proxied all the way to the app. 0 = disabled, 1 = pass through all http2 traffic, 2 = pass through gRPC only.</td>
</tr>
<tr>
    <td><CopyableCode code="httpLoggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if HTTP logging is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="ipSecurityRestrictions" /></td>
    <td><code>array</code></td>
    <td>IP security restrictions for main.</td>
</tr>
<tr>
    <td><CopyableCode code="ipSecurityRestrictionsDefaultAction" /></td>
    <td><code>string</code></td>
    <td>Default action for main access restriction if no rules are matched. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="javaContainer" /></td>
    <td><code>string</code></td>
    <td>Java container.</td>
</tr>
<tr>
    <td><CopyableCode code="javaContainerVersion" /></td>
    <td><code>string</code></td>
    <td>Java container version.</td>
</tr>
<tr>
    <td><CopyableCode code="javaVersion" /></td>
    <td><code>string</code></td>
    <td>Java version.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReferenceIdentity" /></td>
    <td><code>string</code></td>
    <td>Identity to use for Key Vault Reference authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="limits" /></td>
    <td><code>object</code></td>
    <td>Site limits.</td>
</tr>
<tr>
    <td><CopyableCode code="linuxFxVersion" /></td>
    <td><code>string</code></td>
    <td>Linux App Framework and version.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancing" /></td>
    <td><code>string</code></td>
    <td>Site load balancing. Known values are: "WeightedRoundRobin", "LeastRequests", "LeastResponseTime", "WeightedTotalTraffic", "RequestHash", "PerSiteRoundRobin", and "LeastRequestsWithTieBreaker". (WeightedRoundRobin, LeastRequests, LeastResponseTime, WeightedTotalTraffic, RequestHash, PerSiteRoundRobin, LeastRequestsWithTieBreaker)</td>
</tr>
<tr>
    <td><CopyableCode code="localMySqlEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable local MySQL; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="logsDirectorySizeLimit" /></td>
    <td><code>integer</code></td>
    <td>HTTP logs directory size limit.</td>
</tr>
<tr>
    <td><CopyableCode code="machineKey" /></td>
    <td><code>object</code></td>
    <td>Site MachineKey.</td>
</tr>
<tr>
    <td><CopyableCode code="managedPipelineMode" /></td>
    <td><code>string</code></td>
    <td>Managed pipeline mode. Known values are: "Integrated" and "Classic". (Integrated, Classic)</td>
</tr>
<tr>
    <td><CopyableCode code="managedServiceIdentityId" /></td>
    <td><code>integer</code></td>
    <td>Managed Service Identity Id.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>Application metadata. This property cannot be retrieved, since it may contain secrets.</td>
</tr>
<tr>
    <td><CopyableCode code="minTlsCipherSuite" /></td>
    <td><code>string</code></td>
    <td>The minimum strength TLS cipher suite allowed for an application. Known values are: "TLS_AES_256_GCM_SHA384", "TLS_AES_128_GCM_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256", "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA", "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA", "TLS_RSA_WITH_AES_256_GCM_SHA384", "TLS_RSA_WITH_AES_128_GCM_SHA256", "TLS_RSA_WITH_AES_256_CBC_SHA256", "TLS_RSA_WITH_AES_128_CBC_SHA256", "TLS_RSA_WITH_AES_256_CBC_SHA", and "TLS_RSA_WITH_AES_128_CBC_SHA". (TLS_AES_256_GCM_SHA384, TLS_AES_128_GCM_SHA256, TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384, TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256, TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_256_GCM_SHA384, TLS_RSA_WITH_AES_128_GCM_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA256, TLS_RSA_WITH_AES_128_CBC_SHA256, TLS_RSA_WITH_AES_256_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA)</td>
</tr>
<tr>
    <td><CopyableCode code="minTlsVersion" /></td>
    <td><code>string</code></td>
    <td>MinTlsVersion: configures the minimum version of TLS required for SSL requests. Known values are: "1.0", "1.1", "1.2", and "1.3". (1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="minimumElasticInstanceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of minimum instance count for a site This setting only applies to the Elastic Plans.</td>
</tr>
<tr>
    <td><CopyableCode code="netFrameworkVersion" /></td>
    <td><code>string</code></td>
    <td>.NET Framework version.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeVersion" /></td>
    <td><code>string</code></td>
    <td>Version of Node.js.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>Number of workers.</td>
</tr>
<tr>
    <td><CopyableCode code="phpVersion" /></td>
    <td><code>string</code></td>
    <td>Version of PHP.</td>
</tr>
<tr>
    <td><CopyableCode code="powerShellVersion" /></td>
    <td><code>string</code></td>
    <td>Version of PowerShell.</td>
</tr>
<tr>
    <td><CopyableCode code="preWarmedInstanceCount" /></td>
    <td><code>integer</code></td>
    <td>Number of preWarmed instances. This setting only applies to the Consumption and Elastic Plans.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to allow or block all public traffic.</td>
</tr>
<tr>
    <td><CopyableCode code="publishingUsername" /></td>
    <td><code>string</code></td>
    <td>Publishing user name.</td>
</tr>
<tr>
    <td><CopyableCode code="push" /></td>
    <td><code>object</code></td>
    <td>Push endpoint settings.</td>
</tr>
<tr>
    <td><CopyableCode code="pythonVersion" /></td>
    <td><code>string</code></td>
    <td>Version of Python.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteDebuggingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if remote debugging is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="remoteDebuggingVersion" /></td>
    <td><code>string</code></td>
    <td>Remote debugging version.</td>
</tr>
<tr>
    <td><CopyableCode code="requestTracingEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if request tracing is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="requestTracingExpirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Request tracing expiration time.</td>
</tr>
<tr>
    <td><CopyableCode code="scmIpSecurityRestrictions" /></td>
    <td><code>array</code></td>
    <td>IP security restrictions for scm.</td>
</tr>
<tr>
    <td><CopyableCode code="scmIpSecurityRestrictionsDefaultAction" /></td>
    <td><code>string</code></td>
    <td>Default action for scm access restriction if no rules are matched. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="scmIpSecurityRestrictionsUseMain" /></td>
    <td><code>boolean</code></td>
    <td>IP security restrictions for scm to use main.</td>
</tr>
<tr>
    <td><CopyableCode code="scmMinTlsVersion" /></td>
    <td><code>string</code></td>
    <td>ScmMinTlsVersion: configures the minimum version of TLS required for SSL requests for SCM site. Known values are: "1.0", "1.1", "1.2", and "1.3". (1.0, 1.1, 1.2, 1.3)</td>
</tr>
<tr>
    <td><CopyableCode code="scmType" /></td>
    <td><code>string</code></td>
    <td>SCM type. Known values are: "None", "Dropbox", "Tfs", "LocalGit", "GitHub", "CodePlexGit", "CodePlexHg", "BitbucketGit", "BitbucketHg", "ExternalGit", "ExternalHg", "OneDrive", "VSO", and "VSTSRM". (None, Dropbox, Tfs, LocalGit, GitHub, CodePlexGit, CodePlexHg, BitbucketGit, BitbucketHg, ExternalGit, ExternalHg, OneDrive, VSO, VSTSRM)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tracingOptions" /></td>
    <td><code>string</code></td>
    <td>Tracing options.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="use32BitWorkerProcess" /></td>
    <td><code>boolean</code></td>
    <td>true to use 32-bit worker process; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualApplications" /></td>
    <td><code>array</code></td>
    <td>Virtual applications.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetName" /></td>
    <td><code>string</code></td>
    <td>Virtual Network name.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetPrivatePortsCount" /></td>
    <td><code>integer</code></td>
    <td>The number of private ports assigned to this app. These will be assigned dynamically on runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetRouteAllEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Virtual Network Route All enabled. This causes all outbound traffic to have Virtual Network Security Groups and User Defined Routes applied.</td>
</tr>
<tr>
    <td><CopyableCode code="webSocketsEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true if WebSocket is enabled; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="websiteTimeZone" /></td>
    <td><code>string</code></td>
    <td>Sets the time zone a site uses for generating timestamps. Compatible with Linux and Windows App Service. Setting the WEBSITE_TIME_ZONE app setting takes precedence over this config. For Linux, expects tz database values `https://www.iana.org/time-zones `_ (for a quick reference see `https://en.wikipedia.org/wiki/List_of_tz_database_time_zones `_). For Windows, expects one of the time zones listed under HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones.</td>
</tr>
<tr>
    <td><CopyableCode code="windowsFxVersion" /></td>
    <td><code>string</code></td>
    <td>Xenon App Framework and version.</td>
</tr>
<tr>
    <td><CopyableCode code="xManagedServiceIdentityId" /></td>
    <td><code>integer</code></td>
    <td>Explicit Managed Service Identity Id.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_production_site_deployment_status">

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
    <td><CopyableCode code="deploymentId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation id.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>List of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="failedInstancesLogs" /></td>
    <td><code>array</code></td>
    <td>List of URLs pointing to logs for instances which failed to provision.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInstancesFailed" /></td>
    <td><code>integer</code></td>
    <td>Number of site instances failed to provision.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInstancesInProgress" /></td>
    <td><code>integer</code></td>
    <td>Number of site instances currently being provisioned.</td>
</tr>
<tr>
    <td><CopyableCode code="numberOfInstancesSuccessful" /></td>
    <td><code>integer</code></td>
    <td>Number of site instances provisioned successfully.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Deployment build status. Known values are: "TimedOut", "RuntimeFailed", "BuildAborted", "BuildFailed", "BuildRequestReceived", "BuildPending", "BuildInProgress", "BuildSuccessful", "PostBuildRestartRequired", "StartPolling", "StartPollingWithRestart", "RuntimeStarting", and "RuntimeSuccessful". (TimedOut, RuntimeFailed, BuildAborted, BuildFailed, BuildRequestReceived, BuildPending, BuildInProgress, BuildSuccessful, PostBuildRestartRequired, StartPolling, StartPollingWithRestart, RuntimeStarting, RuntimeSuccessful)</td>
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
<TabItem value="get_domain_ownership_identifier">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<TabItem value="get_host_name_binding">

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
    <td><CopyableCode code="azureResourceName" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="azureResourceType" /></td>
    <td><code>string</code></td>
    <td>Azure resource type. Known values are: "Website" and "TrafficManager". (Website, TrafficManager)</td>
</tr>
<tr>
    <td><CopyableCode code="customHostNameDnsRecordType" /></td>
    <td><code>string</code></td>
    <td>Custom DNS record type. Known values are: "CName" and "A". (CName, A)</td>
</tr>
<tr>
    <td><CopyableCode code="domainId" /></td>
    <td><code>string</code></td>
    <td>Fully qualified ARM domain resource URI.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNameType" /></td>
    <td><code>string</code></td>
    <td>Hostname type. Known values are: "Verified" and "Managed". (Verified, Managed)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>App Service app name.</td>
</tr>
<tr>
    <td><CopyableCode code="sslState" /></td>
    <td><code>string</code></td>
    <td>SSL type. Known values are: "Disabled", "SniEnabled", and "IpBasedEnabled". (Disabled, SniEnabled, IpBasedEnabled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>SSL certificate thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="virtualIP" /></td>
    <td><code>string</code></td>
    <td>Virtual IP address assigned to the hostname if IP based SSL is enabled.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_relay_service_connection">

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
    <td><CopyableCode code="biztalkUri" /></td>
    <td><code>string</code></td>
    <td>:vartype biztalk_uri: str</td>
</tr>
<tr>
    <td><CopyableCode code="entityConnectionString" /></td>
    <td><code>string</code></td>
    <td>:vartype entity_connection_string: str</td>
</tr>
<tr>
    <td><CopyableCode code="entityName" /></td>
    <td><code>string</code></td>
    <td>:vartype entity_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>:vartype hostname: str</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>:vartype port: int</td>
</tr>
<tr>
    <td><CopyableCode code="resourceConnectionString" /></td>
    <td><code>string</code></td>
    <td>:vartype resource_connection_string: str</td>
</tr>
<tr>
    <td><CopyableCode code="resourceType" /></td>
    <td><code>string</code></td>
    <td>:vartype resource_type: str</td>
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
<TabItem value="get_premier_add_on">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceOffer" /></td>
    <td><code>string</code></td>
    <td>Premier add on Marketplace offer.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplacePublisher" /></td>
    <td><code>string</code></td>
    <td>Premier add on Marketplace publisher.</td>
</tr>
<tr>
    <td><CopyableCode code="product" /></td>
    <td><code>string</code></td>
    <td>Premier add on Product.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Premier add on SKU.</td>
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
<tr>
    <td><CopyableCode code="vendor" /></td>
    <td><code>string</code></td>
    <td>Premier add on Vendor.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_public_certificate">

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
    <td><CopyableCode code="blob" /></td>
    <td><code>string (byte)</code></td>
    <td>Public Certificate byte array.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publicCertificateLocation" /></td>
    <td><code>string</code></td>
    <td>Public Certificate Location. Known values are: "CurrentUserMy", "LocalMachineMy", and "Unknown". (CurrentUserMy, LocalMachineMy, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>Certificate Thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_site_container">

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
    <td><CopyableCode code="authType" /></td>
    <td><code>string</code></td>
    <td>Auth Type. Known values are: "Anonymous", "UserCredentials", "SystemIdentity", and "UserAssigned". (Anonymous, UserCredentials, SystemIdentity, UserAssigned)</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Created Time.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentVariables" /></td>
    <td><code>array</code></td>
    <td>List of environment variables.</td>
</tr>
<tr>
    <td><CopyableCode code="image" /></td>
    <td><code>string</code></td>
    <td>Image Name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="inheritAppSettingsAndConnectionStrings" /></td>
    <td><code>boolean</code></td>
    <td>true if all AppSettings and ConnectionStrings have to be passed to the container as environment variables; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="isMain" /></td>
    <td><code>boolean</code></td>
    <td>true if the container is the main site container; false otherwise. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last Modified Time.</td>
</tr>
<tr>
    <td><CopyableCode code="passwordSecret" /></td>
    <td><code>string</code></td>
    <td>Password Secret.</td>
</tr>
<tr>
    <td><CopyableCode code="startUpCommand" /></td>
    <td><code>string</code></td>
    <td>StartUp Command.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetPort" /></td>
    <td><code>string</code></td>
    <td>Target Port.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userManagedIdentityClientId" /></td>
    <td><code>string</code></td>
    <td>UserManagedIdentity ClientId.</td>
</tr>
<tr>
    <td><CopyableCode code="userName" /></td>
    <td><code>string</code></td>
    <td>User Name.</td>
</tr>
<tr>
    <td><CopyableCode code="volumeMounts" /></td>
    <td><code>array</code></td>
    <td>List of volume mounts.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_site_extension">

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
    <td><CopyableCode code="extension_id" /></td>
    <td><code>string</code></td>
    <td>Site extension ID.</td>
</tr>
<tr>
    <td><CopyableCode code="authors" /></td>
    <td><code>array</code></td>
    <td>List of authors.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Site Extension comment.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description.</td>
</tr>
<tr>
    <td><CopyableCode code="download_count" /></td>
    <td><code>integer</code></td>
    <td>Count of downloads.</td>
</tr>
<tr>
    <td><CopyableCode code="extension_type" /></td>
    <td><code>string</code></td>
    <td>Site extension type. Known values are: "Gallery" and "WebRoot". (Gallery, WebRoot)</td>
</tr>
<tr>
    <td><CopyableCode code="extension_url" /></td>
    <td><code>string</code></td>
    <td>Extension URL.</td>
</tr>
<tr>
    <td><CopyableCode code="feed_url" /></td>
    <td><code>string</code></td>
    <td>Feed URL.</td>
</tr>
<tr>
    <td><CopyableCode code="icon_url" /></td>
    <td><code>string</code></td>
    <td>Icon URL.</td>
</tr>
<tr>
    <td><CopyableCode code="installed_date_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Installed timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="installer_command_line_params" /></td>
    <td><code>string</code></td>
    <td>Installer command line parameters.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="license_url" /></td>
    <td><code>string</code></td>
    <td>License URL.</td>
</tr>
<tr>
    <td><CopyableCode code="local_is_latest_version" /></td>
    <td><code>boolean</code></td>
    <td>true if the local version is the latest version; false otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="local_path" /></td>
    <td><code>string</code></td>
    <td>Local path.</td>
</tr>
<tr>
    <td><CopyableCode code="project_url" /></td>
    <td><code>string</code></td>
    <td>Project URL.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="published_date_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Published timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>Summary description.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>:vartype title: str</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version information.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_workflow">

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
    <td><CopyableCode code="files" /></td>
    <td><code>object</code></td>
    <td>Gets or sets the files.</td>
</tr>
<tr>
    <td><CopyableCode code="flowState" /></td>
    <td><code>string</code></td>
    <td>Gets or sets the state of the workflow. Known values are: "NotSpecified", "Completed", "Enabled", "Disabled", "Deleted", and "Suspended". (NotSpecified, Completed, Enabled, Disabled, Deleted, Suspended)</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>object</code></td>
    <td>Gets or sets workflow health.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The resource kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
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
    <td><CopyableCode code="autoGeneratedDomainNameLabelScope" /></td>
    <td><code>string</code></td>
    <td>Specifies the scope of uniqueness for the default hostname during resource creation. Known values are: "TenantReuse", "SubscriptionReuse", "ResourceGroupReuse", and "NoReuse". (TenantReuse, SubscriptionReuse, ResourceGroupReuse, NoReuse)</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityState" /></td>
    <td><code>string</code></td>
    <td>Management information availability state for the app. Known values are: "Normal", "Limited", and "DisasterRecoveryMode". (Normal, Limited, DisasterRecoveryMode)</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client affinity; false to stop sending session affinity cookies, which route client requests in the same session to the same instance. Default is true.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityPartitioningEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client affinity partitioning using CHIPS cookies, this will add the partitioned property to the affinity cookies; false to stop sending partitioned affinity cookies. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityProxyEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to override client affinity cookie domain with X-Forwarded-Host request header. false to use default domain. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client certificate authentication (TLS mutual authentication); otherwise, false. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertExclusionPaths" /></td>
    <td><code>string</code></td>
    <td>client certificate authentication comma-separated exclusion paths.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertMode" /></td>
    <td><code>string</code></td>
    <td>This composes with ClientCertEnabled setting. * ClientCertEnabled: false means ClientCert is ignored. * ClientCertEnabled: true and ClientCertMode: Required means ClientCert is required. * ClientCertEnabled: true and ClientCertMode: Optional means ClientCert is optional or accepted. Known values are: "Required", "Optional", and "OptionalInteractiveUser". (Required, Optional, OptionalInteractiveUser)</td>
</tr>
<tr>
    <td><CopyableCode code="cloningInfo" /></td>
    <td><code>object</code></td>
    <td>If specified during app creation, the app is cloned from a source app.</td>
</tr>
<tr>
    <td><CopyableCode code="containerSize" /></td>
    <td><code>integer</code></td>
    <td>Size of the function container.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomainVerificationId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier that verifies the custom domains assigned to the app. Customer will add this id to a txt record for verification.</td>
</tr>
<tr>
    <td><CopyableCode code="dailyMemoryTimeQuota" /></td>
    <td><code>integer</code></td>
    <td>Maximum allowed daily memory-time quota (applicable on dynamic apps only).</td>
</tr>
<tr>
    <td><CopyableCode code="daprConfig" /></td>
    <td><code>object</code></td>
    <td>Dapr configuration of the app.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultHostName" /></td>
    <td><code>string</code></td>
    <td>Default hostname of the app. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Property to configure various DNS related settings for a site.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the app is enabled; otherwise, false. Setting this value to false disables the app (takes the app offline).</td>
</tr>
<tr>
    <td><CopyableCode code="enabledHostNames" /></td>
    <td><code>array</code></td>
    <td>Enabled hostnames for the app.Hostnames need to be assigned (see HostNames) AND enabled. Otherwise, the app is not served on those hostnames.</td>
</tr>
<tr>
    <td><CopyableCode code="endToEndEncryptionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to use end to end encryption between the FrontEnd and the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppConfig" /></td>
    <td><code>object</code></td>
    <td>Configuration specific of the Azure Function app.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNameSslStates" /></td>
    <td><code>array</code></td>
    <td>Hostname SSL states are used to manage the SSL bindings for app's hostnames.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNames" /></td>
    <td><code>array</code></td>
    <td>Hostnames associated with the app.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNamesDisabled" /></td>
    <td><code>boolean</code></td>
    <td>true to disable the public hostnames of the app; otherwise, false. If true, the app is only accessible via API management process.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>App Service Environment to use for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsOnly" /></td>
    <td><code>boolean</code></td>
    <td>HttpsOnly: configures a web site to accept only https requests. Issues redirect for http requests.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperV" /></td>
    <td><code>boolean</code></td>
    <td>Hyper-V sandbox.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="inProgressOperationId" /></td>
    <td><code>string</code></td>
    <td>Specifies an operation id if this site has a pending operation.</td>
</tr>
<tr>
    <td><CopyableCode code="ipMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the IP mode of the app. Known values are: "IPv4", "IPv6", and "IPv4AndIPv6". (IPv4, IPv6, IPv4AndIPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultContainer" /></td>
    <td><code>boolean</code></td>
    <td>true if the app is a default container; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="isXenon" /></td>
    <td><code>boolean</code></td>
    <td>Obsolete: Hyper-V sandbox.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReferenceIdentity" /></td>
    <td><code>string</code></td>
    <td>Identity to use for Key Vault Reference authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the app was modified, in UTC. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager ID of the customer's selected Managed Environment on which to host this app. This must be of the form /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.App/managedEnvironments/&#123;managedEnvironmentName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of workers. This only applies to Functions container.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>string</code></td>
    <td>List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from tenants that site can be hosted with current settings. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundVnetRouting" /></td>
    <td><code>object</code></td>
    <td>Property to configure various outbound traffic routing options over virtual network for a site.</td>
</tr>
<tr>
    <td><CopyableCode code="possibleOutboundIpAddresses" /></td>
    <td><code>string</code></td>
    <td>List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from all tenants except dataComponent. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to allow or block all public traffic. Allowed Values: 'Enabled', 'Disabled' or an empty string.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancyMode" /></td>
    <td><code>string</code></td>
    <td>Site redundancy mode. Known values are: "None", "Manual", "Failover", "ActiveActive", and "GeoRedundant". (None, Manual, Failover, ActiveActive, GeoRedundant)</td>
</tr>
<tr>
    <td><CopyableCode code="repositorySiteName" /></td>
    <td><code>string</code></td>
    <td>Name of the repository site.</td>
</tr>
<tr>
    <td><CopyableCode code="reserved" /></td>
    <td><code>boolean</code></td>
    <td>true if reserved; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceConfig" /></td>
    <td><code>object</code></td>
    <td>Function app resource requirements.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group the app belongs to. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="scmSiteAlsoStopped" /></td>
    <td><code>boolean</code></td>
    <td>true to stop SCM (KUDU) site when the app is stopped; otherwise, false. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="serverFarmId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the associated App Service plan, formatted as: "/subscriptions/&#123;subscriptionID&#125;/resourceGroups/&#123;groupName&#125;/providers/Microsoft.Web/serverfarms/&#123;appServicePlanName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="siteConfig" /></td>
    <td><code>object</code></td>
    <td>Configuration of an App Service app. This property is not returned in response to normal create and read requests since it may contain sensitive information.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Current SKU of application based on associated App Service Plan. Some valid SKU values are Free, Shared, Basic, Dynamic, FlexConsumption, Standard, Premium, PremiumV2, PremiumV3, Isolated, IsolatedV2.</td>
</tr>
<tr>
    <td><CopyableCode code="slotSwapStatus" /></td>
    <td><code>object</code></td>
    <td>Status of the last deployment slot swap operation.</td>
</tr>
<tr>
    <td><CopyableCode code="sshEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable ssh access.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the app.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountRequired" /></td>
    <td><code>boolean</code></td>
    <td>Checks if Customer provided storage account is required.</td>
</tr>
<tr>
    <td><CopyableCode code="suspendedTill" /></td>
    <td><code>string (date-time)</code></td>
    <td>App suspended till in case memory-time quota is exceeded.</td>
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
    <td><CopyableCode code="targetSwapSlot" /></td>
    <td><code>string</code></td>
    <td>Specifies which deployment slot this app will swap into. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficManagerHostNames" /></td>
    <td><code>array</code></td>
    <td>Azure Traffic Manager hostnames associated with the app. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usageState" /></td>
    <td><code>string</code></td>
    <td>State indicating whether the app has exceeded its quota usage. Read-only. Known values are: "Normal" and "Exceeded". (Normal, Exceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkSubnetId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager ID of the Virtual network and subnet to be joined by Regional VNET Integration. This must be of the form /subscriptions/&#123;subscriptionName&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;vnetName&#125;/subnets/&#123;subnetName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name for function app to execute on.</td>
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
    <td><CopyableCode code="autoGeneratedDomainNameLabelScope" /></td>
    <td><code>string</code></td>
    <td>Specifies the scope of uniqueness for the default hostname during resource creation. Known values are: "TenantReuse", "SubscriptionReuse", "ResourceGroupReuse", and "NoReuse". (TenantReuse, SubscriptionReuse, ResourceGroupReuse, NoReuse)</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityState" /></td>
    <td><code>string</code></td>
    <td>Management information availability state for the app. Known values are: "Normal", "Limited", and "DisasterRecoveryMode". (Normal, Limited, DisasterRecoveryMode)</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client affinity; false to stop sending session affinity cookies, which route client requests in the same session to the same instance. Default is true.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityPartitioningEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client affinity partitioning using CHIPS cookies, this will add the partitioned property to the affinity cookies; false to stop sending partitioned affinity cookies. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityProxyEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to override client affinity cookie domain with X-Forwarded-Host request header. false to use default domain. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client certificate authentication (TLS mutual authentication); otherwise, false. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertExclusionPaths" /></td>
    <td><code>string</code></td>
    <td>client certificate authentication comma-separated exclusion paths.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertMode" /></td>
    <td><code>string</code></td>
    <td>This composes with ClientCertEnabled setting. * ClientCertEnabled: false means ClientCert is ignored. * ClientCertEnabled: true and ClientCertMode: Required means ClientCert is required. * ClientCertEnabled: true and ClientCertMode: Optional means ClientCert is optional or accepted. Known values are: "Required", "Optional", and "OptionalInteractiveUser". (Required, Optional, OptionalInteractiveUser)</td>
</tr>
<tr>
    <td><CopyableCode code="cloningInfo" /></td>
    <td><code>object</code></td>
    <td>If specified during app creation, the app is cloned from a source app.</td>
</tr>
<tr>
    <td><CopyableCode code="containerSize" /></td>
    <td><code>integer</code></td>
    <td>Size of the function container.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomainVerificationId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier that verifies the custom domains assigned to the app. Customer will add this id to a txt record for verification.</td>
</tr>
<tr>
    <td><CopyableCode code="dailyMemoryTimeQuota" /></td>
    <td><code>integer</code></td>
    <td>Maximum allowed daily memory-time quota (applicable on dynamic apps only).</td>
</tr>
<tr>
    <td><CopyableCode code="daprConfig" /></td>
    <td><code>object</code></td>
    <td>Dapr configuration of the app.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultHostName" /></td>
    <td><code>string</code></td>
    <td>Default hostname of the app. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Property to configure various DNS related settings for a site.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the app is enabled; otherwise, false. Setting this value to false disables the app (takes the app offline).</td>
</tr>
<tr>
    <td><CopyableCode code="enabledHostNames" /></td>
    <td><code>array</code></td>
    <td>Enabled hostnames for the app.Hostnames need to be assigned (see HostNames) AND enabled. Otherwise, the app is not served on those hostnames.</td>
</tr>
<tr>
    <td><CopyableCode code="endToEndEncryptionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to use end to end encryption between the FrontEnd and the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppConfig" /></td>
    <td><code>object</code></td>
    <td>Configuration specific of the Azure Function app.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNameSslStates" /></td>
    <td><code>array</code></td>
    <td>Hostname SSL states are used to manage the SSL bindings for app's hostnames.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNames" /></td>
    <td><code>array</code></td>
    <td>Hostnames associated with the app.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNamesDisabled" /></td>
    <td><code>boolean</code></td>
    <td>true to disable the public hostnames of the app; otherwise, false. If true, the app is only accessible via API management process.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>App Service Environment to use for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsOnly" /></td>
    <td><code>boolean</code></td>
    <td>HttpsOnly: configures a web site to accept only https requests. Issues redirect for http requests.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperV" /></td>
    <td><code>boolean</code></td>
    <td>Hyper-V sandbox.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="inProgressOperationId" /></td>
    <td><code>string</code></td>
    <td>Specifies an operation id if this site has a pending operation.</td>
</tr>
<tr>
    <td><CopyableCode code="ipMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the IP mode of the app. Known values are: "IPv4", "IPv6", and "IPv4AndIPv6". (IPv4, IPv6, IPv4AndIPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultContainer" /></td>
    <td><code>boolean</code></td>
    <td>true if the app is a default container; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="isXenon" /></td>
    <td><code>boolean</code></td>
    <td>Obsolete: Hyper-V sandbox.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReferenceIdentity" /></td>
    <td><code>string</code></td>
    <td>Identity to use for Key Vault Reference authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the app was modified, in UTC. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager ID of the customer's selected Managed Environment on which to host this app. This must be of the form /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.App/managedEnvironments/&#123;managedEnvironmentName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of workers. This only applies to Functions container.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>string</code></td>
    <td>List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from tenants that site can be hosted with current settings. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundVnetRouting" /></td>
    <td><code>object</code></td>
    <td>Property to configure various outbound traffic routing options over virtual network for a site.</td>
</tr>
<tr>
    <td><CopyableCode code="possibleOutboundIpAddresses" /></td>
    <td><code>string</code></td>
    <td>List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from all tenants except dataComponent. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to allow or block all public traffic. Allowed Values: 'Enabled', 'Disabled' or an empty string.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancyMode" /></td>
    <td><code>string</code></td>
    <td>Site redundancy mode. Known values are: "None", "Manual", "Failover", "ActiveActive", and "GeoRedundant". (None, Manual, Failover, ActiveActive, GeoRedundant)</td>
</tr>
<tr>
    <td><CopyableCode code="repositorySiteName" /></td>
    <td><code>string</code></td>
    <td>Name of the repository site.</td>
</tr>
<tr>
    <td><CopyableCode code="reserved" /></td>
    <td><code>boolean</code></td>
    <td>true if reserved; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceConfig" /></td>
    <td><code>object</code></td>
    <td>Function app resource requirements.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group the app belongs to. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="scmSiteAlsoStopped" /></td>
    <td><code>boolean</code></td>
    <td>true to stop SCM (KUDU) site when the app is stopped; otherwise, false. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="serverFarmId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the associated App Service plan, formatted as: "/subscriptions/&#123;subscriptionID&#125;/resourceGroups/&#123;groupName&#125;/providers/Microsoft.Web/serverfarms/&#123;appServicePlanName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="siteConfig" /></td>
    <td><code>object</code></td>
    <td>Configuration of an App Service app. This property is not returned in response to normal create and read requests since it may contain sensitive information.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Current SKU of application based on associated App Service Plan. Some valid SKU values are Free, Shared, Basic, Dynamic, FlexConsumption, Standard, Premium, PremiumV2, PremiumV3, Isolated, IsolatedV2.</td>
</tr>
<tr>
    <td><CopyableCode code="slotSwapStatus" /></td>
    <td><code>object</code></td>
    <td>Status of the last deployment slot swap operation.</td>
</tr>
<tr>
    <td><CopyableCode code="sshEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable ssh access.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the app.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountRequired" /></td>
    <td><code>boolean</code></td>
    <td>Checks if Customer provided storage account is required.</td>
</tr>
<tr>
    <td><CopyableCode code="suspendedTill" /></td>
    <td><code>string (date-time)</code></td>
    <td>App suspended till in case memory-time quota is exceeded.</td>
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
    <td><CopyableCode code="targetSwapSlot" /></td>
    <td><code>string</code></td>
    <td>Specifies which deployment slot this app will swap into. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficManagerHostNames" /></td>
    <td><code>array</code></td>
    <td>Azure Traffic Manager hostnames associated with the app. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usageState" /></td>
    <td><code>string</code></td>
    <td>State indicating whether the app has exceeded its quota usage. Read-only. Known values are: "Normal" and "Exceeded". (Normal, Exceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkSubnetId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager ID of the Virtual network and subnet to be joined by Regional VNET Integration. This must be of the form /subscriptions/&#123;subscriptionName&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;vnetName&#125;/subnets/&#123;subnetName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name for function app to execute on.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="autoGeneratedDomainNameLabelScope" /></td>
    <td><code>string</code></td>
    <td>Specifies the scope of uniqueness for the default hostname during resource creation. Known values are: "TenantReuse", "SubscriptionReuse", "ResourceGroupReuse", and "NoReuse". (TenantReuse, SubscriptionReuse, ResourceGroupReuse, NoReuse)</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityState" /></td>
    <td><code>string</code></td>
    <td>Management information availability state for the app. Known values are: "Normal", "Limited", and "DisasterRecoveryMode". (Normal, Limited, DisasterRecoveryMode)</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client affinity; false to stop sending session affinity cookies, which route client requests in the same session to the same instance. Default is true.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityPartitioningEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client affinity partitioning using CHIPS cookies, this will add the partitioned property to the affinity cookies; false to stop sending partitioned affinity cookies. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientAffinityProxyEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to override client affinity cookie domain with X-Forwarded-Host request header. false to use default domain. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertEnabled" /></td>
    <td><code>boolean</code></td>
    <td>true to enable client certificate authentication (TLS mutual authentication); otherwise, false. Default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertExclusionPaths" /></td>
    <td><code>string</code></td>
    <td>client certificate authentication comma-separated exclusion paths.</td>
</tr>
<tr>
    <td><CopyableCode code="clientCertMode" /></td>
    <td><code>string</code></td>
    <td>This composes with ClientCertEnabled setting. * ClientCertEnabled: false means ClientCert is ignored. * ClientCertEnabled: true and ClientCertMode: Required means ClientCert is required. * ClientCertEnabled: true and ClientCertMode: Optional means ClientCert is optional or accepted. Known values are: "Required", "Optional", and "OptionalInteractiveUser". (Required, Optional, OptionalInteractiveUser)</td>
</tr>
<tr>
    <td><CopyableCode code="cloningInfo" /></td>
    <td><code>object</code></td>
    <td>If specified during app creation, the app is cloned from a source app.</td>
</tr>
<tr>
    <td><CopyableCode code="containerSize" /></td>
    <td><code>integer</code></td>
    <td>Size of the function container.</td>
</tr>
<tr>
    <td><CopyableCode code="customDomainVerificationId" /></td>
    <td><code>string</code></td>
    <td>Unique identifier that verifies the custom domains assigned to the app. Customer will add this id to a txt record for verification.</td>
</tr>
<tr>
    <td><CopyableCode code="dailyMemoryTimeQuota" /></td>
    <td><code>integer</code></td>
    <td>Maximum allowed daily memory-time quota (applicable on dynamic apps only).</td>
</tr>
<tr>
    <td><CopyableCode code="daprConfig" /></td>
    <td><code>object</code></td>
    <td>Dapr configuration of the app.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultHostName" /></td>
    <td><code>string</code></td>
    <td>Default hostname of the app. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Property to configure various DNS related settings for a site.</td>
</tr>
<tr>
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>true if the app is enabled; otherwise, false. Setting this value to false disables the app (takes the app offline).</td>
</tr>
<tr>
    <td><CopyableCode code="enabledHostNames" /></td>
    <td><code>array</code></td>
    <td>Enabled hostnames for the app.Hostnames need to be assigned (see HostNames) AND enabled. Otherwise, the app is not served on those hostnames.</td>
</tr>
<tr>
    <td><CopyableCode code="endToEndEncryptionEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to use end to end encryption between the FrontEnd and the Worker.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedLocation" /></td>
    <td><code>object</code></td>
    <td>Extended Location.</td>
</tr>
<tr>
    <td><CopyableCode code="functionAppConfig" /></td>
    <td><code>object</code></td>
    <td>Configuration specific of the Azure Function app.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNameSslStates" /></td>
    <td><code>array</code></td>
    <td>Hostname SSL states are used to manage the SSL bindings for app's hostnames.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNames" /></td>
    <td><code>array</code></td>
    <td>Hostnames associated with the app.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNamesDisabled" /></td>
    <td><code>boolean</code></td>
    <td>true to disable the public hostnames of the app; otherwise, false. If true, the app is only accessible via API management process.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>App Service Environment to use for the app.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsOnly" /></td>
    <td><code>boolean</code></td>
    <td>HttpsOnly: configures a web site to accept only https requests. Issues redirect for http requests.</td>
</tr>
<tr>
    <td><CopyableCode code="hyperV" /></td>
    <td><code>boolean</code></td>
    <td>Hyper-V sandbox.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity.</td>
</tr>
<tr>
    <td><CopyableCode code="inProgressOperationId" /></td>
    <td><code>string</code></td>
    <td>Specifies an operation id if this site has a pending operation.</td>
</tr>
<tr>
    <td><CopyableCode code="ipMode" /></td>
    <td><code>string</code></td>
    <td>Specifies the IP mode of the app. Known values are: "IPv4", "IPv6", and "IPv4AndIPv6". (IPv4, IPv6, IPv4AndIPv6)</td>
</tr>
<tr>
    <td><CopyableCode code="isDefaultContainer" /></td>
    <td><code>boolean</code></td>
    <td>true if the app is a default container; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="isXenon" /></td>
    <td><code>boolean</code></td>
    <td>Obsolete: Hyper-V sandbox.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultReferenceIdentity" /></td>
    <td><code>string</code></td>
    <td>Identity to use for Key Vault Reference authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time the app was modified, in UTC. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedEnvironmentId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager ID of the customer's selected Managed Environment on which to host this app. This must be of the form /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroup&#125;/providers/Microsoft.App/managedEnvironments/&#123;managedEnvironmentName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="maxNumberOfWorkers" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of workers. This only applies to Functions container.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundIpAddresses" /></td>
    <td><code>string</code></td>
    <td>List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from tenants that site can be hosted with current settings. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="outboundVnetRouting" /></td>
    <td><code>object</code></td>
    <td>Property to configure various outbound traffic routing options over virtual network for a site.</td>
</tr>
<tr>
    <td><CopyableCode code="possibleOutboundIpAddresses" /></td>
    <td><code>string</code></td>
    <td>List of IP addresses that the app uses for outbound connections (e.g. database access). Includes VIPs from all tenants except dataComponent. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Property to allow or block all public traffic. Allowed Values: 'Enabled', 'Disabled' or an empty string.</td>
</tr>
<tr>
    <td><CopyableCode code="redundancyMode" /></td>
    <td><code>string</code></td>
    <td>Site redundancy mode. Known values are: "None", "Manual", "Failover", "ActiveActive", and "GeoRedundant". (None, Manual, Failover, ActiveActive, GeoRedundant)</td>
</tr>
<tr>
    <td><CopyableCode code="repositorySiteName" /></td>
    <td><code>string</code></td>
    <td>Name of the repository site.</td>
</tr>
<tr>
    <td><CopyableCode code="reserved" /></td>
    <td><code>boolean</code></td>
    <td>true if reserved; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceConfig" /></td>
    <td><code>object</code></td>
    <td>Function app resource requirements.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceGroup" /></td>
    <td><code>string</code></td>
    <td>Name of the resource group the app belongs to. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="scmSiteAlsoStopped" /></td>
    <td><code>boolean</code></td>
    <td>true to stop SCM (KUDU) site when the app is stopped; otherwise, false. The default is false.</td>
</tr>
<tr>
    <td><CopyableCode code="serverFarmId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the associated App Service plan, formatted as: "/subscriptions/&#123;subscriptionID&#125;/resourceGroups/&#123;groupName&#125;/providers/Microsoft.Web/serverfarms/&#123;appServicePlanName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="siteConfig" /></td>
    <td><code>object</code></td>
    <td>Configuration of an App Service app. This property is not returned in response to normal create and read requests since it may contain sensitive information.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>Current SKU of application based on associated App Service Plan. Some valid SKU values are Free, Shared, Basic, Dynamic, FlexConsumption, Standard, Premium, PremiumV2, PremiumV3, Isolated, IsolatedV2.</td>
</tr>
<tr>
    <td><CopyableCode code="slotSwapStatus" /></td>
    <td><code>object</code></td>
    <td>Status of the last deployment slot swap operation.</td>
</tr>
<tr>
    <td><CopyableCode code="sshEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable ssh access.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Current state of the app.</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountRequired" /></td>
    <td><code>boolean</code></td>
    <td>Checks if Customer provided storage account is required.</td>
</tr>
<tr>
    <td><CopyableCode code="suspendedTill" /></td>
    <td><code>string (date-time)</code></td>
    <td>App suspended till in case memory-time quota is exceeded.</td>
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
    <td><CopyableCode code="targetSwapSlot" /></td>
    <td><code>string</code></td>
    <td>Specifies which deployment slot this app will swap into. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficManagerHostNames" /></td>
    <td><code>array</code></td>
    <td>Azure Traffic Manager hostnames associated with the app. Read-only.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="usageState" /></td>
    <td><code>string</code></td>
    <td>State indicating whether the app has exceeded its quota usage. Read-only. Known values are: "Normal" and "Exceeded". (Normal, Exceeded)</td>
</tr>
<tr>
    <td><CopyableCode code="virtualNetworkSubnetId" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager ID of the Virtual network and subnet to be joined by Regional VNET Integration. This must be of the form /subscriptions/&#123;subscriptionName&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/virtualNetworks/&#123;vnetName&#125;/subnets/&#123;subnetName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="workloadProfileName" /></td>
    <td><code>string</code></td>
    <td>Workload profile name for function app to execute on.</td>
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
    <td><a href="#get_instance_process_module_slot"><CopyableCode code="get_instance_process_module_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-base_address"><code>base_address</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_slot_differences_slot"><CopyableCode code="list_slot_differences_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the difference in configuration settings between two web app slots. Description for Get the difference in configuration settings between two web app slots.</td>
</tr>
<tr>
    <td><a href="#list_instance_process_threads_slot"><CopyableCode code="list_instance_process_threads_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the threads in a process by its ID for a specific scaled-out instance in a web site. Description for List the threads in a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_hybrid_connection_slot"><CopyableCode code="get_hybrid_connection_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a specific Service Bus Hybrid Connection used by this Web App. Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App.</td>
</tr>
<tr>
    <td><a href="#get_vnet_connection_gateway_slot"><CopyableCode code="get_vnet_connection_gateway_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an app's Virtual Network gateway. Description for Gets an app's Virtual Network gateway.</td>
</tr>
<tr>
    <td><a href="#get_instance_process_module"><CopyableCode code="get_instance_process_module" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-base_address"><code>base_address</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_process_module_slot"><CopyableCode code="get_process_module_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-base_address"><code>base_address</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_triggered_web_job_history_slot"><CopyableCode code="get_triggered_web_job_history_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a triggered web job's history by its ID for an app, , or a deployment slot. Description for Gets a triggered web job's history by its ID for an app, , or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_slot_differences_from_production"><CopyableCode code="list_slot_differences_from_production" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the difference in configuration settings between two web app slots. Description for Get the difference in configuration settings between two web app slots.</td>
</tr>
<tr>
    <td><a href="#list_backup_status_secrets_slot"><CopyableCode code="list_backup_status_secrets_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-backup_id"><code>backup_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body. Description for Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.</td>
</tr>
<tr>
    <td><a href="#list_deployment_log_slot"><CopyableCode code="list_deployment_log_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List deployment log for specific deployment for an app, or a deployment slot. Description for List deployment log for specific deployment for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_function_keys_slot"><CopyableCode code="list_function_keys_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get function keys for a function in a web site, or a deployment slot. Description for Get function keys for a function in a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_instance_process_threads"><CopyableCode code="list_instance_process_threads" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the threads in a process by its ID for a specific scaled-out instance in a web site. Description for List the threads in a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_instance_processes_slot"><CopyableCode code="list_instance_processes_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_process_threads_slot"><CopyableCode code="list_process_threads_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the threads in a process by its ID for a specific scaled-out instance in a web site. Description for List the threads in a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_network_features_slot"><CopyableCode code="list_network_features_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-view_name"><code>view_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network features used by the app (or deployment slot, if specified). Description for Gets all network features used by the app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_triggered_web_job_history_slot"><CopyableCode code="list_triggered_web_job_history_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List a triggered web job's history for an app, or a deployment slot. Description for List a triggered web job's history for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_network_trace_operation_slot"><CopyableCode code="get_network_trace_operation_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection_slot"><CopyableCode code="get_private_endpoint_connection_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a private endpoint connection. Description for Gets a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#get_hybrid_connection"><CopyableCode code="get_hybrid_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves a specific Service Bus Hybrid Connection used by this Web App. Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App.</td>
</tr>
<tr>
    <td><a href="#get_vnet_connection_slot"><CopyableCode code="get_vnet_connection_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a virtual network the app (or deployment slot) is connected to by name. Description for Gets a virtual network the app (or deployment slot) is connected to by name.</td>
</tr>
<tr>
    <td><a href="#get_vnet_connection_gateway"><CopyableCode code="get_vnet_connection_gateway" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an app's Virtual Network gateway. Description for Gets an app's Virtual Network gateway.</td>
</tr>
<tr>
    <td><a href="#get_app_setting_key_vault_reference_slot"><CopyableCode code="get_app_setting_key_vault_reference_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-app_setting_key"><code>app_setting_key</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the config reference and status of an app. Description for Gets the config reference and status of an app.</td>
</tr>
<tr>
    <td><a href="#get_site_connection_string_key_vault_reference_slot"><CopyableCode code="get_site_connection_string_key_vault_reference_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-connection_string_key"><code>connection_string_key</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the config reference and status of an app. Description for Gets the config reference and status of an app.</td>
</tr>
<tr>
    <td><a href="#get_configuration_snapshot_slot"><CopyableCode code="get_configuration_snapshot_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-snapshot_id"><code>snapshot_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a snapshot of the configuration of an app at a previous point in time. Description for Gets a snapshot of the configuration of an app at a previous point in time.</td>
</tr>
<tr>
    <td><a href="#get_slot_site_deployment_status_slot"><CopyableCode code="get_slot_site_deployment_status_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-deployment_status_id"><code>deployment_status_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the deployment status for an app (or deployment slot, if specified). Gets the deployment status for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_domain_ownership_identifier_slot"><CopyableCode code="get_domain_ownership_identifier_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_ownership_identifier_name"><code>domain_ownership_identifier_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get domain ownership identifier for web app. Description for Get domain ownership identifier for web app.</td>
</tr>
<tr>
    <td><a href="#get_host_name_binding_slot"><CopyableCode code="get_host_name_binding_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the named hostname binding for an app (or deployment slot, if specified). Description for Get the named hostname binding for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_relay_service_connection_slot"><CopyableCode code="get_relay_service_connection_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a hybrid connection configuration by its name. Description for Gets a hybrid connection configuration by its name.</td>
</tr>
<tr>
    <td><a href="#get_process_module"><CopyableCode code="get_process_module" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-base_address"><code>base_address</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_premier_add_on_slot"><CopyableCode code="get_premier_add_on_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-premier_add_on_name"><code>premier_add_on_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named add-on of an app. Description for Gets a named add-on of an app.</td>
</tr>
<tr>
    <td><a href="#get_public_certificate_slot"><CopyableCode code="get_public_certificate_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-public_certificate_name"><code>public_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the named public certificate for an app (or deployment slot, if specified). Description for Get the named public certificate for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_site_container_slot"><CopyableCode code="get_site_container_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a site container of a site, or a deployment slot. Gets a site container of a site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_site_extension_slot"><CopyableCode code="get_site_extension_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-site_extension_id"><code>site_extension_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get site extension information by its ID for a web site, or a deployment slot. Description for Get site extension information by its ID for a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_triggered_web_job_history"><CopyableCode code="get_triggered_web_job_history" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a triggered web job's history by its ID for an app, , or a deployment slot. Description for Gets a triggered web job's history by its ID for an app, , or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_instance_workflow_slot"><CopyableCode code="get_instance_workflow_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get workflow information by its ID for web site, or a deployment slot. Get workflow information by its ID for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_application_settings_slot"><CopyableCode code="list_application_settings_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the application settings of an app. Description for Gets the application settings of an app.</td>
</tr>
<tr>
    <td><a href="#list_backup_status_secrets"><CopyableCode code="list_backup_status_secrets" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-backup_id"><code>backup_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body. Description for Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.</td>
</tr>
<tr>
    <td><a href="#list_deployment_log"><CopyableCode code="list_deployment_log" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List deployment log for specific deployment for an app, or a deployment slot. Description for List deployment log for specific deployment for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_function_keys"><CopyableCode code="list_function_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get function keys for a function in a web site, or a deployment slot. Description for Get function keys for a function in a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_instance_processes"><CopyableCode code="list_instance_processes" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_process_threads"><CopyableCode code="list_process_threads" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the threads in a process by its ID for a specific scaled-out instance in a web site. Description for List the threads in a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_network_features"><CopyableCode code="list_network_features" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-view_name"><code>view_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all network features used by the app (or deployment slot, if specified). Description for Gets all network features used by the app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_triggered_web_job_history"><CopyableCode code="list_triggered_web_job_history" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List a triggered web job's history for an app, or a deployment slot. Description for List a triggered web job's history for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection"><CopyableCode code="get_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a private endpoint connection. Description for Gets a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#get_vnet_connection"><CopyableCode code="get_vnet_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a virtual network the app (or deployment slot) is connected to by name. Description for Gets a virtual network the app (or deployment slot) is connected to by name.</td>
</tr>
<tr>
    <td><a href="#get_network_trace_operation"><CopyableCode code="get_network_trace_operation" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_app_setting_key_vault_reference"><CopyableCode code="get_app_setting_key_vault_reference" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-app_setting_key"><code>app_setting_key</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the config reference and status of an app. Description for Gets the config reference and status of an app.</td>
</tr>
<tr>
    <td><a href="#get_site_connection_string_key_vault_reference"><CopyableCode code="get_site_connection_string_key_vault_reference" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-connection_string_key"><code>connection_string_key</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the config reference and status of an app. Description for Gets the config reference and status of an app.</td>
</tr>
<tr>
    <td><a href="#get_configuration_snapshot"><CopyableCode code="get_configuration_snapshot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-snapshot_id"><code>snapshot_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a snapshot of the configuration of an app at a previous point in time. Description for Gets a snapshot of the configuration of an app at a previous point in time.</td>
</tr>
<tr>
    <td><a href="#get_production_site_deployment_status"><CopyableCode code="get_production_site_deployment_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-deployment_status_id"><code>deployment_status_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the deployment status for an app (or deployment slot, if specified). Gets the deployment status for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_domain_ownership_identifier"><CopyableCode code="get_domain_ownership_identifier" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_ownership_identifier_name"><code>domain_ownership_identifier_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get domain ownership identifier for web app. Description for Get domain ownership identifier for web app.</td>
</tr>
<tr>
    <td><a href="#get_host_name_binding"><CopyableCode code="get_host_name_binding" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the named hostname binding for an app (or deployment slot, if specified). Description for Get the named hostname binding for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_relay_service_connection"><CopyableCode code="get_relay_service_connection" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a hybrid connection configuration by its name. Description for Gets a hybrid connection configuration by its name.</td>
</tr>
<tr>
    <td><a href="#get_premier_add_on"><CopyableCode code="get_premier_add_on" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-premier_add_on_name"><code>premier_add_on_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named add-on of an app. Description for Gets a named add-on of an app.</td>
</tr>
<tr>
    <td><a href="#get_public_certificate"><CopyableCode code="get_public_certificate" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-public_certificate_name"><code>public_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the named public certificate for an app (or deployment slot, if specified). Description for Get the named public certificate for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_site_container"><CopyableCode code="get_site_container" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a site container of a site, or a deployment slot. Gets a site container of a site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_site_extension"><CopyableCode code="get_site_extension" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-site_extension_id"><code>site_extension_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get site extension information by its ID for a web site, or a deployment slot. Description for Get site extension information by its ID for a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_workflow"><CopyableCode code="get_workflow" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-workflow_name"><code>workflow_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get workflow information by its ID for web site, or a deployment slot. Get workflow information by its ID for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a web, mobile, or API app. Description for Gets the details of a web, mobile, or API app.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-includeSlots"><code>includeSlots</code></a></td>
    <td>Gets all web, mobile, and API apps in the specified resource group. Description for Gets all web, mobile, and API apps in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all apps for a subscription. Description for Get all apps for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteMetrics"><code>deleteMetrics</code></a>, <a href="#parameter-deleteEmptyServerFarm"><code>deleteEmptyServerFarm</code></a></td>
    <td>Deletes a web, mobile, or API app, or one of the deployment slots. Description for Deletes a web, mobile, or API app, or one of the deployment slots.</td>
</tr>
<tr>
    <td><a href="#list_slots"><CopyableCode code="list_slots" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an app's deployment slots. Description for Gets an app's deployment slots.</td>
</tr>
<tr>
    <td><a href="#list_azure_storage_accounts_slot"><CopyableCode code="list_azure_storage_accounts_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Azure storage account configurations of an app. Description for Gets the Azure storage account configurations of an app.</td>
</tr>
<tr>
    <td><a href="#list_connection_strings_slot"><CopyableCode code="list_connection_strings_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the connection strings of an app. Description for Gets the connection strings of an app.</td>
</tr>
<tr>
    <td><a href="#list_metadata_slot"><CopyableCode code="list_metadata_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the metadata of an app. Description for Gets the metadata of an app.</td>
</tr>
<tr>
    <td><a href="#list_publishing_credentials_slot"><CopyableCode code="list_publishing_credentials_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Git/FTP publishing credentials of an app. Description for Gets the Git/FTP publishing credentials of an app.</td>
</tr>
<tr>
    <td><a href="#list_site_push_settings_slot"><CopyableCode code="list_site_push_settings_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Push settings associated with web app. Description for Gets the Push settings associated with web app.</td>
</tr>
<tr>
    <td><a href="#list_host_keys_slot"><CopyableCode code="list_host_keys_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get host secrets for a function app. Description for Get host secrets for a function app.</td>
</tr>
<tr>
    <td><a href="#list_sync_status_slot"><CopyableCode code="list_sync_status_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This is to allow calling via powershell and ARM template. Description for This is to allow calling via powershell and ARM template.</td>
</tr>
<tr>
    <td><a href="#list_hybrid_connections_slot"><CopyableCode code="list_hybrid_connections_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves all Service Bus Hybrid Connections used by this Web App. Description for Retrieves all Service Bus Hybrid Connections used by this Web App.</td>
</tr>
<tr>
    <td><a href="#list_relay_service_connections_slot"><CopyableCode code="list_relay_service_connections_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets hybrid connections configured for an app (or deployment slot, if specified). Description for Gets hybrid connections configured for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_site_backups_slot"><CopyableCode code="list_site_backups_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets existing backups of an app. Description for Gets existing backups of an app.</td>
</tr>
<tr>
    <td><a href="#list_sync_function_triggers_slot"><CopyableCode code="list_sync_function_triggers_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This is to allow calling via powershell and ARM template. Description for This is to allow calling via powershell and ARM template.</td>
</tr>
<tr>
    <td><a href="#list_perf_mon_counters_slot"><CopyableCode code="list_perf_mon_counters_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets perfmon counters for web app. Description for Gets perfmon counters for web app.</td>
</tr>
<tr>
    <td><a href="#list_premier_add_ons_slot"><CopyableCode code="list_premier_add_ons_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the premier add-ons of an app. Description for Gets the premier add-ons of an app.</td>
</tr>
<tr>
    <td><a href="#list_publishing_profile_xml_with_secrets_slot"><CopyableCode code="list_publishing_profile_xml_with_secrets_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the publishing profile for an app (or deployment slot, if specified). Description for Gets the publishing profile for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_snapshots_slot"><CopyableCode code="list_snapshots_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all Snapshots to the user. Description for Returns all Snapshots to the user.</td>
</tr>
<tr>
    <td><a href="#list_snapshots_from_dr_secondary_slot"><CopyableCode code="list_snapshots_from_dr_secondary_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all Snapshots to the user from DRSecondary endpoint. Description for Returns all Snapshots to the user from DRSecondary endpoint.</td>
</tr>
<tr>
    <td><a href="#list_usages_slot"><CopyableCode code="list_usages_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets the quota usage information of an app (or deployment slot, if specified). Description for Gets the quota usage information of an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_workflows_connections_slot"><CopyableCode code="list_workflows_connections_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists logic app's connections for web site, or a deployment slot. Lists logic app's connections for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_vnet_connections_slot"><CopyableCode code="list_vnet_connections_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the virtual networks the app (or deployment slot) is connected to. Description for Gets the virtual networks the app (or deployment slot) is connected to.</td>
</tr>
<tr>
    <td><a href="#list_vnet_connections"><CopyableCode code="list_vnet_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the virtual networks the app (or deployment slot) is connected to. Description for Gets the virtual networks the app (or deployment slot) is connected to.</td>
</tr>
<tr>
    <td><a href="#list_application_settings"><CopyableCode code="list_application_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the application settings of an app. Description for Gets the application settings of an app.</td>
</tr>
<tr>
    <td><a href="#list_azure_storage_accounts"><CopyableCode code="list_azure_storage_accounts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Azure storage account configurations of an app. Description for Gets the Azure storage account configurations of an app.</td>
</tr>
<tr>
    <td><a href="#list_connection_strings"><CopyableCode code="list_connection_strings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the connection strings of an app. Description for Gets the connection strings of an app.</td>
</tr>
<tr>
    <td><a href="#list_metadata"><CopyableCode code="list_metadata" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the metadata of an app. Description for Gets the metadata of an app.</td>
</tr>
<tr>
    <td><a href="#list_publishing_credentials"><CopyableCode code="list_publishing_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Git/FTP publishing credentials of an app. Description for Gets the Git/FTP publishing credentials of an app.</td>
</tr>
<tr>
    <td><a href="#list_site_push_settings"><CopyableCode code="list_site_push_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Push settings associated with web app. Description for Gets the Push settings associated with web app.</td>
</tr>
<tr>
    <td><a href="#list_host_keys"><CopyableCode code="list_host_keys" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get host secrets for a function app. Description for Get host secrets for a function app.</td>
</tr>
<tr>
    <td><a href="#list_sync_status"><CopyableCode code="list_sync_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This is to allow calling via powershell and ARM template. Description for This is to allow calling via powershell and ARM template.</td>
</tr>
<tr>
    <td><a href="#list_hybrid_connections"><CopyableCode code="list_hybrid_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves all Service Bus Hybrid Connections used by this Web App. Description for Retrieves all Service Bus Hybrid Connections used by this Web App.</td>
</tr>
<tr>
    <td><a href="#list_relay_service_connections"><CopyableCode code="list_relay_service_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets hybrid connections configured for an app (or deployment slot, if specified). Description for Gets hybrid connections configured for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_site_backups"><CopyableCode code="list_site_backups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets existing backups of an app. Description for Gets existing backups of an app.</td>
</tr>
<tr>
    <td><a href="#list_sync_function_triggers"><CopyableCode code="list_sync_function_triggers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This is to allow calling via powershell and ARM template. Description for This is to allow calling via powershell and ARM template.</td>
</tr>
<tr>
    <td><a href="#list_perf_mon_counters"><CopyableCode code="list_perf_mon_counters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets perfmon counters for web app. Description for Gets perfmon counters for web app.</td>
</tr>
<tr>
    <td><a href="#list_premier_add_ons"><CopyableCode code="list_premier_add_ons" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the premier add-ons of an app. Description for Gets the premier add-ons of an app.</td>
</tr>
<tr>
    <td><a href="#list_publishing_profile_xml_with_secrets"><CopyableCode code="list_publishing_profile_xml_with_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the publishing profile for an app (or deployment slot, if specified). Description for Gets the publishing profile for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_snapshots"><CopyableCode code="list_snapshots" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all Snapshots to the user. Description for Returns all Snapshots to the user.</td>
</tr>
<tr>
    <td><a href="#list_snapshots_from_dr_secondary"><CopyableCode code="list_snapshots_from_dr_secondary" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all Snapshots to the user from DRSecondary endpoint. Description for Returns all Snapshots to the user from DRSecondary endpoint.</td>
</tr>
<tr>
    <td><a href="#list_usages"><CopyableCode code="list_usages" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets the quota usage information of an app (or deployment slot, if specified). Description for Gets the quota usage information of an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_workflows_connections"><CopyableCode code="list_workflows_connections" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists logic app's connections for web site, or a deployment slot. Lists logic app's connections for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_backups"><CopyableCode code="list_backups" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets existing backups of an app. Description for Gets existing backups of an app.</td>
</tr>
<tr>
    <td><a href="#list_backups_slot"><CopyableCode code="list_backups_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets existing backups of an app. Description for Gets existing backups of an app.</td>
</tr>
<tr>
    <td><a href="#list_basic_publishing_credentials_policies"><CopyableCode code="list_basic_publishing_credentials_policies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site. Description for Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site.</td>
</tr>
<tr>
    <td><a href="#list_basic_publishing_credentials_policies_slot"><CopyableCode code="list_basic_publishing_credentials_policies_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site. Description for Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site.</td>
</tr>
<tr>
    <td><a href="#list_slot_configuration_names"><CopyableCode code="list_slot_configuration_names" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the names of app settings and connection strings that stick to the slot (not swapped). Description for Gets the names of app settings and connection strings that stick to the slot (not swapped).</td>
</tr>
<tr>
    <td><a href="#update_slot_configuration_names"><CopyableCode code="update_slot_configuration_names" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the names of application settings and connection string that remain with the slot during swap operation. Description for Updates the names of application settings and connection string that remain with the slot during swap operation.</td>
</tr>
<tr>
    <td><a href="#list_configuration_snapshot_info"><CopyableCode code="list_configuration_snapshot_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot. Description for Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.</td>
</tr>
<tr>
    <td><a href="#list_configurations"><CopyableCode code="list_configurations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the configurations of an app. Description for List the configurations of an app.</td>
</tr>
<tr>
    <td><a href="#list_configuration_snapshot_info_slot"><CopyableCode code="list_configuration_snapshot_info_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot. Description for Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.</td>
</tr>
<tr>
    <td><a href="#list_configurations_slot"><CopyableCode code="list_configurations_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the configurations of an app. Description for List the configurations of an app.</td>
</tr>
<tr>
    <td><a href="#list_continuous_web_jobs"><CopyableCode code="list_continuous_web_jobs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List continuous web jobs for an app, or a deployment slot. Description for List continuous web jobs for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_continuous_web_jobs_slot"><CopyableCode code="list_continuous_web_jobs_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List continuous web jobs for an app, or a deployment slot. Description for List continuous web jobs for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_production_site_deployment_statuses"><CopyableCode code="list_production_site_deployment_statuses" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List deployment statuses for an app (or deployment slot, if specified). List deployment statuses for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_slot_site_deployment_statuses_slot"><CopyableCode code="list_slot_site_deployment_statuses_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List deployment statuses for an app (or deployment slot, if specified). List deployment statuses for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#list_deployments"><CopyableCode code="list_deployments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List deployments for an app, or a deployment slot. Description for List deployments for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_deployments_slot"><CopyableCode code="list_deployments_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List deployments for an app, or a deployment slot. Description for List deployments for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_domain_ownership_identifiers"><CopyableCode code="list_domain_ownership_identifiers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists ownership identifiers for domain associated with web app. Description for Lists ownership identifiers for domain associated with web app.</td>
</tr>
<tr>
    <td><a href="#list_domain_ownership_identifiers_slot"><CopyableCode code="list_domain_ownership_identifiers_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists ownership identifiers for domain associated with web app. Description for Lists ownership identifiers for domain associated with web app.</td>
</tr>
<tr>
    <td><a href="#list_functions"><CopyableCode code="list_functions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the functions for a web site, or a deployment slot. Description for List the functions for a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_function_secrets"><CopyableCode code="list_function_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get function secrets for a function in a web site, or a deployment slot. Description for Get function secrets for a function in a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_instance_functions_slot"><CopyableCode code="list_instance_functions_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the functions for a web site, or a deployment slot. Description for List the functions for a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_function_secrets_slot"><CopyableCode code="list_function_secrets_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get function secrets for a function in a web site, or a deployment slot. Description for Get function secrets for a function in a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_host_name_bindings"><CopyableCode code="list_host_name_bindings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get hostname bindings for an app or a deployment slot. Description for Get hostname bindings for an app or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_host_name_bindings_slot"><CopyableCode code="list_host_name_bindings_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get hostname bindings for an app or a deployment slot. Description for Get hostname bindings for an app or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_instance_identifiers"><CopyableCode code="list_instance_identifiers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all scale-out instances of an app. Description for Gets all scale-out instances of an app.</td>
</tr>
<tr>
    <td><a href="#list_instance_identifiers_slot"><CopyableCode code="list_instance_identifiers_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all scale-out instances of an app. Description for Gets all scale-out instances of an app.</td>
</tr>
<tr>
    <td><a href="#list_processes"><CopyableCode code="list_processes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_processes_slot"><CopyableCode code="list_processes_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_instance_process_modules"><CopyableCode code="list_instance_process_modules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List module information for a process by its ID for a specific scaled-out instance in a web site. Description for List module information for a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_process_modules"><CopyableCode code="list_process_modules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List module information for a process by its ID for a specific scaled-out instance in a web site. Description for List module information for a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_instance_process_modules_slot"><CopyableCode code="list_instance_process_modules_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List module information for a process by its ID for a specific scaled-out instance in a web site. Description for List module information for a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_process_modules_slot"><CopyableCode code="list_process_modules_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List module information for a process by its ID for a specific scaled-out instance in a web site. Description for List module information for a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#list_public_certificates"><CopyableCode code="list_public_certificates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get public certificates for an app or a deployment slot. Description for Get public certificates for an app or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_public_certificates_slot"><CopyableCode code="list_public_certificates_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get public certificates for an app or a deployment slot. Description for Get public certificates for an app or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_site_containers"><CopyableCode code="list_site_containers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the site containers of a site, or a deployment slot. Lists all the site containers of a site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_site_containers_slot"><CopyableCode code="list_site_containers_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all the site containers of a site, or a deployment slot. Lists all the site containers of a site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_site_extensions"><CopyableCode code="list_site_extensions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get list of siteextensions for a web site, or a deployment slot. Description for Get list of siteextensions for a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_site_extensions_slot"><CopyableCode code="list_site_extensions_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get list of siteextensions for a web site, or a deployment slot. Description for Get list of siteextensions for a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_triggered_web_jobs_slot"><CopyableCode code="list_triggered_web_jobs_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List triggered web jobs for an app, or a deployment slot. Description for List triggered web jobs for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_triggered_web_jobs"><CopyableCode code="list_triggered_web_jobs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List triggered web jobs for an app, or a deployment slot. Description for List triggered web jobs for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_web_jobs_slot"><CopyableCode code="list_web_jobs_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List webjobs for an app, or a deployment slot. Description for List webjobs for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_web_jobs"><CopyableCode code="list_web_jobs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List webjobs for an app, or a deployment slot. Description for List webjobs for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_instance_workflows_slot"><CopyableCode code="list_instance_workflows_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the workflows for a web site, or a deployment slot. List the workflows for a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list_workflows"><CopyableCode code="list_workflows" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the workflows for a web site, or a deployment slot. List the workflows for a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_slot"><CopyableCode code="get_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a web, mobile, or API app. Description for Gets the details of a web, mobile, or API app.</td>
</tr>
<tr>
    <td><a href="#create_or_update_slot"><CopyableCode code="create_or_update_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.</td>
</tr>
<tr>
    <td><a href="#update_slot"><CopyableCode code="update_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.</td>
</tr>
<tr>
    <td><a href="#delete_slot"><CopyableCode code="delete_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteMetrics"><code>deleteMetrics</code></a>, <a href="#parameter-deleteEmptyServerFarm"><code>deleteEmptyServerFarm</code></a></td>
    <td>Deletes a web, mobile, or API app, or one of the deployment slots. Description for Deletes a web, mobile, or API app, or one of the deployment slots.</td>
</tr>
<tr>
    <td><a href="#get_auth_settings_slot"><CopyableCode code="get_auth_settings_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Authentication/Authorization settings of an app. Description for Gets the Authentication/Authorization settings of an app.</td>
</tr>
<tr>
    <td><a href="#get_backup_configuration_slot"><CopyableCode code="get_backup_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the backup configuration of an app. Description for Gets the backup configuration of an app.</td>
</tr>
<tr>
    <td><a href="#get_web_site_container_logs_slot"><CopyableCode code="get_web_site_container_logs_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the last lines of docker logs for the given site. Description for Gets the last lines of docker logs for the given site.</td>
</tr>
<tr>
    <td><a href="#get_container_logs_zip_slot"><CopyableCode code="get_container_logs_zip_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the ZIP archived docker log files for the given site. Description for Gets the ZIP archived docker log files for the given site.</td>
</tr>
<tr>
    <td><a href="#get_functions_admin_token_slot"><CopyableCode code="get_functions_admin_token_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetch a short lived token that can be exchanged for a master key. Description for Fetch a short lived token that can be exchanged for a master key.</td>
</tr>
<tr>
    <td><a href="#get_network_traces_slot"><CopyableCode code="get_network_traces_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_network_trace_operation_slot_v2"><CopyableCode code="get_network_trace_operation_slot_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_network_traces_slot_v2"><CopyableCode code="get_network_traces_slot_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_site_php_error_log_flag_slot"><CopyableCode code="get_site_php_error_log_flag_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets web app's event logs. Description for Gets web app's event logs.</td>
</tr>
<tr>
    <td><a href="#get_private_link_resources_slot"><CopyableCode code="get_private_link_resources_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the private link resources. Description for Gets the private link resources.</td>
</tr>
<tr>
    <td><a href="#approve_or_reject_private_endpoint_connection"><CopyableCode code="approve_or_reject_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Approves or rejects a private endpoint connection. Description for Approves or rejects a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#delete_private_endpoint_connection"><CopyableCode code="delete_private_endpoint_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a private endpoint connection. Description for Deletes a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection_list"><CopyableCode code="get_private_endpoint_connection_list" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of private endpoint connections associated with a site. Description for Gets the list of private endpoint connections associated with a site.</td>
</tr>
<tr>
    <td><a href="#approve_or_reject_private_endpoint_connection_slot"><CopyableCode code="approve_or_reject_private_endpoint_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Approves or rejects a private endpoint connection. Description for Approves or rejects a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#delete_private_endpoint_connection_slot"><CopyableCode code="delete_private_endpoint_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-private_endpoint_connection_name"><code>private_endpoint_connection_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a private endpoint connection. Description for Deletes a private endpoint connection.</td>
</tr>
<tr>
    <td><a href="#get_private_endpoint_connection_list_slot"><CopyableCode code="get_private_endpoint_connection_list_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of private endpoint connections associated with a site. Description for Gets the list of private endpoint connections associated with a site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_hybrid_connection"><CopyableCode code="create_or_update_hybrid_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Hybrid Connection using a Service Bus relay. Description for Creates a new Hybrid Connection using a Service Bus relay.</td>
</tr>
<tr>
    <td><a href="#update_hybrid_connection"><CopyableCode code="update_hybrid_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Hybrid Connection using a Service Bus relay. Description for Creates a new Hybrid Connection using a Service Bus relay.</td>
</tr>
<tr>
    <td><a href="#delete_hybrid_connection"><CopyableCode code="delete_hybrid_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Removes a Hybrid Connection from this site. Description for Removes a Hybrid Connection from this site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_hybrid_connection_slot"><CopyableCode code="create_or_update_hybrid_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Hybrid Connection using a Service Bus relay. Description for Creates a new Hybrid Connection using a Service Bus relay.</td>
</tr>
<tr>
    <td><a href="#update_hybrid_connection_slot"><CopyableCode code="update_hybrid_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new Hybrid Connection using a Service Bus relay. Description for Creates a new Hybrid Connection using a Service Bus relay.</td>
</tr>
<tr>
    <td><a href="#delete_hybrid_connection_slot"><CopyableCode code="delete_hybrid_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-relay_name"><code>relay_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Removes a Hybrid Connection from this site. Description for Removes a Hybrid Connection from this site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_vnet_connection_slot"><CopyableCode code="create_or_update_vnet_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).</td>
</tr>
<tr>
    <td><a href="#update_vnet_connection_slot"><CopyableCode code="update_vnet_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).</td>
</tr>
<tr>
    <td><a href="#delete_vnet_connection_slot"><CopyableCode code="delete_vnet_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a connection from an app (or deployment slot to a named virtual network. Description for Deletes a connection from an app (or deployment slot to a named virtual network.</td>
</tr>
<tr>
    <td><a href="#create_or_update_vnet_connection"><CopyableCode code="create_or_update_vnet_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).</td>
</tr>
<tr>
    <td><a href="#update_vnet_connection"><CopyableCode code="update_vnet_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).</td>
</tr>
<tr>
    <td><a href="#delete_vnet_connection"><CopyableCode code="delete_vnet_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a connection from an app (or deployment slot to a named virtual network. Description for Deletes a connection from an app (or deployment slot to a named virtual network.</td>
</tr>
<tr>
    <td><a href="#create_or_update_vnet_connection_gateway_slot"><CopyableCode code="create_or_update_vnet_connection_gateway_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).</td>
</tr>
<tr>
    <td><a href="#update_vnet_connection_gateway_slot"><CopyableCode code="update_vnet_connection_gateway_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).</td>
</tr>
<tr>
    <td><a href="#create_or_update_vnet_connection_gateway"><CopyableCode code="create_or_update_vnet_connection_gateway" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).</td>
</tr>
<tr>
    <td><a href="#update_vnet_connection_gateway"><CopyableCode code="update_vnet_connection_gateway" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-vnet_name"><code>vnet_name</code></a>, <a href="#parameter-gateway_name"><code>gateway_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).</td>
</tr>
<tr>
    <td><a href="#get_auth_settings"><CopyableCode code="get_auth_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Authentication/Authorization settings of an app. Description for Gets the Authentication/Authorization settings of an app.</td>
</tr>
<tr>
    <td><a href="#get_backup_configuration"><CopyableCode code="get_backup_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the backup configuration of an app. Description for Gets the backup configuration of an app.</td>
</tr>
<tr>
    <td><a href="#get_web_site_container_logs"><CopyableCode code="get_web_site_container_logs" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the last lines of docker logs for the given site. Description for Gets the last lines of docker logs for the given site.</td>
</tr>
<tr>
    <td><a href="#get_container_logs_zip"><CopyableCode code="get_container_logs_zip" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the ZIP archived docker log files for the given site. Description for Gets the ZIP archived docker log files for the given site.</td>
</tr>
<tr>
    <td><a href="#get_one_deploy_status"><CopyableCode code="get_one_deploy_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invoke onedeploy status API /api/deployments and gets the deployment status for the site. Description for Invoke onedeploy status API /api/deployments and gets the deployment status for the site.</td>
</tr>
<tr>
    <td><a href="#create_one_deploy_operation"><CopyableCode code="create_one_deploy_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invoke the OneDeploy publish web app extension. Description for Invoke the OneDeploy publish web app extension.</td>
</tr>
<tr>
    <td><a href="#get_functions_admin_token"><CopyableCode code="get_functions_admin_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetch a short lived token that can be exchanged for a master key. Description for Fetch a short lived token that can be exchanged for a master key.</td>
</tr>
<tr>
    <td><a href="#get_network_traces"><CopyableCode code="get_network_traces" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_network_trace_operation_v2"><CopyableCode code="get_network_trace_operation_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_network_traces_v2"><CopyableCode code="get_network_traces_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#get_site_php_error_log_flag"><CopyableCode code="get_site_php_error_log_flag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets web app's event logs. Description for Gets web app's event logs.</td>
</tr>
<tr>
    <td><a href="#get_private_link_resources"><CopyableCode code="get_private_link_resources" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the private link resources. Description for Gets the private link resources.</td>
</tr>
<tr>
    <td><a href="#get_backup_status"><CopyableCode code="get_backup_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-backup_id"><code>backup_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a backup of an app by its ID. Description for Gets a backup of an app by its ID.</td>
</tr>
<tr>
    <td><a href="#delete_backup"><CopyableCode code="delete_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-backup_id"><code>backup_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a backup of an app by its ID. Description for Deletes a backup of an app by its ID.</td>
</tr>
<tr>
    <td><a href="#get_backup_status_slot"><CopyableCode code="get_backup_status_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-backup_id"><code>backup_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a backup of an app by its ID. Description for Gets a backup of an app by its ID.</td>
</tr>
<tr>
    <td><a href="#delete_backup_slot"><CopyableCode code="delete_backup_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-backup_id"><code>backup_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a backup of an app by its ID. Description for Deletes a backup of an app by its ID.</td>
</tr>
<tr>
    <td><a href="#get_ftp_allowed"><CopyableCode code="get_ftp_allowed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns whether FTP is allowed on the site or not. Description for Returns whether FTP is allowed on the site or not.</td>
</tr>
<tr>
    <td><a href="#update_ftp_allowed"><CopyableCode code="update_ftp_allowed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates whether FTP is allowed on the site or not. Description for Updates whether FTP is allowed on the site or not.</td>
</tr>
<tr>
    <td><a href="#get_scm_allowed"><CopyableCode code="get_scm_allowed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns whether Scm basic auth is allowed on the site or not. Description for Returns whether Scm basic auth is allowed on the site or not.</td>
</tr>
<tr>
    <td><a href="#update_scm_allowed"><CopyableCode code="update_scm_allowed" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates whether user publishing credentials are allowed on the site or not. Description for Updates whether user publishing credentials are allowed on the site or not.</td>
</tr>
<tr>
    <td><a href="#get_ftp_allowed_slot"><CopyableCode code="get_ftp_allowed_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns whether FTP is allowed on the site or not. Description for Returns whether FTP is allowed on the site or not.</td>
</tr>
<tr>
    <td><a href="#update_ftp_allowed_slot"><CopyableCode code="update_ftp_allowed_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates whether FTP is allowed on the site or not. Description for Updates whether FTP is allowed on the site or not.</td>
</tr>
<tr>
    <td><a href="#get_scm_allowed_slot"><CopyableCode code="get_scm_allowed_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns whether Scm basic auth is allowed on the site or not. Description for Returns whether Scm basic auth is allowed on the site or not.</td>
</tr>
<tr>
    <td><a href="#update_scm_allowed_slot"><CopyableCode code="update_scm_allowed_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates whether user publishing credentials are allowed on the site or not. Description for Updates whether user publishing credentials are allowed on the site or not.</td>
</tr>
<tr>
    <td><a href="#get_auth_settings_v2_without_secrets"><CopyableCode code="get_auth_settings_v2_without_secrets" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets site's Authentication / Authorization settings for apps via the V2 format. Description for Gets site's Authentication / Authorization settings for apps via the V2 format.</td>
</tr>
<tr>
    <td><a href="#update_auth_settings_v2"><CopyableCode code="update_auth_settings_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates site's Authentication / Authorization settings for apps via the V2 format. Description for Updates site's Authentication / Authorization settings for apps via the V2 format.</td>
</tr>
<tr>
    <td><a href="#get_auth_settings_v2"><CopyableCode code="get_auth_settings_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets site's Authentication / Authorization settings for apps via the V2 format. Description for Gets site's Authentication / Authorization settings for apps via the V2 format.</td>
</tr>
<tr>
    <td><a href="#get_auth_settings_v2_without_secrets_slot"><CopyableCode code="get_auth_settings_v2_without_secrets_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets site's Authentication / Authorization settings for apps via the V2 format. Gets site's Authentication / Authorization settings for apps via the V2 format.</td>
</tr>
<tr>
    <td><a href="#update_auth_settings_v2_slot"><CopyableCode code="update_auth_settings_v2_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates site's Authentication / Authorization settings for apps via the V2 format. Description for Updates site's Authentication / Authorization settings for apps via the V2 format.</td>
</tr>
<tr>
    <td><a href="#get_auth_settings_v2_slot"><CopyableCode code="get_auth_settings_v2_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets site's Authentication / Authorization settings for apps via the V2 format. Description for Gets site's Authentication / Authorization settings for apps via the V2 format.</td>
</tr>
<tr>
    <td><a href="#get_app_settings_key_vault_references"><CopyableCode code="get_app_settings_key_vault_references" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the config reference app settings and status of an app. Description for Gets the config reference app settings and status of an app.</td>
</tr>
<tr>
    <td><a href="#get_site_connection_string_key_vault_references"><CopyableCode code="get_site_connection_string_key_vault_references" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the config reference app settings and status of an app. Description for Gets the config reference app settings and status of an app.</td>
</tr>
<tr>
    <td><a href="#get_app_settings_key_vault_references_slot"><CopyableCode code="get_app_settings_key_vault_references_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the config reference app settings and status of an app. Description for Gets the config reference app settings and status of an app.</td>
</tr>
<tr>
    <td><a href="#get_site_connection_string_key_vault_references_slot"><CopyableCode code="get_site_connection_string_key_vault_references_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the config reference app settings and status of an app. Description for Gets the config reference app settings and status of an app.</td>
</tr>
<tr>
    <td><a href="#get_diagnostic_logs_configuration"><CopyableCode code="get_diagnostic_logs_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the logging configuration of an app. Description for Gets the logging configuration of an app.</td>
</tr>
<tr>
    <td><a href="#update_diagnostic_logs_config"><CopyableCode code="update_diagnostic_logs_config" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the logging configuration of an app. Description for Updates the logging configuration of an app.</td>
</tr>
<tr>
    <td><a href="#get_diagnostic_logs_configuration_slot"><CopyableCode code="get_diagnostic_logs_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the logging configuration of an app. Description for Gets the logging configuration of an app.</td>
</tr>
<tr>
    <td><a href="#update_diagnostic_logs_config_slot"><CopyableCode code="update_diagnostic_logs_config_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the logging configuration of an app. Description for Updates the logging configuration of an app.</td>
</tr>
<tr>
    <td><a href="#get_configuration"><CopyableCode code="get_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc. Description for Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.</td>
</tr>
<tr>
    <td><a href="#create_or_update_configuration"><CopyableCode code="create_or_update_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the configuration of an app. Description for Updates the configuration of an app.</td>
</tr>
<tr>
    <td><a href="#update_configuration"><CopyableCode code="update_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the configuration of an app. Description for Updates the configuration of an app.</td>
</tr>
<tr>
    <td><a href="#get_configuration_slot"><CopyableCode code="get_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc. Description for Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.</td>
</tr>
<tr>
    <td><a href="#create_or_update_configuration_slot"><CopyableCode code="create_or_update_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the configuration of an app. Description for Updates the configuration of an app.</td>
</tr>
<tr>
    <td><a href="#update_configuration_slot"><CopyableCode code="update_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the configuration of an app. Description for Updates the configuration of an app.</td>
</tr>
<tr>
    <td><a href="#get_continuous_web_job"><CopyableCode code="get_continuous_web_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a continuous web job by its ID for an app, or a deployment slot. Description for Gets a continuous web job by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_continuous_web_job"><CopyableCode code="delete_continuous_web_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a continuous web job by its ID for an app, or a deployment slot. Description for Delete a continuous web job by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_continuous_web_job_slot"><CopyableCode code="get_continuous_web_job_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a continuous web job by its ID for an app, or a deployment slot. Description for Gets a continuous web job by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_continuous_web_job_slot"><CopyableCode code="delete_continuous_web_job_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a continuous web job by its ID for an app, or a deployment slot. Description for Delete a continuous web job by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_deployment"><CopyableCode code="get_deployment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a deployment by its ID for an app, or a deployment slot. Description for Get a deployment by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_deployment"><CopyableCode code="create_deployment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a deployment for an app, or a deployment slot. Description for Create a deployment for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_deployment"><CopyableCode code="delete_deployment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a deployment by its ID for an app, or a deployment slot. Description for Delete a deployment by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_deployment_slot"><CopyableCode code="get_deployment_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a deployment by its ID for an app, or a deployment slot. Description for Get a deployment by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_deployment_slot"><CopyableCode code="create_deployment_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a deployment for an app, or a deployment slot. Description for Create a deployment for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_deployment_slot"><CopyableCode code="delete_deployment_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a deployment by its ID for an app, or a deployment slot. Description for Delete a deployment by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_or_update_domain_ownership_identifier"><CopyableCode code="create_or_update_domain_ownership_identifier" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_ownership_identifier_name"><code>domain_ownership_identifier_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a domain ownership identifier for web app, or updates an existing ownership identifier. Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier.</td>
</tr>
<tr>
    <td><a href="#update_domain_ownership_identifier"><CopyableCode code="update_domain_ownership_identifier" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_ownership_identifier_name"><code>domain_ownership_identifier_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a domain ownership identifier for web app, or updates an existing ownership identifier. Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier.</td>
</tr>
<tr>
    <td><a href="#delete_domain_ownership_identifier"><CopyableCode code="delete_domain_ownership_identifier" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_ownership_identifier_name"><code>domain_ownership_identifier_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a domain ownership identifier for a web app. Description for Deletes a domain ownership identifier for a web app.</td>
</tr>
<tr>
    <td><a href="#create_or_update_domain_ownership_identifier_slot"><CopyableCode code="create_or_update_domain_ownership_identifier_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_ownership_identifier_name"><code>domain_ownership_identifier_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a domain ownership identifier for web app, or updates an existing ownership identifier. Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier.</td>
</tr>
<tr>
    <td><a href="#update_domain_ownership_identifier_slot"><CopyableCode code="update_domain_ownership_identifier_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_ownership_identifier_name"><code>domain_ownership_identifier_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a domain ownership identifier for web app, or updates an existing ownership identifier. Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier.</td>
</tr>
<tr>
    <td><a href="#delete_domain_ownership_identifier_slot"><CopyableCode code="delete_domain_ownership_identifier_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-domain_ownership_identifier_name"><code>domain_ownership_identifier_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a domain ownership identifier for a web app. Description for Deletes a domain ownership identifier for a web app.</td>
</tr>
<tr>
    <td><a href="#get_ms_deploy_status"><CopyableCode code="get_ms_deploy_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of the last MSDeploy operation. Description for Get the status of the last MSDeploy operation.</td>
</tr>
<tr>
    <td><a href="#create_ms_deploy_operation"><CopyableCode code="create_ms_deploy_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invoke the MSDeploy web app extension. Description for Invoke the MSDeploy web app extension.</td>
</tr>
<tr>
    <td><a href="#get_ms_deploy_log"><CopyableCode code="get_ms_deploy_log" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the MSDeploy Log for the last MSDeploy operation. Description for Get the MSDeploy Log for the last MSDeploy operation.</td>
</tr>
<tr>
    <td><a href="#get_instance_ms_deploy_status"><CopyableCode code="get_instance_ms_deploy_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of the last MSDeploy operation. Description for Get the status of the last MSDeploy operation.</td>
</tr>
<tr>
    <td><a href="#create_instance_ms_deploy_operation"><CopyableCode code="create_instance_ms_deploy_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invoke the MSDeploy web app extension. Description for Invoke the MSDeploy web app extension.</td>
</tr>
<tr>
    <td><a href="#get_instance_ms_deploy_log"><CopyableCode code="get_instance_ms_deploy_log" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the MSDeploy Log for the last MSDeploy operation. Description for Get the MSDeploy Log for the last MSDeploy operation.</td>
</tr>
<tr>
    <td><a href="#get_ms_deploy_status_slot"><CopyableCode code="get_ms_deploy_status_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of the last MSDeploy operation. Description for Get the status of the last MSDeploy operation.</td>
</tr>
<tr>
    <td><a href="#create_ms_deploy_operation_slot"><CopyableCode code="create_ms_deploy_operation_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invoke the MSDeploy web app extension. Description for Invoke the MSDeploy web app extension.</td>
</tr>
<tr>
    <td><a href="#get_ms_deploy_log_slot"><CopyableCode code="get_ms_deploy_log_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the MSDeploy Log for the last MSDeploy operation. Description for Get the MSDeploy Log for the last MSDeploy operation.</td>
</tr>
<tr>
    <td><a href="#get_instance_ms_deploy_status_slot"><CopyableCode code="get_instance_ms_deploy_status_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the status of the last MSDeploy operation. Description for Get the status of the last MSDeploy operation.</td>
</tr>
<tr>
    <td><a href="#create_instance_ms_deploy_operation_slot"><CopyableCode code="create_instance_ms_deploy_operation_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invoke the MSDeploy web app extension. Description for Invoke the MSDeploy web app extension.</td>
</tr>
<tr>
    <td><a href="#get_instance_ms_deploy_log_slot"><CopyableCode code="get_instance_ms_deploy_log_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the MSDeploy Log for the last MSDeploy operation. Description for Get the MSDeploy Log for the last MSDeploy operation.</td>
</tr>
<tr>
    <td><a href="#get_function"><CopyableCode code="get_function" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get function information by its ID for web site, or a deployment slot. Description for Get function information by its ID for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_function"><CopyableCode code="create_function" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create function for web site, or a deployment slot. Description for Create function for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_function"><CopyableCode code="delete_function" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a function for web site, or a deployment slot. Description for Delete a function for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_instance_function_slot"><CopyableCode code="get_instance_function_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get function information by its ID for web site, or a deployment slot. Description for Get function information by its ID for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_instance_function_slot"><CopyableCode code="create_instance_function_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create function for web site, or a deployment slot. Description for Create function for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_instance_function_slot"><CopyableCode code="delete_instance_function_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a function for web site, or a deployment slot. Description for Delete a function for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_or_update_host_name_binding"><CopyableCode code="create_or_update_host_name_binding" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a hostname binding for an app. Description for Creates a hostname binding for an app.</td>
</tr>
<tr>
    <td><a href="#delete_host_name_binding"><CopyableCode code="delete_host_name_binding" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a hostname binding for an app. Description for Deletes a hostname binding for an app.</td>
</tr>
<tr>
    <td><a href="#create_or_update_host_name_binding_slot"><CopyableCode code="create_or_update_host_name_binding_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a hostname binding for an app. Description for Creates a hostname binding for an app.</td>
</tr>
<tr>
    <td><a href="#delete_host_name_binding_slot"><CopyableCode code="delete_host_name_binding_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-host_name"><code>host_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a hostname binding for an app. Description for Deletes a hostname binding for an app.</td>
</tr>
<tr>
    <td><a href="#create_or_update_relay_service_connection"><CopyableCode code="create_or_update_relay_service_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).</td>
</tr>
<tr>
    <td><a href="#update_relay_service_connection"><CopyableCode code="update_relay_service_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).</td>
</tr>
<tr>
    <td><a href="#delete_relay_service_connection"><CopyableCode code="delete_relay_service_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a relay service connection by its name. Description for Deletes a relay service connection by its name.</td>
</tr>
<tr>
    <td><a href="#create_or_update_relay_service_connection_slot"><CopyableCode code="create_or_update_relay_service_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).</td>
</tr>
<tr>
    <td><a href="#update_relay_service_connection_slot"><CopyableCode code="update_relay_service_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).</td>
</tr>
<tr>
    <td><a href="#delete_relay_service_connection_slot"><CopyableCode code="delete_relay_service_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-entity_name"><code>entity_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a relay service connection by its name. Description for Deletes a relay service connection by its name.</td>
</tr>
<tr>
    <td><a href="#get_instance_info"><CopyableCode code="get_instance_info" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all scale-out instances of an app. Description for Gets all scale-out instances of an app.</td>
</tr>
<tr>
    <td><a href="#get_instance_info_slot"><CopyableCode code="get_instance_info_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all scale-out instances of an app. Description for Gets all scale-out instances of an app.</td>
</tr>
<tr>
    <td><a href="#get_instance_process"><CopyableCode code="get_instance_process" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#delete_instance_process"><CopyableCode code="delete_instance_process" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_instance_process_dump"><CopyableCode code="get_instance_process_dump" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_process"><CopyableCode code="get_process" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#delete_process"><CopyableCode code="delete_process" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_process_dump"><CopyableCode code="get_process_dump" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_instance_process_slot"><CopyableCode code="get_instance_process_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#delete_instance_process_slot"><CopyableCode code="delete_instance_process_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_instance_process_dump_slot"><CopyableCode code="get_instance_process_dump_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-instance_id"><code>instance_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_process_slot"><CopyableCode code="get_process_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#delete_process_slot"><CopyableCode code="delete_process_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_process_dump_slot"><CopyableCode code="get_process_dump_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-process_id"><code>process_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.</td>
</tr>
<tr>
    <td><a href="#get_migrate_my_sql_status"><CopyableCode code="get_migrate_my_sql_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled. Description for Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled.</td>
</tr>
<tr>
    <td><a href="#get_migrate_my_sql_status_slot"><CopyableCode code="get_migrate_my_sql_status_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled. Description for Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled.</td>
</tr>
<tr>
    <td><a href="#get_swift_virtual_network_connection"><CopyableCode code="get_swift_virtual_network_connection" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Swift Virtual Network connection. Description for Gets a Swift Virtual Network connection.</td>
</tr>
<tr>
    <td><a href="#create_or_update_swift_virtual_network_connection_with_check"><CopyableCode code="create_or_update_swift_virtual_network_connection_with_check" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in. Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.</td>
</tr>
<tr>
    <td><a href="#update_swift_virtual_network_connection_with_check"><CopyableCode code="update_swift_virtual_network_connection_with_check" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in. Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.</td>
</tr>
<tr>
    <td><a href="#delete_swift_virtual_network"><CopyableCode code="delete_swift_virtual_network" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Swift Virtual Network connection from an app (or deployment slot). Description for Deletes a Swift Virtual Network connection from an app (or deployment slot).</td>
</tr>
<tr>
    <td><a href="#get_swift_virtual_network_connection_slot"><CopyableCode code="get_swift_virtual_network_connection_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Swift Virtual Network connection. Description for Gets a Swift Virtual Network connection.</td>
</tr>
<tr>
    <td><a href="#create_or_update_swift_virtual_network_connection_with_check_slot"><CopyableCode code="create_or_update_swift_virtual_network_connection_with_check_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in. Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.</td>
</tr>
<tr>
    <td><a href="#update_swift_virtual_network_connection_with_check_slot"><CopyableCode code="update_swift_virtual_network_connection_with_check_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in. Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.</td>
</tr>
<tr>
    <td><a href="#delete_swift_virtual_network_slot"><CopyableCode code="delete_swift_virtual_network_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Swift Virtual Network connection from an app (or deployment slot). Description for Deletes a Swift Virtual Network connection from an app (or deployment slot).</td>
</tr>
<tr>
    <td><a href="#add_premier_add_on"><CopyableCode code="add_premier_add_on" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-premier_add_on_name"><code>premier_add_on_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Updates a named add-on of an app. Description for Updates a named add-on of an app.</td>
</tr>
<tr>
    <td><a href="#update_premier_add_on"><CopyableCode code="update_premier_add_on" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-premier_add_on_name"><code>premier_add_on_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a named add-on of an app. Description for Updates a named add-on of an app.</td>
</tr>
<tr>
    <td><a href="#delete_premier_add_on"><CopyableCode code="delete_premier_add_on" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-premier_add_on_name"><code>premier_add_on_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a premier add-on from an app. Description for Delete a premier add-on from an app.</td>
</tr>
<tr>
    <td><a href="#add_premier_add_on_slot"><CopyableCode code="add_premier_add_on_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-premier_add_on_name"><code>premier_add_on_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Updates a named add-on of an app. Description for Updates a named add-on of an app.</td>
</tr>
<tr>
    <td><a href="#update_premier_add_on_slot"><CopyableCode code="update_premier_add_on_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-premier_add_on_name"><code>premier_add_on_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a named add-on of an app. Description for Updates a named add-on of an app.</td>
</tr>
<tr>
    <td><a href="#delete_premier_add_on_slot"><CopyableCode code="delete_premier_add_on_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-premier_add_on_name"><code>premier_add_on_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a premier add-on from an app. Description for Delete a premier add-on from an app.</td>
</tr>
<tr>
    <td><a href="#get_private_access"><CopyableCode code="get_private_access" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets data around private site access enablement and authorized Virtual Networks that can access the site. Description for Gets data around private site access enablement and authorized Virtual Networks that can access the site.</td>
</tr>
<tr>
    <td><a href="#put_private_access_vnet"><CopyableCode code="put_private_access_vnet" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sets data around private site access enablement and authorized Virtual Networks that can access the site. Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site.</td>
</tr>
<tr>
    <td><a href="#get_private_access_slot"><CopyableCode code="get_private_access_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets data around private site access enablement and authorized Virtual Networks that can access the site. Description for Gets data around private site access enablement and authorized Virtual Networks that can access the site.</td>
</tr>
<tr>
    <td><a href="#put_private_access_vnet_slot"><CopyableCode code="put_private_access_vnet_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sets data around private site access enablement and authorized Virtual Networks that can access the site. Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_public_certificate"><CopyableCode code="create_or_update_public_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-public_certificate_name"><code>public_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a hostname binding for an app. Description for Creates a hostname binding for an app.</td>
</tr>
<tr>
    <td><a href="#delete_public_certificate"><CopyableCode code="delete_public_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-public_certificate_name"><code>public_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a hostname binding for an app. Description for Deletes a hostname binding for an app.</td>
</tr>
<tr>
    <td><a href="#create_or_update_public_certificate_slot"><CopyableCode code="create_or_update_public_certificate_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-public_certificate_name"><code>public_certificate_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a hostname binding for an app. Description for Creates a hostname binding for an app.</td>
</tr>
<tr>
    <td><a href="#delete_public_certificate_slot"><CopyableCode code="delete_public_certificate_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-public_certificate_name"><code>public_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a hostname binding for an app. Description for Deletes a hostname binding for an app.</td>
</tr>
<tr>
    <td><a href="#create_or_update_site_container"><CopyableCode code="create_or_update_site_container" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates a site container for a site, or a deployment slot. Creates or Updates a site container for a site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_site_container"><CopyableCode code="delete_site_container" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a site container for a site, or a deployment slot. Deletes a site container for a site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_or_update_site_container_slot"><CopyableCode code="create_or_update_site_container_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or Updates a site container for a site, or a deployment slot. Creates or Updates a site container for a site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_site_container_slot"><CopyableCode code="delete_site_container_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-container_name"><code>container_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a site container for a site, or a deployment slot. Deletes a site container for a site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#install_site_extension"><CopyableCode code="install_site_extension" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-site_extension_id"><code>site_extension_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Install site extension on a web site, or a deployment slot. Description for Install site extension on a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_site_extension"><CopyableCode code="delete_site_extension" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-site_extension_id"><code>site_extension_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove a site extension from a web site, or a deployment slot. Description for Remove a site extension from a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#install_site_extension_slot"><CopyableCode code="install_site_extension_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-site_extension_id"><code>site_extension_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Install site extension on a web site, or a deployment slot. Description for Install site extension on a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_site_extension_slot"><CopyableCode code="delete_site_extension_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-site_extension_id"><code>site_extension_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Remove a site extension from a web site, or a deployment slot. Description for Remove a site extension from a web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_source_control_slot"><CopyableCode code="get_source_control_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the source control configuration of an app. Description for Gets the source control configuration of an app.</td>
</tr>
<tr>
    <td><a href="#create_or_update_source_control_slot"><CopyableCode code="create_or_update_source_control_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the source control configuration of an app. Description for Updates the source control configuration of an app.</td>
</tr>
<tr>
    <td><a href="#update_source_control_slot"><CopyableCode code="update_source_control_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the source control configuration of an app. Description for Updates the source control configuration of an app.</td>
</tr>
<tr>
    <td><a href="#delete_source_control_slot"><CopyableCode code="delete_source_control_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-additionalFlags"><code>additionalFlags</code></a></td>
    <td>Deletes the source control configuration of an app. Description for Deletes the source control configuration of an app.</td>
</tr>
<tr>
    <td><a href="#get_source_control"><CopyableCode code="get_source_control" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the source control configuration of an app. Description for Gets the source control configuration of an app.</td>
</tr>
<tr>
    <td><a href="#create_or_update_source_control"><CopyableCode code="create_or_update_source_control" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the source control configuration of an app. Description for Updates the source control configuration of an app.</td>
</tr>
<tr>
    <td><a href="#update_source_control"><CopyableCode code="update_source_control" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the source control configuration of an app. Description for Updates the source control configuration of an app.</td>
</tr>
<tr>
    <td><a href="#delete_source_control"><CopyableCode code="delete_source_control" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-additionalFlags"><code>additionalFlags</code></a></td>
    <td>Deletes the source control configuration of an app. Description for Deletes the source control configuration of an app.</td>
</tr>
<tr>
    <td><a href="#get_triggered_web_job_slot"><CopyableCode code="get_triggered_web_job_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a triggered web job by its ID for an app, or a deployment slot. Description for Gets a triggered web job by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_triggered_web_job_slot"><CopyableCode code="delete_triggered_web_job_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a triggered web job by its ID for an app, or a deployment slot. Description for Delete a triggered web job by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_triggered_web_job"><CopyableCode code="get_triggered_web_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a triggered web job by its ID for an app, or a deployment slot. Description for Gets a triggered web job by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete_triggered_web_job"><CopyableCode code="delete_triggered_web_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a triggered web job by its ID for an app, or a deployment slot. Description for Delete a triggered web job by its ID for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_web_job_slot"><CopyableCode code="get_web_job_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get webjob information for an app, or a deployment slot. Description for Get webjob information for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#get_web_job"><CopyableCode code="get_web_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get webjob information for an app, or a deployment slot. Description for Get webjob information for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#analyze_custom_hostname_slot"><CopyableCode code="analyze_custom_hostname_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-hostName"><code>hostName</code></a></td>
    <td>Analyze a custom hostname. Description for Analyze a custom hostname.</td>
</tr>
<tr>
    <td><a href="#apply_slot_configuration_slot"><CopyableCode code="apply_slot_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetSlot"><code>targetSlot</code></a>, <a href="#parameter-preserveVnet"><code>preserveVnet</code></a></td>
    <td></td>
    <td>Applies the configuration settings from the target slot onto the current slot. Description for Applies the configuration settings from the target slot onto the current slot.</td>
</tr>
<tr>
    <td><a href="#backup_slot"><CopyableCode code="backup_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a backup of an app. Description for Creates a backup of an app.</td>
</tr>
<tr>
    <td><a href="#update_application_settings_slot"><CopyableCode code="update_application_settings_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Replaces the application settings of an app. Description for Replaces the application settings of an app.</td>
</tr>
<tr>
    <td><a href="#update_auth_settings_slot"><CopyableCode code="update_auth_settings_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Authentication / Authorization settings associated with web app. Description for Updates the Authentication / Authorization settings associated with web app.</td>
</tr>
<tr>
    <td><a href="#update_azure_storage_accounts_slot"><CopyableCode code="update_azure_storage_accounts_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Azure storage account configurations of an app. Description for Updates the Azure storage account configurations of an app.</td>
</tr>
<tr>
    <td><a href="#update_backup_configuration_slot"><CopyableCode code="update_backup_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the backup configuration of an app. Description for Updates the backup configuration of an app.</td>
</tr>
<tr>
    <td><a href="#delete_backup_configuration_slot"><CopyableCode code="delete_backup_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the backup configuration of an app. Description for Deletes the backup configuration of an app.</td>
</tr>
<tr>
    <td><a href="#update_connection_strings_slot"><CopyableCode code="update_connection_strings_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Replaces the connection strings of an app. Description for Replaces the connection strings of an app.</td>
</tr>
<tr>
    <td><a href="#update_metadata_slot"><CopyableCode code="update_metadata_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Replaces the metadata of an app. Description for Replaces the metadata of an app.</td>
</tr>
<tr>
    <td><a href="#update_site_push_settings_slot"><CopyableCode code="update_site_push_settings_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Push settings associated with web app. Description for Updates the Push settings associated with web app.</td>
</tr>
<tr>
    <td><a href="#discover_backup_slot"><CopyableCode code="discover_backup_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.</td>
</tr>
<tr>
    <td><a href="#sync_functions_slot"><CopyableCode code="sync_functions_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Syncs function trigger metadata to the management database. Description for Syncs function trigger metadata to the management database.</td>
</tr>
<tr>
    <td><a href="#create_or_update_host_secret_slot"><CopyableCode code="create_or_update_host_secret_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-key_type"><code>key_type</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add or update a host level secret. Description for Add or update a host level secret.</td>
</tr>
<tr>
    <td><a href="#delete_host_secret_slot"><CopyableCode code="delete_host_secret_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-key_type"><code>key_type</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a host level secret. Description for Delete a host level secret.</td>
</tr>
<tr>
    <td><a href="#is_cloneable_slot"><CopyableCode code="is_cloneable_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Shows whether an app can be cloned to another resource group or subscription. Description for Shows whether an app can be cloned to another resource group or subscription.</td>
</tr>
<tr>
    <td><a href="#start_web_site_network_trace_slot"><CopyableCode code="start_web_site_network_trace_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a>, <a href="#parameter-maxFrameLength"><code>maxFrameLength</code></a>, <a href="#parameter-sasUrl"><code>sasUrl</code></a></td>
    <td>Start capturing network packets for the site (To be deprecated). Description for Start capturing network packets for the site (To be deprecated).</td>
</tr>
<tr>
    <td><a href="#start_web_site_network_trace_operation_slot"><CopyableCode code="start_web_site_network_trace_operation_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a>, <a href="#parameter-maxFrameLength"><code>maxFrameLength</code></a>, <a href="#parameter-sasUrl"><code>sasUrl</code></a></td>
    <td>Start capturing network packets for the site. Description for Start capturing network packets for the site.</td>
</tr>
<tr>
    <td><a href="#stop_web_site_network_trace_slot"><CopyableCode code="stop_web_site_network_trace_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop ongoing capturing network packets for the site. Description for Stop ongoing capturing network packets for the site.</td>
</tr>
<tr>
    <td><a href="#generate_new_site_publishing_password_slot"><CopyableCode code="generate_new_site_publishing_password_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates a new publishing password for an app (or deployment slot, if specified). Description for Generates a new publishing password for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#reset_slot_configuration_slot"><CopyableCode code="reset_slot_configuration_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.</td>
</tr>
<tr>
    <td><a href="#restart_slot"><CopyableCode code="restart_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-softRestart"><code>softRestart</code></a>, <a href="#parameter-synchronous"><code>synchronous</code></a></td>
    <td>Restarts an app (or deployment slot, if specified). Description for Restarts an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#restore_from_backup_blob_slot"><CopyableCode code="restore_from_backup_blob_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores an app from a backup blob in Azure Storage. Description for Restores an app from a backup blob in Azure Storage.</td>
</tr>
<tr>
    <td><a href="#restore_from_deleted_app_slot"><CopyableCode code="restore_from_deleted_app_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores a deleted web app to this web app. Description for Restores a deleted web app to this web app.</td>
</tr>
<tr>
    <td><a href="#restore_snapshot_slot"><CopyableCode code="restore_snapshot_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores a web app from a snapshot. Description for Restores a web app from a snapshot.</td>
</tr>
<tr>
    <td><a href="#swap_slot"><CopyableCode code="swap_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetSlot"><code>targetSlot</code></a>, <a href="#parameter-preserveVnet"><code>preserveVnet</code></a></td>
    <td></td>
    <td>Swaps two deployment slots of an app. Description for Swaps two deployment slots of an app.</td>
</tr>
<tr>
    <td><a href="#start_slot"><CopyableCode code="start_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts an app (or deployment slot, if specified). Description for Starts an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#start_network_trace_slot"><CopyableCode code="start_network_trace_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a>, <a href="#parameter-maxFrameLength"><code>maxFrameLength</code></a>, <a href="#parameter-sasUrl"><code>sasUrl</code></a></td>
    <td>Start capturing network packets for the site. Description for Start capturing network packets for the site.</td>
</tr>
<tr>
    <td><a href="#stop_slot"><CopyableCode code="stop_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops an app (or deployment slot, if specified). Description for Stops an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#stop_network_trace_slot"><CopyableCode code="stop_network_trace_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop ongoing capturing network packets for the site. Description for Stop ongoing capturing network packets for the site.</td>
</tr>
<tr>
    <td><a href="#sync_repository_slot"><CopyableCode code="sync_repository_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sync web app repository. Description for Sync web app repository.</td>
</tr>
<tr>
    <td><a href="#sync_function_triggers_slot"><CopyableCode code="sync_function_triggers_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Syncs function trigger metadata to the management database. Description for Syncs function trigger metadata to the management database.</td>
</tr>
<tr>
    <td><a href="#deploy_workflow_artifacts_slot"><CopyableCode code="deploy_workflow_artifacts_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates the artifacts for web site, or a deployment slot. Description for Creates the artifacts for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#analyze_custom_hostname"><CopyableCode code="analyze_custom_hostname" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-hostName"><code>hostName</code></a></td>
    <td>Analyze a custom hostname. Description for Analyze a custom hostname.</td>
</tr>
<tr>
    <td><a href="#apply_slot_config_to_production"><CopyableCode code="apply_slot_config_to_production" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetSlot"><code>targetSlot</code></a>, <a href="#parameter-preserveVnet"><code>preserveVnet</code></a></td>
    <td></td>
    <td>Applies the configuration settings from the target slot onto the current slot. Description for Applies the configuration settings from the target slot onto the current slot.</td>
</tr>
<tr>
    <td><a href="#backup"><CopyableCode code="backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a backup of an app. Description for Creates a backup of an app.</td>
</tr>
<tr>
    <td><a href="#update_application_settings"><CopyableCode code="update_application_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Replaces the application settings of an app. Description for Replaces the application settings of an app.</td>
</tr>
<tr>
    <td><a href="#update_auth_settings"><CopyableCode code="update_auth_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Authentication / Authorization settings associated with web app. Description for Updates the Authentication / Authorization settings associated with web app.</td>
</tr>
<tr>
    <td><a href="#update_azure_storage_accounts"><CopyableCode code="update_azure_storage_accounts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Azure storage account configurations of an app. Description for Updates the Azure storage account configurations of an app.</td>
</tr>
<tr>
    <td><a href="#update_backup_configuration"><CopyableCode code="update_backup_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the backup configuration of an app. Description for Updates the backup configuration of an app.</td>
</tr>
<tr>
    <td><a href="#delete_backup_configuration"><CopyableCode code="delete_backup_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the backup configuration of an app. Description for Deletes the backup configuration of an app.</td>
</tr>
<tr>
    <td><a href="#update_connection_strings"><CopyableCode code="update_connection_strings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Replaces the connection strings of an app. Description for Replaces the connection strings of an app.</td>
</tr>
<tr>
    <td><a href="#update_metadata"><CopyableCode code="update_metadata" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Replaces the metadata of an app. Description for Replaces the metadata of an app.</td>
</tr>
<tr>
    <td><a href="#update_site_push_settings"><CopyableCode code="update_site_push_settings" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Push settings associated with web app. Description for Updates the Push settings associated with web app.</td>
</tr>
<tr>
    <td><a href="#discover_backup"><CopyableCode code="discover_backup" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.</td>
</tr>
<tr>
    <td><a href="#sync_functions"><CopyableCode code="sync_functions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Syncs function trigger metadata to the management database. Description for Syncs function trigger metadata to the management database.</td>
</tr>
<tr>
    <td><a href="#create_or_update_host_secret"><CopyableCode code="create_or_update_host_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-key_type"><code>key_type</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add or update a host level secret. Description for Add or update a host level secret.</td>
</tr>
<tr>
    <td><a href="#delete_host_secret"><CopyableCode code="delete_host_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-key_type"><code>key_type</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a host level secret. Description for Delete a host level secret.</td>
</tr>
<tr>
    <td><a href="#is_cloneable"><CopyableCode code="is_cloneable" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Shows whether an app can be cloned to another resource group or subscription. Description for Shows whether an app can be cloned to another resource group or subscription.</td>
</tr>
<tr>
    <td><a href="#update_machine_key"><CopyableCode code="update_machine_key" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the machine key of an app. Updates the machine key of an app.</td>
</tr>
<tr>
    <td><a href="#migrate_storage"><CopyableCode code="migrate_storage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-subscriptionName"><code>subscriptionName</code></a></td>
    <td></td>
    <td>Restores a web app. Description for Restores a web app.</td>
</tr>
<tr>
    <td><a href="#migrate_my_sql"><CopyableCode code="migrate_my_sql" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrates a local (in-app) MySql database to a remote MySql database. Description for Migrates a local (in-app) MySql database to a remote MySql database.</td>
</tr>
<tr>
    <td><a href="#start_web_site_network_trace"><CopyableCode code="start_web_site_network_trace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a>, <a href="#parameter-maxFrameLength"><code>maxFrameLength</code></a>, <a href="#parameter-sasUrl"><code>sasUrl</code></a></td>
    <td>Start capturing network packets for the site (To be deprecated). Description for Start capturing network packets for the site (To be deprecated).</td>
</tr>
<tr>
    <td><a href="#start_web_site_network_trace_operation"><CopyableCode code="start_web_site_network_trace_operation" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a>, <a href="#parameter-maxFrameLength"><code>maxFrameLength</code></a>, <a href="#parameter-sasUrl"><code>sasUrl</code></a></td>
    <td>Start capturing network packets for the site. Description for Start capturing network packets for the site.</td>
</tr>
<tr>
    <td><a href="#stop_web_site_network_trace"><CopyableCode code="stop_web_site_network_trace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop ongoing capturing network packets for the site. Description for Stop ongoing capturing network packets for the site.</td>
</tr>
<tr>
    <td><a href="#generate_new_site_publishing_password"><CopyableCode code="generate_new_site_publishing_password" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates a new publishing password for an app (or deployment slot, if specified). Description for Generates a new publishing password for an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#reset_production_slot_config"><CopyableCode code="reset_production_slot_config" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-softRestart"><code>softRestart</code></a>, <a href="#parameter-synchronous"><code>synchronous</code></a></td>
    <td>Restarts an app (or deployment slot, if specified). Description for Restarts an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#restore_from_backup_blob"><CopyableCode code="restore_from_backup_blob" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores an app from a backup blob in Azure Storage. Description for Restores an app from a backup blob in Azure Storage.</td>
</tr>
<tr>
    <td><a href="#restore_from_deleted_app"><CopyableCode code="restore_from_deleted_app" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores a deleted web app to this web app. Description for Restores a deleted web app to this web app.</td>
</tr>
<tr>
    <td><a href="#restore_snapshot"><CopyableCode code="restore_snapshot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores a web app from a snapshot. Description for Restores a web app from a snapshot.</td>
</tr>
<tr>
    <td><a href="#swap_slot_with_production"><CopyableCode code="swap_slot_with_production" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targetSlot"><code>targetSlot</code></a>, <a href="#parameter-preserveVnet"><code>preserveVnet</code></a></td>
    <td></td>
    <td>Swaps two deployment slots of an app. Description for Swaps two deployment slots of an app.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts an app (or deployment slot, if specified). Description for Starts an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#start_network_trace"><CopyableCode code="start_network_trace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-durationInSeconds"><code>durationInSeconds</code></a>, <a href="#parameter-maxFrameLength"><code>maxFrameLength</code></a>, <a href="#parameter-sasUrl"><code>sasUrl</code></a></td>
    <td>Start capturing network packets for the site. Description for Start capturing network packets for the site.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops an app (or deployment slot, if specified). Description for Stops an app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#stop_network_trace"><CopyableCode code="stop_network_trace" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop ongoing capturing network packets for the site. Description for Stop ongoing capturing network packets for the site.</td>
</tr>
<tr>
    <td><a href="#sync_repository"><CopyableCode code="sync_repository" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sync web app repository. Description for Sync web app repository.</td>
</tr>
<tr>
    <td><a href="#sync_function_triggers"><CopyableCode code="sync_function_triggers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Syncs function trigger metadata to the management database. Description for Syncs function trigger metadata to the management database.</td>
</tr>
<tr>
    <td><a href="#deploy_workflow_artifacts"><CopyableCode code="deploy_workflow_artifacts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates the artifacts for web site, or a deployment slot. Description for Creates the artifacts for web site, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#restore"><CopyableCode code="restore" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-backup_id"><code>backup_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores a specific backup to another app (or deployment slot, if specified). Description for Restores a specific backup to another app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#restore_slot"><CopyableCode code="restore_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-backup_id"><code>backup_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restores a specific backup to another app (or deployment slot, if specified). Description for Restores a specific backup to another app (or deployment slot, if specified).</td>
</tr>
<tr>
    <td><a href="#recover_site_configuration_snapshot"><CopyableCode code="recover_site_configuration_snapshot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-snapshot_id"><code>snapshot_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reverts the configuration of an app to a previous snapshot. Description for Reverts the configuration of an app to a previous snapshot.</td>
</tr>
<tr>
    <td><a href="#recover_site_configuration_snapshot_slot"><CopyableCode code="recover_site_configuration_snapshot_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-snapshot_id"><code>snapshot_id</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reverts the configuration of an app to a previous snapshot. Description for Reverts the configuration of an app to a previous snapshot.</td>
</tr>
<tr>
    <td><a href="#start_continuous_web_job"><CopyableCode code="start_continuous_web_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start a continuous web job for an app, or a deployment slot. Description for Start a continuous web job for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#stop_continuous_web_job"><CopyableCode code="stop_continuous_web_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop a continuous web job for an app, or a deployment slot. Description for Stop a continuous web job for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#start_continuous_web_job_slot"><CopyableCode code="start_continuous_web_job_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start a continuous web job for an app, or a deployment slot. Description for Start a continuous web job for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#stop_continuous_web_job_slot"><CopyableCode code="stop_continuous_web_job_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop a continuous web job for an app, or a deployment slot. Description for Stop a continuous web job for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_or_update_function_secret"><CopyableCode code="create_or_update_function_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add or update a function secret. Description for Add or update a function secret.</td>
</tr>
<tr>
    <td><a href="#delete_function_secret"><CopyableCode code="delete_function_secret" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a function secret. Description for Delete a function secret.</td>
</tr>
<tr>
    <td><a href="#create_or_update_function_secret_slot"><CopyableCode code="create_or_update_function_secret_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add or update a function secret. Description for Add or update a function secret.</td>
</tr>
<tr>
    <td><a href="#delete_function_secret_slot"><CopyableCode code="delete_function_secret_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-function_name"><code>function_name</code></a>, <a href="#parameter-key_name"><code>key_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a function secret. Description for Delete a function secret.</td>
</tr>
<tr>
    <td><a href="#run_triggered_web_job_slot"><CopyableCode code="run_triggered_web_job_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Run a triggered web job for an app, or a deployment slot. Description for Run a triggered web job for an app, or a deployment slot.</td>
</tr>
<tr>
    <td><a href="#run_triggered_web_job"><CopyableCode code="run_triggered_web_job" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-web_job_name"><code>web_job_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Run a triggered web job for an app, or a deployment slot. Description for Run a triggered web job for an app, or a deployment slot.</td>
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
<tr id="parameter-app_setting_key">
    <td><CopyableCode code="app_setting_key" /></td>
    <td><code>string</code></td>
    <td>App Setting key name. Required.</td>
</tr>
<tr id="parameter-backup_id">
    <td><CopyableCode code="backup_id" /></td>
    <td><code>string</code></td>
    <td>ID of the backup. Required.</td>
</tr>
<tr id="parameter-base_address">
    <td><CopyableCode code="base_address" /></td>
    <td><code>string</code></td>
    <td>Module base address. Required.</td>
</tr>
<tr id="parameter-connection_string_key">
    <td><CopyableCode code="connection_string_key" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-container_name">
    <td><CopyableCode code="container_name" /></td>
    <td><code>string</code></td>
    <td>Site Container Name. Required.</td>
</tr>
<tr id="parameter-deployment_status_id">
    <td><CopyableCode code="deployment_status_id" /></td>
    <td><code>string</code></td>
    <td>GUID of the deployment operation. Required.</td>
</tr>
<tr id="parameter-domain_ownership_identifier_name">
    <td><CopyableCode code="domain_ownership_identifier_name" /></td>
    <td><code>string</code></td>
    <td>Name of domain ownership identifier. Required.</td>
</tr>
<tr id="parameter-entity_name">
    <td><CopyableCode code="entity_name" /></td>
    <td><code>string</code></td>
    <td>Name of the hybrid connection. Required.</td>
</tr>
<tr id="parameter-function_name">
    <td><CopyableCode code="function_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-gateway_name">
    <td><CopyableCode code="gateway_name" /></td>
    <td><code>string</code></td>
    <td>Name of the gateway. Currently, the only supported string is "primary". Required.</td>
</tr>
<tr id="parameter-host_name">
    <td><CopyableCode code="host_name" /></td>
    <td><code>string</code></td>
    <td>Hostname in the hostname binding. Required.</td>
</tr>
<tr id="parameter-id">
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Deployment ID. Required.</td>
</tr>
<tr id="parameter-instance_id">
    <td><CopyableCode code="instance_id" /></td>
    <td><code>string</code></td>
    <td>ID of a specific scaled-out instance. This is the value of the name property in the JSON response from "GET api/sites/&#123;siteName&#125;/instances". Required.</td>
</tr>
<tr id="parameter-key_name">
    <td><CopyableCode code="key_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-key_type">
    <td><CopyableCode code="key_type" /></td>
    <td><code>string</code></td>
    <td>The type of host key. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Site name. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>The namespace for this hybrid connection. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>GUID of the operation. Required.</td>
</tr>
<tr id="parameter-premier_add_on_name">
    <td><CopyableCode code="premier_add_on_name" /></td>
    <td><code>string</code></td>
    <td>Add-on name. Required.</td>
</tr>
<tr id="parameter-private_endpoint_connection_name">
    <td><CopyableCode code="private_endpoint_connection_name" /></td>
    <td><code>string</code></td>
    <td>Name of the private endpoint connection. Required.</td>
</tr>
<tr id="parameter-process_id">
    <td><CopyableCode code="process_id" /></td>
    <td><code>string</code></td>
    <td>PID. Required.</td>
</tr>
<tr id="parameter-public_certificate_name">
    <td><CopyableCode code="public_certificate_name" /></td>
    <td><code>string</code></td>
    <td>Public certificate name. Required.</td>
</tr>
<tr id="parameter-relay_name">
    <td><CopyableCode code="relay_name" /></td>
    <td><code>string</code></td>
    <td>The relay name for this hybrid connection. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-site_extension_id">
    <td><CopyableCode code="site_extension_id" /></td>
    <td><code>string</code></td>
    <td>Site extension name. Required.</td>
</tr>
<tr id="parameter-slot">
    <td><CopyableCode code="slot" /></td>
    <td><code>string</code></td>
    <td>Name of the deployment slot. If a slot is not specified, the API uses the production slot. Required.</td>
</tr>
<tr id="parameter-snapshot_id">
    <td><CopyableCode code="snapshot_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the snapshot to read. Required.</td>
</tr>
<tr id="parameter-subscriptionName">
    <td><CopyableCode code="subscriptionName" /></td>
    <td><code>string</code></td>
    <td>Azure subscription. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-view_name">
    <td><CopyableCode code="view_name" /></td>
    <td><code>string</code></td>
    <td>The type of view. Only "summary" is supported at this time. Required.</td>
</tr>
<tr id="parameter-vnet_name">
    <td><CopyableCode code="vnet_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Virtual Network. Required.</td>
</tr>
<tr id="parameter-web_job_name">
    <td><CopyableCode code="web_job_name" /></td>
    <td><code>string</code></td>
    <td>Name of Web Job. Required.</td>
</tr>
<tr id="parameter-workflow_name">
    <td><CopyableCode code="workflow_name" /></td>
    <td><code>string</code></td>
    <td>Workflow name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Return only information specified in the filter (using OData syntax). For example: $filter=(name.value eq 'Metric1' or name.value eq 'Metric2') and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[Hour|Minute|Day]'. Default value is None.</td>
</tr>
<tr id="parameter-additionalFlags">
    <td><CopyableCode code="additionalFlags" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
</tr>
<tr id="parameter-deleteEmptyServerFarm">
    <td><CopyableCode code="deleteEmptyServerFarm" /></td>
    <td><code>boolean</code></td>
    <td>Specify false if you want to keep empty App Service plan. By default, empty App Service plan is deleted. Default value is None.</td>
</tr>
<tr id="parameter-deleteMetrics">
    <td><CopyableCode code="deleteMetrics" /></td>
    <td><code>boolean</code></td>
    <td>If true, web app metrics are also deleted. Default value is None.</td>
</tr>
<tr id="parameter-durationInSeconds">
    <td><CopyableCode code="durationInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The duration to keep capturing in seconds. Default value is None.</td>
</tr>
<tr id="parameter-hostName">
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>Custom hostname. Default value is None.</td>
</tr>
<tr id="parameter-includeSlots">
    <td><CopyableCode code="includeSlots" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to include deployment slots in results. The default is false, which only gives you the production slot of all apps. Default value is None.</td>
</tr>
<tr id="parameter-maxFrameLength">
    <td><CopyableCode code="maxFrameLength" /></td>
    <td><code>integer</code></td>
    <td>The maximum frame length in bytes (Optional). Default value is None.</td>
</tr>
<tr id="parameter-sasUrl">
    <td><CopyableCode code="sasUrl" /></td>
    <td><code>string</code></td>
    <td>The Blob URL to store capture file. Default value is None.</td>
</tr>
<tr id="parameter-softRestart">
    <td><CopyableCode code="softRestart" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to apply the configuration settings and restarts the app only if necessary. By default, the API always restarts and reprovisions the app. Default value is None.</td>
</tr>
<tr id="parameter-synchronous">
    <td><CopyableCode code="synchronous" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to block until the app is restarted. By default, it is set to false, and the API responds immediately (asynchronous). Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_instance_process_module_slot"
    values={[
        { label: 'get_instance_process_module_slot', value: 'get_instance_process_module_slot' },
        { label: 'list_slot_differences_slot', value: 'list_slot_differences_slot' },
        { label: 'list_instance_process_threads_slot', value: 'list_instance_process_threads_slot' },
        { label: 'get_hybrid_connection_slot', value: 'get_hybrid_connection_slot' },
        { label: 'get_vnet_connection_gateway_slot', value: 'get_vnet_connection_gateway_slot' },
        { label: 'get_instance_process_module', value: 'get_instance_process_module' },
        { label: 'get_process_module_slot', value: 'get_process_module_slot' },
        { label: 'get_triggered_web_job_history_slot', value: 'get_triggered_web_job_history_slot' },
        { label: 'list_slot_differences_from_production', value: 'list_slot_differences_from_production' },
        { label: 'list_backup_status_secrets_slot', value: 'list_backup_status_secrets_slot' },
        { label: 'list_deployment_log_slot', value: 'list_deployment_log_slot' },
        { label: 'list_function_keys_slot', value: 'list_function_keys_slot' },
        { label: 'list_instance_process_threads', value: 'list_instance_process_threads' },
        { label: 'list_instance_processes_slot', value: 'list_instance_processes_slot' },
        { label: 'list_process_threads_slot', value: 'list_process_threads_slot' },
        { label: 'list_network_features_slot', value: 'list_network_features_slot' },
        { label: 'list_triggered_web_job_history_slot', value: 'list_triggered_web_job_history_slot' },
        { label: 'get_network_trace_operation_slot', value: 'get_network_trace_operation_slot' },
        { label: 'get_private_endpoint_connection_slot', value: 'get_private_endpoint_connection_slot' },
        { label: 'get_hybrid_connection', value: 'get_hybrid_connection' },
        { label: 'get_vnet_connection_slot', value: 'get_vnet_connection_slot' },
        { label: 'get_vnet_connection_gateway', value: 'get_vnet_connection_gateway' },
        { label: 'get_app_setting_key_vault_reference_slot', value: 'get_app_setting_key_vault_reference_slot' },
        { label: 'get_site_connection_string_key_vault_reference_slot', value: 'get_site_connection_string_key_vault_reference_slot' },
        { label: 'get_configuration_snapshot_slot', value: 'get_configuration_snapshot_slot' },
        { label: 'get_slot_site_deployment_status_slot', value: 'get_slot_site_deployment_status_slot' },
        { label: 'get_domain_ownership_identifier_slot', value: 'get_domain_ownership_identifier_slot' },
        { label: 'get_host_name_binding_slot', value: 'get_host_name_binding_slot' },
        { label: 'get_relay_service_connection_slot', value: 'get_relay_service_connection_slot' },
        { label: 'get_process_module', value: 'get_process_module' },
        { label: 'get_premier_add_on_slot', value: 'get_premier_add_on_slot' },
        { label: 'get_public_certificate_slot', value: 'get_public_certificate_slot' },
        { label: 'get_site_container_slot', value: 'get_site_container_slot' },
        { label: 'get_site_extension_slot', value: 'get_site_extension_slot' },
        { label: 'get_triggered_web_job_history', value: 'get_triggered_web_job_history' },
        { label: 'get_instance_workflow_slot', value: 'get_instance_workflow_slot' },
        { label: 'list_application_settings_slot', value: 'list_application_settings_slot' },
        { label: 'list_backup_status_secrets', value: 'list_backup_status_secrets' },
        { label: 'list_deployment_log', value: 'list_deployment_log' },
        { label: 'list_function_keys', value: 'list_function_keys' },
        { label: 'list_instance_processes', value: 'list_instance_processes' },
        { label: 'list_process_threads', value: 'list_process_threads' },
        { label: 'list_network_features', value: 'list_network_features' },
        { label: 'list_triggered_web_job_history', value: 'list_triggered_web_job_history' },
        { label: 'get_private_endpoint_connection', value: 'get_private_endpoint_connection' },
        { label: 'get_vnet_connection', value: 'get_vnet_connection' },
        { label: 'get_network_trace_operation', value: 'get_network_trace_operation' },
        { label: 'get_app_setting_key_vault_reference', value: 'get_app_setting_key_vault_reference' },
        { label: 'get_site_connection_string_key_vault_reference', value: 'get_site_connection_string_key_vault_reference' },
        { label: 'get_configuration_snapshot', value: 'get_configuration_snapshot' },
        { label: 'get_production_site_deployment_status', value: 'get_production_site_deployment_status' },
        { label: 'get_domain_ownership_identifier', value: 'get_domain_ownership_identifier' },
        { label: 'get_host_name_binding', value: 'get_host_name_binding' },
        { label: 'get_relay_service_connection', value: 'get_relay_service_connection' },
        { label: 'get_premier_add_on', value: 'get_premier_add_on' },
        { label: 'get_public_certificate', value: 'get_public_certificate' },
        { label: 'get_site_container', value: 'get_site_container' },
        { label: 'get_site_extension', value: 'get_site_extension' },
        { label: 'get_workflow', value: 'get_workflow' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_instance_process_module_slot">

Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
file_name,
base_address,
file_description,
file_path,
file_version,
href,
is_debug,
kind,
language,
module_memory_size,
product,
product_version,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND process_id = '{{ process_id }}' -- required
AND base_address = '{{ base_address }}' -- required
AND slot = '{{ slot }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_slot_differences_slot">

Get the difference in configuration settings between two web app slots. Description for Get the difference in configuration settings between two web app slots.

```sql
SELECT
id,
name,
description,
diffRule,
kind,
level,
settingName,
settingType,
type,
valueInCurrentSlot,
valueInTargetSlot
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_instance_process_threads_slot">

List the threads in a process by its ID for a specific scaled-out instance in a web site. Description for List the threads in a process by its ID for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
base_priority,
current_priority,
href,
identifier,
kind,
priority_level,
process,
start_address,
start_time,
state,
total_processor_time,
type,
user_processor_time,
wait_reason
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND process_id = '{{ process_id }}' -- required
AND slot = '{{ slot }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_hybrid_connection_slot">

Retrieves a specific Service Bus Hybrid Connection used by this Web App. Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App.

```sql
SELECT
id,
name,
hostname,
kind,
port,
relayArmUri,
relayName,
sendKeyName,
sendKeyValue,
serviceBusNamespace,
serviceBusSuffix,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND relay_name = '{{ relay_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_vnet_connection_gateway_slot">

Gets an app's Virtual Network gateway. Description for Gets an app's Virtual Network gateway.

```sql
SELECT
id,
name,
kind,
systemData,
type,
vnetName,
vpnPackageUri
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND vnet_name = '{{ vnet_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_instance_process_module">

Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
file_name,
base_address,
file_description,
file_path,
file_version,
href,
is_debug,
kind,
language,
module_memory_size,
product,
product_version,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND process_id = '{{ process_id }}' -- required
AND base_address = '{{ base_address }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_process_module_slot">

Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
file_name,
base_address,
file_description,
file_path,
file_version,
href,
is_debug,
kind,
language,
module_memory_size,
product,
product_version,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND process_id = '{{ process_id }}' -- required
AND base_address = '{{ base_address }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_triggered_web_job_history_slot">

Gets a triggered web job's history by its ID for an app, , or a deployment slot. Description for Gets a triggered web job's history by its ID for an app, , or a deployment slot.

```sql
SELECT
id,
name,
kind,
runs,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND web_job_name = '{{ web_job_name }}' -- required
AND id = '{{ id }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_slot_differences_from_production">

Get the difference in configuration settings between two web app slots. Description for Get the difference in configuration settings between two web app slots.

```sql
SELECT
id,
name,
description,
diffRule,
kind,
level,
settingName,
settingType,
type,
valueInCurrentSlot,
valueInTargetSlot
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_backup_status_secrets_slot">

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body. Description for Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

```sql
SELECT
id,
name,
blobName,
correlationId,
created,
databases,
finishedTimeStamp,
kind,
lastRestoreTimeStamp,
log,
scheduled,
sizeInBytes,
status,
storageAccountUrl,
systemData,
type,
websiteSizeInBytes
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND backup_id = '{{ backup_id }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_deployment_log_slot">

List deployment log for specific deployment for an app, or a deployment slot. Description for List deployment log for specific deployment for an app, or a deployment slot.

```sql
SELECT
id,
name,
active,
author,
author_email,
deployer,
details,
end_time,
kind,
message,
start_time,
status,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND id = '{{ id }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_function_keys_slot">

Get function keys for a function in a web site, or a deployment slot. Description for Get function keys for a function in a web site, or a deployment slot.

```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND function_name = '{{ function_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_instance_process_threads">

List the threads in a process by its ID for a specific scaled-out instance in a web site. Description for List the threads in a process by its ID for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
base_priority,
current_priority,
href,
identifier,
kind,
priority_level,
process,
start_address,
start_time,
state,
total_processor_time,
type,
user_processor_time,
wait_reason
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND process_id = '{{ process_id }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_instance_processes_slot">

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
deployment_name,
file_name,
user_name,
children,
command_line,
description,
environment_variables,
handle_count,
href,
identifier,
iis_profile_timeout_in_seconds,
is_iis_profile_running,
is_profile_running,
is_scm_site,
is_webjob,
kind,
minidump,
module_count,
modules,
non_paged_system_memory,
open_file_handles,
paged_memory,
paged_system_memory,
parent,
peak_paged_memory,
peak_virtual_memory,
peak_working_set,
private_memory,
privileged_cpu_time,
start_time,
systemData,
thread_count,
threads,
time_stamp,
total_cpu_time,
type,
user_cpu_time,
virtual_memory,
working_set
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_process_threads_slot">

List the threads in a process by its ID for a specific scaled-out instance in a web site. Description for List the threads in a process by its ID for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
base_priority,
current_priority,
href,
identifier,
kind,
priority_level,
process,
start_address,
start_time,
state,
total_processor_time,
type,
user_processor_time,
wait_reason
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND process_id = '{{ process_id }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_network_features_slot">

Gets all network features used by the app (or deployment slot, if specified). Description for Gets all network features used by the app (or deployment slot, if specified).

```sql
SELECT
id,
name,
hybridConnections,
hybridConnectionsV2,
kind,
systemData,
type,
virtualNetworkConnection,
virtualNetworkName
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND view_name = '{{ view_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_triggered_web_job_history_slot">

List a triggered web job's history for an app, or a deployment slot. Description for List a triggered web job's history for an app, or a deployment slot.

```sql
SELECT
id,
name,
kind,
runs,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND web_job_name = '{{ web_job_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_network_trace_operation_slot">

Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).

```sql
SELECT
message,
path,
status
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection_slot">

Gets a private endpoint connection. Description for Gets a private endpoint connection.

```sql
SELECT
id,
name,
ipAddresses,
kind,
privateEndpoint,
privateLinkServiceConnectionState,
provisioningState,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_hybrid_connection">

Retrieves a specific Service Bus Hybrid Connection used by this Web App. Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App.

```sql
SELECT
id,
name,
hostname,
kind,
port,
relayArmUri,
relayName,
sendKeyName,
sendKeyValue,
serviceBusNamespace,
serviceBusSuffix,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND relay_name = '{{ relay_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_vnet_connection_slot">

Gets a virtual network the app (or deployment slot) is connected to by name. Description for Gets a virtual network the app (or deployment slot) is connected to by name.

```sql
SELECT
id,
name,
certBlob,
certThumbprint,
dnsServers,
isSwift,
kind,
resyncRequired,
routes,
systemData,
type,
vnetResourceId
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND vnet_name = '{{ vnet_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_vnet_connection_gateway">

Gets an app's Virtual Network gateway. Description for Gets an app's Virtual Network gateway.

```sql
SELECT
id,
name,
kind,
systemData,
type,
vnetName,
vpnPackageUri
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND vnet_name = '{{ vnet_name }}' -- required
AND gateway_name = '{{ gateway_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_app_setting_key_vault_reference_slot">

Gets the config reference and status of an app. Description for Gets the config reference and status of an app.

```sql
SELECT
id,
name,
activeVersion,
details,
identityType,
kind,
reference,
secretName,
secretVersion,
source,
status,
systemData,
type,
vaultName
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND app_setting_key = '{{ app_setting_key }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_connection_string_key_vault_reference_slot">

Gets the config reference and status of an app. Description for Gets the config reference and status of an app.

```sql
SELECT
id,
name,
activeVersion,
details,
identityType,
kind,
reference,
secretName,
secretVersion,
source,
status,
systemData,
type,
vaultName
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND connection_string_key = '{{ connection_string_key }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_configuration_snapshot_slot">

Gets a snapshot of the configuration of an app at a previous point in time. Description for Gets a snapshot of the configuration of an app at a previous point in time.

```sql
SELECT
id,
name,
acrUseManagedIdentityCreds,
acrUserManagedIdentityID,
alwaysOn,
apiDefinition,
apiManagementConfig,
appCommandLine,
appSettings,
autoHealEnabled,
autoHealRules,
autoSwapSlotName,
azureStorageAccounts,
connectionStrings,
cors,
defaultDocuments,
detailedErrorLoggingEnabled,
documentRoot,
elasticWebAppScaleLimit,
experiments,
ftpsState,
functionAppScaleLimit,
functionsRuntimeScaleMonitoringEnabled,
handlerMappings,
healthCheckPath,
http20Enabled,
http20ProxyFlag,
httpLoggingEnabled,
ipSecurityRestrictions,
ipSecurityRestrictionsDefaultAction,
javaContainer,
javaContainerVersion,
javaVersion,
keyVaultReferenceIdentity,
kind,
limits,
linuxFxVersion,
loadBalancing,
localMySqlEnabled,
logsDirectorySizeLimit,
machineKey,
managedPipelineMode,
managedServiceIdentityId,
metadata,
minTlsCipherSuite,
minTlsVersion,
minimumElasticInstanceCount,
netFrameworkVersion,
nodeVersion,
numberOfWorkers,
phpVersion,
powerShellVersion,
preWarmedInstanceCount,
publicNetworkAccess,
publishingUsername,
push,
pythonVersion,
remoteDebuggingEnabled,
remoteDebuggingVersion,
requestTracingEnabled,
requestTracingExpirationTime,
scmIpSecurityRestrictions,
scmIpSecurityRestrictionsDefaultAction,
scmIpSecurityRestrictionsUseMain,
scmMinTlsVersion,
scmType,
systemData,
tracingOptions,
type,
use32BitWorkerProcess,
virtualApplications,
vnetName,
vnetPrivatePortsCount,
vnetRouteAllEnabled,
webSocketsEnabled,
websiteTimeZone,
windowsFxVersion,
xManagedServiceIdentityId
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND snapshot_id = '{{ snapshot_id }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_slot_site_deployment_status_slot">

Gets the deployment status for an app (or deployment slot, if specified). Gets the deployment status for an app (or deployment slot, if specified).

```sql
SELECT
id,
name,
deploymentId,
errors,
failedInstancesLogs,
kind,
numberOfInstancesFailed,
numberOfInstancesInProgress,
numberOfInstancesSuccessful,
status,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND deployment_status_id = '{{ deployment_status_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_domain_ownership_identifier_slot">

Get domain ownership identifier for web app. Description for Get domain ownership identifier for web app.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND domain_ownership_identifier_name = '{{ domain_ownership_identifier_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_host_name_binding_slot">

Get the named hostname binding for an app (or deployment slot, if specified). Description for Get the named hostname binding for an app (or deployment slot, if specified).

```sql
SELECT
id,
name,
azureResourceName,
azureResourceType,
customHostNameDnsRecordType,
domainId,
hostNameType,
kind,
siteName,
sslState,
systemData,
thumbprint,
type,
virtualIP
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND host_name = '{{ host_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_relay_service_connection_slot">

Gets a hybrid connection configuration by its name. Description for Gets a hybrid connection configuration by its name.

```sql
SELECT
id,
name,
biztalkUri,
entityConnectionString,
entityName,
hostname,
kind,
port,
resourceConnectionString,
resourceType,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND entity_name = '{{ entity_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_process_module">

Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
file_name,
base_address,
file_description,
file_path,
file_version,
href,
is_debug,
kind,
language,
module_memory_size,
product,
product_version,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND process_id = '{{ process_id }}' -- required
AND base_address = '{{ base_address }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_premier_add_on_slot">

Gets a named add-on of an app. Description for Gets a named add-on of an app.

```sql
SELECT
id,
name,
kind,
location,
marketplaceOffer,
marketplacePublisher,
product,
sku,
systemData,
tags,
type,
vendor
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND premier_add_on_name = '{{ premier_add_on_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_public_certificate_slot">

Get the named public certificate for an app (or deployment slot, if specified). Description for Get the named public certificate for an app (or deployment slot, if specified).

```sql
SELECT
id,
name,
blob,
kind,
publicCertificateLocation,
systemData,
thumbprint,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND public_certificate_name = '{{ public_certificate_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_container_slot">

Gets a site container of a site, or a deployment slot. Gets a site container of a site, or a deployment slot.

```sql
SELECT
id,
name,
authType,
createdTime,
environmentVariables,
image,
inheritAppSettingsAndConnectionStrings,
isMain,
kind,
lastModifiedTime,
passwordSecret,
startUpCommand,
systemData,
targetPort,
type,
userManagedIdentityClientId,
userName,
volumeMounts
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND container_name = '{{ container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_extension_slot">

Get site extension information by its ID for a web site, or a deployment slot. Description for Get site extension information by its ID for a web site, or a deployment slot.

```sql
SELECT
id,
name,
extension_id,
authors,
comment,
description,
download_count,
extension_type,
extension_url,
feed_url,
icon_url,
installed_date_time,
installer_command_line_params,
kind,
license_url,
local_is_latest_version,
local_path,
project_url,
provisioningState,
published_date_time,
summary,
systemData,
title,
type,
version
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND site_extension_id = '{{ site_extension_id }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_triggered_web_job_history">

Gets a triggered web job's history by its ID for an app, , or a deployment slot. Description for Gets a triggered web job's history by its ID for an app, , or a deployment slot.

```sql
SELECT
id,
name,
kind,
runs,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND web_job_name = '{{ web_job_name }}' -- required
AND id = '{{ id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_instance_workflow_slot">

Get workflow information by its ID for web site, or a deployment slot. Get workflow information by its ID for web site, or a deployment slot.

```sql
SELECT
id,
name,
files,
flowState,
health,
kind,
location,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_application_settings_slot">

Gets the application settings of an app. Description for Gets the application settings of an app.

```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_backup_status_secrets">

Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body. Description for Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

```sql
SELECT
id,
name,
blobName,
correlationId,
created,
databases,
finishedTimeStamp,
kind,
lastRestoreTimeStamp,
log,
scheduled,
sizeInBytes,
status,
storageAccountUrl,
systemData,
type,
websiteSizeInBytes
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND backup_id = '{{ backup_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_deployment_log">

List deployment log for specific deployment for an app, or a deployment slot. Description for List deployment log for specific deployment for an app, or a deployment slot.

```sql
SELECT
id,
name,
active,
author,
author_email,
deployer,
details,
end_time,
kind,
message,
start_time,
status,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND id = '{{ id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_function_keys">

Get function keys for a function in a web site, or a deployment slot. Description for Get function keys for a function in a web site, or a deployment slot.

```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND function_name = '{{ function_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_instance_processes">

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
deployment_name,
file_name,
user_name,
children,
command_line,
description,
environment_variables,
handle_count,
href,
identifier,
iis_profile_timeout_in_seconds,
is_iis_profile_running,
is_profile_running,
is_scm_site,
is_webjob,
kind,
minidump,
module_count,
modules,
non_paged_system_memory,
open_file_handles,
paged_memory,
paged_system_memory,
parent,
peak_paged_memory,
peak_virtual_memory,
peak_working_set,
private_memory,
privileged_cpu_time,
start_time,
systemData,
thread_count,
threads,
time_stamp,
total_cpu_time,
type,
user_cpu_time,
virtual_memory,
working_set
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND instance_id = '{{ instance_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_process_threads">

List the threads in a process by its ID for a specific scaled-out instance in a web site. Description for List the threads in a process by its ID for a specific scaled-out instance in a web site.

```sql
SELECT
id,
name,
base_priority,
current_priority,
href,
identifier,
kind,
priority_level,
process,
start_address,
start_time,
state,
total_processor_time,
type,
user_processor_time,
wait_reason
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND process_id = '{{ process_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_network_features">

Gets all network features used by the app (or deployment slot, if specified). Description for Gets all network features used by the app (or deployment slot, if specified).

```sql
SELECT
id,
name,
hybridConnections,
hybridConnectionsV2,
kind,
systemData,
type,
virtualNetworkConnection,
virtualNetworkName
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND view_name = '{{ view_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_triggered_web_job_history">

List a triggered web job's history for an app, or a deployment slot. Description for List a triggered web job's history for an app, or a deployment slot.

```sql
SELECT
id,
name,
kind,
runs,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND web_job_name = '{{ web_job_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection">

Gets a private endpoint connection. Description for Gets a private endpoint connection.

```sql
SELECT
id,
name,
ipAddresses,
kind,
privateEndpoint,
privateLinkServiceConnectionState,
provisioningState,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND private_endpoint_connection_name = '{{ private_endpoint_connection_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_vnet_connection">

Gets a virtual network the app (or deployment slot) is connected to by name. Description for Gets a virtual network the app (or deployment slot) is connected to by name.

```sql
SELECT
id,
name,
certBlob,
certThumbprint,
dnsServers,
isSwift,
kind,
resyncRequired,
routes,
systemData,
type,
vnetResourceId
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND vnet_name = '{{ vnet_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_network_trace_operation">

Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).

```sql
SELECT
message,
path,
status
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_app_setting_key_vault_reference">

Gets the config reference and status of an app. Description for Gets the config reference and status of an app.

```sql
SELECT
id,
name,
activeVersion,
details,
identityType,
kind,
reference,
secretName,
secretVersion,
source,
status,
systemData,
type,
vaultName
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND app_setting_key = '{{ app_setting_key }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_connection_string_key_vault_reference">

Gets the config reference and status of an app. Description for Gets the config reference and status of an app.

```sql
SELECT
id,
name,
activeVersion,
details,
identityType,
kind,
reference,
secretName,
secretVersion,
source,
status,
systemData,
type,
vaultName
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND connection_string_key = '{{ connection_string_key }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_configuration_snapshot">

Gets a snapshot of the configuration of an app at a previous point in time. Description for Gets a snapshot of the configuration of an app at a previous point in time.

```sql
SELECT
id,
name,
acrUseManagedIdentityCreds,
acrUserManagedIdentityID,
alwaysOn,
apiDefinition,
apiManagementConfig,
appCommandLine,
appSettings,
autoHealEnabled,
autoHealRules,
autoSwapSlotName,
azureStorageAccounts,
connectionStrings,
cors,
defaultDocuments,
detailedErrorLoggingEnabled,
documentRoot,
elasticWebAppScaleLimit,
experiments,
ftpsState,
functionAppScaleLimit,
functionsRuntimeScaleMonitoringEnabled,
handlerMappings,
healthCheckPath,
http20Enabled,
http20ProxyFlag,
httpLoggingEnabled,
ipSecurityRestrictions,
ipSecurityRestrictionsDefaultAction,
javaContainer,
javaContainerVersion,
javaVersion,
keyVaultReferenceIdentity,
kind,
limits,
linuxFxVersion,
loadBalancing,
localMySqlEnabled,
logsDirectorySizeLimit,
machineKey,
managedPipelineMode,
managedServiceIdentityId,
metadata,
minTlsCipherSuite,
minTlsVersion,
minimumElasticInstanceCount,
netFrameworkVersion,
nodeVersion,
numberOfWorkers,
phpVersion,
powerShellVersion,
preWarmedInstanceCount,
publicNetworkAccess,
publishingUsername,
push,
pythonVersion,
remoteDebuggingEnabled,
remoteDebuggingVersion,
requestTracingEnabled,
requestTracingExpirationTime,
scmIpSecurityRestrictions,
scmIpSecurityRestrictionsDefaultAction,
scmIpSecurityRestrictionsUseMain,
scmMinTlsVersion,
scmType,
systemData,
tracingOptions,
type,
use32BitWorkerProcess,
virtualApplications,
vnetName,
vnetPrivatePortsCount,
vnetRouteAllEnabled,
webSocketsEnabled,
websiteTimeZone,
windowsFxVersion,
xManagedServiceIdentityId
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND snapshot_id = '{{ snapshot_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_production_site_deployment_status">

Gets the deployment status for an app (or deployment slot, if specified). Gets the deployment status for an app (or deployment slot, if specified).

```sql
SELECT
id,
name,
deploymentId,
errors,
failedInstancesLogs,
kind,
numberOfInstancesFailed,
numberOfInstancesInProgress,
numberOfInstancesSuccessful,
status,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND deployment_status_id = '{{ deployment_status_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_domain_ownership_identifier">

Get domain ownership identifier for web app. Description for Get domain ownership identifier for web app.

```sql
SELECT
id,
name,
kind,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND domain_ownership_identifier_name = '{{ domain_ownership_identifier_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_host_name_binding">

Get the named hostname binding for an app (or deployment slot, if specified). Description for Get the named hostname binding for an app (or deployment slot, if specified).

```sql
SELECT
id,
name,
azureResourceName,
azureResourceType,
customHostNameDnsRecordType,
domainId,
hostNameType,
kind,
siteName,
sslState,
systemData,
thumbprint,
type,
virtualIP
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND host_name = '{{ host_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_relay_service_connection">

Gets a hybrid connection configuration by its name. Description for Gets a hybrid connection configuration by its name.

```sql
SELECT
id,
name,
biztalkUri,
entityConnectionString,
entityName,
hostname,
kind,
port,
resourceConnectionString,
resourceType,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND entity_name = '{{ entity_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_premier_add_on">

Gets a named add-on of an app. Description for Gets a named add-on of an app.

```sql
SELECT
id,
name,
kind,
location,
marketplaceOffer,
marketplacePublisher,
product,
sku,
systemData,
tags,
type,
vendor
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND premier_add_on_name = '{{ premier_add_on_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_public_certificate">

Get the named public certificate for an app (or deployment slot, if specified). Description for Get the named public certificate for an app (or deployment slot, if specified).

```sql
SELECT
id,
name,
blob,
kind,
publicCertificateLocation,
systemData,
thumbprint,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND public_certificate_name = '{{ public_certificate_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_container">

Gets a site container of a site, or a deployment slot. Gets a site container of a site, or a deployment slot.

```sql
SELECT
id,
name,
authType,
createdTime,
environmentVariables,
image,
inheritAppSettingsAndConnectionStrings,
isMain,
kind,
lastModifiedTime,
passwordSecret,
startUpCommand,
systemData,
targetPort,
type,
userManagedIdentityClientId,
userName,
volumeMounts
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND container_name = '{{ container_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_extension">

Get site extension information by its ID for a web site, or a deployment slot. Description for Get site extension information by its ID for a web site, or a deployment slot.

```sql
SELECT
id,
name,
extension_id,
authors,
comment,
description,
download_count,
extension_type,
extension_url,
feed_url,
icon_url,
installed_date_time,
installer_command_line_params,
kind,
license_url,
local_is_latest_version,
local_path,
project_url,
provisioningState,
published_date_time,
summary,
systemData,
title,
type,
version
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND site_extension_id = '{{ site_extension_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_workflow">

Get workflow information by its ID for web site, or a deployment slot. Get workflow information by its ID for web site, or a deployment slot.

```sql
SELECT
id,
name,
files,
flowState,
health,
kind,
location,
systemData,
type
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND workflow_name = '{{ workflow_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the details of a web, mobile, or API app. Description for Gets the details of a web, mobile, or API app.

```sql
SELECT
id,
name,
autoGeneratedDomainNameLabelScope,
availabilityState,
clientAffinityEnabled,
clientAffinityPartitioningEnabled,
clientAffinityProxyEnabled,
clientCertEnabled,
clientCertExclusionPaths,
clientCertMode,
cloningInfo,
containerSize,
customDomainVerificationId,
dailyMemoryTimeQuota,
daprConfig,
defaultHostName,
dnsConfiguration,
enabled,
enabledHostNames,
endToEndEncryptionEnabled,
extendedLocation,
functionAppConfig,
hostNameSslStates,
hostNames,
hostNamesDisabled,
hostingEnvironmentProfile,
httpsOnly,
hyperV,
identity,
inProgressOperationId,
ipMode,
isDefaultContainer,
isXenon,
keyVaultReferenceIdentity,
kind,
lastModifiedTimeUtc,
location,
managedEnvironmentId,
maxNumberOfWorkers,
outboundIpAddresses,
outboundVnetRouting,
possibleOutboundIpAddresses,
publicNetworkAccess,
redundancyMode,
repositorySiteName,
reserved,
resourceConfig,
resourceGroup,
scmSiteAlsoStopped,
serverFarmId,
siteConfig,
sku,
slotSwapStatus,
sshEnabled,
state,
storageAccountRequired,
suspendedTill,
systemData,
tags,
targetSwapSlot,
trafficManagerHostNames,
type,
usageState,
virtualNetworkSubnetId,
workloadProfileName
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all web, mobile, and API apps in the specified resource group. Description for Gets all web, mobile, and API apps in the specified resource group.

```sql
SELECT
id,
name,
autoGeneratedDomainNameLabelScope,
availabilityState,
clientAffinityEnabled,
clientAffinityPartitioningEnabled,
clientAffinityProxyEnabled,
clientCertEnabled,
clientCertExclusionPaths,
clientCertMode,
cloningInfo,
containerSize,
customDomainVerificationId,
dailyMemoryTimeQuota,
daprConfig,
defaultHostName,
dnsConfiguration,
enabled,
enabledHostNames,
endToEndEncryptionEnabled,
extendedLocation,
functionAppConfig,
hostNameSslStates,
hostNames,
hostNamesDisabled,
hostingEnvironmentProfile,
httpsOnly,
hyperV,
identity,
inProgressOperationId,
ipMode,
isDefaultContainer,
isXenon,
keyVaultReferenceIdentity,
kind,
lastModifiedTimeUtc,
location,
managedEnvironmentId,
maxNumberOfWorkers,
outboundIpAddresses,
outboundVnetRouting,
possibleOutboundIpAddresses,
publicNetworkAccess,
redundancyMode,
repositorySiteName,
reserved,
resourceConfig,
resourceGroup,
scmSiteAlsoStopped,
serverFarmId,
siteConfig,
sku,
slotSwapStatus,
sshEnabled,
state,
storageAccountRequired,
suspendedTill,
systemData,
tags,
targetSwapSlot,
trafficManagerHostNames,
type,
usageState,
virtualNetworkSubnetId,
workloadProfileName
FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND includeSlots = '{{ includeSlots }}'
;
```
</TabItem>
<TabItem value="list">

Get all apps for a subscription. Description for Get all apps for a subscription.

```sql
SELECT
id,
name,
autoGeneratedDomainNameLabelScope,
availabilityState,
clientAffinityEnabled,
clientAffinityPartitioningEnabled,
clientAffinityProxyEnabled,
clientCertEnabled,
clientCertExclusionPaths,
clientCertMode,
cloningInfo,
containerSize,
customDomainVerificationId,
dailyMemoryTimeQuota,
daprConfig,
defaultHostName,
dnsConfiguration,
enabled,
enabledHostNames,
endToEndEncryptionEnabled,
extendedLocation,
functionAppConfig,
hostNameSslStates,
hostNames,
hostNamesDisabled,
hostingEnvironmentProfile,
httpsOnly,
hyperV,
identity,
inProgressOperationId,
ipMode,
isDefaultContainer,
isXenon,
keyVaultReferenceIdentity,
kind,
lastModifiedTimeUtc,
location,
managedEnvironmentId,
maxNumberOfWorkers,
outboundIpAddresses,
outboundVnetRouting,
possibleOutboundIpAddresses,
publicNetworkAccess,
redundancyMode,
repositorySiteName,
reserved,
resourceConfig,
resourceGroup,
scmSiteAlsoStopped,
serverFarmId,
siteConfig,
sku,
slotSwapStatus,
sshEnabled,
state,
storageAccountRequired,
suspendedTill,
systemData,
tags,
targetSwapSlot,
trafficManagerHostNames,
type,
usageState,
virtualNetworkSubnetId,
workloadProfileName
FROM azure.web.web_apps
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

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

```sql
INSERT INTO azure.web.web_apps (
tags,
location,
properties,
identity,
extendedLocation,
kind,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ extendedLocation }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
extendedLocation,
identity,
kind,
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
- name: web_apps
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the web_apps resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the web_apps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the web_apps resource.
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
        Site resource specific properties.
      value:
        state: "{{ state }}"
        hostNames:
          - "{{ hostNames }}"
        repositorySiteName: "{{ repositorySiteName }}"
        usageState: "{{ usageState }}"
        enabled: {{ enabled }}
        enabledHostNames:
          - "{{ enabledHostNames }}"
        availabilityState: "{{ availabilityState }}"
        hostNameSslStates:
          - name: "{{ name }}"
            sslState: "{{ sslState }}"
            virtualIP: "{{ virtualIP }}"
            thumbprint: "{{ thumbprint }}"
            toUpdate: {{ toUpdate }}
            hostType: "{{ hostType }}"
        serverFarmId: "{{ serverFarmId }}"
        reserved: {{ reserved }}
        isXenon: {{ isXenon }}
        hyperV: {{ hyperV }}
        lastModifiedTimeUtc: "{{ lastModifiedTimeUtc }}"
        dnsConfiguration:
          dnsServers:
            - "{{ dnsServers }}"
          dnsAltServer: "{{ dnsAltServer }}"
          dnsRetryAttemptTimeout: {{ dnsRetryAttemptTimeout }}
          dnsRetryAttemptCount: {{ dnsRetryAttemptCount }}
          dnsMaxCacheTimeout: {{ dnsMaxCacheTimeout }}
          dnsLegacySortOrder: {{ dnsLegacySortOrder }}
        outboundVnetRouting:
          allTraffic: {{ allTraffic }}
          applicationTraffic: {{ applicationTraffic }}
          contentShareTraffic: {{ contentShareTraffic }}
          imagePullTraffic: {{ imagePullTraffic }}
          backupRestoreTraffic: {{ backupRestoreTraffic }}
        siteConfig:
          numberOfWorkers: {{ numberOfWorkers }}
          defaultDocuments:
            - "{{ defaultDocuments }}"
          netFrameworkVersion: "{{ netFrameworkVersion }}"
          phpVersion: "{{ phpVersion }}"
          pythonVersion: "{{ pythonVersion }}"
          nodeVersion: "{{ nodeVersion }}"
          powerShellVersion: "{{ powerShellVersion }}"
          linuxFxVersion: "{{ linuxFxVersion }}"
          windowsFxVersion: "{{ windowsFxVersion }}"
          requestTracingEnabled: {{ requestTracingEnabled }}
          requestTracingExpirationTime: "{{ requestTracingExpirationTime }}"
          remoteDebuggingEnabled: {{ remoteDebuggingEnabled }}
          remoteDebuggingVersion: "{{ remoteDebuggingVersion }}"
          httpLoggingEnabled: {{ httpLoggingEnabled }}
          acrUseManagedIdentityCreds: {{ acrUseManagedIdentityCreds }}
          acrUserManagedIdentityID: "{{ acrUserManagedIdentityID }}"
          logsDirectorySizeLimit: {{ logsDirectorySizeLimit }}
          detailedErrorLoggingEnabled: {{ detailedErrorLoggingEnabled }}
          publishingUsername: "{{ publishingUsername }}"
          appSettings:
            - name: "{{ name }}"
              value: "{{ value }}"
          metadata:
            - name: "{{ name }}"
              value: "{{ value }}"
          connectionStrings:
            - name: "{{ name }}"
              connectionString: "{{ connectionString }}"
              type: "{{ type }}"
          machineKey:
            validation: "{{ validation }}"
            validationKey: "{{ validationKey }}"
            decryption: "{{ decryption }}"
            decryptionKey: "{{ decryptionKey }}"
          handlerMappings:
            - extension: "{{ extension }}"
              scriptProcessor: "{{ scriptProcessor }}"
              arguments: "{{ arguments }}"
          documentRoot: "{{ documentRoot }}"
          scmType: "{{ scmType }}"
          use32BitWorkerProcess: {{ use32BitWorkerProcess }}
          webSocketsEnabled: {{ webSocketsEnabled }}
          alwaysOn: {{ alwaysOn }}
          javaVersion: "{{ javaVersion }}"
          javaContainer: "{{ javaContainer }}"
          javaContainerVersion: "{{ javaContainerVersion }}"
          appCommandLine: "{{ appCommandLine }}"
          managedPipelineMode: "{{ managedPipelineMode }}"
          virtualApplications:
            - virtualPath: "{{ virtualPath }}"
              physicalPath: "{{ physicalPath }}"
              preloadEnabled: {{ preloadEnabled }}
              virtualDirectories: "{{ virtualDirectories }}"
          loadBalancing: "{{ loadBalancing }}"
          experiments:
            rampUpRules:
              - actionHostName: "{{ actionHostName }}"
                reroutePercentage: {{ reroutePercentage }}
                changeStep: {{ changeStep }}
                changeIntervalInMinutes: {{ changeIntervalInMinutes }}
                minReroutePercentage: {{ minReroutePercentage }}
                maxReroutePercentage: {{ maxReroutePercentage }}
                changeDecisionCallbackUrl: "{{ changeDecisionCallbackUrl }}"
                name: "{{ name }}"
          limits:
            maxPercentageCpu: {{ maxPercentageCpu }}
            maxMemoryInMb: {{ maxMemoryInMb }}
            maxDiskSizeInMb: {{ maxDiskSizeInMb }}
          autoHealEnabled: {{ autoHealEnabled }}
          autoHealRules:
            triggers:
              requests:
                count: {{ count }}
                timeInterval: "{{ timeInterval }}"
              privateBytesInKB: {{ privateBytesInKB }}
              statusCodes:
                - status: {{ status }}
                  subStatus: {{ subStatus }}
                  win32Status: {{ win32Status }}
                  count: {{ count }}
                  timeInterval: "{{ timeInterval }}"
                  path: "{{ path }}"
              slowRequests:
                timeTaken: "{{ timeTaken }}"
                path: "{{ path }}"
                count: {{ count }}
                timeInterval: "{{ timeInterval }}"
              slowRequestsWithPath:
                - timeTaken: "{{ timeTaken }}"
                  path: "{{ path }}"
                  count: {{ count }}
                  timeInterval: "{{ timeInterval }}"
              statusCodesRange:
                - statusCodes: "{{ statusCodes }}"
                  path: "{{ path }}"
                  count: {{ count }}
                  timeInterval: "{{ timeInterval }}"
            actions:
              actionType: "{{ actionType }}"
              customAction:
                exe: "{{ exe }}"
                parameters: "{{ parameters }}"
              minProcessExecutionTime: "{{ minProcessExecutionTime }}"
          tracingOptions: "{{ tracingOptions }}"
          vnetName: "{{ vnetName }}"
          vnetRouteAllEnabled: {{ vnetRouteAllEnabled }}
          vnetPrivatePortsCount: {{ vnetPrivatePortsCount }}
          cors:
            allowedOrigins:
              - "{{ allowedOrigins }}"
            supportCredentials: {{ supportCredentials }}
          push:
            id: "{{ id }}"
            name: "{{ name }}"
            kind: "{{ kind }}"
            type: "{{ type }}"
            properties:
              isPushEnabled: {{ isPushEnabled }}
              tagWhitelistJson: "{{ tagWhitelistJson }}"
              tagsRequiringAuth: "{{ tagsRequiringAuth }}"
              dynamicTagsJson: "{{ dynamicTagsJson }}"
          apiDefinition:
            url: "{{ url }}"
          apiManagementConfig:
            id: "{{ id }}"
          autoSwapSlotName: "{{ autoSwapSlotName }}"
          localMySqlEnabled: {{ localMySqlEnabled }}
          managedServiceIdentityId: {{ managedServiceIdentityId }}
          xManagedServiceIdentityId: {{ xManagedServiceIdentityId }}
          keyVaultReferenceIdentity: "{{ keyVaultReferenceIdentity }}"
          ipSecurityRestrictions:
            - ipAddress: "{{ ipAddress }}"
              subnetMask: "{{ subnetMask }}"
              vnetSubnetResourceId: "{{ vnetSubnetResourceId }}"
              vnetTrafficTag: {{ vnetTrafficTag }}
              subnetTrafficTag: {{ subnetTrafficTag }}
              action: "{{ action }}"
              tag: "{{ tag }}"
              priority: {{ priority }}
              name: "{{ name }}"
              description: "{{ description }}"
              headers: "{{ headers }}"
          ipSecurityRestrictionsDefaultAction: "{{ ipSecurityRestrictionsDefaultAction }}"
          scmIpSecurityRestrictions:
            - ipAddress: "{{ ipAddress }}"
              subnetMask: "{{ subnetMask }}"
              vnetSubnetResourceId: "{{ vnetSubnetResourceId }}"
              vnetTrafficTag: {{ vnetTrafficTag }}
              subnetTrafficTag: {{ subnetTrafficTag }}
              action: "{{ action }}"
              tag: "{{ tag }}"
              priority: {{ priority }}
              name: "{{ name }}"
              description: "{{ description }}"
              headers: "{{ headers }}"
          scmIpSecurityRestrictionsDefaultAction: "{{ scmIpSecurityRestrictionsDefaultAction }}"
          scmIpSecurityRestrictionsUseMain: {{ scmIpSecurityRestrictionsUseMain }}
          http20Enabled: {{ http20Enabled }}
          http20ProxyFlag: {{ http20ProxyFlag }}
          minTlsVersion: "{{ minTlsVersion }}"
          minTlsCipherSuite: "{{ minTlsCipherSuite }}"
          scmMinTlsVersion: "{{ scmMinTlsVersion }}"
          ftpsState: "{{ ftpsState }}"
          preWarmedInstanceCount: {{ preWarmedInstanceCount }}
          functionAppScaleLimit: {{ functionAppScaleLimit }}
          elasticWebAppScaleLimit: {{ elasticWebAppScaleLimit }}
          healthCheckPath: "{{ healthCheckPath }}"
          functionsRuntimeScaleMonitoringEnabled: {{ functionsRuntimeScaleMonitoringEnabled }}
          websiteTimeZone: "{{ websiteTimeZone }}"
          minimumElasticInstanceCount: {{ minimumElasticInstanceCount }}
          azureStorageAccounts: "{{ azureStorageAccounts }}"
          publicNetworkAccess: "{{ publicNetworkAccess }}"
        functionAppConfig:
          deployment:
            storage:
              type: "{{ type }}"
              value: "{{ value }}"
              authentication:
                type: "{{ type }}"
                userAssignedIdentityResourceId: "{{ userAssignedIdentityResourceId }}"
                storageAccountConnectionStringName: "{{ storageAccountConnectionStringName }}"
          runtime:
            name: "{{ name }}"
            version: "{{ version }}"
          scaleAndConcurrency:
            alwaysReady:
              - name: "{{ name }}"
                instanceCount: {{ instanceCount }}
            maximumInstanceCount: {{ maximumInstanceCount }}
            instanceMemoryMB: {{ instanceMemoryMB }}
            triggers:
              http:
                perInstanceConcurrency: {{ perInstanceConcurrency }}
          siteUpdateStrategy:
            type: "{{ type }}"
        daprConfig:
          enabled: {{ enabled }}
          appId: "{{ appId }}"
          appPort: {{ appPort }}
          httpReadBufferSize: {{ httpReadBufferSize }}
          httpMaxRequestSize: {{ httpMaxRequestSize }}
          logLevel: "{{ logLevel }}"
          enableApiLogging: {{ enableApiLogging }}
        workloadProfileName: "{{ workloadProfileName }}"
        resourceConfig:
          cpu: {{ cpu }}
          memory: "{{ memory }}"
        trafficManagerHostNames:
          - "{{ trafficManagerHostNames }}"
        scmSiteAlsoStopped: {{ scmSiteAlsoStopped }}
        targetSwapSlot: "{{ targetSwapSlot }}"
        hostingEnvironmentProfile:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
        clientAffinityEnabled: {{ clientAffinityEnabled }}
        clientAffinityPartitioningEnabled: {{ clientAffinityPartitioningEnabled }}
        clientAffinityProxyEnabled: {{ clientAffinityProxyEnabled }}
        clientCertEnabled: {{ clientCertEnabled }}
        clientCertMode: "{{ clientCertMode }}"
        clientCertExclusionPaths: "{{ clientCertExclusionPaths }}"
        ipMode: "{{ ipMode }}"
        endToEndEncryptionEnabled: {{ endToEndEncryptionEnabled }}
        sshEnabled: {{ sshEnabled }}
        hostNamesDisabled: {{ hostNamesDisabled }}
        customDomainVerificationId: "{{ customDomainVerificationId }}"
        outboundIpAddresses: "{{ outboundIpAddresses }}"
        possibleOutboundIpAddresses: "{{ possibleOutboundIpAddresses }}"
        containerSize: {{ containerSize }}
        dailyMemoryTimeQuota: {{ dailyMemoryTimeQuota }}
        suspendedTill: "{{ suspendedTill }}"
        maxNumberOfWorkers: {{ maxNumberOfWorkers }}
        cloningInfo:
          correlationId: "{{ correlationId }}"
          overwrite: {{ overwrite }}
          cloneCustomHostNames: {{ cloneCustomHostNames }}
          cloneSourceControl: {{ cloneSourceControl }}
          sourceWebAppId: "{{ sourceWebAppId }}"
          sourceWebAppLocation: "{{ sourceWebAppLocation }}"
          hostingEnvironment: "{{ hostingEnvironment }}"
          appSettingsOverrides: "{{ appSettingsOverrides }}"
          configureLoadBalancing: {{ configureLoadBalancing }}
          trafficManagerProfileId: "{{ trafficManagerProfileId }}"
          trafficManagerProfileName: "{{ trafficManagerProfileName }}"
        resourceGroup: "{{ resourceGroup }}"
        isDefaultContainer: {{ isDefaultContainer }}
        defaultHostName: "{{ defaultHostName }}"
        slotSwapStatus:
          timestampUtc: "{{ timestampUtc }}"
          sourceSlotName: "{{ sourceSlotName }}"
          destinationSlotName: "{{ destinationSlotName }}"
        httpsOnly: {{ httpsOnly }}
        redundancyMode: "{{ redundancyMode }}"
        inProgressOperationId: "{{ inProgressOperationId }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        storageAccountRequired: {{ storageAccountRequired }}
        keyVaultReferenceIdentity: "{{ keyVaultReferenceIdentity }}"
        autoGeneratedDomainNameLabelScope: "{{ autoGeneratedDomainNameLabelScope }}"
        virtualNetworkSubnetId: "{{ virtualNetworkSubnetId }}"
        managedEnvironmentId: "{{ managedEnvironmentId }}"
        sku: "{{ sku }}"
    - name: identity
      description: |
        Managed service identity.
      value:
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: extendedLocation
      description: |
        Extended Location.
      value:
        name: "{{ name }}"
        type: "{{ type }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of resource. If the resource is an app, you can refer to \`https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference \`_ for details supported values for kind.
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

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

```sql
UPDATE azure.web.web_apps
SET 
kind = '{{ kind }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
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

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

```sql
REPLACE azure.web.web_apps
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
extendedLocation = '{{ extendedLocation }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
extendedLocation,
identity,
kind,
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

Deletes a web, mobile, or API app, or one of the deployment slots. Description for Deletes a web, mobile, or API app, or one of the deployment slots.

```sql
DELETE FROM azure.web.web_apps
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteMetrics = '{{ deleteMetrics }}'
AND deleteEmptyServerFarm = '{{ deleteEmptyServerFarm }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_slots"
    values={[
        { label: 'list_slots', value: 'list_slots' },
        { label: 'list_azure_storage_accounts_slot', value: 'list_azure_storage_accounts_slot' },
        { label: 'list_connection_strings_slot', value: 'list_connection_strings_slot' },
        { label: 'list_metadata_slot', value: 'list_metadata_slot' },
        { label: 'list_publishing_credentials_slot', value: 'list_publishing_credentials_slot' },
        { label: 'list_site_push_settings_slot', value: 'list_site_push_settings_slot' },
        { label: 'list_host_keys_slot', value: 'list_host_keys_slot' },
        { label: 'list_sync_status_slot', value: 'list_sync_status_slot' },
        { label: 'list_hybrid_connections_slot', value: 'list_hybrid_connections_slot' },
        { label: 'list_relay_service_connections_slot', value: 'list_relay_service_connections_slot' },
        { label: 'list_site_backups_slot', value: 'list_site_backups_slot' },
        { label: 'list_sync_function_triggers_slot', value: 'list_sync_function_triggers_slot' },
        { label: 'list_perf_mon_counters_slot', value: 'list_perf_mon_counters_slot' },
        { label: 'list_premier_add_ons_slot', value: 'list_premier_add_ons_slot' },
        { label: 'list_publishing_profile_xml_with_secrets_slot', value: 'list_publishing_profile_xml_with_secrets_slot' },
        { label: 'list_snapshots_slot', value: 'list_snapshots_slot' },
        { label: 'list_snapshots_from_dr_secondary_slot', value: 'list_snapshots_from_dr_secondary_slot' },
        { label: 'list_usages_slot', value: 'list_usages_slot' },
        { label: 'list_workflows_connections_slot', value: 'list_workflows_connections_slot' },
        { label: 'list_vnet_connections_slot', value: 'list_vnet_connections_slot' },
        { label: 'list_vnet_connections', value: 'list_vnet_connections' },
        { label: 'list_application_settings', value: 'list_application_settings' },
        { label: 'list_azure_storage_accounts', value: 'list_azure_storage_accounts' },
        { label: 'list_connection_strings', value: 'list_connection_strings' },
        { label: 'list_metadata', value: 'list_metadata' },
        { label: 'list_publishing_credentials', value: 'list_publishing_credentials' },
        { label: 'list_site_push_settings', value: 'list_site_push_settings' },
        { label: 'list_host_keys', value: 'list_host_keys' },
        { label: 'list_sync_status', value: 'list_sync_status' },
        { label: 'list_hybrid_connections', value: 'list_hybrid_connections' },
        { label: 'list_relay_service_connections', value: 'list_relay_service_connections' },
        { label: 'list_site_backups', value: 'list_site_backups' },
        { label: 'list_sync_function_triggers', value: 'list_sync_function_triggers' },
        { label: 'list_perf_mon_counters', value: 'list_perf_mon_counters' },
        { label: 'list_premier_add_ons', value: 'list_premier_add_ons' },
        { label: 'list_publishing_profile_xml_with_secrets', value: 'list_publishing_profile_xml_with_secrets' },
        { label: 'list_snapshots', value: 'list_snapshots' },
        { label: 'list_snapshots_from_dr_secondary', value: 'list_snapshots_from_dr_secondary' },
        { label: 'list_usages', value: 'list_usages' },
        { label: 'list_workflows_connections', value: 'list_workflows_connections' },
        { label: 'list_backups', value: 'list_backups' },
        { label: 'list_backups_slot', value: 'list_backups_slot' },
        { label: 'list_basic_publishing_credentials_policies', value: 'list_basic_publishing_credentials_policies' },
        { label: 'list_basic_publishing_credentials_policies_slot', value: 'list_basic_publishing_credentials_policies_slot' },
        { label: 'list_slot_configuration_names', value: 'list_slot_configuration_names' },
        { label: 'update_slot_configuration_names', value: 'update_slot_configuration_names' },
        { label: 'list_configuration_snapshot_info', value: 'list_configuration_snapshot_info' },
        { label: 'list_configurations', value: 'list_configurations' },
        { label: 'list_configuration_snapshot_info_slot', value: 'list_configuration_snapshot_info_slot' },
        { label: 'list_configurations_slot', value: 'list_configurations_slot' },
        { label: 'list_continuous_web_jobs', value: 'list_continuous_web_jobs' },
        { label: 'list_continuous_web_jobs_slot', value: 'list_continuous_web_jobs_slot' },
        { label: 'list_production_site_deployment_statuses', value: 'list_production_site_deployment_statuses' },
        { label: 'list_slot_site_deployment_statuses_slot', value: 'list_slot_site_deployment_statuses_slot' },
        { label: 'list_deployments', value: 'list_deployments' },
        { label: 'list_deployments_slot', value: 'list_deployments_slot' },
        { label: 'list_domain_ownership_identifiers', value: 'list_domain_ownership_identifiers' },
        { label: 'list_domain_ownership_identifiers_slot', value: 'list_domain_ownership_identifiers_slot' },
        { label: 'list_functions', value: 'list_functions' },
        { label: 'list_function_secrets', value: 'list_function_secrets' },
        { label: 'list_instance_functions_slot', value: 'list_instance_functions_slot' },
        { label: 'list_function_secrets_slot', value: 'list_function_secrets_slot' },
        { label: 'list_host_name_bindings', value: 'list_host_name_bindings' },
        { label: 'list_host_name_bindings_slot', value: 'list_host_name_bindings_slot' },
        { label: 'list_instance_identifiers', value: 'list_instance_identifiers' },
        { label: 'list_instance_identifiers_slot', value: 'list_instance_identifiers_slot' },
        { label: 'list_processes', value: 'list_processes' },
        { label: 'list_processes_slot', value: 'list_processes_slot' },
        { label: 'list_instance_process_modules', value: 'list_instance_process_modules' },
        { label: 'list_process_modules', value: 'list_process_modules' },
        { label: 'list_instance_process_modules_slot', value: 'list_instance_process_modules_slot' },
        { label: 'list_process_modules_slot', value: 'list_process_modules_slot' },
        { label: 'list_public_certificates', value: 'list_public_certificates' },
        { label: 'list_public_certificates_slot', value: 'list_public_certificates_slot' },
        { label: 'list_site_containers', value: 'list_site_containers' },
        { label: 'list_site_containers_slot', value: 'list_site_containers_slot' },
        { label: 'list_site_extensions', value: 'list_site_extensions' },
        { label: 'list_site_extensions_slot', value: 'list_site_extensions_slot' },
        { label: 'list_triggered_web_jobs_slot', value: 'list_triggered_web_jobs_slot' },
        { label: 'list_triggered_web_jobs', value: 'list_triggered_web_jobs' },
        { label: 'list_web_jobs_slot', value: 'list_web_jobs_slot' },
        { label: 'list_web_jobs', value: 'list_web_jobs' },
        { label: 'list_instance_workflows_slot', value: 'list_instance_workflows_slot' },
        { label: 'list_workflows', value: 'list_workflows' },
        { label: 'get_slot', value: 'get_slot' },
        { label: 'create_or_update_slot', value: 'create_or_update_slot' },
        { label: 'update_slot', value: 'update_slot' },
        { label: 'delete_slot', value: 'delete_slot' },
        { label: 'get_auth_settings_slot', value: 'get_auth_settings_slot' },
        { label: 'get_backup_configuration_slot', value: 'get_backup_configuration_slot' },
        { label: 'get_web_site_container_logs_slot', value: 'get_web_site_container_logs_slot' },
        { label: 'get_container_logs_zip_slot', value: 'get_container_logs_zip_slot' },
        { label: 'get_functions_admin_token_slot', value: 'get_functions_admin_token_slot' },
        { label: 'get_network_traces_slot', value: 'get_network_traces_slot' },
        { label: 'get_network_trace_operation_slot_v2', value: 'get_network_trace_operation_slot_v2' },
        { label: 'get_network_traces_slot_v2', value: 'get_network_traces_slot_v2' },
        { label: 'get_site_php_error_log_flag_slot', value: 'get_site_php_error_log_flag_slot' },
        { label: 'get_private_link_resources_slot', value: 'get_private_link_resources_slot' },
        { label: 'approve_or_reject_private_endpoint_connection', value: 'approve_or_reject_private_endpoint_connection' },
        { label: 'delete_private_endpoint_connection', value: 'delete_private_endpoint_connection' },
        { label: 'get_private_endpoint_connection_list', value: 'get_private_endpoint_connection_list' },
        { label: 'approve_or_reject_private_endpoint_connection_slot', value: 'approve_or_reject_private_endpoint_connection_slot' },
        { label: 'delete_private_endpoint_connection_slot', value: 'delete_private_endpoint_connection_slot' },
        { label: 'get_private_endpoint_connection_list_slot', value: 'get_private_endpoint_connection_list_slot' },
        { label: 'create_or_update_hybrid_connection', value: 'create_or_update_hybrid_connection' },
        { label: 'update_hybrid_connection', value: 'update_hybrid_connection' },
        { label: 'delete_hybrid_connection', value: 'delete_hybrid_connection' },
        { label: 'create_or_update_hybrid_connection_slot', value: 'create_or_update_hybrid_connection_slot' },
        { label: 'update_hybrid_connection_slot', value: 'update_hybrid_connection_slot' },
        { label: 'delete_hybrid_connection_slot', value: 'delete_hybrid_connection_slot' },
        { label: 'create_or_update_vnet_connection_slot', value: 'create_or_update_vnet_connection_slot' },
        { label: 'update_vnet_connection_slot', value: 'update_vnet_connection_slot' },
        { label: 'delete_vnet_connection_slot', value: 'delete_vnet_connection_slot' },
        { label: 'create_or_update_vnet_connection', value: 'create_or_update_vnet_connection' },
        { label: 'update_vnet_connection', value: 'update_vnet_connection' },
        { label: 'delete_vnet_connection', value: 'delete_vnet_connection' },
        { label: 'create_or_update_vnet_connection_gateway_slot', value: 'create_or_update_vnet_connection_gateway_slot' },
        { label: 'update_vnet_connection_gateway_slot', value: 'update_vnet_connection_gateway_slot' },
        { label: 'create_or_update_vnet_connection_gateway', value: 'create_or_update_vnet_connection_gateway' },
        { label: 'update_vnet_connection_gateway', value: 'update_vnet_connection_gateway' },
        { label: 'get_auth_settings', value: 'get_auth_settings' },
        { label: 'get_backup_configuration', value: 'get_backup_configuration' },
        { label: 'get_web_site_container_logs', value: 'get_web_site_container_logs' },
        { label: 'get_container_logs_zip', value: 'get_container_logs_zip' },
        { label: 'get_one_deploy_status', value: 'get_one_deploy_status' },
        { label: 'create_one_deploy_operation', value: 'create_one_deploy_operation' },
        { label: 'get_functions_admin_token', value: 'get_functions_admin_token' },
        { label: 'get_network_traces', value: 'get_network_traces' },
        { label: 'get_network_trace_operation_v2', value: 'get_network_trace_operation_v2' },
        { label: 'get_network_traces_v2', value: 'get_network_traces_v2' },
        { label: 'get_site_php_error_log_flag', value: 'get_site_php_error_log_flag' },
        { label: 'get_private_link_resources', value: 'get_private_link_resources' },
        { label: 'get_backup_status', value: 'get_backup_status' },
        { label: 'delete_backup', value: 'delete_backup' },
        { label: 'get_backup_status_slot', value: 'get_backup_status_slot' },
        { label: 'delete_backup_slot', value: 'delete_backup_slot' },
        { label: 'get_ftp_allowed', value: 'get_ftp_allowed' },
        { label: 'update_ftp_allowed', value: 'update_ftp_allowed' },
        { label: 'get_scm_allowed', value: 'get_scm_allowed' },
        { label: 'update_scm_allowed', value: 'update_scm_allowed' },
        { label: 'get_ftp_allowed_slot', value: 'get_ftp_allowed_slot' },
        { label: 'update_ftp_allowed_slot', value: 'update_ftp_allowed_slot' },
        { label: 'get_scm_allowed_slot', value: 'get_scm_allowed_slot' },
        { label: 'update_scm_allowed_slot', value: 'update_scm_allowed_slot' },
        { label: 'get_auth_settings_v2_without_secrets', value: 'get_auth_settings_v2_without_secrets' },
        { label: 'update_auth_settings_v2', value: 'update_auth_settings_v2' },
        { label: 'get_auth_settings_v2', value: 'get_auth_settings_v2' },
        { label: 'get_auth_settings_v2_without_secrets_slot', value: 'get_auth_settings_v2_without_secrets_slot' },
        { label: 'update_auth_settings_v2_slot', value: 'update_auth_settings_v2_slot' },
        { label: 'get_auth_settings_v2_slot', value: 'get_auth_settings_v2_slot' },
        { label: 'get_app_settings_key_vault_references', value: 'get_app_settings_key_vault_references' },
        { label: 'get_site_connection_string_key_vault_references', value: 'get_site_connection_string_key_vault_references' },
        { label: 'get_app_settings_key_vault_references_slot', value: 'get_app_settings_key_vault_references_slot' },
        { label: 'get_site_connection_string_key_vault_references_slot', value: 'get_site_connection_string_key_vault_references_slot' },
        { label: 'get_diagnostic_logs_configuration', value: 'get_diagnostic_logs_configuration' },
        { label: 'update_diagnostic_logs_config', value: 'update_diagnostic_logs_config' },
        { label: 'get_diagnostic_logs_configuration_slot', value: 'get_diagnostic_logs_configuration_slot' },
        { label: 'update_diagnostic_logs_config_slot', value: 'update_diagnostic_logs_config_slot' },
        { label: 'get_configuration', value: 'get_configuration' },
        { label: 'create_or_update_configuration', value: 'create_or_update_configuration' },
        { label: 'update_configuration', value: 'update_configuration' },
        { label: 'get_configuration_slot', value: 'get_configuration_slot' },
        { label: 'create_or_update_configuration_slot', value: 'create_or_update_configuration_slot' },
        { label: 'update_configuration_slot', value: 'update_configuration_slot' },
        { label: 'get_continuous_web_job', value: 'get_continuous_web_job' },
        { label: 'delete_continuous_web_job', value: 'delete_continuous_web_job' },
        { label: 'get_continuous_web_job_slot', value: 'get_continuous_web_job_slot' },
        { label: 'delete_continuous_web_job_slot', value: 'delete_continuous_web_job_slot' },
        { label: 'get_deployment', value: 'get_deployment' },
        { label: 'create_deployment', value: 'create_deployment' },
        { label: 'delete_deployment', value: 'delete_deployment' },
        { label: 'get_deployment_slot', value: 'get_deployment_slot' },
        { label: 'create_deployment_slot', value: 'create_deployment_slot' },
        { label: 'delete_deployment_slot', value: 'delete_deployment_slot' },
        { label: 'create_or_update_domain_ownership_identifier', value: 'create_or_update_domain_ownership_identifier' },
        { label: 'update_domain_ownership_identifier', value: 'update_domain_ownership_identifier' },
        { label: 'delete_domain_ownership_identifier', value: 'delete_domain_ownership_identifier' },
        { label: 'create_or_update_domain_ownership_identifier_slot', value: 'create_or_update_domain_ownership_identifier_slot' },
        { label: 'update_domain_ownership_identifier_slot', value: 'update_domain_ownership_identifier_slot' },
        { label: 'delete_domain_ownership_identifier_slot', value: 'delete_domain_ownership_identifier_slot' },
        { label: 'get_ms_deploy_status', value: 'get_ms_deploy_status' },
        { label: 'create_ms_deploy_operation', value: 'create_ms_deploy_operation' },
        { label: 'get_ms_deploy_log', value: 'get_ms_deploy_log' },
        { label: 'get_instance_ms_deploy_status', value: 'get_instance_ms_deploy_status' },
        { label: 'create_instance_ms_deploy_operation', value: 'create_instance_ms_deploy_operation' },
        { label: 'get_instance_ms_deploy_log', value: 'get_instance_ms_deploy_log' },
        { label: 'get_ms_deploy_status_slot', value: 'get_ms_deploy_status_slot' },
        { label: 'create_ms_deploy_operation_slot', value: 'create_ms_deploy_operation_slot' },
        { label: 'get_ms_deploy_log_slot', value: 'get_ms_deploy_log_slot' },
        { label: 'get_instance_ms_deploy_status_slot', value: 'get_instance_ms_deploy_status_slot' },
        { label: 'create_instance_ms_deploy_operation_slot', value: 'create_instance_ms_deploy_operation_slot' },
        { label: 'get_instance_ms_deploy_log_slot', value: 'get_instance_ms_deploy_log_slot' },
        { label: 'get_function', value: 'get_function' },
        { label: 'create_function', value: 'create_function' },
        { label: 'delete_function', value: 'delete_function' },
        { label: 'get_instance_function_slot', value: 'get_instance_function_slot' },
        { label: 'create_instance_function_slot', value: 'create_instance_function_slot' },
        { label: 'delete_instance_function_slot', value: 'delete_instance_function_slot' },
        { label: 'create_or_update_host_name_binding', value: 'create_or_update_host_name_binding' },
        { label: 'delete_host_name_binding', value: 'delete_host_name_binding' },
        { label: 'create_or_update_host_name_binding_slot', value: 'create_or_update_host_name_binding_slot' },
        { label: 'delete_host_name_binding_slot', value: 'delete_host_name_binding_slot' },
        { label: 'create_or_update_relay_service_connection', value: 'create_or_update_relay_service_connection' },
        { label: 'update_relay_service_connection', value: 'update_relay_service_connection' },
        { label: 'delete_relay_service_connection', value: 'delete_relay_service_connection' },
        { label: 'create_or_update_relay_service_connection_slot', value: 'create_or_update_relay_service_connection_slot' },
        { label: 'update_relay_service_connection_slot', value: 'update_relay_service_connection_slot' },
        { label: 'delete_relay_service_connection_slot', value: 'delete_relay_service_connection_slot' },
        { label: 'get_instance_info', value: 'get_instance_info' },
        { label: 'get_instance_info_slot', value: 'get_instance_info_slot' },
        { label: 'get_instance_process', value: 'get_instance_process' },
        { label: 'delete_instance_process', value: 'delete_instance_process' },
        { label: 'get_instance_process_dump', value: 'get_instance_process_dump' },
        { label: 'get_process', value: 'get_process' },
        { label: 'delete_process', value: 'delete_process' },
        { label: 'get_process_dump', value: 'get_process_dump' },
        { label: 'get_instance_process_slot', value: 'get_instance_process_slot' },
        { label: 'delete_instance_process_slot', value: 'delete_instance_process_slot' },
        { label: 'get_instance_process_dump_slot', value: 'get_instance_process_dump_slot' },
        { label: 'get_process_slot', value: 'get_process_slot' },
        { label: 'delete_process_slot', value: 'delete_process_slot' },
        { label: 'get_process_dump_slot', value: 'get_process_dump_slot' },
        { label: 'get_migrate_my_sql_status', value: 'get_migrate_my_sql_status' },
        { label: 'get_migrate_my_sql_status_slot', value: 'get_migrate_my_sql_status_slot' },
        { label: 'get_swift_virtual_network_connection', value: 'get_swift_virtual_network_connection' },
        { label: 'create_or_update_swift_virtual_network_connection_with_check', value: 'create_or_update_swift_virtual_network_connection_with_check' },
        { label: 'update_swift_virtual_network_connection_with_check', value: 'update_swift_virtual_network_connection_with_check' },
        { label: 'delete_swift_virtual_network', value: 'delete_swift_virtual_network' },
        { label: 'get_swift_virtual_network_connection_slot', value: 'get_swift_virtual_network_connection_slot' },
        { label: 'create_or_update_swift_virtual_network_connection_with_check_slot', value: 'create_or_update_swift_virtual_network_connection_with_check_slot' },
        { label: 'update_swift_virtual_network_connection_with_check_slot', value: 'update_swift_virtual_network_connection_with_check_slot' },
        { label: 'delete_swift_virtual_network_slot', value: 'delete_swift_virtual_network_slot' },
        { label: 'add_premier_add_on', value: 'add_premier_add_on' },
        { label: 'update_premier_add_on', value: 'update_premier_add_on' },
        { label: 'delete_premier_add_on', value: 'delete_premier_add_on' },
        { label: 'add_premier_add_on_slot', value: 'add_premier_add_on_slot' },
        { label: 'update_premier_add_on_slot', value: 'update_premier_add_on_slot' },
        { label: 'delete_premier_add_on_slot', value: 'delete_premier_add_on_slot' },
        { label: 'get_private_access', value: 'get_private_access' },
        { label: 'put_private_access_vnet', value: 'put_private_access_vnet' },
        { label: 'get_private_access_slot', value: 'get_private_access_slot' },
        { label: 'put_private_access_vnet_slot', value: 'put_private_access_vnet_slot' },
        { label: 'create_or_update_public_certificate', value: 'create_or_update_public_certificate' },
        { label: 'delete_public_certificate', value: 'delete_public_certificate' },
        { label: 'create_or_update_public_certificate_slot', value: 'create_or_update_public_certificate_slot' },
        { label: 'delete_public_certificate_slot', value: 'delete_public_certificate_slot' },
        { label: 'create_or_update_site_container', value: 'create_or_update_site_container' },
        { label: 'delete_site_container', value: 'delete_site_container' },
        { label: 'create_or_update_site_container_slot', value: 'create_or_update_site_container_slot' },
        { label: 'delete_site_container_slot', value: 'delete_site_container_slot' },
        { label: 'install_site_extension', value: 'install_site_extension' },
        { label: 'delete_site_extension', value: 'delete_site_extension' },
        { label: 'install_site_extension_slot', value: 'install_site_extension_slot' },
        { label: 'delete_site_extension_slot', value: 'delete_site_extension_slot' },
        { label: 'get_source_control_slot', value: 'get_source_control_slot' },
        { label: 'create_or_update_source_control_slot', value: 'create_or_update_source_control_slot' },
        { label: 'update_source_control_slot', value: 'update_source_control_slot' },
        { label: 'delete_source_control_slot', value: 'delete_source_control_slot' },
        { label: 'get_source_control', value: 'get_source_control' },
        { label: 'create_or_update_source_control', value: 'create_or_update_source_control' },
        { label: 'update_source_control', value: 'update_source_control' },
        { label: 'delete_source_control', value: 'delete_source_control' },
        { label: 'get_triggered_web_job_slot', value: 'get_triggered_web_job_slot' },
        { label: 'delete_triggered_web_job_slot', value: 'delete_triggered_web_job_slot' },
        { label: 'get_triggered_web_job', value: 'get_triggered_web_job' },
        { label: 'delete_triggered_web_job', value: 'delete_triggered_web_job' },
        { label: 'get_web_job_slot', value: 'get_web_job_slot' },
        { label: 'get_web_job', value: 'get_web_job' },
        { label: 'analyze_custom_hostname_slot', value: 'analyze_custom_hostname_slot' },
        { label: 'apply_slot_configuration_slot', value: 'apply_slot_configuration_slot' },
        { label: 'backup_slot', value: 'backup_slot' },
        { label: 'update_application_settings_slot', value: 'update_application_settings_slot' },
        { label: 'update_auth_settings_slot', value: 'update_auth_settings_slot' },
        { label: 'update_azure_storage_accounts_slot', value: 'update_azure_storage_accounts_slot' },
        { label: 'update_backup_configuration_slot', value: 'update_backup_configuration_slot' },
        { label: 'delete_backup_configuration_slot', value: 'delete_backup_configuration_slot' },
        { label: 'update_connection_strings_slot', value: 'update_connection_strings_slot' },
        { label: 'update_metadata_slot', value: 'update_metadata_slot' },
        { label: 'update_site_push_settings_slot', value: 'update_site_push_settings_slot' },
        { label: 'discover_backup_slot', value: 'discover_backup_slot' },
        { label: 'sync_functions_slot', value: 'sync_functions_slot' },
        { label: 'create_or_update_host_secret_slot', value: 'create_or_update_host_secret_slot' },
        { label: 'delete_host_secret_slot', value: 'delete_host_secret_slot' },
        { label: 'is_cloneable_slot', value: 'is_cloneable_slot' },
        { label: 'start_web_site_network_trace_slot', value: 'start_web_site_network_trace_slot' },
        { label: 'start_web_site_network_trace_operation_slot', value: 'start_web_site_network_trace_operation_slot' },
        { label: 'stop_web_site_network_trace_slot', value: 'stop_web_site_network_trace_slot' },
        { label: 'generate_new_site_publishing_password_slot', value: 'generate_new_site_publishing_password_slot' },
        { label: 'reset_slot_configuration_slot', value: 'reset_slot_configuration_slot' },
        { label: 'restart_slot', value: 'restart_slot' },
        { label: 'restore_from_backup_blob_slot', value: 'restore_from_backup_blob_slot' },
        { label: 'restore_from_deleted_app_slot', value: 'restore_from_deleted_app_slot' },
        { label: 'restore_snapshot_slot', value: 'restore_snapshot_slot' },
        { label: 'swap_slot', value: 'swap_slot' },
        { label: 'start_slot', value: 'start_slot' },
        { label: 'start_network_trace_slot', value: 'start_network_trace_slot' },
        { label: 'stop_slot', value: 'stop_slot' },
        { label: 'stop_network_trace_slot', value: 'stop_network_trace_slot' },
        { label: 'sync_repository_slot', value: 'sync_repository_slot' },
        { label: 'sync_function_triggers_slot', value: 'sync_function_triggers_slot' },
        { label: 'deploy_workflow_artifacts_slot', value: 'deploy_workflow_artifacts_slot' },
        { label: 'analyze_custom_hostname', value: 'analyze_custom_hostname' },
        { label: 'apply_slot_config_to_production', value: 'apply_slot_config_to_production' },
        { label: 'backup', value: 'backup' },
        { label: 'update_application_settings', value: 'update_application_settings' },
        { label: 'update_auth_settings', value: 'update_auth_settings' },
        { label: 'update_azure_storage_accounts', value: 'update_azure_storage_accounts' },
        { label: 'update_backup_configuration', value: 'update_backup_configuration' },
        { label: 'delete_backup_configuration', value: 'delete_backup_configuration' },
        { label: 'update_connection_strings', value: 'update_connection_strings' },
        { label: 'update_metadata', value: 'update_metadata' },
        { label: 'update_site_push_settings', value: 'update_site_push_settings' },
        { label: 'discover_backup', value: 'discover_backup' },
        { label: 'sync_functions', value: 'sync_functions' },
        { label: 'create_or_update_host_secret', value: 'create_or_update_host_secret' },
        { label: 'delete_host_secret', value: 'delete_host_secret' },
        { label: 'is_cloneable', value: 'is_cloneable' },
        { label: 'update_machine_key', value: 'update_machine_key' },
        { label: 'migrate_storage', value: 'migrate_storage' },
        { label: 'migrate_my_sql', value: 'migrate_my_sql' },
        { label: 'start_web_site_network_trace', value: 'start_web_site_network_trace' },
        { label: 'start_web_site_network_trace_operation', value: 'start_web_site_network_trace_operation' },
        { label: 'stop_web_site_network_trace', value: 'stop_web_site_network_trace' },
        { label: 'generate_new_site_publishing_password', value: 'generate_new_site_publishing_password' },
        { label: 'reset_production_slot_config', value: 'reset_production_slot_config' },
        { label: 'restart', value: 'restart' },
        { label: 'restore_from_backup_blob', value: 'restore_from_backup_blob' },
        { label: 'restore_from_deleted_app', value: 'restore_from_deleted_app' },
        { label: 'restore_snapshot', value: 'restore_snapshot' },
        { label: 'swap_slot_with_production', value: 'swap_slot_with_production' },
        { label: 'start', value: 'start' },
        { label: 'start_network_trace', value: 'start_network_trace' },
        { label: 'stop', value: 'stop' },
        { label: 'stop_network_trace', value: 'stop_network_trace' },
        { label: 'sync_repository', value: 'sync_repository' },
        { label: 'sync_function_triggers', value: 'sync_function_triggers' },
        { label: 'deploy_workflow_artifacts', value: 'deploy_workflow_artifacts' },
        { label: 'restore', value: 'restore' },
        { label: 'restore_slot', value: 'restore_slot' },
        { label: 'recover_site_configuration_snapshot', value: 'recover_site_configuration_snapshot' },
        { label: 'recover_site_configuration_snapshot_slot', value: 'recover_site_configuration_snapshot_slot' },
        { label: 'start_continuous_web_job', value: 'start_continuous_web_job' },
        { label: 'stop_continuous_web_job', value: 'stop_continuous_web_job' },
        { label: 'start_continuous_web_job_slot', value: 'start_continuous_web_job_slot' },
        { label: 'stop_continuous_web_job_slot', value: 'stop_continuous_web_job_slot' },
        { label: 'create_or_update_function_secret', value: 'create_or_update_function_secret' },
        { label: 'delete_function_secret', value: 'delete_function_secret' },
        { label: 'create_or_update_function_secret_slot', value: 'create_or_update_function_secret_slot' },
        { label: 'delete_function_secret_slot', value: 'delete_function_secret_slot' },
        { label: 'run_triggered_web_job_slot', value: 'run_triggered_web_job_slot' },
        { label: 'run_triggered_web_job', value: 'run_triggered_web_job' }
    ]}
>
<TabItem value="list_slots">

Gets an app's deployment slots. Description for Gets an app's deployment slots.

```sql
EXEC azure.web.web_apps.list_slots 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_azure_storage_accounts_slot">

Gets the Azure storage account configurations of an app. Description for Gets the Azure storage account configurations of an app.

```sql
EXEC azure.web.web_apps.list_azure_storage_accounts_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_connection_strings_slot">

Gets the connection strings of an app. Description for Gets the connection strings of an app.

```sql
EXEC azure.web.web_apps.list_connection_strings_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_metadata_slot">

Gets the metadata of an app. Description for Gets the metadata of an app.

```sql
EXEC azure.web.web_apps.list_metadata_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_publishing_credentials_slot">

Gets the Git/FTP publishing credentials of an app. Description for Gets the Git/FTP publishing credentials of an app.

```sql
EXEC azure.web.web_apps.list_publishing_credentials_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_push_settings_slot">

Gets the Push settings associated with web app. Description for Gets the Push settings associated with web app.

```sql
EXEC azure.web.web_apps.list_site_push_settings_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_host_keys_slot">

Get host secrets for a function app. Description for Get host secrets for a function app.

```sql
EXEC azure.web.web_apps.list_host_keys_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_sync_status_slot">

This is to allow calling via powershell and ARM template. Description for This is to allow calling via powershell and ARM template.

```sql
EXEC azure.web.web_apps.list_sync_status_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_hybrid_connections_slot">

Retrieves all Service Bus Hybrid Connections used by this Web App. Description for Retrieves all Service Bus Hybrid Connections used by this Web App.

```sql
EXEC azure.web.web_apps.list_hybrid_connections_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_relay_service_connections_slot">

Gets hybrid connections configured for an app (or deployment slot, if specified). Description for Gets hybrid connections configured for an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.list_relay_service_connections_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_backups_slot">

Gets existing backups of an app. Description for Gets existing backups of an app.

```sql
EXEC azure.web.web_apps.list_site_backups_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_sync_function_triggers_slot">

This is to allow calling via powershell and ARM template. Description for This is to allow calling via powershell and ARM template.

```sql
EXEC azure.web.web_apps.list_sync_function_triggers_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_perf_mon_counters_slot">

Gets perfmon counters for web app. Description for Gets perfmon counters for web app.

```sql
EXEC azure.web.web_apps.list_perf_mon_counters_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_premier_add_ons_slot">

Gets the premier add-ons of an app. Description for Gets the premier add-ons of an app.

```sql
EXEC azure.web.web_apps.list_premier_add_ons_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_publishing_profile_xml_with_secrets_slot">

Gets the publishing profile for an app (or deployment slot, if specified). Description for Gets the publishing profile for an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.list_publishing_profile_xml_with_secrets_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"format": "{{ format }}", 
"includeDisasterRecoveryEndpoints": {{ includeDisasterRecoveryEndpoints }}
}'
;
```
</TabItem>
<TabItem value="list_snapshots_slot">

Returns all Snapshots to the user. Description for Returns all Snapshots to the user.

```sql
EXEC azure.web.web_apps.list_snapshots_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_snapshots_from_dr_secondary_slot">

Returns all Snapshots to the user from DRSecondary endpoint. Description for Returns all Snapshots to the user from DRSecondary endpoint.

```sql
EXEC azure.web.web_apps.list_snapshots_from_dr_secondary_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_usages_slot">

Gets the quota usage information of an app (or deployment slot, if specified). Description for Gets the quota usage information of an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.list_usages_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_workflows_connections_slot">

Lists logic app's connections for web site, or a deployment slot. Lists logic app's connections for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_workflows_connections_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_vnet_connections_slot">

Gets the virtual networks the app (or deployment slot) is connected to. Description for Gets the virtual networks the app (or deployment slot) is connected to.

```sql
EXEC azure.web.web_apps.list_vnet_connections_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_vnet_connections">

Gets the virtual networks the app (or deployment slot) is connected to. Description for Gets the virtual networks the app (or deployment slot) is connected to.

```sql
EXEC azure.web.web_apps.list_vnet_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_application_settings">

Gets the application settings of an app. Description for Gets the application settings of an app.

```sql
EXEC azure.web.web_apps.list_application_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_azure_storage_accounts">

Gets the Azure storage account configurations of an app. Description for Gets the Azure storage account configurations of an app.

```sql
EXEC azure.web.web_apps.list_azure_storage_accounts 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_connection_strings">

Gets the connection strings of an app. Description for Gets the connection strings of an app.

```sql
EXEC azure.web.web_apps.list_connection_strings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_metadata">

Gets the metadata of an app. Description for Gets the metadata of an app.

```sql
EXEC azure.web.web_apps.list_metadata 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_publishing_credentials">

Gets the Git/FTP publishing credentials of an app. Description for Gets the Git/FTP publishing credentials of an app.

```sql
EXEC azure.web.web_apps.list_publishing_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_push_settings">

Gets the Push settings associated with web app. Description for Gets the Push settings associated with web app.

```sql
EXEC azure.web.web_apps.list_site_push_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_host_keys">

Get host secrets for a function app. Description for Get host secrets for a function app.

```sql
EXEC azure.web.web_apps.list_host_keys 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_sync_status">

This is to allow calling via powershell and ARM template. Description for This is to allow calling via powershell and ARM template.

```sql
EXEC azure.web.web_apps.list_sync_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_hybrid_connections">

Retrieves all Service Bus Hybrid Connections used by this Web App. Description for Retrieves all Service Bus Hybrid Connections used by this Web App.

```sql
EXEC azure.web.web_apps.list_hybrid_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_relay_service_connections">

Gets hybrid connections configured for an app (or deployment slot, if specified). Description for Gets hybrid connections configured for an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.list_relay_service_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_backups">

Gets existing backups of an app. Description for Gets existing backups of an app.

```sql
EXEC azure.web.web_apps.list_site_backups 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_sync_function_triggers">

This is to allow calling via powershell and ARM template. Description for This is to allow calling via powershell and ARM template.

```sql
EXEC azure.web.web_apps.list_sync_function_triggers 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_perf_mon_counters">

Gets perfmon counters for web app. Description for Gets perfmon counters for web app.

```sql
EXEC azure.web.web_apps.list_perf_mon_counters 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_premier_add_ons">

Gets the premier add-ons of an app. Description for Gets the premier add-ons of an app.

```sql
EXEC azure.web.web_apps.list_premier_add_ons 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_publishing_profile_xml_with_secrets">

Gets the publishing profile for an app (or deployment slot, if specified). Description for Gets the publishing profile for an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.list_publishing_profile_xml_with_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"format": "{{ format }}", 
"includeDisasterRecoveryEndpoints": {{ includeDisasterRecoveryEndpoints }}
}'
;
```
</TabItem>
<TabItem value="list_snapshots">

Returns all Snapshots to the user. Description for Returns all Snapshots to the user.

```sql
EXEC azure.web.web_apps.list_snapshots 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_snapshots_from_dr_secondary">

Returns all Snapshots to the user from DRSecondary endpoint. Description for Returns all Snapshots to the user from DRSecondary endpoint.

```sql
EXEC azure.web.web_apps.list_snapshots_from_dr_secondary 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_usages">

Gets the quota usage information of an app (or deployment slot, if specified). Description for Gets the quota usage information of an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.list_usages 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@$filter='{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_workflows_connections">

Lists logic app's connections for web site, or a deployment slot. Lists logic app's connections for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_workflows_connections 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_backups">

Gets existing backups of an app. Description for Gets existing backups of an app.

```sql
EXEC azure.web.web_apps.list_backups 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_backups_slot">

Gets existing backups of an app. Description for Gets existing backups of an app.

```sql
EXEC azure.web.web_apps.list_backups_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_basic_publishing_credentials_policies">

Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site. Description for Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site.

```sql
EXEC azure.web.web_apps.list_basic_publishing_credentials_policies 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_basic_publishing_credentials_policies_slot">

Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site. Description for Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site.

```sql
EXEC azure.web.web_apps.list_basic_publishing_credentials_policies_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_slot_configuration_names">

Gets the names of app settings and connection strings that stick to the slot (not swapped). Description for Gets the names of app settings and connection strings that stick to the slot (not swapped).

```sql
EXEC azure.web.web_apps.list_slot_configuration_names 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_slot_configuration_names">

Updates the names of application settings and connection string that remain with the slot during swap operation. Description for Updates the names of application settings and connection string that remain with the slot during swap operation.

```sql
EXEC azure.web.web_apps.update_slot_configuration_names 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="list_configuration_snapshot_info">

Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot. Description for Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

```sql
EXEC azure.web.web_apps.list_configuration_snapshot_info 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_configurations">

List the configurations of an app. Description for List the configurations of an app.

```sql
EXEC azure.web.web_apps.list_configurations 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_configuration_snapshot_info_slot">

Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot. Description for Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

```sql
EXEC azure.web.web_apps.list_configuration_snapshot_info_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_configurations_slot">

List the configurations of an app. Description for List the configurations of an app.

```sql
EXEC azure.web.web_apps.list_configurations_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_continuous_web_jobs">

List continuous web jobs for an app, or a deployment slot. Description for List continuous web jobs for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_continuous_web_jobs 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_continuous_web_jobs_slot">

List continuous web jobs for an app, or a deployment slot. Description for List continuous web jobs for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_continuous_web_jobs_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_production_site_deployment_statuses">

List deployment statuses for an app (or deployment slot, if specified). List deployment statuses for an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.list_production_site_deployment_statuses 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_slot_site_deployment_statuses_slot">

List deployment statuses for an app (or deployment slot, if specified). List deployment statuses for an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.list_slot_site_deployment_statuses_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_deployments">

List deployments for an app, or a deployment slot. Description for List deployments for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_deployments 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_deployments_slot">

List deployments for an app, or a deployment slot. Description for List deployments for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_deployments_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_domain_ownership_identifiers">

Lists ownership identifiers for domain associated with web app. Description for Lists ownership identifiers for domain associated with web app.

```sql
EXEC azure.web.web_apps.list_domain_ownership_identifiers 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_domain_ownership_identifiers_slot">

Lists ownership identifiers for domain associated with web app. Description for Lists ownership identifiers for domain associated with web app.

```sql
EXEC azure.web.web_apps.list_domain_ownership_identifiers_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_functions">

List the functions for a web site, or a deployment slot. Description for List the functions for a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_functions 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_function_secrets">

Get function secrets for a function in a web site, or a deployment slot. Description for Get function secrets for a function in a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_function_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_instance_functions_slot">

List the functions for a web site, or a deployment slot. Description for List the functions for a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_instance_functions_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_function_secrets_slot">

Get function secrets for a function in a web site, or a deployment slot. Description for Get function secrets for a function in a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_function_secrets_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_host_name_bindings">

Get hostname bindings for an app or a deployment slot. Description for Get hostname bindings for an app or a deployment slot.

```sql
EXEC azure.web.web_apps.list_host_name_bindings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_host_name_bindings_slot">

Get hostname bindings for an app or a deployment slot. Description for Get hostname bindings for an app or a deployment slot.

```sql
EXEC azure.web.web_apps.list_host_name_bindings_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_instance_identifiers">

Gets all scale-out instances of an app. Description for Gets all scale-out instances of an app.

```sql
EXEC azure.web.web_apps.list_instance_identifiers 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_instance_identifiers_slot">

Gets all scale-out instances of an app. Description for Gets all scale-out instances of an app.

```sql
EXEC azure.web.web_apps.list_instance_identifiers_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_processes">

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.list_processes 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_processes_slot">

Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.list_processes_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_instance_process_modules">

List module information for a process by its ID for a specific scaled-out instance in a web site. Description for List module information for a process by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.list_instance_process_modules 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_process_modules">

List module information for a process by its ID for a specific scaled-out instance in a web site. Description for List module information for a process by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.list_process_modules 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_instance_process_modules_slot">

List module information for a process by its ID for a specific scaled-out instance in a web site. Description for List module information for a process by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.list_instance_process_modules_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@slot='{{ slot }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_process_modules_slot">

List module information for a process by its ID for a specific scaled-out instance in a web site. Description for List module information for a process by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.list_process_modules_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_public_certificates">

Get public certificates for an app or a deployment slot. Description for Get public certificates for an app or a deployment slot.

```sql
EXEC azure.web.web_apps.list_public_certificates 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_public_certificates_slot">

Get public certificates for an app or a deployment slot. Description for Get public certificates for an app or a deployment slot.

```sql
EXEC azure.web.web_apps.list_public_certificates_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_containers">

Lists all the site containers of a site, or a deployment slot. Lists all the site containers of a site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_site_containers 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_containers_slot">

Lists all the site containers of a site, or a deployment slot. Lists all the site containers of a site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_site_containers_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_extensions">

Get list of siteextensions for a web site, or a deployment slot. Description for Get list of siteextensions for a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_site_extensions 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_extensions_slot">

Get list of siteextensions for a web site, or a deployment slot. Description for Get list of siteextensions for a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_site_extensions_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_triggered_web_jobs_slot">

List triggered web jobs for an app, or a deployment slot. Description for List triggered web jobs for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_triggered_web_jobs_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_triggered_web_jobs">

List triggered web jobs for an app, or a deployment slot. Description for List triggered web jobs for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_triggered_web_jobs 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_web_jobs_slot">

List webjobs for an app, or a deployment slot. Description for List webjobs for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_web_jobs_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_web_jobs">

List webjobs for an app, or a deployment slot. Description for List webjobs for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_web_jobs 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_instance_workflows_slot">

List the workflows for a web site, or a deployment slot. List the workflows for a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_instance_workflows_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_workflows">

List the workflows for a web site, or a deployment slot. List the workflows for a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.list_workflows 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_slot">

Gets the details of a web, mobile, or API app. Description for Gets the details of a web, mobile, or API app.

```sql
EXEC azure.web.web_apps.get_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_slot">

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

```sql
EXEC azure.web.web_apps.create_or_update_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"identity": "{{ identity }}", 
"extendedLocation": "{{ extendedLocation }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_slot">

Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

```sql
EXEC azure.web.web_apps.update_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}", 
"identity": "{{ identity }}"
}'
;
```
</TabItem>
<TabItem value="delete_slot">

Deletes a web, mobile, or API app, or one of the deployment slots. Description for Deletes a web, mobile, or API app, or one of the deployment slots.

```sql
EXEC azure.web.web_apps.delete_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@deleteMetrics={{ deleteMetrics }}, 
@deleteEmptyServerFarm={{ deleteEmptyServerFarm }}
;
```
</TabItem>
<TabItem value="get_auth_settings_slot">

Gets the Authentication/Authorization settings of an app. Description for Gets the Authentication/Authorization settings of an app.

```sql
EXEC azure.web.web_apps.get_auth_settings_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_backup_configuration_slot">

Gets the backup configuration of an app. Description for Gets the backup configuration of an app.

```sql
EXEC azure.web.web_apps.get_backup_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_web_site_container_logs_slot">

Gets the last lines of docker logs for the given site. Description for Gets the last lines of docker logs for the given site.

```sql
EXEC azure.web.web_apps.get_web_site_container_logs_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_container_logs_zip_slot">

Gets the ZIP archived docker log files for the given site. Description for Gets the ZIP archived docker log files for the given site.

```sql
EXEC azure.web.web_apps.get_container_logs_zip_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_functions_admin_token_slot">

Fetch a short lived token that can be exchanged for a master key. Description for Fetch a short lived token that can be exchanged for a master key.

```sql
EXEC azure.web.web_apps.get_functions_admin_token_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_network_traces_slot">

Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.get_network_traces_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_network_trace_operation_slot_v2">

Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.get_network_trace_operation_slot_v2 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_network_traces_slot_v2">

Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.get_network_traces_slot_v2 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_site_php_error_log_flag_slot">

Gets web app's event logs. Description for Gets web app's event logs.

```sql
EXEC azure.web.web_apps.get_site_php_error_log_flag_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_link_resources_slot">

Gets the private link resources. Description for Gets the private link resources.

```sql
EXEC azure.web.web_apps.get_private_link_resources_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="approve_or_reject_private_endpoint_connection">

Approves or rejects a private endpoint connection. Description for Approves or rejects a private endpoint connection.

```sql
EXEC azure.web.web_apps.approve_or_reject_private_endpoint_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@private_endpoint_connection_name='{{ private_endpoint_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_private_endpoint_connection">

Deletes a private endpoint connection. Description for Deletes a private endpoint connection.

```sql
EXEC azure.web.web_apps.delete_private_endpoint_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@private_endpoint_connection_name='{{ private_endpoint_connection_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection_list">

Gets the list of private endpoint connections associated with a site. Description for Gets the list of private endpoint connections associated with a site.

```sql
EXEC azure.web.web_apps.get_private_endpoint_connection_list 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="approve_or_reject_private_endpoint_connection_slot">

Approves or rejects a private endpoint connection. Description for Approves or rejects a private endpoint connection.

```sql
EXEC azure.web.web_apps.approve_or_reject_private_endpoint_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@private_endpoint_connection_name='{{ private_endpoint_connection_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_private_endpoint_connection_slot">

Deletes a private endpoint connection. Description for Deletes a private endpoint connection.

```sql
EXEC azure.web.web_apps.delete_private_endpoint_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@private_endpoint_connection_name='{{ private_endpoint_connection_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_endpoint_connection_list_slot">

Gets the list of private endpoint connections associated with a site. Description for Gets the list of private endpoint connections associated with a site.

```sql
EXEC azure.web.web_apps.get_private_endpoint_connection_list_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_hybrid_connection">

Creates a new Hybrid Connection using a Service Bus relay. Description for Creates a new Hybrid Connection using a Service Bus relay.

```sql
EXEC azure.web.web_apps.create_or_update_hybrid_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@relay_name='{{ relay_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_hybrid_connection">

Creates a new Hybrid Connection using a Service Bus relay. Description for Creates a new Hybrid Connection using a Service Bus relay.

```sql
EXEC azure.web.web_apps.update_hybrid_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@relay_name='{{ relay_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_hybrid_connection">

Removes a Hybrid Connection from this site. Description for Removes a Hybrid Connection from this site.

```sql
EXEC azure.web.web_apps.delete_hybrid_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@relay_name='{{ relay_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_hybrid_connection_slot">

Creates a new Hybrid Connection using a Service Bus relay. Description for Creates a new Hybrid Connection using a Service Bus relay.

```sql
EXEC azure.web.web_apps.create_or_update_hybrid_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@relay_name='{{ relay_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_hybrid_connection_slot">

Creates a new Hybrid Connection using a Service Bus relay. Description for Creates a new Hybrid Connection using a Service Bus relay.

```sql
EXEC azure.web.web_apps.update_hybrid_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@relay_name='{{ relay_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_hybrid_connection_slot">

Removes a Hybrid Connection from this site. Description for Removes a Hybrid Connection from this site.

```sql
EXEC azure.web.web_apps.delete_hybrid_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@relay_name='{{ relay_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_vnet_connection_slot">

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

```sql
EXEC azure.web.web_apps.create_or_update_vnet_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_vnet_connection_slot">

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

```sql
EXEC azure.web.web_apps.update_vnet_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_vnet_connection_slot">

Deletes a connection from an app (or deployment slot to a named virtual network. Description for Deletes a connection from an app (or deployment slot to a named virtual network.

```sql
EXEC azure.web.web_apps.delete_vnet_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_vnet_connection">

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

```sql
EXEC azure.web.web_apps.create_or_update_vnet_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_vnet_connection">

Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

```sql
EXEC azure.web.web_apps.update_vnet_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_vnet_connection">

Deletes a connection from an app (or deployment slot to a named virtual network. Description for Deletes a connection from an app (or deployment slot to a named virtual network.

```sql
EXEC azure.web.web_apps.delete_vnet_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_vnet_connection_gateway_slot">

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

```sql
EXEC azure.web.web_apps.create_or_update_vnet_connection_gateway_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_vnet_connection_gateway_slot">

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

```sql
EXEC azure.web.web_apps.update_vnet_connection_gateway_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="create_or_update_vnet_connection_gateway">

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

```sql
EXEC azure.web.web_apps.create_or_update_vnet_connection_gateway 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_vnet_connection_gateway">

Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

```sql
EXEC azure.web.web_apps.update_vnet_connection_gateway 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@vnet_name='{{ vnet_name }}' --required, 
@gateway_name='{{ gateway_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_auth_settings">

Gets the Authentication/Authorization settings of an app. Description for Gets the Authentication/Authorization settings of an app.

```sql
EXEC azure.web.web_apps.get_auth_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_backup_configuration">

Gets the backup configuration of an app. Description for Gets the backup configuration of an app.

```sql
EXEC azure.web.web_apps.get_backup_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_web_site_container_logs">

Gets the last lines of docker logs for the given site. Description for Gets the last lines of docker logs for the given site.

```sql
EXEC azure.web.web_apps.get_web_site_container_logs 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_container_logs_zip">

Gets the ZIP archived docker log files for the given site. Description for Gets the ZIP archived docker log files for the given site.

```sql
EXEC azure.web.web_apps.get_container_logs_zip 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_one_deploy_status">

Invoke onedeploy status API /api/deployments and gets the deployment status for the site. Description for Invoke onedeploy status API /api/deployments and gets the deployment status for the site.

```sql
EXEC azure.web.web_apps.get_one_deploy_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_one_deploy_operation">

Invoke the OneDeploy publish web app extension. Description for Invoke the OneDeploy publish web app extension.

```sql
EXEC azure.web.web_apps.create_one_deploy_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_functions_admin_token">

Fetch a short lived token that can be exchanged for a master key. Description for Fetch a short lived token that can be exchanged for a master key.

```sql
EXEC azure.web.web_apps.get_functions_admin_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_network_traces">

Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.get_network_traces 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_network_trace_operation_v2">

Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.get_network_trace_operation_v2 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_network_traces_v2">

Gets a named operation for a network trace capturing (or deployment slot, if specified). Description for Gets a named operation for a network trace capturing (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.get_network_traces_v2 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_site_php_error_log_flag">

Gets web app's event logs. Description for Gets web app's event logs.

```sql
EXEC azure.web.web_apps.get_site_php_error_log_flag 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_link_resources">

Gets the private link resources. Description for Gets the private link resources.

```sql
EXEC azure.web.web_apps.get_private_link_resources 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_backup_status">

Gets a backup of an app by its ID. Description for Gets a backup of an app by its ID.

```sql
EXEC azure.web.web_apps.get_backup_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@backup_id='{{ backup_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_backup">

Deletes a backup of an app by its ID. Description for Deletes a backup of an app by its ID.

```sql
EXEC azure.web.web_apps.delete_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@backup_id='{{ backup_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_backup_status_slot">

Gets a backup of an app by its ID. Description for Gets a backup of an app by its ID.

```sql
EXEC azure.web.web_apps.get_backup_status_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@backup_id='{{ backup_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_backup_slot">

Deletes a backup of an app by its ID. Description for Deletes a backup of an app by its ID.

```sql
EXEC azure.web.web_apps.delete_backup_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@backup_id='{{ backup_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_ftp_allowed">

Returns whether FTP is allowed on the site or not. Description for Returns whether FTP is allowed on the site or not.

```sql
EXEC azure.web.web_apps.get_ftp_allowed 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_ftp_allowed">

Updates whether FTP is allowed on the site or not. Description for Updates whether FTP is allowed on the site or not.

```sql
EXEC azure.web.web_apps.update_ftp_allowed 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_scm_allowed">

Returns whether Scm basic auth is allowed on the site or not. Description for Returns whether Scm basic auth is allowed on the site or not.

```sql
EXEC azure.web.web_apps.get_scm_allowed 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_scm_allowed">

Updates whether user publishing credentials are allowed on the site or not. Description for Updates whether user publishing credentials are allowed on the site or not.

```sql
EXEC azure.web.web_apps.update_scm_allowed 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_ftp_allowed_slot">

Returns whether FTP is allowed on the site or not. Description for Returns whether FTP is allowed on the site or not.

```sql
EXEC azure.web.web_apps.get_ftp_allowed_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_ftp_allowed_slot">

Updates whether FTP is allowed on the site or not. Description for Updates whether FTP is allowed on the site or not.

```sql
EXEC azure.web.web_apps.update_ftp_allowed_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_scm_allowed_slot">

Returns whether Scm basic auth is allowed on the site or not. Description for Returns whether Scm basic auth is allowed on the site or not.

```sql
EXEC azure.web.web_apps.get_scm_allowed_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_scm_allowed_slot">

Updates whether user publishing credentials are allowed on the site or not. Description for Updates whether user publishing credentials are allowed on the site or not.

```sql
EXEC azure.web.web_apps.update_scm_allowed_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_auth_settings_v2_without_secrets">

Gets site's Authentication / Authorization settings for apps via the V2 format. Description for Gets site's Authentication / Authorization settings for apps via the V2 format.

```sql
EXEC azure.web.web_apps.get_auth_settings_v2_without_secrets 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_auth_settings_v2">

Updates site's Authentication / Authorization settings for apps via the V2 format. Description for Updates site's Authentication / Authorization settings for apps via the V2 format.

```sql
EXEC azure.web.web_apps.update_auth_settings_v2 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_auth_settings_v2">

Gets site's Authentication / Authorization settings for apps via the V2 format. Description for Gets site's Authentication / Authorization settings for apps via the V2 format.

```sql
EXEC azure.web.web_apps.get_auth_settings_v2 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_auth_settings_v2_without_secrets_slot">

Gets site's Authentication / Authorization settings for apps via the V2 format. Gets site's Authentication / Authorization settings for apps via the V2 format.

```sql
EXEC azure.web.web_apps.get_auth_settings_v2_without_secrets_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_auth_settings_v2_slot">

Updates site's Authentication / Authorization settings for apps via the V2 format. Description for Updates site's Authentication / Authorization settings for apps via the V2 format.

```sql
EXEC azure.web.web_apps.update_auth_settings_v2_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_auth_settings_v2_slot">

Gets site's Authentication / Authorization settings for apps via the V2 format. Description for Gets site's Authentication / Authorization settings for apps via the V2 format.

```sql
EXEC azure.web.web_apps.get_auth_settings_v2_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_app_settings_key_vault_references">

Gets the config reference app settings and status of an app. Description for Gets the config reference app settings and status of an app.

```sql
EXEC azure.web.web_apps.get_app_settings_key_vault_references 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_site_connection_string_key_vault_references">

Gets the config reference app settings and status of an app. Description for Gets the config reference app settings and status of an app.

```sql
EXEC azure.web.web_apps.get_site_connection_string_key_vault_references 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_app_settings_key_vault_references_slot">

Gets the config reference app settings and status of an app. Description for Gets the config reference app settings and status of an app.

```sql
EXEC azure.web.web_apps.get_app_settings_key_vault_references_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_site_connection_string_key_vault_references_slot">

Gets the config reference app settings and status of an app. Description for Gets the config reference app settings and status of an app.

```sql
EXEC azure.web.web_apps.get_site_connection_string_key_vault_references_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_diagnostic_logs_configuration">

Gets the logging configuration of an app. Description for Gets the logging configuration of an app.

```sql
EXEC azure.web.web_apps.get_diagnostic_logs_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_diagnostic_logs_config">

Updates the logging configuration of an app. Description for Updates the logging configuration of an app.

```sql
EXEC azure.web.web_apps.update_diagnostic_logs_config 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_diagnostic_logs_configuration_slot">

Gets the logging configuration of an app. Description for Gets the logging configuration of an app.

```sql
EXEC azure.web.web_apps.get_diagnostic_logs_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_diagnostic_logs_config_slot">

Updates the logging configuration of an app. Description for Updates the logging configuration of an app.

```sql
EXEC azure.web.web_apps.update_diagnostic_logs_config_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_configuration">

Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc. Description for Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

```sql
EXEC azure.web.web_apps.get_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_configuration">

Updates the configuration of an app. Description for Updates the configuration of an app.

```sql
EXEC azure.web.web_apps.create_or_update_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_configuration">

Updates the configuration of an app. Description for Updates the configuration of an app.

```sql
EXEC azure.web.web_apps.update_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_configuration_slot">

Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc. Description for Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

```sql
EXEC azure.web.web_apps.get_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_configuration_slot">

Updates the configuration of an app. Description for Updates the configuration of an app.

```sql
EXEC azure.web.web_apps.create_or_update_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_configuration_slot">

Updates the configuration of an app. Description for Updates the configuration of an app.

```sql
EXEC azure.web.web_apps.update_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_continuous_web_job">

Gets a continuous web job by its ID for an app, or a deployment slot. Description for Gets a continuous web job by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_continuous_web_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_continuous_web_job">

Delete a continuous web job by its ID for an app, or a deployment slot. Description for Delete a continuous web job by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_continuous_web_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_continuous_web_job_slot">

Gets a continuous web job by its ID for an app, or a deployment slot. Description for Gets a continuous web job by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_continuous_web_job_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_continuous_web_job_slot">

Delete a continuous web job by its ID for an app, or a deployment slot. Description for Delete a continuous web job by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_continuous_web_job_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_deployment">

Get a deployment by its ID for an app, or a deployment slot. Description for Get a deployment by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_deployment 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@id='{{ id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_deployment">

Create a deployment for an app, or a deployment slot. Description for Create a deployment for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.create_deployment 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@id='{{ id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_deployment">

Delete a deployment by its ID for an app, or a deployment slot. Description for Delete a deployment by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_deployment 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@id='{{ id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_deployment_slot">

Get a deployment by its ID for an app, or a deployment slot. Description for Get a deployment by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_deployment_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@id='{{ id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_deployment_slot">

Create a deployment for an app, or a deployment slot. Description for Create a deployment for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.create_deployment_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@id='{{ id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_deployment_slot">

Delete a deployment by its ID for an app, or a deployment slot. Description for Delete a deployment by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_deployment_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@id='{{ id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_domain_ownership_identifier">

Creates a domain ownership identifier for web app, or updates an existing ownership identifier. Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

```sql
EXEC azure.web.web_apps.create_or_update_domain_ownership_identifier 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_ownership_identifier_name='{{ domain_ownership_identifier_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_domain_ownership_identifier">

Creates a domain ownership identifier for web app, or updates an existing ownership identifier. Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

```sql
EXEC azure.web.web_apps.update_domain_ownership_identifier 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_ownership_identifier_name='{{ domain_ownership_identifier_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_domain_ownership_identifier">

Deletes a domain ownership identifier for a web app. Description for Deletes a domain ownership identifier for a web app.

```sql
EXEC azure.web.web_apps.delete_domain_ownership_identifier 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_ownership_identifier_name='{{ domain_ownership_identifier_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_domain_ownership_identifier_slot">

Creates a domain ownership identifier for web app, or updates an existing ownership identifier. Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

```sql
EXEC azure.web.web_apps.create_or_update_domain_ownership_identifier_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_ownership_identifier_name='{{ domain_ownership_identifier_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_domain_ownership_identifier_slot">

Creates a domain ownership identifier for web app, or updates an existing ownership identifier. Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

```sql
EXEC azure.web.web_apps.update_domain_ownership_identifier_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_ownership_identifier_name='{{ domain_ownership_identifier_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_domain_ownership_identifier_slot">

Deletes a domain ownership identifier for a web app. Description for Deletes a domain ownership identifier for a web app.

```sql
EXEC azure.web.web_apps.delete_domain_ownership_identifier_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@domain_ownership_identifier_name='{{ domain_ownership_identifier_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_ms_deploy_status">

Get the status of the last MSDeploy operation. Description for Get the status of the last MSDeploy operation.

```sql
EXEC azure.web.web_apps.get_ms_deploy_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_ms_deploy_operation">

Invoke the MSDeploy web app extension. Description for Invoke the MSDeploy web app extension.

```sql
EXEC azure.web.web_apps.create_ms_deploy_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_ms_deploy_log">

Get the MSDeploy Log for the last MSDeploy operation. Description for Get the MSDeploy Log for the last MSDeploy operation.

```sql
EXEC azure.web.web_apps.get_ms_deploy_log 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_ms_deploy_status">

Get the status of the last MSDeploy operation. Description for Get the status of the last MSDeploy operation.

```sql
EXEC azure.web.web_apps.get_instance_ms_deploy_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_instance_ms_deploy_operation">

Invoke the MSDeploy web app extension. Description for Invoke the MSDeploy web app extension.

```sql
EXEC azure.web.web_apps.create_instance_ms_deploy_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_instance_ms_deploy_log">

Get the MSDeploy Log for the last MSDeploy operation. Description for Get the MSDeploy Log for the last MSDeploy operation.

```sql
EXEC azure.web.web_apps.get_instance_ms_deploy_log 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_ms_deploy_status_slot">

Get the status of the last MSDeploy operation. Description for Get the status of the last MSDeploy operation.

```sql
EXEC azure.web.web_apps.get_ms_deploy_status_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_ms_deploy_operation_slot">

Invoke the MSDeploy web app extension. Description for Invoke the MSDeploy web app extension.

```sql
EXEC azure.web.web_apps.create_ms_deploy_operation_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_ms_deploy_log_slot">

Get the MSDeploy Log for the last MSDeploy operation. Description for Get the MSDeploy Log for the last MSDeploy operation.

```sql
EXEC azure.web.web_apps.get_ms_deploy_log_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_ms_deploy_status_slot">

Get the status of the last MSDeploy operation. Description for Get the status of the last MSDeploy operation.

```sql
EXEC azure.web.web_apps.get_instance_ms_deploy_status_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_instance_ms_deploy_operation_slot">

Invoke the MSDeploy web app extension. Description for Invoke the MSDeploy web app extension.

```sql
EXEC azure.web.web_apps.create_instance_ms_deploy_operation_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="get_instance_ms_deploy_log_slot">

Get the MSDeploy Log for the last MSDeploy operation. Description for Get the MSDeploy Log for the last MSDeploy operation.

```sql
EXEC azure.web.web_apps.get_instance_ms_deploy_log_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_function">

Get function information by its ID for web site, or a deployment slot. Description for Get function information by its ID for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_function 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_function">

Create function for web site, or a deployment slot. Description for Create function for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.create_function 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_function">

Delete a function for web site, or a deployment slot. Description for Delete a function for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_function 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_function_slot">

Get function information by its ID for web site, or a deployment slot. Description for Get function information by its ID for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_instance_function_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_instance_function_slot">

Create function for web site, or a deployment slot. Description for Create function for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.create_instance_function_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_instance_function_slot">

Delete a function for web site, or a deployment slot. Description for Delete a function for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_instance_function_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_host_name_binding">

Creates a hostname binding for an app. Description for Creates a hostname binding for an app.

```sql
EXEC azure.web.web_apps.create_or_update_host_name_binding 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@host_name='{{ host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_host_name_binding">

Deletes a hostname binding for an app. Description for Deletes a hostname binding for an app.

```sql
EXEC azure.web.web_apps.delete_host_name_binding 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@host_name='{{ host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_host_name_binding_slot">

Creates a hostname binding for an app. Description for Creates a hostname binding for an app.

```sql
EXEC azure.web.web_apps.create_or_update_host_name_binding_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@host_name='{{ host_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_host_name_binding_slot">

Deletes a hostname binding for an app. Description for Deletes a hostname binding for an app.

```sql
EXEC azure.web.web_apps.delete_host_name_binding_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@host_name='{{ host_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_relay_service_connection">

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

```sql
EXEC azure.web.web_apps.create_or_update_relay_service_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@entity_name='{{ entity_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_relay_service_connection">

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

```sql
EXEC azure.web.web_apps.update_relay_service_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@entity_name='{{ entity_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_relay_service_connection">

Deletes a relay service connection by its name. Description for Deletes a relay service connection by its name.

```sql
EXEC azure.web.web_apps.delete_relay_service_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@entity_name='{{ entity_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_relay_service_connection_slot">

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

```sql
EXEC azure.web.web_apps.create_or_update_relay_service_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@entity_name='{{ entity_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_relay_service_connection_slot">

Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

```sql
EXEC azure.web.web_apps.update_relay_service_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@entity_name='{{ entity_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_relay_service_connection_slot">

Deletes a relay service connection by its name. Description for Deletes a relay service connection by its name.

```sql
EXEC azure.web.web_apps.delete_relay_service_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@entity_name='{{ entity_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_info">

Gets all scale-out instances of an app. Description for Gets all scale-out instances of an app.

```sql
EXEC azure.web.web_apps.get_instance_info 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_info_slot">

Gets all scale-out instances of an app. Description for Gets all scale-out instances of an app.

```sql
EXEC azure.web.web_apps.get_instance_info_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_process">

Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.get_instance_process 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_instance_process">

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.delete_instance_process 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_process_dump">

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.get_instance_process_dump 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_process">

Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.get_process 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_process">

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.delete_process 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_process_dump">

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.get_process_dump 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_process_slot">

Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.get_instance_process_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@slot='{{ slot }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_instance_process_slot">

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.delete_instance_process_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@slot='{{ slot }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_instance_process_dump_slot">

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.get_instance_process_dump_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@slot='{{ slot }}' --required, 
@instance_id='{{ instance_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_process_slot">

Get process information by its ID for a specific scaled-out instance in a web site. Description for Get process information by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.get_process_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_process_slot">

Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.delete_process_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_process_dump_slot">

Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

```sql
EXEC azure.web.web_apps.get_process_dump_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@process_id='{{ process_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_migrate_my_sql_status">

Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled. Description for Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled.

```sql
EXEC azure.web.web_apps.get_migrate_my_sql_status 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_migrate_my_sql_status_slot">

Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled. Description for Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled.

```sql
EXEC azure.web.web_apps.get_migrate_my_sql_status_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_swift_virtual_network_connection">

Gets a Swift Virtual Network connection. Description for Gets a Swift Virtual Network connection.

```sql
EXEC azure.web.web_apps.get_swift_virtual_network_connection 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_swift_virtual_network_connection_with_check">

Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in. Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.

```sql
EXEC azure.web.web_apps.create_or_update_swift_virtual_network_connection_with_check 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_swift_virtual_network_connection_with_check">

Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in. Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.

```sql
EXEC azure.web.web_apps.update_swift_virtual_network_connection_with_check 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_swift_virtual_network">

Deletes a Swift Virtual Network connection from an app (or deployment slot). Description for Deletes a Swift Virtual Network connection from an app (or deployment slot).

```sql
EXEC azure.web.web_apps.delete_swift_virtual_network 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_swift_virtual_network_connection_slot">

Gets a Swift Virtual Network connection. Description for Gets a Swift Virtual Network connection.

```sql
EXEC azure.web.web_apps.get_swift_virtual_network_connection_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_swift_virtual_network_connection_with_check_slot">

Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in. Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.

```sql
EXEC azure.web.web_apps.create_or_update_swift_virtual_network_connection_with_check_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_swift_virtual_network_connection_with_check_slot">

Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in. Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not in use by another App Service Plan other than the one this App is in.

```sql
EXEC azure.web.web_apps.update_swift_virtual_network_connection_with_check_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_swift_virtual_network_slot">

Deletes a Swift Virtual Network connection from an app (or deployment slot). Description for Deletes a Swift Virtual Network connection from an app (or deployment slot).

```sql
EXEC azure.web.web_apps.delete_swift_virtual_network_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="add_premier_add_on">

Updates a named add-on of an app. Description for Updates a named add-on of an app.

```sql
EXEC azure.web.web_apps.add_premier_add_on 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@premier_add_on_name='{{ premier_add_on_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_premier_add_on">

Updates a named add-on of an app. Description for Updates a named add-on of an app.

```sql
EXEC azure.web.web_apps.update_premier_add_on 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@premier_add_on_name='{{ premier_add_on_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_premier_add_on">

Delete a premier add-on from an app. Description for Delete a premier add-on from an app.

```sql
EXEC azure.web.web_apps.delete_premier_add_on 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@premier_add_on_name='{{ premier_add_on_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="add_premier_add_on_slot">

Updates a named add-on of an app. Description for Updates a named add-on of an app.

```sql
EXEC azure.web.web_apps.add_premier_add_on_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@premier_add_on_name='{{ premier_add_on_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tags": "{{ tags }}", 
"location": "{{ location }}", 
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_premier_add_on_slot">

Updates a named add-on of an app. Description for Updates a named add-on of an app.

```sql
EXEC azure.web.web_apps.update_premier_add_on_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@premier_add_on_name='{{ premier_add_on_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_premier_add_on_slot">

Delete a premier add-on from an app. Description for Delete a premier add-on from an app.

```sql
EXEC azure.web.web_apps.delete_premier_add_on_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@premier_add_on_name='{{ premier_add_on_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_private_access">

Gets data around private site access enablement and authorized Virtual Networks that can access the site. Description for Gets data around private site access enablement and authorized Virtual Networks that can access the site.

```sql
EXEC azure.web.web_apps.get_private_access 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="put_private_access_vnet">

Sets data around private site access enablement and authorized Virtual Networks that can access the site. Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site.

```sql
EXEC azure.web.web_apps.put_private_access_vnet 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="get_private_access_slot">

Gets data around private site access enablement and authorized Virtual Networks that can access the site. Description for Gets data around private site access enablement and authorized Virtual Networks that can access the site.

```sql
EXEC azure.web.web_apps.get_private_access_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="put_private_access_vnet_slot">

Sets data around private site access enablement and authorized Virtual Networks that can access the site. Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site.

```sql
EXEC azure.web.web_apps.put_private_access_vnet_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="create_or_update_public_certificate">

Creates a hostname binding for an app. Description for Creates a hostname binding for an app.

```sql
EXEC azure.web.web_apps.create_or_update_public_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@public_certificate_name='{{ public_certificate_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_public_certificate">

Deletes a hostname binding for an app. Description for Deletes a hostname binding for an app.

```sql
EXEC azure.web.web_apps.delete_public_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@public_certificate_name='{{ public_certificate_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_public_certificate_slot">

Creates a hostname binding for an app. Description for Creates a hostname binding for an app.

```sql
EXEC azure.web.web_apps.create_or_update_public_certificate_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@public_certificate_name='{{ public_certificate_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_public_certificate_slot">

Deletes a hostname binding for an app. Description for Deletes a hostname binding for an app.

```sql
EXEC azure.web.web_apps.delete_public_certificate_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@public_certificate_name='{{ public_certificate_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_site_container">

Creates or Updates a site container for a site, or a deployment slot. Creates or Updates a site container for a site, or a deployment slot.

```sql
EXEC azure.web.web_apps.create_or_update_site_container 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_site_container">

Deletes a site container for a site, or a deployment slot. Deletes a site container for a site, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_site_container 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_site_container_slot">

Creates or Updates a site container for a site, or a deployment slot. Creates or Updates a site container for a site, or a deployment slot.

```sql
EXEC azure.web.web_apps.create_or_update_site_container_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_site_container_slot">

Deletes a site container for a site, or a deployment slot. Deletes a site container for a site, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_site_container_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@container_name='{{ container_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="install_site_extension">

Install site extension on a web site, or a deployment slot. Description for Install site extension on a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.install_site_extension 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@site_extension_id='{{ site_extension_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_site_extension">

Remove a site extension from a web site, or a deployment slot. Description for Remove a site extension from a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_site_extension 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@site_extension_id='{{ site_extension_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="install_site_extension_slot">

Install site extension on a web site, or a deployment slot. Description for Install site extension on a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.install_site_extension_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@site_extension_id='{{ site_extension_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_site_extension_slot">

Remove a site extension from a web site, or a deployment slot. Description for Remove a site extension from a web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_site_extension_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@site_extension_id='{{ site_extension_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_source_control_slot">

Gets the source control configuration of an app. Description for Gets the source control configuration of an app.

```sql
EXEC azure.web.web_apps.get_source_control_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_source_control_slot">

Updates the source control configuration of an app. Description for Updates the source control configuration of an app.

```sql
EXEC azure.web.web_apps.create_or_update_source_control_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_source_control_slot">

Updates the source control configuration of an app. Description for Updates the source control configuration of an app.

```sql
EXEC azure.web.web_apps.update_source_control_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_source_control_slot">

Deletes the source control configuration of an app. Description for Deletes the source control configuration of an app.

```sql
EXEC azure.web.web_apps.delete_source_control_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@additionalFlags='{{ additionalFlags }}'
;
```
</TabItem>
<TabItem value="get_source_control">

Gets the source control configuration of an app. Description for Gets the source control configuration of an app.

```sql
EXEC azure.web.web_apps.get_source_control 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_source_control">

Updates the source control configuration of an app. Description for Updates the source control configuration of an app.

```sql
EXEC azure.web.web_apps.create_or_update_source_control 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="update_source_control">

Updates the source control configuration of an app. Description for Updates the source control configuration of an app.

```sql
EXEC azure.web.web_apps.update_source_control 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}", 
"kind": "{{ kind }}"
}'
;
```
</TabItem>
<TabItem value="delete_source_control">

Deletes the source control configuration of an app. Description for Deletes the source control configuration of an app.

```sql
EXEC azure.web.web_apps.delete_source_control 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@additionalFlags='{{ additionalFlags }}'
;
```
</TabItem>
<TabItem value="get_triggered_web_job_slot">

Gets a triggered web job by its ID for an app, or a deployment slot. Description for Gets a triggered web job by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_triggered_web_job_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_triggered_web_job_slot">

Delete a triggered web job by its ID for an app, or a deployment slot. Description for Delete a triggered web job by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_triggered_web_job_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_triggered_web_job">

Gets a triggered web job by its ID for an app, or a deployment slot. Description for Gets a triggered web job by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_triggered_web_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete_triggered_web_job">

Delete a triggered web job by its ID for an app, or a deployment slot. Description for Delete a triggered web job by its ID for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.delete_triggered_web_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_web_job_slot">

Get webjob information for an app, or a deployment slot. Description for Get webjob information for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_web_job_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_web_job">

Get webjob information for an app, or a deployment slot. Description for Get webjob information for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.get_web_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="analyze_custom_hostname_slot">

Analyze a custom hostname. Description for Analyze a custom hostname.

```sql
EXEC azure.web.web_apps.analyze_custom_hostname_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@hostName='{{ hostName }}'
;
```
</TabItem>
<TabItem value="apply_slot_configuration_slot">

Applies the configuration settings from the target slot onto the current slot. Description for Applies the configuration settings from the target slot onto the current slot.

```sql
EXEC azure.web.web_apps.apply_slot_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetSlot": "{{ targetSlot }}", 
"preserveVnet": {{ preserveVnet }}
}'
;
```
</TabItem>
<TabItem value="backup_slot">

Creates a backup of an app. Description for Creates a backup of an app.

```sql
EXEC azure.web.web_apps.backup_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_application_settings_slot">

Replaces the application settings of an app. Description for Replaces the application settings of an app.

```sql
EXEC azure.web.web_apps.update_application_settings_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_auth_settings_slot">

Updates the Authentication / Authorization settings associated with web app. Description for Updates the Authentication / Authorization settings associated with web app.

```sql
EXEC azure.web.web_apps.update_auth_settings_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_azure_storage_accounts_slot">

Updates the Azure storage account configurations of an app. Description for Updates the Azure storage account configurations of an app.

```sql
EXEC azure.web.web_apps.update_azure_storage_accounts_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_backup_configuration_slot">

Updates the backup configuration of an app. Description for Updates the backup configuration of an app.

```sql
EXEC azure.web.web_apps.update_backup_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_backup_configuration_slot">

Deletes the backup configuration of an app. Description for Deletes the backup configuration of an app.

```sql
EXEC azure.web.web_apps.delete_backup_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_connection_strings_slot">

Replaces the connection strings of an app. Description for Replaces the connection strings of an app.

```sql
EXEC azure.web.web_apps.update_connection_strings_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_metadata_slot">

Replaces the metadata of an app. Description for Replaces the metadata of an app.

```sql
EXEC azure.web.web_apps.update_metadata_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_site_push_settings_slot">

Updates the Push settings associated with web app. Description for Updates the Push settings associated with web app.

```sql
EXEC azure.web.web_apps.update_site_push_settings_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="discover_backup_slot">

Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.

```sql
EXEC azure.web.web_apps.discover_backup_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="sync_functions_slot">

Syncs function trigger metadata to the management database. Description for Syncs function trigger metadata to the management database.

```sql
EXEC azure.web.web_apps.sync_functions_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_host_secret_slot">

Add or update a host level secret. Description for Add or update a host level secret.

```sql
EXEC azure.web.web_apps.create_or_update_host_secret_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@key_type='{{ key_type }}' --required, 
@key_name='{{ key_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="delete_host_secret_slot">

Delete a host level secret. Description for Delete a host level secret.

```sql
EXEC azure.web.web_apps.delete_host_secret_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@key_type='{{ key_type }}' --required, 
@key_name='{{ key_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="is_cloneable_slot">

Shows whether an app can be cloned to another resource group or subscription. Description for Shows whether an app can be cloned to another resource group or subscription.

```sql
EXEC azure.web.web_apps.is_cloneable_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_web_site_network_trace_slot">

Start capturing network packets for the site (To be deprecated). Description for Start capturing network packets for the site (To be deprecated).

```sql
EXEC azure.web.web_apps.start_web_site_network_trace_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@durationInSeconds='{{ durationInSeconds }}', 
@maxFrameLength='{{ maxFrameLength }}', 
@sasUrl='{{ sasUrl }}'
;
```
</TabItem>
<TabItem value="start_web_site_network_trace_operation_slot">

Start capturing network packets for the site. Description for Start capturing network packets for the site.

```sql
EXEC azure.web.web_apps.start_web_site_network_trace_operation_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@durationInSeconds='{{ durationInSeconds }}', 
@maxFrameLength='{{ maxFrameLength }}', 
@sasUrl='{{ sasUrl }}'
;
```
</TabItem>
<TabItem value="stop_web_site_network_trace_slot">

Stop ongoing capturing network packets for the site. Description for Stop ongoing capturing network packets for the site.

```sql
EXEC azure.web.web_apps.stop_web_site_network_trace_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_new_site_publishing_password_slot">

Generates a new publishing password for an app (or deployment slot, if specified). Description for Generates a new publishing password for an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.generate_new_site_publishing_password_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_slot_configuration_slot">

Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

```sql
EXEC azure.web.web_apps.reset_slot_configuration_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart_slot">

Restarts an app (or deployment slot, if specified). Description for Restarts an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.restart_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@softRestart={{ softRestart }}, 
@synchronous={{ synchronous }}
;
```
</TabItem>
<TabItem value="restore_from_backup_blob_slot">

Restores an app from a backup blob in Azure Storage. Description for Restores an app from a backup blob in Azure Storage.

```sql
EXEC azure.web.web_apps.restore_from_backup_blob_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="restore_from_deleted_app_slot">

Restores a deleted web app to this web app. Description for Restores a deleted web app to this web app.

```sql
EXEC azure.web.web_apps.restore_from_deleted_app_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="restore_snapshot_slot">

Restores a web app from a snapshot. Description for Restores a web app from a snapshot.

```sql
EXEC azure.web.web_apps.restore_snapshot_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="swap_slot">

Swaps two deployment slots of an app. Description for Swaps two deployment slots of an app.

```sql
EXEC azure.web.web_apps.swap_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetSlot": "{{ targetSlot }}", 
"preserveVnet": {{ preserveVnet }}
}'
;
```
</TabItem>
<TabItem value="start_slot">

Starts an app (or deployment slot, if specified). Description for Starts an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.start_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_network_trace_slot">

Start capturing network packets for the site. Description for Start capturing network packets for the site.

```sql
EXEC azure.web.web_apps.start_network_trace_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@durationInSeconds='{{ durationInSeconds }}', 
@maxFrameLength='{{ maxFrameLength }}', 
@sasUrl='{{ sasUrl }}'
;
```
</TabItem>
<TabItem value="stop_slot">

Stops an app (or deployment slot, if specified). Description for Stops an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.stop_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop_network_trace_slot">

Stop ongoing capturing network packets for the site. Description for Stop ongoing capturing network packets for the site.

```sql
EXEC azure.web.web_apps.stop_network_trace_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="sync_repository_slot">

Sync web app repository. Description for Sync web app repository.

```sql
EXEC azure.web.web_apps.sync_repository_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="sync_function_triggers_slot">

Syncs function trigger metadata to the management database. Description for Syncs function trigger metadata to the management database.

```sql
EXEC azure.web.web_apps.sync_function_triggers_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="deploy_workflow_artifacts_slot">

Creates the artifacts for web site, or a deployment slot. Description for Creates the artifacts for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.deploy_workflow_artifacts_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"appSettings": "{{ appSettings }}", 
"files": "{{ files }}", 
"filesToDelete": "{{ filesToDelete }}"
}'
;
```
</TabItem>
<TabItem value="analyze_custom_hostname">

Analyze a custom hostname. Description for Analyze a custom hostname.

```sql
EXEC azure.web.web_apps.analyze_custom_hostname 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@hostName='{{ hostName }}'
;
```
</TabItem>
<TabItem value="apply_slot_config_to_production">

Applies the configuration settings from the target slot onto the current slot. Description for Applies the configuration settings from the target slot onto the current slot.

```sql
EXEC azure.web.web_apps.apply_slot_config_to_production 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetSlot": "{{ targetSlot }}", 
"preserveVnet": {{ preserveVnet }}
}'
;
```
</TabItem>
<TabItem value="backup">

Creates a backup of an app. Description for Creates a backup of an app.

```sql
EXEC azure.web.web_apps.backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_application_settings">

Replaces the application settings of an app. Description for Replaces the application settings of an app.

```sql
EXEC azure.web.web_apps.update_application_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_auth_settings">

Updates the Authentication / Authorization settings associated with web app. Description for Updates the Authentication / Authorization settings associated with web app.

```sql
EXEC azure.web.web_apps.update_auth_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_azure_storage_accounts">

Updates the Azure storage account configurations of an app. Description for Updates the Azure storage account configurations of an app.

```sql
EXEC azure.web.web_apps.update_azure_storage_accounts 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_backup_configuration">

Updates the backup configuration of an app. Description for Updates the backup configuration of an app.

```sql
EXEC azure.web.web_apps.update_backup_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_backup_configuration">

Deletes the backup configuration of an app. Description for Deletes the backup configuration of an app.

```sql
EXEC azure.web.web_apps.delete_backup_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_connection_strings">

Replaces the connection strings of an app. Description for Replaces the connection strings of an app.

```sql
EXEC azure.web.web_apps.update_connection_strings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_metadata">

Replaces the metadata of an app. Description for Replaces the metadata of an app.

```sql
EXEC azure.web.web_apps.update_metadata 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_site_push_settings">

Updates the Push settings associated with web app. Description for Updates the Push settings associated with web app.

```sql
EXEC azure.web.web_apps.update_site_push_settings 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="discover_backup">

Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup.

```sql
EXEC azure.web.web_apps.discover_backup 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="sync_functions">

Syncs function trigger metadata to the management database. Description for Syncs function trigger metadata to the management database.

```sql
EXEC azure.web.web_apps.sync_functions 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_host_secret">

Add or update a host level secret. Description for Add or update a host level secret.

```sql
EXEC azure.web.web_apps.create_or_update_host_secret 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@key_type='{{ key_type }}' --required, 
@key_name='{{ key_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="delete_host_secret">

Delete a host level secret. Description for Delete a host level secret.

```sql
EXEC azure.web.web_apps.delete_host_secret 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@key_type='{{ key_type }}' --required, 
@key_name='{{ key_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="is_cloneable">

Shows whether an app can be cloned to another resource group or subscription. Description for Shows whether an app can be cloned to another resource group or subscription.

```sql
EXEC azure.web.web_apps.is_cloneable 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="update_machine_key">

Updates the machine key of an app. Updates the machine key of an app.

```sql
EXEC azure.web.web_apps.update_machine_key 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_storage">

Restores a web app. Description for Restores a web app.

```sql
EXEC azure.web.web_apps.migrate_storage 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@subscriptionName='{{ subscriptionName }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="migrate_my_sql">

Migrates a local (in-app) MySql database to a remote MySql database. Description for Migrates a local (in-app) MySql database to a remote MySql database.

```sql
EXEC azure.web.web_apps.migrate_my_sql 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="start_web_site_network_trace">

Start capturing network packets for the site (To be deprecated). Description for Start capturing network packets for the site (To be deprecated).

```sql
EXEC azure.web.web_apps.start_web_site_network_trace 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@durationInSeconds='{{ durationInSeconds }}', 
@maxFrameLength='{{ maxFrameLength }}', 
@sasUrl='{{ sasUrl }}'
;
```
</TabItem>
<TabItem value="start_web_site_network_trace_operation">

Start capturing network packets for the site. Description for Start capturing network packets for the site.

```sql
EXEC azure.web.web_apps.start_web_site_network_trace_operation 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@durationInSeconds='{{ durationInSeconds }}', 
@maxFrameLength='{{ maxFrameLength }}', 
@sasUrl='{{ sasUrl }}'
;
```
</TabItem>
<TabItem value="stop_web_site_network_trace">

Stop ongoing capturing network packets for the site. Description for Stop ongoing capturing network packets for the site.

```sql
EXEC azure.web.web_apps.stop_web_site_network_trace 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_new_site_publishing_password">

Generates a new publishing password for an app (or deployment slot, if specified). Description for Generates a new publishing password for an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.generate_new_site_publishing_password 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reset_production_slot_config">

Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

```sql
EXEC azure.web.web_apps.reset_production_slot_config 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restarts an app (or deployment slot, if specified). Description for Restarts an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@softRestart={{ softRestart }}, 
@synchronous={{ synchronous }}
;
```
</TabItem>
<TabItem value="restore_from_backup_blob">

Restores an app from a backup blob in Azure Storage. Description for Restores an app from a backup blob in Azure Storage.

```sql
EXEC azure.web.web_apps.restore_from_backup_blob 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="restore_from_deleted_app">

Restores a deleted web app to this web app. Description for Restores a deleted web app to this web app.

```sql
EXEC azure.web.web_apps.restore_from_deleted_app 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="restore_snapshot">

Restores a web app from a snapshot. Description for Restores a web app from a snapshot.

```sql
EXEC azure.web.web_apps.restore_snapshot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="swap_slot_with_production">

Swaps two deployment slots of an app. Description for Swaps two deployment slots of an app.

```sql
EXEC azure.web.web_apps.swap_slot_with_production 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targetSlot": "{{ targetSlot }}", 
"preserveVnet": {{ preserveVnet }}
}'
;
```
</TabItem>
<TabItem value="start">

Starts an app (or deployment slot, if specified). Description for Starts an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_network_trace">

Start capturing network packets for the site. Description for Start capturing network packets for the site.

```sql
EXEC azure.web.web_apps.start_network_trace 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@durationInSeconds='{{ durationInSeconds }}', 
@maxFrameLength='{{ maxFrameLength }}', 
@sasUrl='{{ sasUrl }}'
;
```
</TabItem>
<TabItem value="stop">

Stops an app (or deployment slot, if specified). Description for Stops an app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop_network_trace">

Stop ongoing capturing network packets for the site. Description for Stop ongoing capturing network packets for the site.

```sql
EXEC azure.web.web_apps.stop_network_trace 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="sync_repository">

Sync web app repository. Description for Sync web app repository.

```sql
EXEC azure.web.web_apps.sync_repository 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="sync_function_triggers">

Syncs function trigger metadata to the management database. Description for Syncs function trigger metadata to the management database.

```sql
EXEC azure.web.web_apps.sync_function_triggers 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="deploy_workflow_artifacts">

Creates the artifacts for web site, or a deployment slot. Description for Creates the artifacts for web site, or a deployment slot.

```sql
EXEC azure.web.web_apps.deploy_workflow_artifacts 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"appSettings": "{{ appSettings }}", 
"files": "{{ files }}", 
"filesToDelete": "{{ filesToDelete }}"
}'
;
```
</TabItem>
<TabItem value="restore">

Restores a specific backup to another app (or deployment slot, if specified). Description for Restores a specific backup to another app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.restore 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@backup_id='{{ backup_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="restore_slot">

Restores a specific backup to another app (or deployment slot, if specified). Description for Restores a specific backup to another app (or deployment slot, if specified).

```sql
EXEC azure.web.web_apps.restore_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@backup_id='{{ backup_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="recover_site_configuration_snapshot">

Reverts the configuration of an app to a previous snapshot. Description for Reverts the configuration of an app to a previous snapshot.

```sql
EXEC azure.web.web_apps.recover_site_configuration_snapshot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@snapshot_id='{{ snapshot_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="recover_site_configuration_snapshot_slot">

Reverts the configuration of an app to a previous snapshot. Description for Reverts the configuration of an app to a previous snapshot.

```sql
EXEC azure.web.web_apps.recover_site_configuration_snapshot_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@snapshot_id='{{ snapshot_id }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_continuous_web_job">

Start a continuous web job for an app, or a deployment slot. Description for Start a continuous web job for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.start_continuous_web_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop_continuous_web_job">

Stop a continuous web job for an app, or a deployment slot. Description for Stop a continuous web job for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.stop_continuous_web_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_continuous_web_job_slot">

Start a continuous web job for an app, or a deployment slot. Description for Start a continuous web job for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.start_continuous_web_job_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop_continuous_web_job_slot">

Stop a continuous web job for an app, or a deployment slot. Description for Stop a continuous web job for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.stop_continuous_web_job_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_function_secret">

Add or update a function secret. Description for Add or update a function secret.

```sql
EXEC azure.web.web_apps.create_or_update_function_secret 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@key_name='{{ key_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="delete_function_secret">

Delete a function secret. Description for Delete a function secret.

```sql
EXEC azure.web.web_apps.delete_function_secret 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@key_name='{{ key_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_function_secret_slot">

Add or update a function secret. Description for Add or update a function secret.

```sql
EXEC azure.web.web_apps.create_or_update_function_secret_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@key_name='{{ key_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"value": "{{ value }}"
}'
;
```
</TabItem>
<TabItem value="delete_function_secret_slot">

Delete a function secret. Description for Delete a function secret.

```sql
EXEC azure.web.web_apps.delete_function_secret_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@function_name='{{ function_name }}' --required, 
@key_name='{{ key_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_triggered_web_job_slot">

Run a triggered web job for an app, or a deployment slot. Description for Run a triggered web job for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.run_triggered_web_job_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_triggered_web_job">

Run a triggered web job for an app, or a deployment slot. Description for Run a triggered web job for an app, or a deployment slot.

```sql
EXEC azure.web.web_apps.run_triggered_web_job 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@web_job_name='{{ web_job_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
