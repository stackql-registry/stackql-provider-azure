--- 
title: reservations
hide_title: false
hide_table_of_contents: false
keywords:
  - reservations
  - billing
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

Creates, updates, deletes, gets or lists a <code>reservations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reservations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.reservations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_reservation_order"
    values={[
        { label: 'get_by_reservation_order', value: 'get_by_reservation_order' },
        { label: 'list_by_reservation_order', value: 'list_by_reservation_order' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get_by_reservation_order">

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
    <td>The applied scope type of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopes" /></td>
    <td><code>array</code></td>
    <td>The array of applied scopes of a reservation. Will be null if the reservation is in Shared scope.</td>
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
    <td>The display name of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The effective date time of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string</code></td>
    <td>The expiry date of the reservation.</td>
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
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the last time the reservation was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="mergeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation merge.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSubState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
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
    <td><code>number</code></td>
    <td>The number of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>The renew state of the reservation.</td>
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
    <td>The renew source of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceType" /></td>
    <td><code>string</code></td>
    <td>The reserved source type of the reservation, e.g. virtual machine.</td>
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
    <td>The sku description of the reservation.</td>
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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>The term of the reservation, e.g. P1Y.</td>
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
<TabItem value="list_by_reservation_order">

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
    <td>The applied scope type of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopes" /></td>
    <td><code>array</code></td>
    <td>The array of applied scopes of a reservation. Will be null if the reservation is in Shared scope.</td>
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
    <td>The display name of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The effective date time of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string</code></td>
    <td>The expiry date of the reservation.</td>
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
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the last time the reservation was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="mergeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation merge.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSubState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
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
    <td><code>number</code></td>
    <td>The number of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>The renew state of the reservation.</td>
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
    <td>The renew source of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceType" /></td>
    <td><code>string</code></td>
    <td>The reserved source type of the reservation, e.g. virtual machine.</td>
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
    <td>The sku description of the reservation.</td>
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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>The term of the reservation, e.g. P1Y.</td>
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
<TabItem value="list_by_billing_profile">

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
    <td>The applied scope type of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopes" /></td>
    <td><code>array</code></td>
    <td>The array of applied scopes of a reservation. Will be null if the reservation is in Shared scope.</td>
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
    <td>The display name of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The effective date time of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string</code></td>
    <td>The expiry date of the reservation.</td>
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
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the last time the reservation was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="mergeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation merge.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSubState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
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
    <td><code>number</code></td>
    <td>The number of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>The renew state of the reservation.</td>
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
    <td>The renew source of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceType" /></td>
    <td><code>string</code></td>
    <td>The reserved source type of the reservation, e.g. virtual machine.</td>
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
    <td>The sku description of the reservation.</td>
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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>The term of the reservation, e.g. P1Y.</td>
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
<TabItem value="list_by_billing_account">

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
    <td>The applied scope type of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopes" /></td>
    <td><code>array</code></td>
    <td>The array of applied scopes of a reservation. Will be null if the reservation is in Shared scope.</td>
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
    <td>The display name of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="displayProvisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation for display, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="effectiveDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The effective date time of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>integer</code></td>
    <td>:vartype etag: int</td>
</tr>
<tr>
    <td><CopyableCode code="expiryDate" /></td>
    <td><code>string</code></td>
    <td>The expiry date of the reservation.</td>
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
    <td><CopyableCode code="lastUpdatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>DateTime of the last time the reservation was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="mergeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties of reservation merge.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningSubState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the reservation, e.g. Succeeded.</td>
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
    <td><code>number</code></td>
    <td>The number of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>The renew state of the reservation.</td>
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
    <td>The renew source of the reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceType" /></td>
    <td><code>string</code></td>
    <td>The reserved source type of the reservation, e.g. virtual machine.</td>
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
    <td>The sku description of the reservation.</td>
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
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Tags for this reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>The term of the reservation, e.g. P1Y.</td>
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
    <td><a href="#get_by_reservation_order"><CopyableCode code="get_by_reservation_order" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a></td>
    <td><a href="#parameter-expand"><code>expand</code></a></td>
    <td>Get Reservation details in the billing account. Get specific Reservation details in the billing account.</td>
</tr>
<tr>
    <td><a href="#list_by_reservation_order"><CopyableCode code="list_by_reservation_order" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a></td>
    <td></td>
    <td>Get Reservations in a given reservation Order in the billing account. List Reservations within a single ReservationOrder in the billing account.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-skiptoken"><code>skiptoken</code></a>, <a href="#parameter-refreshSummary"><code>refreshSummary</code></a>, <a href="#parameter-selectedState"><code>selectedState</code></a>, <a href="#parameter-take"><code>take</code></a></td>
    <td>Lists the reservations for a billing profile and the roll up counts of reservations group by provisioning state.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-orderBy"><code>orderBy</code></a>, <a href="#parameter-skiptoken"><code>skiptoken</code></a>, <a href="#parameter-refreshSummary"><code>refreshSummary</code></a>, <a href="#parameter-selectedState"><code>selectedState</code></a>, <a href="#parameter-take"><code>take</code></a></td>
    <td>Lists the reservations in the billing account and the roll up counts of reservations group by provisioning states.</td>
</tr>
<tr>
    <td><a href="#update_by_billing_account"><CopyableCode code="update_by_billing_account" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-reservation_order_id"><code>reservation_order_id</code></a>, <a href="#parameter-reservation_id"><code>reservation_id</code></a></td>
    <td></td>
    <td>Update reservation by billing account.</td>
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
<tr id="parameter-billing_account_name">
    <td><CopyableCode code="billing_account_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing account. Required.</td>
</tr>
<tr id="parameter-billing_profile_name">
    <td><CopyableCode code="billing_profile_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a billing profile. Required.</td>
</tr>
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
<tr id="parameter-expand">
    <td><CopyableCode code="expand" /></td>
    <td><code>string</code></td>
    <td>May be used to expand the detail information of some properties. Default value is None.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>The filter query option allows clients to filter a collection of resources that are addressed by a request URL. Default value is None.</td>
</tr>
<tr id="parameter-orderBy">
    <td><CopyableCode code="orderBy" /></td>
    <td><code>string</code></td>
    <td>The orderby query option allows clients to request resources in a particular order. Default value is None.</td>
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
<tr id="parameter-skiptoken">
    <td><CopyableCode code="skiptoken" /></td>
    <td><code>number</code></td>
    <td>The number of reservations to skip from the list before returning results. Default value is None.</td>
</tr>
<tr id="parameter-take">
    <td><CopyableCode code="take" /></td>
    <td><code>number</code></td>
    <td>The number of reservations to return in API response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_reservation_order"
    values={[
        { label: 'get_by_reservation_order', value: 'get_by_reservation_order' },
        { label: 'list_by_reservation_order', value: 'list_by_reservation_order' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get_by_reservation_order">

Get Reservation details in the billing account. Get specific Reservation details in the billing account.

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
lastUpdatedDateTime,
location,
mergeProperties,
productCode,
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
tags,
term,
type,
userFriendlyAppliedScopeType,
userFriendlyRenewState,
utilization
FROM azure.billing.reservations
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND reservation_order_id = '{{ reservation_order_id }}' -- required
AND reservation_id = '{{ reservation_id }}' -- required
AND expand = '{{ expand }}'
;
```
</TabItem>
<TabItem value="list_by_reservation_order">

Get Reservations in a given reservation Order in the billing account. List Reservations within a single ReservationOrder in the billing account.

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
lastUpdatedDateTime,
location,
mergeProperties,
productCode,
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
tags,
term,
type,
userFriendlyAppliedScopeType,
userFriendlyRenewState,
utilization
FROM azure.billing.reservations
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND reservation_order_id = '{{ reservation_order_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_profile">

Lists the reservations for a billing profile and the roll up counts of reservations group by provisioning state.

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
lastUpdatedDateTime,
location,
mergeProperties,
productCode,
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
tags,
term,
type,
userFriendlyAppliedScopeType,
userFriendlyRenewState,
utilization
FROM azure.billing.reservations
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND skiptoken = '{{ skiptoken }}'
AND refreshSummary = '{{ refreshSummary }}'
AND selectedState = '{{ selectedState }}'
AND take = '{{ take }}'
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the reservations in the billing account and the roll up counts of reservations group by provisioning states.

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
lastUpdatedDateTime,
location,
mergeProperties,
productCode,
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
tags,
term,
type,
userFriendlyAppliedScopeType,
userFriendlyRenewState,
utilization
FROM azure.billing.reservations
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND filter = '{{ filter }}'
AND orderBy = '{{ orderBy }}'
AND skiptoken = '{{ skiptoken }}'
AND refreshSummary = '{{ refreshSummary }}'
AND selectedState = '{{ selectedState }}'
AND take = '{{ take }}'
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_by_billing_account"
    values={[
        { label: 'update_by_billing_account', value: 'update_by_billing_account' }
    ]}
>
<TabItem value="update_by_billing_account">

Update reservation by billing account.

```sql
UPDATE azure.billing.reservations
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND reservation_order_id = '{{ reservation_order_id }}' --required
AND reservation_id = '{{ reservation_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
systemData,
tags,
type;
```
</TabItem>
</Tabs>
