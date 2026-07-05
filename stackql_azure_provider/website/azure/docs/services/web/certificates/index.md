--- 
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
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

Creates, updates, deletes, gets or lists a <code>certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a certificate. Description for Get a certificate.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all certificates in a resource group. Description for Get all certificates in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all certificates for a subscription. Description for Get all certificates for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a certificate. Description for Create or update a certificate.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a certificate. Description for Create or update a certificate.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a certificate. Description for Create or update a certificate.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a certificate. Description for Delete a certificate.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the certificate. Required.</td>
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
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Return only information specified in the filter (using OData syntax). For example: $filter=KeyVaultId eq 'KeyVaultId'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a certificate. Description for Get a certificate.

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
FROM azure.web.certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all certificates in a resource group. Description for Get all certificates in a resource group.

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
FROM azure.web.certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all certificates for a subscription. Description for Get all certificates for a subscription.

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
FROM azure.web.certificates
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Create or update a certificate. Description for Create or update a certificate.

```sql
INSERT INTO azure.web.certificates (
tags,
location,
properties,
kind,
resource_group_name,
name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ name }}',
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
- name: certificates
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the certificates resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the certificates resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the certificates resource.
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
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Create or update a certificate. Description for Create or update a certificate.

```sql
UPDATE azure.web.certificates
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
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

Create or update a certificate. Description for Create or update a certificate.

```sql
REPLACE azure.web.certificates
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
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

Delete a certificate. Description for Delete a certificate.

```sql
DELETE FROM azure.web.certificates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
