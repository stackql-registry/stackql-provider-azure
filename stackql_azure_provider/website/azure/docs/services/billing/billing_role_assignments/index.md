--- 
title: billing_role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_role_assignments
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

Creates, updates, deletes, gets or lists a <code>billing_role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="billing_role_assignments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.billing_role_assignments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_customer"
    values={[
        { label: 'get_by_customer', value: 'get_by_customer' },
        { label: 'get_by_invoice_section', value: 'get_by_invoice_section' },
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'get_by_billing_profile', value: 'get_by_billing_profile' },
        { label: 'get_by_department', value: 'get_by_department' },
        { label: 'get_by_enrollment_account', value: 'get_by_enrollment_account' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_department', value: 'list_by_department' },
        { label: 'list_by_enrollment_account', value: 'list_by_enrollment_account' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get_by_customer">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_invoice_section">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_customer">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_invoice_section">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_billing_profile">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_department">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_enrollment_account">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_department">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_enrollment_account">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_billing_account">

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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
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
    <td><CopyableCode code="billingAccountDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingAccountId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingProfileId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a billing profile.</td>
</tr>
<tr>
    <td><CopyableCode code="billingRequestId" /></td>
    <td><code>string</code></td>
    <td>The ID of the billing request that was created for the role assignment. This is only applicable to cross tenant role assignments or role assignments created through the billing request.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The object ID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who created the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="createdByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who created the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="createdOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was created.</td>
</tr>
<tr>
    <td><CopyableCode code="customerDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the customer.</td>
</tr>
<tr>
    <td><CopyableCode code="customerId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies a customer.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionDisplayName" /></td>
    <td><code>string</code></td>
    <td>The name of the invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="invoiceSectionId" /></td>
    <td><code>string</code></td>
    <td>The fully qualified ID that uniquely identifies an invoice section.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalId" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByPrincipalTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant Id of the user who modified the role assignment.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedByUserEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user who modified the role assignment. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedOn" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date the role assignment was modified.</td>
</tr>
<tr>
    <td><CopyableCode code="principalDisplayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the principal to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalId" /></td>
    <td><code>string</code></td>
    <td>The object id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalPuid" /></td>
    <td><code>string</code></td>
    <td>The principal PUID of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantId" /></td>
    <td><code>string</code></td>
    <td>The principal tenant id of the user to whom the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="principalTenantName" /></td>
    <td><code>string</code></td>
    <td>The friendly name of the tenant of the user to whom the role was assigned. This will be 'Primary Tenant' for the primary tenant of the billing account.</td>
</tr>
<tr>
    <td><CopyableCode code="principalType" /></td>
    <td><code>string</code></td>
    <td>The type of a role Assignment. Known values are: "Unknown", "None", "User", "Group", "DirectoryRole", "ServicePrincipal", and "Everyone". (Unknown, None, User, Group, DirectoryRole, ServicePrincipal, Everyone)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource during a long-running operation. Known values are: "Succeeded", "Canceled", "Failed", "New", "Pending", "Provisioning", "PendingBilling", "ConfirmedBilling", "Creating", "Created", and "Expired". (Succeeded, Canceled, Failed, New, Pending, Provisioning, PendingBilling, ConfirmedBilling, Creating, Created, Expired)</td>
</tr>
<tr>
    <td><CopyableCode code="roleDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The ID of the role definition. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope at which the role was assigned.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain &lt; &gt; % & \ ? /.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="userAuthenticationType" /></td>
    <td><code>string</code></td>
    <td>The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><CopyableCode code="userEmailAddress" /></td>
    <td><code>string</code></td>
    <td>The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.</td>
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
    <td><a href="#get_by_customer"><CopyableCode code="get_by_customer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Gets a role assignment for the caller on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_invoice_section"><CopyableCode code="get_by_invoice_section" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Gets a role assignment for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_customer"><CopyableCode code="list_by_customer" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a></td>
    <td>Lists the role assignments for the caller on customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_invoice_section"><CopyableCode code="list_by_invoice_section" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a></td>
    <td>Lists the role assignments for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_profile"><CopyableCode code="get_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Gets a role assignment for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_department"><CopyableCode code="get_by_department" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Gets a role assignment for the caller on a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_enrollment_account"><CopyableCode code="get_by_enrollment_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Gets a role assignment for the caller on a enrollment Account. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_profile"><CopyableCode code="list_by_billing_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a></td>
    <td>Lists the role assignments for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_department"><CopyableCode code="list_by_department" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a></td>
    <td></td>
    <td>Lists the role assignments for the caller on a department. The operation is supported for billing accounts of type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_enrollment_account"><CopyableCode code="list_by_enrollment_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a></td>
    <td></td>
    <td>Lists the role assignments for the caller on a enrollment account. The operation is supported for billing accounts of type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#get_by_billing_account"><CopyableCode code="get_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Gets a role assignment for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#list_by_billing_account"><CopyableCode code="list_by_billing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-filter"><code>filter</code></a>, <a href="#parameter-top"><code>top</code></a>, <a href="#parameter-skip"><code>skip</code></a></td>
    <td>Lists the role assignments for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#create_by_customer"><CopyableCode code="create_by_customer" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a>, <a href="#parameter-roleDefinitionId"><code>roleDefinitionId</code></a></td>
    <td></td>
    <td>Adds a role assignment on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#create_by_invoice_section"><CopyableCode code="create_by_invoice_section" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-roleDefinitionId"><code>roleDefinitionId</code></a></td>
    <td></td>
    <td>Adds a role assignment on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_department"><CopyableCode code="create_or_update_by_department" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_enrollment_account"><CopyableCode code="create_or_update_by_enrollment_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#create_by_billing_profile"><CopyableCode code="create_by_billing_profile" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-roleDefinitionId"><code>roleDefinitionId</code></a></td>
    <td></td>
    <td>Adds a role assignment on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_billing_account"><CopyableCode code="create_or_update_by_billing_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#create_by_billing_account"><CopyableCode code="create_by_billing_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-roleDefinitionId"><code>roleDefinitionId</code></a></td>
    <td></td>
    <td>Adds a role assignment on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_department"><CopyableCode code="create_or_update_by_department" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_enrollment_account"><CopyableCode code="create_or_update_by_enrollment_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update_by_billing_account"><CopyableCode code="create_or_update_by_billing_account" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#delete_by_customer"><CopyableCode code="delete_by_customer" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Deletes a role assignment on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#delete_by_invoice_section"><CopyableCode code="delete_by_invoice_section" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Deletes a role assignment on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#delete_by_billing_profile"><CopyableCode code="delete_by_billing_profile" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Deletes a role assignment on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#delete_by_department"><CopyableCode code="delete_by_department" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-department_name"><code>department_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Deletes a role assignment on a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#delete_by_enrollment_account"><CopyableCode code="delete_by_enrollment_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-enrollment_account_name"><code>enrollment_account_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Deletes a role assignment on a enrollment Account. The operation is supported only for billing accounts with agreement type Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#delete_by_billing_account"><CopyableCode code="delete_by_billing_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_role_assignment_name"><code>billing_role_assignment_name</code></a></td>
    <td></td>
    <td>Deletes a role assignment on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#resolve_by_billing_account"><CopyableCode code="resolve_by_billing_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a></td>
    <td><a href="#parameter-resolveScopeDisplayNames"><code>resolveScopeDisplayNames</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists the role assignments for the caller on a billing account while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.</td>
</tr>
<tr>
    <td><a href="#resolve_by_billing_profile"><CopyableCode code="resolve_by_billing_profile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a></td>
    <td><a href="#parameter-resolveScopeDisplayNames"><code>resolveScopeDisplayNames</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists the role assignments for the caller on an billing profile while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.</td>
</tr>
<tr>
    <td><a href="#resolve_by_customer"><CopyableCode code="resolve_by_customer" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-customer_name"><code>customer_name</code></a></td>
    <td><a href="#parameter-resolveScopeDisplayNames"><code>resolveScopeDisplayNames</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists the role assignments for the caller on a customer while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.</td>
</tr>
<tr>
    <td><a href="#resolve_by_invoice_section"><CopyableCode code="resolve_by_invoice_section" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-billing_account_name"><code>billing_account_name</code></a>, <a href="#parameter-billing_profile_name"><code>billing_profile_name</code></a>, <a href="#parameter-invoice_section_name"><code>invoice_section_name</code></a></td>
    <td><a href="#parameter-resolveScopeDisplayNames"><code>resolveScopeDisplayNames</code></a>, <a href="#parameter-filter"><code>filter</code></a></td>
    <td>Lists the role assignments for the caller on an invoice section while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.</td>
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
<tr id="parameter-billing_role_assignment_name">
    <td><CopyableCode code="billing_role_assignment_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a role assignment. Required.</td>
</tr>
<tr id="parameter-customer_name">
    <td><CopyableCode code="customer_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies a customer. Required.</td>
</tr>
<tr id="parameter-department_name">
    <td><CopyableCode code="department_name" /></td>
    <td><code>string</code></td>
    <td>The name of the department. Required.</td>
</tr>
<tr id="parameter-enrollment_account_name">
    <td><CopyableCode code="enrollment_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the enrollment account. Required.</td>
</tr>
<tr id="parameter-invoice_section_name">
    <td><CopyableCode code="invoice_section_name" /></td>
    <td><code>string</code></td>
    <td>The ID that uniquely identifies an invoice section. Required.</td>
</tr>
<tr id="parameter-filter">
    <td><CopyableCode code="filter" /></td>
    <td><code>string</code></td>
    <td>The filter query option allows clients to filter a collection of resources that are addressed by a request URL. Default value is None.</td>
</tr>
<tr id="parameter-resolveScopeDisplayNames">
    <td><CopyableCode code="resolveScopeDisplayNames" /></td>
    <td><code>boolean</code></td>
    <td>Resolves the scope display name for each of the role assignments. Default value is False.</td>
</tr>
<tr id="parameter-skip">
    <td><CopyableCode code="skip" /></td>
    <td><code>integer</code></td>
    <td>The skip query option requests the number of items in the queried collection that are to be skipped and not included in the result. Default value is None.</td>
</tr>
<tr id="parameter-top">
    <td><CopyableCode code="top" /></td>
    <td><code>integer</code></td>
    <td>The top query option requests the number of items in the queried collection to be included in the result. The maximum supported value for top is 50. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_customer"
    values={[
        { label: 'get_by_customer', value: 'get_by_customer' },
        { label: 'get_by_invoice_section', value: 'get_by_invoice_section' },
        { label: 'list_by_customer', value: 'list_by_customer' },
        { label: 'list_by_invoice_section', value: 'list_by_invoice_section' },
        { label: 'get_by_billing_profile', value: 'get_by_billing_profile' },
        { label: 'get_by_department', value: 'get_by_department' },
        { label: 'get_by_enrollment_account', value: 'get_by_enrollment_account' },
        { label: 'list_by_billing_profile', value: 'list_by_billing_profile' },
        { label: 'list_by_department', value: 'list_by_department' },
        { label: 'list_by_enrollment_account', value: 'list_by_enrollment_account' },
        { label: 'get_by_billing_account', value: 'get_by_billing_account' },
        { label: 'list_by_billing_account', value: 'list_by_billing_account' }
    ]}
>
<TabItem value="get_by_customer">

Gets a role assignment for the caller on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_invoice_section">

Gets a role assignment for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_customer">

Lists the role assignments for the caller on customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND customer_name = '{{ customer_name }}' -- required
AND filter = '{{ filter }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
;
```
</TabItem>
<TabItem value="list_by_invoice_section">

Lists the role assignments for the caller on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND invoice_section_name = '{{ invoice_section_name }}' -- required
AND filter = '{{ filter }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
;
```
</TabItem>
<TabItem value="get_by_billing_profile">

Gets a role assignment for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_department">

Gets a role assignment for the caller on a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND department_name = '{{ department_name }}' -- required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_enrollment_account">

Gets a role assignment for the caller on a enrollment Account. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND enrollment_account_name = '{{ enrollment_account_name }}' -- required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_profile">

Lists the role assignments for the caller on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_profile_name = '{{ billing_profile_name }}' -- required
AND filter = '{{ filter }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
;
```
</TabItem>
<TabItem value="list_by_department">

Lists the role assignments for the caller on a department. The operation is supported for billing accounts of type Enterprise Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND department_name = '{{ department_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_enrollment_account">

Lists the role assignments for the caller on a enrollment account. The operation is supported for billing accounts of type Enterprise Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND enrollment_account_name = '{{ enrollment_account_name }}' -- required
;
```
</TabItem>
<TabItem value="get_by_billing_account">

Gets a role assignment for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_billing_account">

Lists the role assignments for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.

```sql
SELECT
id,
name,
billingAccountDisplayName,
billingAccountId,
billingProfileDisplayName,
billingProfileId,
billingRequestId,
createdByPrincipalId,
createdByPrincipalPuid,
createdByPrincipalTenantId,
createdByUserEmailAddress,
createdOn,
customerDisplayName,
customerId,
invoiceSectionDisplayName,
invoiceSectionId,
modifiedByPrincipalId,
modifiedByPrincipalPuid,
modifiedByPrincipalTenantId,
modifiedByUserEmailAddress,
modifiedOn,
principalDisplayName,
principalId,
principalPuid,
principalTenantId,
principalTenantName,
principalType,
provisioningState,
roleDefinitionId,
scope,
systemData,
tags,
type,
userAuthenticationType,
userEmailAddress
FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' -- required
AND filter = '{{ filter }}'
AND top = '{{ top }}'
AND skip = '{{ skip }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_by_customer"
    values={[
        { label: 'create_by_customer', value: 'create_by_customer' },
        { label: 'create_by_invoice_section', value: 'create_by_invoice_section' },
        { label: 'create_or_update_by_department', value: 'create_or_update_by_department' },
        { label: 'create_or_update_by_enrollment_account', value: 'create_or_update_by_enrollment_account' },
        { label: 'create_by_billing_profile', value: 'create_by_billing_profile' },
        { label: 'create_or_update_by_billing_account', value: 'create_or_update_by_billing_account' },
        { label: 'create_by_billing_account', value: 'create_by_billing_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_by_customer">

Adds a role assignment on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.

```sql
INSERT INTO azure.billing.billing_role_assignments (
principalPuid,
principalId,
principalTenantId,
roleDefinitionId,
scope,
userAuthenticationType,
userEmailAddress,
billing_account_name,
billing_profile_name,
customer_name
)
SELECT 
'{{ principalPuid }}',
'{{ principalId }}',
'{{ principalTenantId }}',
'{{ roleDefinitionId }}' /* required */,
'{{ scope }}',
'{{ userAuthenticationType }}',
'{{ userEmailAddress }}',
'{{ billing_account_name }}',
'{{ billing_profile_name }}',
'{{ customer_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_by_invoice_section">

Adds a role assignment on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
INSERT INTO azure.billing.billing_role_assignments (
principalPuid,
principalId,
principalTenantId,
roleDefinitionId,
scope,
userAuthenticationType,
userEmailAddress,
billing_account_name,
billing_profile_name,
invoice_section_name
)
SELECT 
'{{ principalPuid }}',
'{{ principalId }}',
'{{ principalTenantId }}',
'{{ roleDefinitionId }}' /* required */,
'{{ scope }}',
'{{ userAuthenticationType }}',
'{{ userEmailAddress }}',
'{{ billing_account_name }}',
'{{ billing_profile_name }}',
'{{ invoice_section_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_by_department">

Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
INSERT INTO azure.billing.billing_role_assignments (
properties,
tags,
billing_account_name,
department_name,
billing_role_assignment_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}',
'{{ department_name }}',
'{{ billing_role_assignment_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_by_enrollment_account">

Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
INSERT INTO azure.billing.billing_role_assignments (
properties,
tags,
billing_account_name,
enrollment_account_name,
billing_role_assignment_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}',
'{{ enrollment_account_name }}',
'{{ billing_role_assignment_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_by_billing_profile">

Adds a role assignment on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
INSERT INTO azure.billing.billing_role_assignments (
principalPuid,
principalId,
principalTenantId,
roleDefinitionId,
scope,
userAuthenticationType,
userEmailAddress,
billing_account_name,
billing_profile_name
)
SELECT 
'{{ principalPuid }}',
'{{ principalId }}',
'{{ principalTenantId }}',
'{{ roleDefinitionId }}' /* required */,
'{{ scope }}',
'{{ userAuthenticationType }}',
'{{ userEmailAddress }}',
'{{ billing_account_name }}',
'{{ billing_profile_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_by_billing_account">

Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
INSERT INTO azure.billing.billing_role_assignments (
properties,
tags,
billing_account_name,
billing_role_assignment_name
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ billing_account_name }}',
'{{ billing_role_assignment_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_by_billing_account">

Adds a role assignment on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
INSERT INTO azure.billing.billing_role_assignments (
principalPuid,
principalId,
principalTenantId,
roleDefinitionId,
scope,
userAuthenticationType,
userEmailAddress,
billing_account_name
)
SELECT 
'{{ principalPuid }}',
'{{ principalId }}',
'{{ principalTenantId }}',
'{{ roleDefinitionId }}' /* required */,
'{{ scope }}',
'{{ userAuthenticationType }}',
'{{ userEmailAddress }}',
'{{ billing_account_name }}'
RETURNING
id,
name,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: billing_role_assignments
  props:
    - name: billing_account_name
      value: "{{ billing_account_name }}"
      description: Required parameter for the billing_role_assignments resource.
    - name: billing_profile_name
      value: "{{ billing_profile_name }}"
      description: Required parameter for the billing_role_assignments resource.
    - name: customer_name
      value: "{{ customer_name }}"
      description: Required parameter for the billing_role_assignments resource.
    - name: invoice_section_name
      value: "{{ invoice_section_name }}"
      description: Required parameter for the billing_role_assignments resource.
    - name: department_name
      value: "{{ department_name }}"
      description: Required parameter for the billing_role_assignments resource.
    - name: billing_role_assignment_name
      value: "{{ billing_role_assignment_name }}"
      description: Required parameter for the billing_role_assignments resource.
    - name: enrollment_account_name
      value: "{{ enrollment_account_name }}"
      description: Required parameter for the billing_role_assignments resource.
    - name: principalPuid
      value: "{{ principalPuid }}"
      description: |
        The principal PUID of the user to whom the role was assigned.
    - name: principalId
      value: "{{ principalId }}"
      description: |
        The object id of the user to whom the role was assigned.
    - name: principalTenantId
      value: "{{ principalTenantId }}"
      description: |
        The principal tenant id of the user to whom the role was assigned.
    - name: roleDefinitionId
      value: "{{ roleDefinitionId }}"
      description: |
        The ID of the role definition. Required.
    - name: scope
      value: "{{ scope }}"
      description: |
        The scope at which the role was assigned.
    - name: userAuthenticationType
      value: "{{ userAuthenticationType }}"
      description: |
        The authentication type of the user, whether Organization or MSA, of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
    - name: userEmailAddress
      value: "{{ userEmailAddress }}"
      description: |
        The email address of the user to whom the role was assigned. This is supported only for billing accounts with agreement type Enterprise Agreement.
    - name: properties
      description: |
        The properties of the billing role assignment.
      value:
        provisioningState: "{{ provisioningState }}"
        createdOn: "{{ createdOn }}"
        createdByPrincipalTenantId: "{{ createdByPrincipalTenantId }}"
        createdByPrincipalId: "{{ createdByPrincipalId }}"
        createdByPrincipalPuid: "{{ createdByPrincipalPuid }}"
        createdByUserEmailAddress: "{{ createdByUserEmailAddress }}"
        modifiedOn: "{{ modifiedOn }}"
        modifiedByPrincipalPuid: "{{ modifiedByPrincipalPuid }}"
        modifiedByUserEmailAddress: "{{ modifiedByUserEmailAddress }}"
        modifiedByPrincipalId: "{{ modifiedByPrincipalId }}"
        modifiedByPrincipalTenantId: "{{ modifiedByPrincipalTenantId }}"
        principalPuid: "{{ principalPuid }}"
        principalId: "{{ principalId }}"
        principalTenantId: "{{ principalTenantId }}"
        roleDefinitionId: "{{ roleDefinitionId }}"
        scope: "{{ scope }}"
        userAuthenticationType: "{{ userAuthenticationType }}"
        userEmailAddress: "{{ userEmailAddress }}"
        principalTenantName: "{{ principalTenantName }}"
        principalDisplayName: "{{ principalDisplayName }}"
        principalType: "{{ principalType }}"
        billingRequestId: "{{ billingRequestId }}"
        billingAccountId: "{{ billingAccountId }}"
        billingAccountDisplayName: "{{ billingAccountDisplayName }}"
        billingProfileId: "{{ billingProfileId }}"
        billingProfileDisplayName: "{{ billingProfileDisplayName }}"
        invoiceSectionId: "{{ invoiceSectionId }}"
        invoiceSectionDisplayName: "{{ invoiceSectionDisplayName }}"
        customerId: "{{ customerId }}"
        customerDisplayName: "{{ customerDisplayName }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? /.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_by_department"
    values={[
        { label: 'create_or_update_by_department', value: 'create_or_update_by_department' },
        { label: 'create_or_update_by_enrollment_account', value: 'create_or_update_by_enrollment_account' },
        { label: 'create_or_update_by_billing_account', value: 'create_or_update_by_billing_account' }
    ]}
>
<TabItem value="create_or_update_by_department">

Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
REPLACE azure.billing.billing_role_assignments
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND department_name = '{{ department_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_by_enrollment_account">

Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
REPLACE azure.billing.billing_role_assignments
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND enrollment_account_name = '{{ enrollment_account_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_by_billing_account">

Create or update a billing role assignment. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
REPLACE azure.billing.billing_role_assignments
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
billing_account_name = '{{ billing_account_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_by_customer"
    values={[
        { label: 'delete_by_customer', value: 'delete_by_customer' },
        { label: 'delete_by_invoice_section', value: 'delete_by_invoice_section' },
        { label: 'delete_by_billing_profile', value: 'delete_by_billing_profile' },
        { label: 'delete_by_department', value: 'delete_by_department' },
        { label: 'delete_by_enrollment_account', value: 'delete_by_enrollment_account' },
        { label: 'delete_by_billing_account', value: 'delete_by_billing_account' }
    ]}
>
<TabItem value="delete_by_customer">

Deletes a role assignment on a customer. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.

```sql
DELETE FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
AND customer_name = '{{ customer_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_by_invoice_section">

Deletes a role assignment on an invoice section. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
DELETE FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
AND invoice_section_name = '{{ invoice_section_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_by_billing_profile">

Deletes a role assignment on a billing profile. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
DELETE FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND billing_profile_name = '{{ billing_profile_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_by_department">

Deletes a role assignment on a department. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
DELETE FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND department_name = '{{ department_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_by_enrollment_account">

Deletes a role assignment on a enrollment Account. The operation is supported only for billing accounts with agreement type Enterprise Agreement.

```sql
DELETE FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND enrollment_account_name = '{{ enrollment_account_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
;
```
</TabItem>
<TabItem value="delete_by_billing_account">

Deletes a role assignment on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.

```sql
DELETE FROM azure.billing.billing_role_assignments
WHERE billing_account_name = '{{ billing_account_name }}' --required
AND billing_role_assignment_name = '{{ billing_role_assignment_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="resolve_by_billing_account"
    values={[
        { label: 'resolve_by_billing_account', value: 'resolve_by_billing_account' },
        { label: 'resolve_by_billing_profile', value: 'resolve_by_billing_profile' },
        { label: 'resolve_by_customer', value: 'resolve_by_customer' },
        { label: 'resolve_by_invoice_section', value: 'resolve_by_invoice_section' }
    ]}
>
<TabItem value="resolve_by_billing_account">

Lists the role assignments for the caller on a billing account while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement.

```sql
EXEC azure.billing.billing_role_assignments.resolve_by_billing_account 
@billing_account_name='{{ billing_account_name }}' --required, 
@resolveScopeDisplayNames={{ resolveScopeDisplayNames }}, 
@filter='{{ filter }}'
;
```
</TabItem>
<TabItem value="resolve_by_billing_profile">

Lists the role assignments for the caller on an billing profile while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

```sql
EXEC azure.billing.billing_role_assignments.resolve_by_billing_profile 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@resolveScopeDisplayNames={{ resolveScopeDisplayNames }}, 
@filter='{{ filter }}'
;
```
</TabItem>
<TabItem value="resolve_by_customer">

Lists the role assignments for the caller on a customer while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement.

```sql
EXEC azure.billing.billing_role_assignments.resolve_by_customer 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@customer_name='{{ customer_name }}' --required, 
@resolveScopeDisplayNames={{ resolveScopeDisplayNames }}, 
@filter='{{ filter }}'
;
```
</TabItem>
<TabItem value="resolve_by_invoice_section">

Lists the role assignments for the caller on an invoice section while fetching user info for each role assignment. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement.

```sql
EXEC azure.billing.billing_role_assignments.resolve_by_invoice_section 
@billing_account_name='{{ billing_account_name }}' --required, 
@billing_profile_name='{{ billing_profile_name }}' --required, 
@invoice_section_name='{{ invoice_section_name }}' --required, 
@resolveScopeDisplayNames={{ resolveScopeDisplayNames }}, 
@filter='{{ filter }}'
;
```
</TabItem>
</Tabs>
