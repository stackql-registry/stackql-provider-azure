--- 
title: attestation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - attestation_statuses
  - azure_stack_hci_vm
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>attestation_statuses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="attestation_statuses" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci_vm.attestation_statuses" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="attestDiskSecurityEncryptionType" /></td>
    <td><code>string</code></td>
    <td>The managed disk security encryption type from attestation token. This only applies to Confidential VM. Known values are: "NonPersistedTPM" and "Unknown". (NonPersistedTPM, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="attestHardwarePlatform" /></td>
    <td><code>string</code></td>
    <td>The hardware platform information from attestation token. This only applies to Confidential VM. Known values are: "SEVSNP" and "Unknown". (SEVSNP, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="attestSecureBootEnabled" /></td>
    <td><code>string</code></td>
    <td>The status of whether secure boot is enabled. Known values are: "Enabled", "Disabled", and "Unknown". (Enabled, Disabled, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="attestationCertValidated" /></td>
    <td><code>string</code></td>
    <td>The status of whether attestation certificate is validated. Known values are: "Valid", "Invalid", and "Unknown". (Valid, Invalid, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="bootIntegrityValidated" /></td>
    <td><code>string</code></td>
    <td>The status of whether the list of boot integrity properties is validated. Known values are: "Valid", "Invalid", and "Unknown". (Valid, Invalid, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>The error message of attestation validation and parsing.</td>
</tr>
<tr>
    <td><CopyableCode code="healthStatus" /></td>
    <td><code>string</code></td>
    <td>The health status of attestation validation and parsing. Known values are: "Pending", "Healthy", "Unhealthy", and "Unknown". (Pending, Healthy, Unhealthy, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="linuxKernelVersion" /></td>
    <td><code>string</code></td>
    <td>kernel version string for Linux VM.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the virtual machine instance. Known values are: "Succeeded", "Failed", "InProgress", "Accepted", "Deleting", and "Canceled". (Succeeded, Failed, InProgress, Accepted, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string</code></td>
    <td>The time stamp of the last time attestation token is validated by relying party service.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Implements AttestationStatus GET method.</td>
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
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Implements AttestationStatus GET method.

```sql
SELECT
id,
name,
attestDiskSecurityEncryptionType,
attestHardwarePlatform,
attestSecureBootEnabled,
attestationCertValidated,
bootIntegrityValidated,
errorMessage,
healthStatus,
linuxKernelVersion,
provisioningState,
systemData,
timestamp,
type
FROM azure_stack.azure_stack_hci_vm.attestation_statuses
WHERE resource_uri = '{{ resource_uri }}' -- required
;
```
</TabItem>
</Tabs>
