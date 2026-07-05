--- 
title: reservation
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation
  - reservations
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

Creates, updates, deletes, gets or lists a <code>reservation</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reservation" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.reservations.reservation" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
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
    <td><CopyableCode code="appliedScopeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to applied scope type. Not required if not applicable. Required and need to provide tenantId and managementGroupId if AppliedScopeType is ManagementGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type. Known values are: "Single", "Shared", and "ManagementGroup". (Single, Shared, ManagementGroup)</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopes" /></td>
    <td><code>array</code></td>
    <td>The list of applied scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="archived" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the reservation is archived.</td>
</tr>
<tr>
    <td><CopyableCode code="benefitStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>The billing plan options available for this sku. Known values are: "Upfront" and "Monthly". (Upfront, Monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing reservation or savings plan.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>string</code></td>
    <td>Capabilities of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Friendly name for user to easily identify the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the reservation starting when this version is effective from.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>The message giving detailed information about the status code.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceFlexibility" /></td>
    <td><code>string</code></td>
    <td>Allows reservation discount to be applied across skus within the same auto fit group. Not all skus support instance size flexibility. Known values are: "On" and "Off". (On, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Resource Provider type to be reserved. Default value is "Microsoft.Compute".</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the last time the reservation was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure region where the reserved resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="mergeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation merge.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of the reservation. Known values are: "Creating", "PendingResourceHold", "ConfirmedResourceHold", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", "BillingFailed", "Failed", "Split", and "Merged". (Creating, PendingResourceHold, ConfirmedResourceHold, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, BillingFailed, Failed, Split, Merged)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSubState" /></td>
    <td><code>string</code></td>
    <td>The provisioning sub-state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>Quantity of the skus that are part of the reservation. Must be greater than zero.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true will automatically purchase a new reservation on the expiration date time.</td>
</tr>
<tr>
    <td><CopyableCode code="renewDestination" /></td>
    <td><code>string</code></td>
    <td>Reservation Id of the reservation which is purchased because of renew. Format of the resource Id is /providers/Microsoft.Capacity/reservationOrders/&#123;reservationOrderId&#125;/reservations/&#123;reservationId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="renewProperties" /></td>
    <td><code>object</code></td>
    <td>The renew properties for a reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="renewSource" /></td>
    <td><code>string</code></td>
    <td>Reservation Id of the reservation from which this reservation is renewed. Format of the resource Id is /providers/Microsoft.Capacity/reservationOrders/&#123;reservationOrderId&#125;/reservations/&#123;reservationId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceType" /></td>
    <td><code>string</code></td>
    <td>The type of the resource that is being reserved. Known values are: "VirtualMachines", "SqlDatabases", "SuseLinux", "CosmosDb", "RedHat", "SqlDataWarehouse", "VMwareCloudSimple", "RedHatOsa", "Databricks", "AppService", "ManagedDisk", "BlockBlob", "RedisCache", "AzureDataExplorer", "MySql", "MariaDb", "PostgreSql", "DedicatedHost", "SapHana", "SqlAzureHybridBenefit", "AVS", "DataFactory", "NetAppStorage", "AzureFiles", "SqlEdge", and "VirtualMachineSoftware". (VirtualMachines, SqlDatabases, SuseLinux, CosmosDb, RedHat, SqlDataWarehouse, VMwareCloudSimple, RedHatOsa, Databricks, AppService, ManagedDisk, BlockBlob, RedisCache, AzureDataExplorer, MySql, MariaDb, PostgreSql, DedicatedHost, SapHana, SqlAzureHybridBenefit, AVS, DataFactory, NetAppStorage, AzureFiles, SqlEdge, VirtualMachineSoftware)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the Azure Hybrid Benefit needs to be reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku information associated to this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the sku in english.</td>
</tr>
<tr>
    <td><CopyableCode code="splitProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation split.</td>
</tr>
<tr>
    <td><CopyableCode code="swapProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation swap.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent the term of reservation. Known values are: "P1Y", "P3Y", and "P5Y". (P1Y, P3Y, P5Y)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyAppliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type of the reservation for display, e.g. Shared.</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyRenewState" /></td>
    <td><code>string</code></td>
    <td>The renew state of the reservation for display, e.g. On.</td>
</tr>
<tr>
    <td><CopyableCode code="utilization" /></td>
    <td><code>object</code></td>
    <td>Reservation utilization.</td>
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
    <td><CopyableCode code="appliedScopeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to applied scope type. Not required if not applicable. Required and need to provide tenantId and managementGroupId if AppliedScopeType is ManagementGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type. Known values are: "Single", "Shared", and "ManagementGroup". (Single, Shared, ManagementGroup)</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopes" /></td>
    <td><code>array</code></td>
    <td>The list of applied scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="archived" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the reservation is archived.</td>
</tr>
<tr>
    <td><CopyableCode code="benefitStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>The billing plan options available for this sku. Known values are: "Upfront" and "Monthly". (Upfront, Monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing reservation or savings plan.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>string</code></td>
    <td>Capabilities of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Friendly name for user to easily identify the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the reservation starting when this version is effective from.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>The message giving detailed information about the status code.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceFlexibility" /></td>
    <td><code>string</code></td>
    <td>Allows reservation discount to be applied across skus within the same auto fit group. Not all skus support instance size flexibility. Known values are: "On" and "Off". (On, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Resource Provider type to be reserved. Default value is "Microsoft.Compute".</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the last time the reservation was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure region where the reserved resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="mergeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation merge.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of the reservation. Known values are: "Creating", "PendingResourceHold", "ConfirmedResourceHold", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", "BillingFailed", "Failed", "Split", and "Merged". (Creating, PendingResourceHold, ConfirmedResourceHold, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, BillingFailed, Failed, Split, Merged)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSubState" /></td>
    <td><code>string</code></td>
    <td>The provisioning sub-state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>Quantity of the skus that are part of the reservation. Must be greater than zero.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true will automatically purchase a new reservation on the expiration date time.</td>
</tr>
<tr>
    <td><CopyableCode code="renewDestination" /></td>
    <td><code>string</code></td>
    <td>Reservation Id of the reservation which is purchased because of renew. Format of the resource Id is /providers/Microsoft.Capacity/reservationOrders/&#123;reservationOrderId&#125;/reservations/&#123;reservationId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="renewProperties" /></td>
    <td><code>object</code></td>
    <td>The renew properties for a reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="renewSource" /></td>
    <td><code>string</code></td>
    <td>Reservation Id of the reservation from which this reservation is renewed. Format of the resource Id is /providers/Microsoft.Capacity/reservationOrders/&#123;reservationOrderId&#125;/reservations/&#123;reservationId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceType" /></td>
    <td><code>string</code></td>
    <td>The type of the resource that is being reserved. Known values are: "VirtualMachines", "SqlDatabases", "SuseLinux", "CosmosDb", "RedHat", "SqlDataWarehouse", "VMwareCloudSimple", "RedHatOsa", "Databricks", "AppService", "ManagedDisk", "BlockBlob", "RedisCache", "AzureDataExplorer", "MySql", "MariaDb", "PostgreSql", "DedicatedHost", "SapHana", "SqlAzureHybridBenefit", "AVS", "DataFactory", "NetAppStorage", "AzureFiles", "SqlEdge", and "VirtualMachineSoftware". (VirtualMachines, SqlDatabases, SuseLinux, CosmosDb, RedHat, SqlDataWarehouse, VMwareCloudSimple, RedHatOsa, Databricks, AppService, ManagedDisk, BlockBlob, RedisCache, AzureDataExplorer, MySql, MariaDb, PostgreSql, DedicatedHost, SapHana, SqlAzureHybridBenefit, AVS, DataFactory, NetAppStorage, AzureFiles, SqlEdge, VirtualMachineSoftware)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the Azure Hybrid Benefit needs to be reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku information associated to this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the sku in english.</td>
</tr>
<tr>
    <td><CopyableCode code="splitProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation split.</td>
</tr>
<tr>
    <td><CopyableCode code="swapProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation swap.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent the term of reservation. Known values are: "P1Y", "P3Y", and "P5Y". (P1Y, P3Y, P5Y)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyAppliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type of the reservation for display, e.g. Shared.</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyRenewState" /></td>
    <td><code>string</code></td>
    <td>The renew state of the reservation for display, e.g. On.</td>
</tr>
<tr>
    <td><CopyableCode code="utilization" /></td>
    <td><code>object</code></td>
    <td>Reservation utilization.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td><CopyableCode code="appliedScopeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to applied scope type. Not required if not applicable. Required and need to provide tenantId and managementGroupId if AppliedScopeType is ManagementGroup.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type. Known values are: "Single", "Shared", and "ManagementGroup". (Single, Shared, ManagementGroup)</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopes" /></td>
    <td><code>array</code></td>
    <td>The list of applied scopes.</td>
</tr>
<tr>
    <td><CopyableCode code="archived" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the reservation is archived.</td>
</tr>
<tr>
    <td><CopyableCode code="benefitStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the DateTime when the reservation benefit started.</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>The billing plan options available for this sku. Known values are: "Upfront" and "Monthly". (Upfront, Monthly)</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing reservation or savings plan.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>string</code></td>
    <td>Capabilities of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Friendly name for user to easily identify the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the reservation starting when this version is effective from.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedStatusInfo" /></td>
    <td><code>object</code></td>
    <td>The message giving detailed information about the status code.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceFlexibility" /></td>
    <td><code>string</code></td>
    <td>Allows reservation discount to be applied across skus within the same auto fit group. Not all skus support instance size flexibility. Known values are: "On" and "Off". (On, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Resource Provider type to be reserved. Default value is "Microsoft.Compute".</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the last time the reservation was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure region where the reserved resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="mergeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation merge.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of the reservation. Known values are: "Creating", "PendingResourceHold", "ConfirmedResourceHold", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", "BillingFailed", "Failed", "Split", and "Merged". (Creating, PendingResourceHold, ConfirmedResourceHold, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, BillingFailed, Failed, Split, Merged)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSubState" /></td>
    <td><code>string</code></td>
    <td>The provisioning sub-state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDate" /></td>
    <td><code>string (date)</code></td>
    <td>This is the date when the reservation was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="purchaseDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the reservation was purchased.</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>Quantity of the skus that are part of the reservation. Must be greater than zero.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true will automatically purchase a new reservation on the expiration date time.</td>
</tr>
<tr>
    <td><CopyableCode code="renewDestination" /></td>
    <td><code>string</code></td>
    <td>Reservation Id of the reservation which is purchased because of renew. Format of the resource Id is /providers/Microsoft.Capacity/reservationOrders/&#123;reservationOrderId&#125;/reservations/&#123;reservationId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="renewProperties" /></td>
    <td><code>object</code></td>
    <td>The renew properties for a reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="renewSource" /></td>
    <td><code>string</code></td>
    <td>Reservation Id of the reservation from which this reservation is renewed. Format of the resource Id is /providers/Microsoft.Capacity/reservationOrders/&#123;reservationOrderId&#125;/reservations/&#123;reservationId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceType" /></td>
    <td><code>string</code></td>
    <td>The type of the resource that is being reserved. Known values are: "VirtualMachines", "SqlDatabases", "SuseLinux", "CosmosDb", "RedHat", "SqlDataWarehouse", "VMwareCloudSimple", "RedHatOsa", "Databricks", "AppService", "ManagedDisk", "BlockBlob", "RedisCache", "AzureDataExplorer", "MySql", "MariaDb", "PostgreSql", "DedicatedHost", "SapHana", "SqlAzureHybridBenefit", "AVS", "DataFactory", "NetAppStorage", "AzureFiles", "SqlEdge", and "VirtualMachineSoftware". (VirtualMachines, SqlDatabases, SuseLinux, CosmosDb, RedHat, SqlDataWarehouse, VMwareCloudSimple, RedHatOsa, Databricks, AppService, ManagedDisk, BlockBlob, RedisCache, AzureDataExplorer, MySql, MariaDb, PostgreSql, DedicatedHost, SapHana, SqlAzureHybridBenefit, AVS, DataFactory, NetAppStorage, AzureFiles, SqlEdge, VirtualMachineSoftware)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the Azure Hybrid Benefit needs to be reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The sku information associated to this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="skuDescription" /></td>
    <td><code>string</code></td>
    <td>Description of the sku in english.</td>
</tr>
<tr>
    <td><CopyableCode code="splitProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation split.</td>
</tr>
<tr>
    <td><CopyableCode code="swapProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation swap.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent the term of reservation. Known values are: "P1Y", "P3Y", and "P5Y". (P1Y, P3Y, P5Y)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyAppliedScopeType" /></td>
    <td><code>string</code></td>
    <td>The applied scope type of the reservation for display, e.g. Shared.</td>
</tr>
<tr>
    <td><CopyableCode code="userFriendlyRenewState" /></td>
    <td><code>string</code></td>
    <td>The renew state of the reservation for display, e.g. On.</td>
</tr>
<tr>
    <td><CopyableCode code="utilization" /></td>
    <td><code>object</code></td>
    <td>Reservation utilization.</td>
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
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get `Reservation` details. Get specific `Reservation` details.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a></td>
    <td></td>
    <td>Get `Reservation`s in a given reservation Order. List `Reservation`s within a single `ReservationOrder`.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-refreshSummary"><code>refreshSummary</code></a>, <a href="#parameter-$skiptoken"><code>$skiptoken</code></a>, <a href="#parameter-selectedState"><code>selectedState</code></a>, <a href="#parameter-take"><code>take</code></a></td>
    <td>List the reservations and the roll up counts of reservations group by provisioning states that the user has access to in the current tenant.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a></td>
    <td></td>
    <td>Updates a `Reservation`. Updates the applied scopes of the `Reservation`.</td>
</tr>
<tr>
    <td><a href="#list_revisions"><CopyableCode code="list_revisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a></td>
    <td></td>
    <td>Get `Reservation` revisions. List of all the revisions for the `Reservation`.</td>
</tr>
<tr>
    <td><a href="#available_scopes"><CopyableCode code="available_scopes" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a></td>
    <td></td>
    <td>Get Available Scopes for `Reservation`. Check whether the scopes from request is valid for `Reservation`.</td>
</tr>
<tr>
    <td><a href="#archive"><CopyableCode code="archive" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a></td>
    <td></td>
    <td>Archive a `Reservation`. Archiving a `Reservation` moves it to `Archived` state.</td>
</tr>
<tr>
    <td><a href="#unarchive"><CopyableCode code="unarchive" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a></td>
    <td></td>
    <td>Unarchive a `Reservation`. Restores a `Reservation` to the state it was before archiving.</td>
</tr>
<tr>
    <td><a href="#split"><CopyableCode code="split" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a></td>
    <td></td>
    <td>Split the `Reservation`. Split a `Reservation` into two `Reservation`s with specified quantity distribution.</td>
</tr>
<tr>
    <td><a href="#merge"><CopyableCode code="merge" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a></td>
    <td></td>
    <td>Merges two `Reservation`s. Merge the specified `Reservation`s into a new `Reservation`. The two `Reservation`s being merged must have same properties.</td>
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
<tr id="parameter-reservation_id">
    <td><CopyableCode code="reservation_id" /></td>
    <td><code>string</code></td>
    <td>Id of the reservation item. Required.</td>
</tr>
<tr id="parameter-reservation_order_id">
    <td><CopyableCode code="reservation_order_id" /></td>
    <td><code>string</code></td>
    <td>Order Id of the reservation. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Supported value of this query is renewProperties. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>May be used to filter by reservation properties. The filter supports 'eq', 'or', and 'and'. It does not currently support 'ne', 'gt', 'le', 'ge', or 'not'. Reservation properties include sku/name, properties/&#123;appliedScopeType, archived, displayName, displayProvisioningState, effectiveDateTime, expiryDate, expiryDateTime, provisioningState, quantity, renew, reservedResourceType, term, userFriendlyAppliedScopeType, userFriendlyRenewState&#125;. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>May be used to sort order by reservation properties. Default value is None.</td>
</tr>
<tr id="parameter-$skiptoken">
    <td><CopyableCode code="$skiptoken" /></td>
    <td><code>number</code></td>
    <td>The number of reservations to skip from the list before returning results. Default value is None.</td>
</tr>
<tr id="parameter-refreshSummary">
    <td><CopyableCode code="refreshSummary" /></td>
    <td><code>string</code></td>
    <td>To indicate whether to refresh the roll up counts of the reservations group by provisioning states. Default value is None.</td>
</tr>
<tr id="parameter-selectedState">
    <td><CopyableCode code="selectedState" /></td>
    <td><code>string</code></td>
    <td>The selected provisioning state. Default value is None.</td>
</tr>
<tr id="parameter-take">
    <td><CopyableCode code="take" /></td>
    <td><code>number</code></td>
    <td>To number of reservations to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Get `Reservation` details. Get specific `Reservation` details.

```sql
SELECT
id,
name,
appliedScopeProperties,
appliedScopeType,
appliedScopes,
archived,
benefitStartTime,
billingPlan,
billingScopeId,
capabilities,
displayName,
displayProvisioningState,
effectiveDateTime,
etag,
expiryDate,
expiryDateTime,
extendedStatusInfo,
instanceFlexibility,
kind,
lastUpdatedDateTime,
location,
mergeProperties,
provisioningState,
provisioningSubState,
purchaseDate,
purchaseDateTime,
quantity,
renew,
renewDestination,
renewProperties,
renewSource,
reservedResourceType,
reviewDateTime,
sku,
skuDescription,
splitProperties,
swapProperties,
systemData,
term,
type,
userFriendlyAppliedScopeType,
userFriendlyRenewState,
utilization
FROM azure.reservations.reservation
WHERE reservation_order_id = '{{ reservation_order_id }}' -- required
AND reservation_id = '{{ reservation_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get `Reservation`s in a given reservation Order. List `Reservation`s within a single `ReservationOrder`.

```sql
SELECT
id,
name,
appliedScopeProperties,
appliedScopeType,
appliedScopes,
archived,
benefitStartTime,
billingPlan,
billingScopeId,
capabilities,
displayName,
displayProvisioningState,
effectiveDateTime,
etag,
expiryDate,
expiryDateTime,
extendedStatusInfo,
instanceFlexibility,
kind,
lastUpdatedDateTime,
location,
mergeProperties,
provisioningState,
provisioningSubState,
purchaseDate,
purchaseDateTime,
quantity,
renew,
renewDestination,
renewProperties,
renewSource,
reservedResourceType,
reviewDateTime,
sku,
skuDescription,
splitProperties,
swapProperties,
systemData,
term,
type,
userFriendlyAppliedScopeType,
userFriendlyRenewState,
utilization
FROM azure.reservations.reservation
WHERE reservation_order_id = '{{ reservation_order_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

List the reservations and the roll up counts of reservations group by provisioning states that the user has access to in the current tenant.

```sql
SELECT
id,
name,
appliedScopeProperties,
appliedScopeType,
appliedScopes,
archived,
benefitStartTime,
billingPlan,
billingScopeId,
capabilities,
displayName,
displayProvisioningState,
effectiveDateTime,
etag,
expiryDate,
expiryDateTime,
extendedStatusInfo,
instanceFlexibility,
kind,
lastUpdatedDateTime,
location,
mergeProperties,
provisioningState,
provisioningSubState,
purchaseDate,
purchaseDateTime,
quantity,
renew,
renewDestination,
renewProperties,
renewSource,
reservedResourceType,
reviewDateTime,
sku,
skuDescription,
splitProperties,
swapProperties,
systemData,
term,
type,
userFriendlyAppliedScopeType,
userFriendlyRenewState,
utilization
FROM azure.reservations.reservation
WHERE $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
AND refreshSummary = '{{ refreshSummary }}'
AND $skiptoken = '{{ $skiptoken }}'
AND selectedState = '{{ selectedState }}'
AND take = '{{ take }}'
;
```
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

Updates a `Reservation`. Updates the applied scopes of the `Reservation`.

```sql
UPDATE azure.reservations.reservation
SET 
properties = '{{ properties }}'
WHERE 
reservation_order_id = '{{ reservation_order_id }}' --required
AND reservation_id = '{{ reservation_id }}' --required
RETURNING
id,
name,
etag,
kind,
location,
properties,
sku,
systemData,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_revisions"
    values={[
        { label: 'list_revisions', value: 'list_revisions' },
        { label: 'available_scopes', value: 'available_scopes' },
        { label: 'archive', value: 'archive' },
        { label: 'unarchive', value: 'unarchive' },
        { label: 'split', value: 'split' },
        { label: 'merge', value: 'merge' }
    ]}
>
<TabItem value="list_revisions">

Get `Reservation` revisions. List of all the revisions for the `Reservation`.

```sql
EXEC azure.reservations.reservation.list_revisions 
@reservation_order_id='{{ reservation_order_id }}' --required, 
@reservation_id='{{ reservation_id }}' --required
;
```
</TabItem>
<TabItem value="available_scopes">

Get Available Scopes for `Reservation`. Check whether the scopes from request is valid for `Reservation`.

```sql
EXEC azure.reservations.reservation.available_scopes 
@reservation_order_id='{{ reservation_order_id }}' --required, 
@reservation_id='{{ reservation_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="archive">

Archive a `Reservation`. Archiving a `Reservation` moves it to `Archived` state.

```sql
EXEC azure.reservations.reservation.archive 
@reservation_order_id='{{ reservation_order_id }}' --required, 
@reservation_id='{{ reservation_id }}' --required
;
```
</TabItem>
<TabItem value="unarchive">

Unarchive a `Reservation`. Restores a `Reservation` to the state it was before archiving.

```sql
EXEC azure.reservations.reservation.unarchive 
@reservation_order_id='{{ reservation_order_id }}' --required, 
@reservation_id='{{ reservation_id }}' --required
;
```
</TabItem>
<TabItem value="split">

Split the `Reservation`. Split a `Reservation` into two `Reservation`s with specified quantity distribution.

```sql
EXEC azure.reservations.reservation.split 
@reservation_order_id='{{ reservation_order_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="merge">

Merges two `Reservation`s. Merge the specified `Reservation`s into a new `Reservation`. The two `Reservation`s being merged must have same properties.

```sql
EXEC azure.reservations.reservation.merge 
@reservation_order_id='{{ reservation_order_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
