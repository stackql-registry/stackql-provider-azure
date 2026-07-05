--- 
title: crypto_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - crypto_certificates
  - iotfirmwaredefense
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

Creates, updates, deletes, gets or lists a <code>crypto_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="crypto_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iotfirmwaredefense.crypto_certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_firmware"
    values={[
        { label: 'list_by_firmware', value: 'list_by_firmware' }
    ]}
>
<TabItem value="list_by_firmware">

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
    <td><CopyableCode code="certificateKeyAlgorithm" /></td>
    <td><code>string</code></td>
    <td>Key algorithm used in the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateKeySize" /></td>
    <td><code>integer</code></td>
    <td>Size of the certificate's key in bits.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateName" /></td>
    <td><code>string</code></td>
    <td>Name of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateRole" /></td>
    <td><code>string</code></td>
    <td>Role of the certificate (Root CA, etc).</td>
</tr>
<tr>
    <td><CopyableCode code="certificateUsage" /></td>
    <td><code>array</code></td>
    <td>List of functions the certificate can fulfill.</td>
</tr>
<tr>
    <td><CopyableCode code="cryptoCertId" /></td>
    <td><code>string</code></td>
    <td>ID for the certificate result.</td>
</tr>
<tr>
    <td><CopyableCode code="encoding" /></td>
    <td><code>string</code></td>
    <td>Encoding used for the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiration date for the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="filePaths" /></td>
    <td><code>array</code></td>
    <td>List of files where this certificate was found.</td>
</tr>
<tr>
    <td><CopyableCode code="fingerprint" /></td>
    <td><code>string</code></td>
    <td>Fingerprint of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="isExpired" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the certificate is expired.</td>
</tr>
<tr>
    <td><CopyableCode code="isSelfSigned" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the certificate is self-signed.</td>
</tr>
<tr>
    <td><CopyableCode code="isShortKeySize" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the certificate's key size is considered too small to be secure for the key algorithm according to NIST guidance.</td>
</tr>
<tr>
    <td><CopyableCode code="isWeakSignature" /></td>
    <td><code>boolean</code></td>
    <td>Indicates the signature algorithm used is insecure according to NIST guidance.</td>
</tr>
<tr>
    <td><CopyableCode code="issuedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Issue date for the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="issuer" /></td>
    <td><code>object</code></td>
    <td>Issuer information of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="pairedKey" /></td>
    <td><code>object</code></td>
    <td>A matching paired private key.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "Extracting", and "Analyzing". (Succeeded, Failed, Canceled, Pending, Extracting, Analyzing)</td>
</tr>
<tr>
    <td><CopyableCode code="serialNumber" /></td>
    <td><code>string</code></td>
    <td>Serial number of the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="signatureAlgorithm" /></td>
    <td><code>string</code></td>
    <td>The signature algorithm used in the certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>object</code></td>
    <td>Subject information of the certificate.</td>
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
    <td><a href="#list_by_firmware"><CopyableCode code="list_by_firmware" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-firmware_id"><code>firmware_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists crypto certificate analysis results of a firmware.</td>
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
<tr id="parameter-firmware_id">
    <td><CopyableCode code="firmware_id" /></td>
    <td><code>string</code></td>
    <td>The id of the firmware. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the firmware analysis workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_firmware"
    values={[
        { label: 'list_by_firmware', value: 'list_by_firmware' }
    ]}
>
<TabItem value="list_by_firmware">

Lists crypto certificate analysis results of a firmware.

```sql
SELECT
id,
name,
certificateKeyAlgorithm,
certificateKeySize,
certificateName,
certificateRole,
certificateUsage,
cryptoCertId,
encoding,
expirationDate,
filePaths,
fingerprint,
isExpired,
isSelfSigned,
isShortKeySize,
isWeakSignature,
issuedDate,
issuer,
pairedKey,
provisioningState,
serialNumber,
signatureAlgorithm,
subject,
systemData,
type
FROM azure.iotfirmwaredefense.crypto_certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND firmware_id = '{{ firmware_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
