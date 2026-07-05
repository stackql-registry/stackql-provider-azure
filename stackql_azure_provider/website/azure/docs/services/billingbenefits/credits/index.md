--- 
title: credits
hide_title: false
hide_table_of_contents: false
keywords:
  - credits
  - billingbenefits
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

Creates, updates, deletes, gets or lists a <code>credits</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="credits" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billingbenefits.credits" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_applicable', value: 'list_applicable' }
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
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="breakdown" /></td>
    <td><code>array</code></td>
    <td>Credit line-items/milestones/no-charge services breakdown.</td>
</tr>
<tr>
    <td><CopyableCode code="credit" /></td>
    <td><code>object</code></td>
    <td>The entire investment amount for the credit contract, including currency and amount.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers. Format is /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity (system assigned and/or user assigned identities).</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>object</code></td>
    <td>Credit breakdown item representing a milestone, line-item, or no-charge service.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Product UPN for the credit type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>object</code></td>
    <td>The reason for the credit. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the resource. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/&#123;benefitType&#125;/&#123;benefitName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the credit. Known values are: "Unknown", "Pending", "Active", "Succeeded", "Canceled", "Failed", "Expired", "Exhausted", and "NotStarted". (Unknown, Pending, Active, Succeeded, Canceled, Failed, Expired, Exhausted, NotStarted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>System identifier.</td>
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
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="breakdown" /></td>
    <td><code>array</code></td>
    <td>Credit line-items/milestones/no-charge services breakdown.</td>
</tr>
<tr>
    <td><CopyableCode code="credit" /></td>
    <td><code>object</code></td>
    <td>The entire investment amount for the credit contract, including currency and amount.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers. Format is /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity (system assigned and/or user assigned identities).</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>object</code></td>
    <td>Credit breakdown item representing a milestone, line-item, or no-charge service.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Product UPN for the credit type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>object</code></td>
    <td>The reason for the credit. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the resource. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/&#123;benefitType&#125;/&#123;benefitName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the credit. Known values are: "Unknown", "Pending", "Active", "Succeeded", "Canceled", "Failed", "Expired", "Exhausted", and "NotStarted". (Unknown, Pending, Active, Succeeded, Canceled, Failed, Expired, Exhausted, NotStarted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>System identifier.</td>
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
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="breakdown" /></td>
    <td><code>array</code></td>
    <td>Credit line-items/milestones/no-charge services breakdown.</td>
</tr>
<tr>
    <td><CopyableCode code="credit" /></td>
    <td><code>object</code></td>
    <td>The entire investment amount for the credit contract, including currency and amount.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers. Format is /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity (system assigned and/or user assigned identities).</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>object</code></td>
    <td>Credit breakdown item representing a milestone, line-item, or no-charge service.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Product UPN for the credit type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>object</code></td>
    <td>The reason for the credit. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the resource. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/&#123;benefitType&#125;/&#123;benefitName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the credit. Known values are: "Unknown", "Pending", "Active", "Succeeded", "Canceled", "Failed", "Expired", "Exhausted", and "NotStarted". (Unknown, Pending, Active, Succeeded, Canceled, Failed, Expired, Exhausted, NotStarted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>System identifier.</td>
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
<TabItem value="list_applicable">

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
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the benefit is applied. Present only for Enterprise Agreement customers.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing profile where the benefit is applied. Present only for Field-led or Customer-led customers.</td>
</tr>
<tr>
    <td><CopyableCode code="breakdown" /></td>
    <td><code>array</code></td>
    <td>Credit line-items/milestones/no-charge services breakdown.</td>
</tr>
<tr>
    <td><CopyableCode code="credit" /></td>
    <td><code>object</code></td>
    <td>The entire investment amount for the credit contract, including currency and amount.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the customer where the savings plan is applied. Present only for Partner-led customers. Format is /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>End DateTime in UTC.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity (system assigned and/or user assigned identities).</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedBy" /></td>
    <td><code>string</code></td>
    <td>The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="policies" /></td>
    <td><code>object</code></td>
    <td>Credit breakdown item representing a milestone, line-item, or no-charge service.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Product UPN for the credit type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>object</code></td>
    <td>The reason for the credit. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the resource. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/&#123;benefitType&#125;/&#123;benefitName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start DateTime.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the credit. Known values are: "Unknown", "Pending", "Active", "Succeeded", "Canceled", "Failed", "Expired", "Exhausted", and "NotStarted". (Unknown, Pending, Active, Succeeded, Canceled, Failed, Expired, Exhausted, NotStarted)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>System identifier.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-credit_name"><code>credit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a credit.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Credits under a resource group from primary service admin.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List credits under a subscription from primary service tenant.</td>
