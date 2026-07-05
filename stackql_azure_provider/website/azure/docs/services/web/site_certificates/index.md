--- 
title: site_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - site_certificates
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

Creates, updates, deletes, gets or lists a <code>site_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="site_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.site_certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_slot"
    values={[
        { label: 'get_slot', value: 'get_slot' },
        { label: 'get', value: 'get' },
        { label: 'list_slot', value: 'list_slot' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_slot">

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
    <td><CopyableCode code="canonicalName" /></td>
    <td><code>string</code></td>
    <td>CNAME of the certificate to be issued via free certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="cerBlob" /></td>
    <td><code>string (byte)</code></td>
    <td>Raw bytes of .cer file.</td>
</tr>
<tr>
    <td><CopyableCode code="domainValidationMethod" /></td>
    <td><code>string</code></td>
    <td>Method of domain validation for free cert.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate expiration date.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNames" /></td>
    <td><code>array</code></td>
    <td>Host names the certificate applies to.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the App Service Environment to use for the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="issueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate issue Date.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>Certificate issuer.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultId" /></td>
    <td><code>string</code></td>
    <td>Azure Key Vault Csm resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretName" /></td>
    <td><code>string</code></td>
    <td>Azure Key Vault secret name.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Key Vault secret. Known values are: "Initialized", "WaitingOnCertificateOrder", "Succeeded", "CertificateOrderFailed", "OperationNotPermittedOnKeyVault", "AzureServiceUnauthorizedToAccessKeyVault", "KeyVaultDoesNotExist", "KeyVaultSecretDoesNotExist", "UnknownError", "ExternalPrivateKey", and "Unknown". (Initialized, WaitingOnCertificateOrder, Succeeded, CertificateOrderFailed, OperationNotPermittedOnKeyVault, AzureServiceUnauthorizedToAccessKeyVault, KeyVaultDoesNotExist, KeyVaultSecretDoesNotExist, UnknownError, ExternalPrivateKey, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Certificate password.</td>
</tr>
<tr>
    <td><CopyableCode code="pfxBlob" /></td>
    <td><code>string (byte)</code></td>
    <td>Pfx blob.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKeyHash" /></td>
    <td><code>string</code></td>
    <td>Public key hash.</td>
</tr>
<tr>
    <td><CopyableCode code="selfLink" /></td>
    <td><code>string</code></td>
    <td>Self link.</td>
</tr>
<tr>
    <td><CopyableCode code="serverFarmId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the associated App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>App name.</td>
</tr>
<tr>
    <td><CopyableCode code="subjectName" /></td>
    <td><code>string</code></td>
    <td>Subject name of the certificate.</td>
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
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>Certificate thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="valid" /></td>
    <td><code>boolean</code></td>
    <td>Is the certificate valid?.</td>
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
    <td><CopyableCode code="canonicalName" /></td>
    <td><code>string</code></td>
    <td>CNAME of the certificate to be issued via free certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="cerBlob" /></td>
    <td><code>string (byte)</code></td>
    <td>Raw bytes of .cer file.</td>
</tr>
<tr>
    <td><CopyableCode code="domainValidationMethod" /></td>
    <td><code>string</code></td>
    <td>Method of domain validation for free cert.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate expiration date.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNames" /></td>
    <td><code>array</code></td>
    <td>Host names the certificate applies to.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the App Service Environment to use for the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="issueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate issue Date.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>Certificate issuer.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultId" /></td>
    <td><code>string</code></td>
    <td>Azure Key Vault Csm resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretName" /></td>
    <td><code>string</code></td>
    <td>Azure Key Vault secret name.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Key Vault secret. Known values are: "Initialized", "WaitingOnCertificateOrder", "Succeeded", "CertificateOrderFailed", "OperationNotPermittedOnKeyVault", "AzureServiceUnauthorizedToAccessKeyVault", "KeyVaultDoesNotExist", "KeyVaultSecretDoesNotExist", "UnknownError", "ExternalPrivateKey", and "Unknown". (Initialized, WaitingOnCertificateOrder, Succeeded, CertificateOrderFailed, OperationNotPermittedOnKeyVault, AzureServiceUnauthorizedToAccessKeyVault, KeyVaultDoesNotExist, KeyVaultSecretDoesNotExist, UnknownError, ExternalPrivateKey, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Certificate password.</td>
</tr>
<tr>
    <td><CopyableCode code="pfxBlob" /></td>
    <td><code>string (byte)</code></td>
    <td>Pfx blob.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKeyHash" /></td>
    <td><code>string</code></td>
    <td>Public key hash.</td>
</tr>
<tr>
    <td><CopyableCode code="selfLink" /></td>
    <td><code>string</code></td>
    <td>Self link.</td>
</tr>
<tr>
    <td><CopyableCode code="serverFarmId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the associated App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>App name.</td>
</tr>
<tr>
    <td><CopyableCode code="subjectName" /></td>
    <td><code>string</code></td>
    <td>Subject name of the certificate.</td>
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
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>Certificate thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="valid" /></td>
    <td><code>boolean</code></td>
    <td>Is the certificate valid?.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_slot">

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
    <td><CopyableCode code="canonicalName" /></td>
    <td><code>string</code></td>
    <td>CNAME of the certificate to be issued via free certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="cerBlob" /></td>
    <td><code>string (byte)</code></td>
    <td>Raw bytes of .cer file.</td>
</tr>
<tr>
    <td><CopyableCode code="domainValidationMethod" /></td>
    <td><code>string</code></td>
    <td>Method of domain validation for free cert.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate expiration date.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNames" /></td>
    <td><code>array</code></td>
    <td>Host names the certificate applies to.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the App Service Environment to use for the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="issueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate issue Date.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>Certificate issuer.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultId" /></td>
    <td><code>string</code></td>
    <td>Azure Key Vault Csm resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretName" /></td>
    <td><code>string</code></td>
    <td>Azure Key Vault secret name.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Key Vault secret. Known values are: "Initialized", "WaitingOnCertificateOrder", "Succeeded", "CertificateOrderFailed", "OperationNotPermittedOnKeyVault", "AzureServiceUnauthorizedToAccessKeyVault", "KeyVaultDoesNotExist", "KeyVaultSecretDoesNotExist", "UnknownError", "ExternalPrivateKey", and "Unknown". (Initialized, WaitingOnCertificateOrder, Succeeded, CertificateOrderFailed, OperationNotPermittedOnKeyVault, AzureServiceUnauthorizedToAccessKeyVault, KeyVaultDoesNotExist, KeyVaultSecretDoesNotExist, UnknownError, ExternalPrivateKey, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Certificate password.</td>
</tr>
<tr>
    <td><CopyableCode code="pfxBlob" /></td>
    <td><code>string (byte)</code></td>
    <td>Pfx blob.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKeyHash" /></td>
    <td><code>string</code></td>
    <td>Public key hash.</td>
</tr>
<tr>
    <td><CopyableCode code="selfLink" /></td>
    <td><code>string</code></td>
    <td>Self link.</td>
</tr>
<tr>
    <td><CopyableCode code="serverFarmId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the associated App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>App name.</td>
</tr>
<tr>
    <td><CopyableCode code="subjectName" /></td>
    <td><code>string</code></td>
    <td>Subject name of the certificate.</td>
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
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>Certificate thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="valid" /></td>
    <td><code>boolean</code></td>
    <td>Is the certificate valid?.</td>
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
    <td><CopyableCode code="canonicalName" /></td>
    <td><code>string</code></td>
    <td>CNAME of the certificate to be issued via free certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="cerBlob" /></td>
    <td><code>string (byte)</code></td>
    <td>Raw bytes of .cer file.</td>
</tr>
<tr>
    <td><CopyableCode code="domainValidationMethod" /></td>
    <td><code>string</code></td>
    <td>Method of domain validation for free cert.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate expiration date.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="hostNames" /></td>
    <td><code>array</code></td>
    <td>Host names the certificate applies to.</td>
</tr>
<tr>
    <td><CopyableCode code="hostingEnvironmentProfile" /></td>
    <td><code>object</code></td>
    <td>Specification for the App Service Environment to use for the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="issueDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate issue Date.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>string</code></td>
    <td>Certificate issuer.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultId" /></td>
    <td><code>string</code></td>
    <td>Azure Key Vault Csm resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretName" /></td>
    <td><code>string</code></td>
    <td>Azure Key Vault secret name.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultSecretStatus" /></td>
    <td><code>string</code></td>
    <td>Status of the Key Vault secret. Known values are: "Initialized", "WaitingOnCertificateOrder", "Succeeded", "CertificateOrderFailed", "OperationNotPermittedOnKeyVault", "AzureServiceUnauthorizedToAccessKeyVault", "KeyVaultDoesNotExist", "KeyVaultSecretDoesNotExist", "UnknownError", "ExternalPrivateKey", and "Unknown". (Initialized, WaitingOnCertificateOrder, Succeeded, CertificateOrderFailed, OperationNotPermittedOnKeyVault, AzureServiceUnauthorizedToAccessKeyVault, KeyVaultDoesNotExist, KeyVaultSecretDoesNotExist, UnknownError, ExternalPrivateKey, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource. If the resource is an app, you can refer to `https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference `_ for details supported values for kind.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string</code></td>
    <td>Certificate password.</td>
</tr>
<tr>
    <td><CopyableCode code="pfxBlob" /></td>
    <td><code>string (byte)</code></td>
    <td>Pfx blob.</td>
</tr>
<tr>
    <td><CopyableCode code="publicKeyHash" /></td>
    <td><code>string</code></td>
    <td>Public key hash.</td>
</tr>
<tr>
    <td><CopyableCode code="selfLink" /></td>
    <td><code>string</code></td>
    <td>Self link.</td>
</tr>
<tr>
    <td><CopyableCode code="serverFarmId" /></td>
    <td><code>string</code></td>
    <td>Resource ID of the associated App Service plan.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>App name.</td>
</tr>
<tr>
    <td><CopyableCode code="subjectName" /></td>
    <td><code>string</code></td>
    <td>Subject name of the certificate.</td>
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
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>Certificate thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="valid" /></td>
    <td><code>boolean</code></td>
    <td>Is the certificate valid?.</td>
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
    <td><a href="#get_slot"><CopyableCode code="get_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a certificate for a given site and deployment slot. Get a certificate for a given site and deployment slot.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a certificate belonging to a given site. Get a certificate belonging to a given site.</td>
</tr>
<tr>
    <td><a href="#list_slot"><CopyableCode code="list_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all certificates in a resource group for a given site and a deployment slot. Get all certificates in a resource group for a given site and a deployment slot.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all certificates in a resource group under a site. Get all certificates in a resource group under a site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_slot"><CopyableCode code="create_or_update_slot" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a certificate in a given site and deployment slot. Create or update a certificate in a given site and deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a certificate under a given site. Create or update a certificate under a given site.</td>
</tr>
<tr>
    <td><a href="#update_slot"><CopyableCode code="update_slot" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a certificate for a site and deployment slot. Create or update a certificate for a site and deployment slot.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a certificate under a given site. Create or update a certificate under a given site.</td>
</tr>
<tr>
    <td><a href="#create_or_update_slot"><CopyableCode code="create_or_update_slot" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a certificate in a given site and deployment slot. Create or update a certificate in a given site and deployment slot.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a certificate under a given site. Create or update a certificate under a given site.</td>
</tr>
<tr>
    <td><a href="#delete_slot"><CopyableCode code="delete_slot" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a certificate for a given site and deployment slot. Delete a certificate for a given site and deployment slot.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a certificate from the site. Delete a certificate from the site.</td>
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
<tr id="parameter-certificate_name">
    <td><CopyableCode code="certificate_name" /></td>
    <td><code>string</code></td>
    <td>Name of the certificate. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the site. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-slot">
    <td><CopyableCode code="slot" /></td>
    <td><code>string</code></td>
    <td>Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot. Required.</td>
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
    defaultValue="get_slot"
    values={[
        { label: 'get_slot', value: 'get_slot' },
        { label: 'get', value: 'get' },
        { label: 'list_slot', value: 'list_slot' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_slot">

Get a certificate for a given site and deployment slot. Get a certificate for a given site and deployment slot.

```sql
SELECT
id,
name,
canonicalName,
cerBlob,
domainValidationMethod,
expirationDate,
friendlyName,
hostNames,
hostingEnvironmentProfile,
issueDate,
issuer,
keyVaultId,
keyVaultSecretName,
keyVaultSecretStatus,
kind,
location,
password,
pfxBlob,
publicKeyHash,
selfLink,
serverFarmId,
siteName,
subjectName,
systemData,
tags,
thumbprint,
type,
valid
FROM azure.web.site_certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND certificate_name = '{{ certificate_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a certificate belonging to a given site. Get a certificate belonging to a given site.

```sql
SELECT
id,
name,
canonicalName,
cerBlob,
domainValidationMethod,
expirationDate,
friendlyName,
hostNames,
hostingEnvironmentProfile,
issueDate,
issuer,
keyVaultId,
keyVaultSecretName,
keyVaultSecretStatus,
kind,
location,
password,
pfxBlob,
publicKeyHash,
selfLink,
serverFarmId,
siteName,
subjectName,
systemData,
tags,
thumbprint,
type,
valid
FROM azure.web.site_certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND certificate_name = '{{ certificate_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_slot">

Get all certificates in a resource group for a given site and a deployment slot. Get all certificates in a resource group for a given site and a deployment slot.

```sql
SELECT
id,
name,
canonicalName,
cerBlob,
domainValidationMethod,
expirationDate,
friendlyName,
hostNames,
hostingEnvironmentProfile,
issueDate,
issuer,
keyVaultId,
keyVaultSecretName,
keyVaultSecretStatus,
kind,
location,
password,
pfxBlob,
publicKeyHash,
selfLink,
serverFarmId,
siteName,
subjectName,
systemData,
tags,
thumbprint,
type,
valid
FROM azure.web.site_certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all certificates in a resource group under a site. Get all certificates in a resource group under a site.

```sql
SELECT
id,
name,
canonicalName,
cerBlob,
domainValidationMethod,
expirationDate,
friendlyName,
hostNames,
hostingEnvironmentProfile,
issueDate,
issuer,
keyVaultId,
keyVaultSecretName,
keyVaultSecretStatus,
kind,
location,
password,
pfxBlob,
publicKeyHash,
selfLink,
serverFarmId,
siteName,
subjectName,
systemData,
tags,
thumbprint,
type,
valid
FROM azure.web.site_certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_slot"
    values={[
        { label: 'create_or_update_slot', value: 'create_or_update_slot' },
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_slot">

Create or update a certificate in a given site and deployment slot. Create or update a certificate in a given site and deployment slot.

```sql
INSERT INTO azure.web.site_certificates (
tags,
location,
properties,
kind,
resource_group_name,
name,
slot,
certificate_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ slot }}',
'{{ certificate_name }}',
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
<TabItem value="create_or_update">

Create or update a certificate under a given site. Create or update a certificate under a given site.

```sql
INSERT INTO azure.web.site_certificates (
tags,
location,
properties,
kind,
resource_group_name,
name,
certificate_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ name }}',
'{{ certificate_name }}',
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
- name: site_certificates
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the site_certificates resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the site_certificates resource.
    - name: slot
      value: "{{ slot }}"
      description: Required parameter for the site_certificates resource.
    - name: certificate_name
      value: "{{ certificate_name }}"
      description: Required parameter for the site_certificates resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the site_certificates resource.
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
        Certificate resource specific properties.
      value:
        password: "{{ password }}"
        friendlyName: "{{ friendlyName }}"
        subjectName: "{{ subjectName }}"
        hostNames:
          - "{{ hostNames }}"
        pfxBlob: "{{ pfxBlob }}"
        siteName: "{{ siteName }}"
        selfLink: "{{ selfLink }}"
        issuer: "{{ issuer }}"
        issueDate: "{{ issueDate }}"
        expirationDate: "{{ expirationDate }}"
        thumbprint: "{{ thumbprint }}"
        valid: {{ valid }}
        cerBlob: "{{ cerBlob }}"
        publicKeyHash: "{{ publicKeyHash }}"
        hostingEnvironmentProfile:
          id: "{{ id }}"
          name: "{{ name }}"
          type: "{{ type }}"
        keyVaultId: "{{ keyVaultId }}"
        keyVaultSecretName: "{{ keyVaultSecretName }}"
        keyVaultSecretStatus: "{{ keyVaultSecretStatus }}"
        serverFarmId: "{{ serverFarmId }}"
        canonicalName: "{{ canonicalName }}"
        domainValidationMethod: "{{ domainValidationMethod }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of resource. If the resource is an app, you can refer to \`https://github.com/Azure/app-service-linux-docs/blob/master/Things_You_Should_Know/kind_property.md#app-service-resource-kind-reference \`_ for details supported values for kind.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_slot"
    values={[
        { label: 'update_slot', value: 'update_slot' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update_slot">

Create or update a certificate for a site and deployment slot. Create or update a certificate for a site and deployment slot.

```sql
UPDATE azure.web.site_certificates
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND slot = '{{ slot }}' --required
AND certificate_name = '{{ certificate_name }}' --required
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
<TabItem value="update">

Create or update a certificate under a given site. Create or update a certificate under a given site.

```sql
UPDATE azure.web.site_certificates
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND certificate_name = '{{ certificate_name }}' --required
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
    defaultValue="create_or_update_slot"
    values={[
        { label: 'create_or_update_slot', value: 'create_or_update_slot' },
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update_slot">

Create or update a certificate in a given site and deployment slot. Create or update a certificate in a given site and deployment slot.

```sql
REPLACE azure.web.site_certificates
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND slot = '{{ slot }}' --required
AND certificate_name = '{{ certificate_name }}' --required
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
<TabItem value="create_or_update">

Create or update a certificate under a given site. Create or update a certificate under a given site.

```sql
REPLACE azure.web.site_certificates
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND certificate_name = '{{ certificate_name }}' --required
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
    defaultValue="delete_slot"
    values={[
        { label: 'delete_slot', value: 'delete_slot' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_slot">

Delete a certificate for a given site and deployment slot. Delete a certificate for a given site and deployment slot.

```sql
DELETE FROM azure.web.site_certificates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND slot = '{{ slot }}' --required
AND certificate_name = '{{ certificate_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete a certificate from the site. Delete a certificate from the site.

```sql
DELETE FROM azure.web.site_certificates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND certificate_name = '{{ certificate_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
