--- 
title: maccs
hide_title: false
hide_table_of_contents: false
keywords:
  - maccs
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

Creates, updates, deletes, gets or lists a <code>maccs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="maccs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billingbenefits.maccs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="allowContributors" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true means multi-entity.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticShortfall" /></td>
    <td><code>string</code></td>
    <td>Setting this to 'Enable' enables automatic shortfall charging when commitment is not met. Known values are: "Unknown", "Enabled", and "Disabled". (Unknown, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="automaticShortfallSuppressReason" /></td>
    <td><code>object</code></td>
    <td>Optional field to record suppression reason for automatic shortfall.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the MACC is applied. Present only for Enterprise Agreement customers. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="commitment" /></td>
    <td><code>object</code></td>
    <td>Commitment towards the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Must be end of month. Timestamp must be in the ISO date format YYYY-MM-DDT23:59:59Z.</td>
</tr>
<tr>
    <td><CopyableCode code="entityType" /></td>
    <td><code>string</code></td>
    <td>Represents type of the object being operated on. Possible values are primary or contributor. Required. Known values are: "Primary" and "Contributor". (Primary, Contributor)</td>
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
    <td><CopyableCode code="milestones" /></td>
    <td><code>array</code></td>
    <td>List of milestones associated with this MACC.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryBillingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified billing account resource identifier of the primary MACC. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the primary MACC. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/maccs/&#123;maccName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents catalog UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of MACC as assigned by RPaaS. This indicates the last operation's status. For all practical purposes, this can be ignored. For current status of MACC resource, refer to MaccStatus.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>This is the resource identifier of either the primary MACC or the contributor. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/maccs/&#123;maccName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="shortfall" /></td>
    <td><code>object</code></td>
    <td>MACC shortfall.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Must be start of month. Timestamp must be in the ISO date format YYYY-MM-DDT00:00:00Z.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Represents the current status of the MACC. Known values are: "Unknown", "Scheduled", "Active", "Pending", "Failed", "Canceled", "Completed", "Stopped", "PendingSettlement", "ShortfallCharged", and "ShortfallWaived". (Unknown, Scheduled, Active, Pending, Failed, Canceled, Completed, Stopped, PendingSettlement, ShortfallCharged, ShortfallWaived)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>This is the globally unique identifier of the MACC which will not change for the lifetime of the MACC.</td>
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
    <td><CopyableCode code="allowContributors" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true means multi-entity.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticShortfall" /></td>
    <td><code>string</code></td>
    <td>Setting this to 'Enable' enables automatic shortfall charging when commitment is not met. Known values are: "Unknown", "Enabled", and "Disabled". (Unknown, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="automaticShortfallSuppressReason" /></td>
    <td><code>object</code></td>
    <td>Optional field to record suppression reason for automatic shortfall.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the MACC is applied. Present only for Enterprise Agreement customers. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="commitment" /></td>
    <td><code>object</code></td>
    <td>Commitment towards the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Must be end of month. Timestamp must be in the ISO date format YYYY-MM-DDT23:59:59Z.</td>
</tr>
<tr>
    <td><CopyableCode code="entityType" /></td>
    <td><code>string</code></td>
    <td>Represents type of the object being operated on. Possible values are primary or contributor. Required. Known values are: "Primary" and "Contributor". (Primary, Contributor)</td>
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
    <td><CopyableCode code="milestones" /></td>
    <td><code>array</code></td>
    <td>List of milestones associated with this MACC.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryBillingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified billing account resource identifier of the primary MACC. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the primary MACC. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/maccs/&#123;maccName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents catalog UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of MACC as assigned by RPaaS. This indicates the last operation's status. For all practical purposes, this can be ignored. For current status of MACC resource, refer to MaccStatus.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>This is the resource identifier of either the primary MACC or the contributor. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/maccs/&#123;maccName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="shortfall" /></td>
    <td><code>object</code></td>
    <td>MACC shortfall.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Must be start of month. Timestamp must be in the ISO date format YYYY-MM-DDT00:00:00Z.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Represents the current status of the MACC. Known values are: "Unknown", "Scheduled", "Active", "Pending", "Failed", "Canceled", "Completed", "Stopped", "PendingSettlement", "ShortfallCharged", and "ShortfallWaived". (Unknown, Scheduled, Active, Pending, Failed, Canceled, Completed, Stopped, PendingSettlement, ShortfallCharged, ShortfallWaived)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>This is the globally unique identifier of the MACC which will not change for the lifetime of the MACC.</td>
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
    <td><CopyableCode code="allowContributors" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true means multi-entity.</td>
</tr>
<tr>
    <td><CopyableCode code="automaticShortfall" /></td>
    <td><code>string</code></td>
    <td>Setting this to 'Enable' enables automatic shortfall charging when commitment is not met. Known values are: "Unknown", "Enabled", and "Disabled". (Unknown, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="automaticShortfallSuppressReason" /></td>
    <td><code>object</code></td>
    <td>Optional field to record suppression reason for automatic shortfall.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified identifier of the billing account where the MACC is applied. Present only for Enterprise Agreement customers. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="commitment" /></td>
    <td><code>object</code></td>
    <td>Commitment towards the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="endAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Must be end of month. Timestamp must be in the ISO date format YYYY-MM-DDT23:59:59Z.</td>
</tr>
<tr>
    <td><CopyableCode code="entityType" /></td>
    <td><code>string</code></td>
    <td>Represents type of the object being operated on. Possible values are primary or contributor. Required. Known values are: "Primary" and "Contributor". (Primary, Contributor)</td>
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
    <td><CopyableCode code="milestones" /></td>
    <td><code>array</code></td>
    <td>List of milestones associated with this MACC.</td>
</tr>
<tr>
    <td><CopyableCode code="plan" /></td>
    <td><code>object</code></td>
    <td>Plan for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryBillingAccountResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified billing account resource identifier of the primary MACC. Format must be Azure Resource ID: /providers/Microsoft.Billing/billingAccounts/&#123;acctId:orgId&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryResourceId" /></td>
    <td><code>string</code></td>
    <td>Fully-qualified resource identifier of the primary MACC. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/maccs/&#123;maccName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="productCode" /></td>
    <td><code>string</code></td>
    <td>Represents catalog UPN.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of MACC as assigned by RPaaS. This indicates the last operation's status. For all practical purposes, this can be ignored. For current status of MACC resource, refer to MaccStatus.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>This is the resource identifier of either the primary MACC or the contributor. Format: /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.BillingBenefits/maccs/&#123;maccName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="shortfall" /></td>
    <td><code>object</code></td>
    <td>MACC shortfall.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The resource model definition representing SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="startAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Must be start of month. Timestamp must be in the ISO date format YYYY-MM-DDT00:00:00Z.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Represents the current status of the MACC. Known values are: "Unknown", "Scheduled", "Active", "Pending", "Failed", "Canceled", "Completed", "Stopped", "PendingSettlement", "ShortfallCharged", and "ShortfallWaived". (Unknown, Scheduled, Active, Pending, Failed, Canceled, Completed, Stopped, PendingSettlement, ShortfallCharged, ShortfallWaived)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemId" /></td>
    <td><code>string</code></td>
    <td>This is the globally unique identifier of the MACC which will not change for the lifetime of the MACC.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-macc_name"><code>macc_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a MACC.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List MACCs under a resource group for primary service admin.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List MACCs under a subscription from primary service tenant.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-macc_name"><code>macc_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create MACC.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-macc_name"><code>macc_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update MACC.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-macc_name"><code>macc_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete MACC.</td>
</tr>
<tr>
    <td><a href="#cancel"><CopyableCode code="cancel" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-macc_name"><code>macc_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Represents an operation to cancel MACC contract. This operation does not indicate deletion of the MACC, but rather stops applying the benefit to the account.</td>
</tr>
<tr>
    <td><a href="#write_off"><CopyableCode code="write_off" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-macc_name"><code>macc_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to waive a customer's pending MACC balance (Shortfall) from their account, ensuring they are not charged for the outstanding amount.</td>
</tr>
<tr>
    <td><a href="#charge_shortfall"><CopyableCode code="charge_shortfall" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-macc_name"><code>macc_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to charge shortfall to a customer's account, ensuring they are charged for the outstanding amount of MACC credit.</td>
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
<tr id="parameter-macc_name">
    <td><CopyableCode code="macc_name" /></td>
    <td><code>string</code></td>
    <td>Name of primary MACC. Required.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a MACC.

```sql
SELECT
id,
name,
allowContributors,
automaticShortfall,
automaticShortfallSuppressReason,
billingAccountResourceId,
commitment,
displayName,
endAt,
entityType,
etag,
identity,
kind,
location,
managedBy,
milestones,
plan,
primaryBillingAccountResourceId,
primaryResourceId,
productCode,
provisioningState,
resourceId,
shortfall,
sku,
startAt,
status,
systemData,
systemId,
tags,
type
FROM azure.billingbenefits.maccs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND macc_name = '{{ macc_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List MACCs under a resource group for primary service admin.

```sql
SELECT
id,
name,
allowContributors,
automaticShortfall,
automaticShortfallSuppressReason,
billingAccountResourceId,
commitment,
displayName,
endAt,
entityType,
etag,
identity,
kind,
location,
managedBy,
milestones,
plan,
primaryBillingAccountResourceId,
primaryResourceId,
productCode,
provisioningState,
resourceId,
shortfall,
sku,
startAt,
status,
systemData,
systemId,
tags,
type
FROM azure.billingbenefits.maccs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List MACCs under a subscription from primary service tenant.

```sql
SELECT
id,
name,
allowContributors,
automaticShortfall,
automaticShortfallSuppressReason,
billingAccountResourceId,
commitment,
displayName,
endAt,
entityType,
etag,
identity,
kind,
location,
managedBy,
milestones,
plan,
primaryBillingAccountResourceId,
primaryResourceId,
productCode,
provisioningState,
resourceId,
shortfall,
sku,
startAt,
status,
systemData,
systemId,
tags,
type
FROM azure.billingbenefits.maccs
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create MACC.

```sql
INSERT INTO azure.billingbenefits.maccs (
tags,
location,
properties,
managedBy,
kind,
identity,
sku,
plan,
resource_group_name,
macc_name,
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
'{{ macc_name }}',
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
- name: maccs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the maccs resource.
    - name: macc_name
      value: "{{ macc_name }}"
      description: Required parameter for the maccs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the maccs resource.
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
        MACC properties.
      value:
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        entityType: "{{ entityType }}"
        displayName: "{{ displayName }}"
        productCode: "{{ productCode }}"
        billingAccountResourceId: "{{ billingAccountResourceId }}"
        commitment:
          currencyCode: "{{ currencyCode }}"
          amount: {{ amount }}
          grain: "{{ grain }}"
        startAt: "{{ startAt }}"
        endAt: "{{ endAt }}"
        systemId: "{{ systemId }}"
        automaticShortfall: "{{ automaticShortfall }}"
        automaticShortfallSuppressReason:
          code: "{{ code }}"
          message: "{{ message }}"
        shortfall:
          productCode: "{{ productCode }}"
          charge:
            currencyCode: "{{ currencyCode }}"
            amount: {{ amount }}
            grain: "{{ grain }}"
          startAt: "{{ startAt }}"
          endAt: "{{ endAt }}"
          resourceId: "{{ resourceId }}"
          balanceVersion: {{ balanceVersion }}
          systemId: "{{ systemId }}"
        milestones:
          - milestoneId: "{{ milestoneId }}"
            commitment:
              currencyCode: "{{ currencyCode }}"
              amount: {{ amount }}
            endAt: "{{ endAt }}"
            automaticShortfall: "{{ automaticShortfall }}"
            automaticShortfallSuppressReason:
              code: "{{ code }}"
              message: "{{ message }}"
            status: "{{ status }}"
            shortfall:
              productCode: "{{ productCode }}"
              charge:
                currencyCode: "{{ currencyCode }}"
                amount: {{ amount }}
                grain: "{{ grain }}"
              startAt: "{{ startAt }}"
              endAt: "{{ endAt }}"
              resourceId: "{{ resourceId }}"
              balanceVersion: {{ balanceVersion }}
              systemId: "{{ systemId }}"
        resourceId: "{{ resourceId }}"
        allowContributors: {{ allowContributors }}
        primaryResourceId: "{{ primaryResourceId }}"
        primaryBillingAccountResourceId: "{{ primaryBillingAccountResourceId }}"
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

Update MACC.

```sql
UPDATE azure.billingbenefits.maccs
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND macc_name = '{{ macc_name }}' --required
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

Delete MACC.

```sql
DELETE FROM azure.billingbenefits.maccs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND macc_name = '{{ macc_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="cancel"
    values={[
        { label: 'cancel', value: 'cancel' },
        { label: 'write_off', value: 'write_off' },
        { label: 'charge_shortfall', value: 'charge_shortfall' }
    ]}
>
<TabItem value="cancel">

Represents an operation to cancel MACC contract. This operation does not indicate deletion of the MACC, but rather stops applying the benefit to the account.

```sql
EXEC azure.billingbenefits.maccs.cancel 
@resource_group_name='{{ resource_group_name }}' --required, 
@macc_name='{{ macc_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="write_off">

Operation to waive a customer's pending MACC balance (Shortfall) from their account, ensuring they are not charged for the outstanding amount.

```sql
EXEC azure.billingbenefits.maccs.write_off 
@resource_group_name='{{ resource_group_name }}' --required, 
@macc_name='{{ macc_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="charge_shortfall">

Operation to charge shortfall to a customer's account, ensuring they are charged for the outstanding amount of MACC credit.

```sql
EXEC azure.billingbenefits.maccs.charge_shortfall 
@resource_group_name='{{ resource_group_name }}' --required, 
@macc_name='{{ macc_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