</tr>
<tr>
    <td><a href="#list_applicable"><CopyableCode code="list_applicable" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>List applicable credits for the provided scope. Currently supported scopes: BillingAccountResourceId.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-credit_name"><code>credit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create a credit.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-credit_name"><code>credit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a credit.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-credit_name"><code>credit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a credit.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-credit_name"><code>credit_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Cancels a credit.</td>
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
<tr id="parameter-credit_name">
    <td><CopyableCode code="credit_name" /></td>
    <td><code>string</code></td>
    <td>Name of the credit. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the benefits are listed. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_applicable', value: 'list_applicable' }
    ]}
>
<TabItem value="get">

Get a credit.

```sql
SELECT
id,
name,
billingAccountResourceId,
billingProfileResourceId,
breakdown,
credit,
customerId,
endAt,
etag,
identity,
kind,
location,
managedBy,
plan,
policies,
productCode,
provisioningState,
reason,
resourceId,
sku,
startAt,
status,
systemData,
systemId,
tags,
type
FROM azure.billingbenefits.credits
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND credit_name = '{{ credit_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List Credits under a resource group from primary service admin.

```sql
SELECT
id,
name,
billingAccountResourceId,
billingProfileResourceId,
breakdown,
credit,
customerId,
endAt,
etag,
identity,
kind,
location,
managedBy,
plan,
policies,
productCode,
provisioningState,
reason,
resourceId,
sku,
startAt,
status,
systemData,
systemId,
tags,
type
FROM azure.billingbenefits.credits
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List credits under a subscription from primary service tenant.

```sql
SELECT
id,
name,
billingAccountResourceId,
billingProfileResourceId,
breakdown,
credit,
customerId,
endAt,
etag,
identity,
kind,
location,
managedBy,
plan,
policies,
productCode,
provisioningState,
reason,
resourceId,
sku,
startAt,
status,
systemData,
systemId,
tags,
type
FROM azure.billingbenefits.credits
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_applicable">

List applicable credits for the provided scope. Currently supported scopes: BillingAccountResourceId.

```sql
SELECT
id,
name,
billingAccountResourceId,
billingProfileResourceId,
breakdown,
credit,
customerId,
endAt,
etag,
identity,
kind,
location,
managedBy,
plan,
policies,
productCode,
provisioningState,
reason,
resourceId,
sku,
startAt,
status,
systemData,
systemId,
tags,
type
FROM azure.billingbenefits.credits
WHERE scope = '{{ scope }}' -- required
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

Create a credit.

```sql
INSERT INTO azure.billingbenefits.credits (
tags,
location,
properties,
managedBy,
kind,
identity,
sku,
plan,
resource_group_name,
credit_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ managedBy }}',
'{{ kind }}',
'{{ identity }}',
'{{ sku }}',
'{{ plan }}',
'{{ resource_group_name }}',
'{{ credit_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
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
- name: credits
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the credits resource.
    - name: credit_name
      value: "{{ credit_name }}"
      description: Required parameter for the credits resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the credits resource.
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
        Credit properties.
      value:
        status: "{{ status }}"
        productCode: "{{ productCode }}"
        reason:
          code: "{{ code }}"
          description: "{{ description }}"
        credit:
          currencyCode: "{{ currencyCode }}"
          amount: {{ amount }}
          grain: "{{ grain }}"
        startAt: "{{ startAt }}"
        endAt: "{{ endAt }}"
        policies:
          redemption: "{{ redemption }}"
          expiration: "{{ expiration }}"
        billingAccountResourceId: "{{ billingAccountResourceId }}"
        billingProfileResourceId: "{{ billingProfileResourceId }}"
        breakdown:
          - allocation:
              currencyCode: "{{ currencyCode }}"
              amount: {{ amount }}
              grain: "{{ grain }}"
            startAt: "{{ startAt }}"
            endAt: "{{ endAt }}"
            dimensions: "{{ dimensions }}"
        provisioningState: "{{ provisioningState }}"
        systemId: "{{ systemId }}"
        customerId: "{{ customerId }}"
        resourceId: "{{ resourceId }}"
    - name: managedBy
      value: "{{ managedBy }}"
      description: |
        The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. E.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value.
    - name: identity
      description: |
        Managed service identity (system assigned and/or user assigned identities).
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: sku
      description: |
        The resource model definition representing SKU.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: plan
      description: |
        Plan for the resource.
      value:
        name: "{{ name }}"
        publisher: "{{ publisher }}"
        product: "{{ product }}"
        promotionCode: "{{ promotionCode }}"
        version: "{{ version }}"
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

Update a credit.

```sql
UPDATE azure.billingbenefits.credits
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND credit_name = '{{ credit_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
location,
managedBy,
plan,
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

Delete a credit.

```sql
DELETE FROM azure.billingbenefits.credits
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND credit_name = '{{ credit_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' }
    ]}
>
<TabItem value="cancel">

Cancels a credit.

```sql
EXEC azure.billingbenefits.credits.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@credit_name='{{ credit_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
