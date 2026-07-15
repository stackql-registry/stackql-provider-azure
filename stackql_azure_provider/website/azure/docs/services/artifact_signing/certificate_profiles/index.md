--- 
title: certificate_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_profiles
  - artifact_signing
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

Creates, updates, deletes, gets or lists a <code>certificate_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.artifact_signing.certificate_profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_code_signing_account', value: 'list_by_code_signing_account' }
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
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>List of renewed certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="identityValidationId" /></td>
    <td><code>string</code></td>
    <td>Identity validation id used for the certificate subject name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="includeCity" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include L in the certificate subject name. Applicable only for private trust, private trust ci profile types.</td>
</tr>
<tr>
    <td><CopyableCode code="includeCountry" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include C in the certificate subject name. Applicable only for private trust, private trust ci profile types.</td>
</tr>
<tr>
    <td><CopyableCode code="includePostalCode" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include PC in the certificate subject name.</td>
</tr>
<tr>
    <td><CopyableCode code="includeState" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include S in the certificate subject name. Applicable only for private trust, private trust ci profile types.</td>
</tr>
<tr>
    <td><CopyableCode code="includeStreetAddress" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include STREET in the certificate subject name.</td>
</tr>
<tr>
    <td><CopyableCode code="profileType" /></td>
    <td><code>string</code></td>
    <td>Profile type of the certificate. Required. Known values are: "PublicTrust", "PrivateTrust", "PrivateTrustCIPolicy", "VBSEnclave", and "PublicTrustTest". (PublicTrust, PrivateTrust, PrivateTrustCIPolicy, VBSEnclave, PublicTrustTest)</td>
</tr>
<tr>
    <td><CopyableCode code="programType" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the resource is intended for a specific usage scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the current operation on certificate profile. Known values are: "Succeeded", "Failed", "Canceled", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the certificate profile. Known values are: "Active", "Disabled", and "Suspended". (Active, Disabled, Suspended)</td>
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
<TabItem value="list_by_code_signing_account">

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
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>List of renewed certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="identityValidationId" /></td>
    <td><code>string</code></td>
    <td>Identity validation id used for the certificate subject name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="includeCity" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include L in the certificate subject name. Applicable only for private trust, private trust ci profile types.</td>
</tr>
<tr>
    <td><CopyableCode code="includeCountry" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include C in the certificate subject name. Applicable only for private trust, private trust ci profile types.</td>
</tr>
<tr>
    <td><CopyableCode code="includePostalCode" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include PC in the certificate subject name.</td>
</tr>
<tr>
    <td><CopyableCode code="includeState" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include S in the certificate subject name. Applicable only for private trust, private trust ci profile types.</td>
</tr>
<tr>
    <td><CopyableCode code="includeStreetAddress" /></td>
    <td><code>boolean</code></td>
    <td>Whether to include STREET in the certificate subject name.</td>
</tr>
<tr>
    <td><CopyableCode code="profileType" /></td>
    <td><code>string</code></td>
    <td>Profile type of the certificate. Required. Known values are: "PublicTrust", "PrivateTrust", "PrivateTrustCIPolicy", "VBSEnclave", and "PublicTrustTest". (PublicTrust, PrivateTrust, PrivateTrustCIPolicy, VBSEnclave, PublicTrustTest)</td>
</tr>
<tr>
    <td><CopyableCode code="programType" /></td>
    <td><code>string</code></td>
    <td>Indicates whether the resource is intended for a specific usage scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the current operation on certificate profile. Known values are: "Succeeded", "Failed", "Canceled", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the certificate profile. Known values are: "Active", "Disabled", and "Suspended". (Active, Disabled, Suspended)</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get details of a certificate profile.</td>
</tr>
<tr>
    <td><a href="#list_by_code_signing_account"><CopyableCode code="list_by_code_signing_account" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List certificate profiles under an artifact signing account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a certificate profile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a certificate profile.</td>
</tr>
<tr>
    <td><a href="#revoke_certificates"><CopyableCode code="revoke_certificates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-revokeCertificates"><code>revokeCertificates</code></a></td>
    <td></td>
    <td>Revokes certificates under a certificate profile.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>Artifact Signing account name. Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>Certificate profile name. Required.</td>
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
        { label: 'list_by_code_signing_account', value: 'list_by_code_signing_account' }
    ]}
>
<TabItem value="get">

Get details of a certificate profile.

```sql
SELECT
id,
name,
certificates,
identityValidationId,
includeCity,
includeCountry,
includePostalCode,
includeState,
includeStreetAddress,
profileType,
programType,
provisioningState,
status,
systemData,
type
FROM azure.artifact_signing.certificate_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_code_signing_account">

List certificate profiles under an artifact signing account.

```sql
SELECT
id,
name,
certificates,
identityValidationId,
includeCity,
includeCountry,
includePostalCode,
includeState,
includeStreetAddress,
profileType,
programType,
provisioningState,
status,
systemData,
type
FROM azure.artifact_signing.certificate_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a certificate profile.

```sql
INSERT INTO azure.artifact_signing.certificate_profiles (
properties,
resource_group_name,
account_name,
profile_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ profile_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: certificate_profiles
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the certificate_profiles resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the certificate_profiles resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the certificate_profiles resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the certificate_profiles resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        profileType: "{{ profileType }}"
        includeStreetAddress: {{ includeStreetAddress }}
        includeCity: {{ includeCity }}
        includeState: {{ includeState }}
        includeCountry: {{ includeCountry }}
        includePostalCode: {{ includePostalCode }}
        identityValidationId: "{{ identityValidationId }}"
        programType: "{{ programType }}"
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        certificates:
          - serialNumber: "{{ serialNumber }}"
            enhancedKeyUsage: "{{ enhancedKeyUsage }}"
            subjectName: "{{ subjectName }}"
            thumbprint: "{{ thumbprint }}"
            createdDate: "{{ createdDate }}"
            expiryDate: "{{ expiryDate }}"
            status: "{{ status }}"
            revocation:
              requestedAt: "{{ requestedAt }}"
              effectiveAt: "{{ effectiveAt }}"
              reason: "{{ reason }}"
              remarks: "{{ remarks }}"
              status: "{{ status }}"
              failureReason: "{{ failureReason }}"
`}</CodeBlock>

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

Delete a certificate profile.

```sql
DELETE FROM azure.artifact_signing.certificate_profiles
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="revoke_certificates"
    values={[
        { label: 'revoke_certificates', value: 'revoke_certificates' }
    ]}
>
<TabItem value="revoke_certificates">

Revokes certificates under a certificate profile.

```sql
EXEC azure.artifact_signing.certificate_profiles.revoke_certificates 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"revokeCertificates": "{{ revokeCertificates }}"
}'
;
```
</TabItem>
</Tabs>
