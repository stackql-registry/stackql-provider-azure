--- 
title: app_service_certificate_orders
hide_title: false
hide_table_of_contents: false
keywords:
  - app_service_certificate_orders
  - certificate_registration
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

Creates, updates, deletes, gets or lists an <code>app_service_certificate_orders</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_service_certificate_orders" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.certificate_registration.app_service_certificate_orders" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_certificate"
    values={[
        { label: 'get_certificate', value: 'get_certificate' },
        { label: 'get', value: 'get' },
        { label: 'retrieve_certificate_actions', value: 'retrieve_certificate_actions' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_certificate">

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
    <td><CopyableCode code="keyVaultId" /></td>
    <td><code>string</code></td>
    <td>Key Vault resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretName" /></td>
    <td><code>string</code></td>
    <td>Key Vault secret name.</td>
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the Key Vault secret. Known values are: "Initialized", "WaitingOnCertificateOrder", "Succeeded", "CertificateOrderFailed", "OperationNotPermittedOnKeyVault", "AzureServiceUnauthorizedToAccessKeyVault", "KeyVaultDoesNotExist", "KeyVaultSecretDoesNotExist", "UnknownError", "ExternalPrivateKey", and "Unknown". (Initialized, WaitingOnCertificateOrder, Succeeded, CertificateOrderFailed, OperationNotPermittedOnKeyVault, AzureServiceUnauthorizedToAccessKeyVault, KeyVaultDoesNotExist, KeyVaultSecretDoesNotExist, UnknownError, ExternalPrivateKey, Unknown)</td>
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
    <td><CopyableCode code="appServiceCertificateNotRenewableReasons" /></td>
    <td><code>array</code></td>
    <td>Reasons why App Service Certificate is not renewable at the current moment.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>true if the certificate should be automatically renewed when it expires; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>object</code></td>
    <td>State of the Key Vault secret.</td>
</tr>
<tr>
    <td><CopyableCode code="contact" /></td>
    <td><code>object</code></td>
    <td>Contact info.</td>
</tr>
<tr>
    <td><CopyableCode code="csr" /></td>
    <td><code>string</code></td>
    <td>Last CSR that was created for this order.</td>
</tr>
<tr>
    <td><CopyableCode code="distinguishedName" /></td>
    <td><code>string</code></td>
    <td>Certificate distinguished name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainVerificationToken" /></td>
    <td><code>string</code></td>
    <td>Domain verification token.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate expiration time.</td>
</tr>
<tr>
    <td><CopyableCode code="intermediate" /></td>
    <td><code>object</code></td>
    <td>Intermediate certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="isPrivateKeyExternal" /></td>
    <td><code>boolean</code></td>
    <td>true if private key is external; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="keySize" /></td>
    <td><code>integer</code></td>
    <td>Certificate key size.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastCertificateIssuanceTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate last issuance time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAutoRenewalTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time stamp when the certificate would be auto renewed next.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>Certificate product type. Required. Known values are: "StandardDomainValidatedSsl" and "StandardDomainValidatedWildCardSsl". (StandardDomainValidatedSsl, StandardDomainValidatedWildCardSsl)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of certificate order. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="root" /></td>
    <td><code>object</code></td>
    <td>Root certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Current serial number of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="signedCertificate" /></td>
    <td><code>object</code></td>
    <td>Signed certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current order status. Known values are: "Pendingissuance", "Issued", "Revoked", "Canceled", "Denied", "Pendingrevocation", "PendingRekey", "Unused", "Expired", and "NotSubmitted". (Pendingissuance, Issued, Revoked, Canceled, Denied, Pendingrevocation, PendingRekey, Unused, Expired, NotSubmitted)</td>
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
    <td><CopyableCode code="validityInYears" /></td>
    <td><code>integer</code></td>
    <td>Duration in years (must be 1).</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="retrieve_certificate_actions">

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
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>Action type. Known values are: "CertificateIssued", "CertificateOrderCanceled", "CertificateOrderCreated", "CertificateRevoked", "DomainValidationComplete", "FraudDetected", "OrgNameChange", "OrgValidationComplete", "SanDrop", "FraudCleared", "CertificateExpired", "CertificateExpirationWarning", "FraudDocumentationRequired", and "Unknown". (CertificateIssued, CertificateOrderCanceled, CertificateOrderCreated, CertificateRevoked, DomainValidationComplete, FraudDetected, OrgNameChange, OrgValidationComplete, SanDrop, FraudCleared, CertificateExpired, CertificateExpirationWarning, FraudDocumentationRequired, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="createdAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time at which the certificate action was performed.</td>
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
    <td><CopyableCode code="appServiceCertificateNotRenewableReasons" /></td>
    <td><code>array</code></td>
    <td>Reasons why App Service Certificate is not renewable at the current moment.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>true if the certificate should be automatically renewed when it expires; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>object</code></td>
    <td>State of the Key Vault secret.</td>
</tr>
<tr>
    <td><CopyableCode code="contact" /></td>
    <td><code>object</code></td>
    <td>Contact info.</td>
</tr>
<tr>
    <td><CopyableCode code="csr" /></td>
    <td><code>string</code></td>
    <td>Last CSR that was created for this order.</td>
</tr>
<tr>
    <td><CopyableCode code="distinguishedName" /></td>
    <td><code>string</code></td>
    <td>Certificate distinguished name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainVerificationToken" /></td>
    <td><code>string</code></td>
    <td>Domain verification token.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate expiration time.</td>
</tr>
<tr>
    <td><CopyableCode code="intermediate" /></td>
    <td><code>object</code></td>
    <td>Intermediate certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="isPrivateKeyExternal" /></td>
    <td><code>boolean</code></td>
    <td>true if private key is external; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="keySize" /></td>
    <td><code>integer</code></td>
    <td>Certificate key size.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastCertificateIssuanceTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate last issuance time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAutoRenewalTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time stamp when the certificate would be auto renewed next.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>Certificate product type. Required. Known values are: "StandardDomainValidatedSsl" and "StandardDomainValidatedWildCardSsl". (StandardDomainValidatedSsl, StandardDomainValidatedWildCardSsl)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of certificate order. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="root" /></td>
    <td><code>object</code></td>
    <td>Root certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Current serial number of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="signedCertificate" /></td>
    <td><code>object</code></td>
    <td>Signed certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current order status. Known values are: "Pendingissuance", "Issued", "Revoked", "Canceled", "Denied", "Pendingrevocation", "PendingRekey", "Unused", "Expired", and "NotSubmitted". (Pendingissuance, Issued, Revoked, Canceled, Denied, Pendingrevocation, PendingRekey, Unused, Expired, NotSubmitted)</td>
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
    <td><CopyableCode code="validityInYears" /></td>
    <td><code>integer</code></td>
    <td>Duration in years (must be 1).</td>
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
    <td><CopyableCode code="appServiceCertificateNotRenewableReasons" /></td>
    <td><code>array</code></td>
    <td>Reasons why App Service Certificate is not renewable at the current moment.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>true if the certificate should be automatically renewed when it expires; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>object</code></td>
    <td>State of the Key Vault secret.</td>
</tr>
<tr>
    <td><CopyableCode code="contact" /></td>
    <td><code>object</code></td>
    <td>Contact info.</td>
</tr>
<tr>
    <td><CopyableCode code="csr" /></td>
    <td><code>string</code></td>
    <td>Last CSR that was created for this order.</td>
</tr>
<tr>
    <td><CopyableCode code="distinguishedName" /></td>
    <td><code>string</code></td>
    <td>Certificate distinguished name.</td>
</tr>
<tr>
    <td><CopyableCode code="domainVerificationToken" /></td>
    <td><code>string</code></td>
    <td>Domain verification token.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate expiration time.</td>
</tr>
<tr>
    <td><CopyableCode code="intermediate" /></td>
    <td><code>object</code></td>
    <td>Intermediate certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="isPrivateKeyExternal" /></td>
    <td><code>boolean</code></td>
    <td>true if private key is external; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="keySize" /></td>
    <td><code>integer</code></td>
    <td>Certificate key size.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastCertificateIssuanceTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate last issuance time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nextAutoRenewalTimeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time stamp when the certificate would be auto renewed next.</td>
</tr>
<tr>
    <td><CopyableCode code="productType" /></td>
    <td><code>string</code></td>
    <td>Certificate product type. Required. Known values are: "StandardDomainValidatedSsl" and "StandardDomainValidatedWildCardSsl". (StandardDomainValidatedSsl, StandardDomainValidatedWildCardSsl)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of certificate order. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="root" /></td>
    <td><code>object</code></td>
    <td>Root certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Current serial number of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="signedCertificate" /></td>
    <td><code>object</code></td>
    <td>Signed certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current order status. Known values are: "Pendingissuance", "Issued", "Revoked", "Canceled", "Denied", "Pendingrevocation", "PendingRekey", "Unused", "Expired", and "NotSubmitted". (Pendingissuance, Issued, Revoked, Canceled, Denied, Pendingrevocation, PendingRekey, Unused, Expired, NotSubmitted)</td>
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
    <td><CopyableCode code="validityInYears" /></td>
    <td><code>integer</code></td>
    <td>Duration in years (must be 1).</td>
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
    <td><a href="#get_certificate"><CopyableCode code="get_certificate" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the certificate associated with a certificate order. Description for Get the certificate associated with a certificate order.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a certificate order. Description for Get a certificate order.</td>
</tr>
<tr>
    <td><a href="#retrieve_certificate_actions"><CopyableCode code="retrieve_certificate_actions" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve the list of certificate actions. Description for Retrieve the list of certificate actions.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get certificate orders in a resource group. Description for Get certificate orders in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all certificate orders in a subscription. Description for List all certificate orders in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a certificate purchase order. Description for Create or update a certificate purchase order.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a certificate purchase order. Description for Create or update a certificate purchase order.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a certificate purchase order. Description for Create or update a certificate purchase order.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an existing certificate order. Description for Delete an existing certificate order.</td>
</tr>
<tr>
    <td><a href="#list_certificates"><CopyableCode code="list_certificates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all certificates associated with a certificate order. Description for List all certificates associated with a certificate order.</td>
</tr>
<tr>
    <td><a href="#create_or_update_certificate"><CopyableCode code="create_or_update_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a certificate and associates with key vault secret. Description for Creates or updates a certificate and associates with key vault secret.</td>
</tr>
<tr>
    <td><a href="#update_certificate"><CopyableCode code="update_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a certificate and associates with key vault secret. Description for Creates or updates a certificate and associates with key vault secret.</td>
</tr>
<tr>
    <td><a href="#delete_certificate"><CopyableCode code="delete_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the certificate associated with a certificate order. Description for Delete the certificate associated with a certificate order.</td>
</tr>
<tr>
    <td><a href="#reissue"><CopyableCode code="reissue" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reissue an existing certificate order. Description for Reissue an existing certificate order.</td>
</tr>
<tr>
    <td><a href="#renew"><CopyableCode code="renew" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Renew an existing certificate order. Description for Renew an existing certificate order.</td>
</tr>
<tr>
    <td><a href="#resend_email"><CopyableCode code="resend_email" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resend certificate email. Description for Resend certificate email.</td>
</tr>
<tr>
    <td><a href="#resend_request_emails"><CopyableCode code="resend_request_emails" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Resend domain verification email to customer for this certificate order. Resend domain verification ownership email containing steps on how to verify a domain for a given certificate order.</td>
</tr>
<tr>
    <td><a href="#retrieve_site_seal"><CopyableCode code="retrieve_site_seal" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This method is used to obtain the site seal information for an issued certificate. This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted by the reseller, to minimize delays for customer page load times.</td>
</tr>
<tr>
    <td><a href="#verify_domain_ownership"><CopyableCode code="verify_domain_ownership" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Verify domain ownership for this certificate order. Description for Verify domain ownership for this certificate order.</td>
</tr>
<tr>
    <td><a href="#retrieve_certificate_email_history"><CopyableCode code="retrieve_certificate_email_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve email history. Description for Retrieve email history.</td>
</tr>
<tr>
    <td><a href="#validate_purchase_information"><CopyableCode code="validate_purchase_information" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Validate information for a certificate order. Description for Validate information for a certificate order.</td>
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
<tr id="parameter-certificate_order_name">
    <td><CopyableCode code="certificate_order_name" /></td>
    <td><code>string</code></td>
    <td>Name of the certificate order.. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the certificate order.. Required.</td>
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
    defaultValue="get_certificate"
    values={[
        { label: 'get_certificate', value: 'get_certificate' },
        { label: 'get', value: 'get' },
        { label: 'retrieve_certificate_actions', value: 'retrieve_certificate_actions' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_certificate">

Get the certificate associated with a certificate order. Description for Get the certificate associated with a certificate order.

```sql
SELECT
id,
name,
keyVaultId,
keyVaultSecretName,
kind,
location,
provisioningState,
systemData,
tags,
type
FROM azure.certificate_registration.app_service_certificate_orders
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND certificate_order_name = '{{ certificate_order_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a certificate order. Description for Get a certificate order.

```sql
SELECT
id,
name,
appServiceCertificateNotRenewableReasons,
autoRenew,
certificates,
contact,
csr,
distinguishedName,
domainVerificationToken,
expirationTime,
intermediate,
isPrivateKeyExternal,
keySize,
kind,
lastCertificateIssuanceTime,
location,
nextAutoRenewalTimeStamp,
productType,
provisioningState,
root,
serialNumber,
signedCertificate,
status,
systemData,
tags,
type,
validityInYears
FROM azure.certificate_registration.app_service_certificate_orders
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND certificate_order_name = '{{ certificate_order_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="retrieve_certificate_actions">

Retrieve the list of certificate actions. Description for Retrieve the list of certificate actions.

```sql
SELECT
actionType,
createdAt
FROM azure.certificate_registration.app_service_certificate_orders
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get certificate orders in a resource group. Description for Get certificate orders in a resource group.

```sql
SELECT
id,
name,
appServiceCertificateNotRenewableReasons,
autoRenew,
certificates,
contact,
csr,
distinguishedName,
domainVerificationToken,
expirationTime,
intermediate,
isPrivateKeyExternal,
keySize,
kind,
lastCertificateIssuanceTime,
location,
nextAutoRenewalTimeStamp,
productType,
provisioningState,
root,
serialNumber,
signedCertificate,
status,
systemData,
tags,
type,
validityInYears
FROM azure.certificate_registration.app_service_certificate_orders
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all certificate orders in a subscription. Description for List all certificate orders in a subscription.

```sql
SELECT
id,
name,
appServiceCertificateNotRenewableReasons,
autoRenew,
certificates,
contact,
csr,
distinguishedName,
domainVerificationToken,
expirationTime,
intermediate,
isPrivateKeyExternal,
keySize,
kind,
lastCertificateIssuanceTime,
location,
nextAutoRenewalTimeStamp,
productType,
provisioningState,
root,
serialNumber,
signedCertificate,
status,
systemData,
tags,
type,
validityInYears
FROM azure.certificate_registration.app_service_certificate_orders
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

Create or update a certificate purchase order. Description for Create or update a certificate purchase order.

```sql
INSERT INTO azure.certificate_registration.app_service_certificate_orders (
tags,
location,
properties,
kind,
resource_group_name,
certificate_order_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ certificate_order_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: app_service_certificate_orders
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the app_service_certificate_orders resource.
    - name: certificate_order_name
      value: "{{ certificate_order_name }}"
      description: Required parameter for the app_service_certificate_orders resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the app_service_certificate_orders resource.
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
        AppServiceCertificateOrder resource specific properties.
      value:
        certificates: "{{ certificates }}"
        distinguishedName: "{{ distinguishedName }}"
        domainVerificationToken: "{{ domainVerificationToken }}"
        validityInYears: {{ validityInYears }}
        keySize: {{ keySize }}
        productType: "{{ productType }}"
        autoRenew: {{ autoRenew }}
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        signedCertificate:
          version: {{ version }}
          serialNumber: "{{ serialNumber }}"
          thumbprint: "{{ thumbprint }}"
          subject: "{{ subject }}"
          notBefore: "{{ notBefore }}"
          notAfter: "{{ notAfter }}"
          signatureAlgorithm: "{{ signatureAlgorithm }}"
          issuer: "{{ issuer }}"
          rawData: "{{ rawData }}"
        csr: "{{ csr }}"
        intermediate:
          version: {{ version }}
          serialNumber: "{{ serialNumber }}"
          thumbprint: "{{ thumbprint }}"
          subject: "{{ subject }}"
          notBefore: "{{ notBefore }}"
          notAfter: "{{ notAfter }}"
          signatureAlgorithm: "{{ signatureAlgorithm }}"
          issuer: "{{ issuer }}"
          rawData: "{{ rawData }}"
        root:
          version: {{ version }}
          serialNumber: "{{ serialNumber }}"
          thumbprint: "{{ thumbprint }}"
          subject: "{{ subject }}"
          notBefore: "{{ notBefore }}"
          notAfter: "{{ notAfter }}"
          signatureAlgorithm: "{{ signatureAlgorithm }}"
          issuer: "{{ issuer }}"
          rawData: "{{ rawData }}"
        serialNumber: "{{ serialNumber }}"
        lastCertificateIssuanceTime: "{{ lastCertificateIssuanceTime }}"
        expirationTime: "{{ expirationTime }}"
        isPrivateKeyExternal: {{ isPrivateKeyExternal }}
        appServiceCertificateNotRenewableReasons:
          - "{{ appServiceCertificateNotRenewableReasons }}"
        nextAutoRenewalTimeStamp: "{{ nextAutoRenewalTimeStamp }}"
        contact:
          email: "{{ email }}"
          nameFirst: "{{ nameFirst }}"
          nameLast: "{{ nameLast }}"
          phone: "{{ phone }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of resource.
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

Create or update a certificate purchase order. Description for Create or update a certificate purchase order.

```sql
UPDATE azure.certificate_registration.app_service_certificate_orders
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND certificate_order_name = '{{ certificate_order_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or update a certificate purchase order. Description for Create or update a certificate purchase order.

```sql
REPLACE azure.certificate_registration.app_service_certificate_orders
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND certificate_order_name = '{{ certificate_order_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete an existing certificate order. Description for Delete an existing certificate order.

```sql
DELETE FROM azure.certificate_registration.app_service_certificate_orders
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND certificate_order_name = '{{ certificate_order_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_certificates"
    values={[
        { label: 'list_certificates', value: 'list_certificates' },
        { label: 'create_or_update_certificate', value: 'create_or_update_certificate' },
        { label: 'update_certificate', value: 'update_certificate' },
        { label: 'delete_certificate', value: 'delete_certificate' },
        { label: 'reissue', value: 'reissue' },
        { label: 'renew', value: 'renew' },
        { label: 'resend_email', value: 'resend_email' },
        { label: 'resend_request_emails', value: 'resend_request_emails' },
        { label: 'retrieve_site_seal', value: 'retrieve_site_seal' },
        { label: 'verify_domain_ownership', value: 'verify_domain_ownership' },
        { label: 'retrieve_certificate_email_history', value: 'retrieve_certificate_email_history' },
        { label: 'validate_purchase_information', value: 'validate_purchase_information' }
    ]}
>
<TabItem value="list_certificates">

List all certificates associated with a certificate order. Description for List all certificates associated with a certificate order.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.list_certificates 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="create_or_update_certificate">

Creates or updates a certificate and associates with key vault secret. Description for Creates or updates a certificate and associates with key vault secret.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.create_or_update_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@name='{{ name }}' --required, 
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
<TabItem value="update_certificate">

Creates or updates a certificate and associates with key vault secret. Description for Creates or updates a certificate and associates with key vault secret.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.update_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
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
<TabItem value="delete_certificate">

Delete the certificate associated with a certificate order. Description for Delete the certificate associated with a certificate order.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.delete_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reissue">

Reissue an existing certificate order. Description for Reissue an existing certificate order.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.reissue 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="renew">

Renew an existing certificate order. Description for Renew an existing certificate order.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.renew 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="resend_email">

Resend certificate email. Description for Resend certificate email.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.resend_email 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="resend_request_emails">

Resend domain verification email to customer for this certificate order. Resend domain verification ownership email containing steps on how to verify a domain for a given certificate order.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.resend_request_emails 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}"
}'
;
```
</TabItem>
<TabItem value="retrieve_site_seal">

This method is used to obtain the site seal information for an issued certificate. This method is used to obtain the site seal information for an issued certificate. A site seal is a graphic that the certificate purchaser can embed on their web site to show their visitors information about their SSL certificate. If a web site visitor clicks on the site seal image, a pop-up page is displayed that contains detailed information about the SSL certificate. The site seal token is used to link the site seal graphic image to the appropriate certificate details pop-up page display when a user clicks on the site seal. The site seal images are expected to be static images and hosted by the reseller, to minimize delays for customer page load times.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.retrieve_site_seal 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"lightTheme": {{ lightTheme }}, 
"locale": "{{ locale }}"
}'
;
```
</TabItem>
<TabItem value="verify_domain_ownership">

Verify domain ownership for this certificate order. Description for Verify domain ownership for this certificate order.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.verify_domain_ownership 
@resource_group_name='{{ resource_group_name }}' --required, 
@certificate_order_name='{{ certificate_order_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="retrieve_certificate_email_history">

Retrieve email history. Description for Retrieve email history.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.retrieve_certificate_email_history 
@resource_group_name='{{ resource_group_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="validate_purchase_information">

Validate information for a certificate order. Description for Validate information for a certificate order.

```sql
EXEC azure.certificate_registration.app_service_certificate_orders.validate_purchase_information 
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
</Tabs>
