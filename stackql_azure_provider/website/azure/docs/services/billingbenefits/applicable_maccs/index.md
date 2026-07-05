--- 
title: applicable_maccs
hide_title: false
hide_table_of_contents: false
keywords:
  - applicable_maccs
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

Creates, updates, deletes, gets or lists an <code>applicable_maccs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applicable_maccs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billingbenefits.applicable_maccs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="milestones" /></td>
    <td><code>array</code></td>
    <td>List of milestones associated with this MACC.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_id"><code>billing_account_id</code></a></td>
    <td></td>
    <td>List maccs that are applicable for a given billing account.</td>
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
<tr id="parameter-billing_account_id">
    <td><CopyableCode code="billing_account_id" /></td>
    <td><code>string</code></td>
    <td>The billing account Id at which the benefits are listed. Accepted format is: &#123;rootId:orgId&#125;. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

List maccs that are applicable for a given billing account.

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
milestones,
primaryBillingAccountResourceId,
primaryResourceId,
productCode,
provisioningState,
resourceId,
shortfall,
startAt,
status,
systemData,
systemId,
type
FROM azure.billingbenefits.applicable_maccs
WHERE billing_account_id = '{{ billing_account_id }}' -- required
;
```
</TabItem>
</Tabs>
