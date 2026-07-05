--- 
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - netapp
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>buckets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="buckets" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.buckets" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td><CopyableCode code="akvDetails" /></td>
    <td><code>object</code></td>
    <td>Specifies the Azure Key Vault settings. These are used when a) retrieving the bucket server certificate, and b) storing the bucket credentials Notes: 1. If a bucket certificate was previously provided directly using the certificateObject property, it is possible to subsequently use the Azure Key Vault for certificate management by using these 'akvDetails' properties. However, once Azure Key Vault is configured, it is no longer possible to provide the certificate directly via the certificateObject property. 2. These properties are mutually exclusive with the server.certificateObject property.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemUser" /></td>
    <td><code>object</code></td>
    <td>File System user having access to volume data. For Unix, this is the user's uid and gid. For Windows, this is the user's username. Note that the Unix and Windows user details are mutually exclusive, meaning one or other must be supplied, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The volume path mounted inside the bucket. The default is the root path '/' if no value is provided when the bucket is created.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>string</code></td>
    <td>Access permissions for the bucket. Either ReadOnly or ReadWrite. The default is ReadOnly if no value is provided during bucket creation. Known values are: "ReadOnly" and "ReadWrite". (ReadOnly, ReadWrite)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="server" /></td>
    <td><code>object</code></td>
    <td>Properties of the server managing the lifecycle of volume buckets.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The bucket credentials status. There states: "NoCredentialsSet": Access and Secret key pair have not been generated. "CredentialsExpired": Access and Secret key pair have expired. "Active": The certificate has been installed and credentials are unexpired. Known values are: "NoCredentialsSet", "CredentialsExpired", and "Active". (NoCredentialsSet, CredentialsExpired, Active)</td>
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
    <td><CopyableCode code="akvDetails" /></td>
    <td><code>object</code></td>
    <td>Specifies the Azure Key Vault settings. These are used when a) retrieving the bucket server certificate, and b) storing the bucket credentials Notes: 1. If a bucket certificate was previously provided directly using the certificateObject property, it is possible to subsequently use the Azure Key Vault for certificate management by using these 'akvDetails' properties. However, once Azure Key Vault is configured, it is no longer possible to provide the certificate directly via the certificateObject property. 2. These properties are mutually exclusive with the server.certificateObject property.</td>
</tr>
<tr>
    <td><CopyableCode code="fileSystemUser" /></td>
    <td><code>object</code></td>
    <td>File System user having access to volume data. For Unix, this is the user's uid and gid. For Windows, this is the user's username. Note that the Unix and Windows user details are mutually exclusive, meaning one or other must be supplied, but not both.</td>
</tr>
<tr>
    <td><CopyableCode code="path" /></td>
    <td><code>string</code></td>
    <td>The volume path mounted inside the bucket. The default is the root path '/' if no value is provided when the bucket is created.</td>
</tr>
<tr>
    <td><CopyableCode code="permissions" /></td>
    <td><code>string</code></td>
    <td>Access permissions for the bucket. Either ReadOnly or ReadWrite. The default is ReadOnly if no value is provided during bucket creation. Known values are: "ReadOnly" and "ReadWrite". (ReadOnly, ReadWrite)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Patching", "Updating", "Deleting", "Moving", "Failed", and "Succeeded". (Accepted, Creating, Patching, Updating, Deleting, Moving, Failed, Succeeded)</td>
</tr>
<tr>
    <td><CopyableCode code="server" /></td>
    <td><code>object</code></td>
    <td>Properties of the server managing the lifecycle of volume buckets.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The bucket credentials status. There states: "NoCredentialsSet": Access and Secret key pair have not been generated. "CredentialsExpired": Access and Secret key pair have expired. "Active": The certificate has been installed and credentials are unexpired. Known values are: "NoCredentialsSet", "CredentialsExpired", and "Active". (NoCredentialsSet, CredentialsExpired, Active)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the details of the specified volume's bucket. A bucket allows additional services, such as AI services, connect to the volume data contained in those buckets.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Describes all buckets belonging to a volume. Buckets allow additional services, such as AI services, connect to the volume data contained in those buckets.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a bucket for a volume. A bucket allows additional services, such as AI services, connect to the volume data contained in those buckets.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the details of a volume bucket.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a bucket for a volume. A bucket allows additional services, such as AI services, connect to the volume data contained in those buckets.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a volume's bucket.</td>
</tr>
<tr>
    <td><a href="#generate_credentials"><CopyableCode code="generate_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate the access key and secret key used for accessing the specified volume bucket. Also return expiry date and time of key pair (in UTC).</td>
</tr>
<tr>
    <td><a href="#generate_akv_credentials"><CopyableCode code="generate_akv_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate the access key and secret key used for accessing the specified volume bucket and store in Azure Key Vault.</td>
</tr>
<tr>
    <td><a href="#refresh_certificate"><CopyableCode code="refresh_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-pool_name"><code>pool_name</code></a>, <a href="#parameter-volume_name"><code>volume_name</code></a>, <a href="#parameter-bucket_name"><code>bucket_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation will fetch the certificate from Azure Key Vault and install it on the bucket server.</td>
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
    <td>The name of the NetApp account. Required.</td>
</tr>
<tr id="parameter-bucket_name">
    <td><CopyableCode code="bucket_name" /></td>
    <td><code>string</code></td>
    <td>The name of the bucket. Required.</td>
</tr>
<tr id="parameter-pool_name">
    <td><CopyableCode code="pool_name" /></td>
    <td><code>string</code></td>
    <td>The name of the capacity pool. Required.</td>
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
<tr id="parameter-volume_name">
    <td><CopyableCode code="volume_name" /></td>
    <td><code>string</code></td>
    <td>The name of the volume. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the details of the specified volume's bucket. A bucket allows additional services, such as AI services, connect to the volume data contained in those buckets.

```sql
SELECT
id,
name,
akvDetails,
fileSystemUser,
path,
permissions,
provisioningState,
server,
status,
systemData,
type
FROM azure_isv.netapp.buckets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND bucket_name = '{{ bucket_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Describes all buckets belonging to a volume. Buckets allow additional services, such as AI services, connect to the volume data contained in those buckets.

```sql
SELECT
id,
name,
akvDetails,
fileSystemUser,
path,
permissions,
provisioningState,
server,
status,
systemData,
type
FROM azure_isv.netapp.buckets
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND pool_name = '{{ pool_name }}' -- required
AND volume_name = '{{ volume_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates a bucket for a volume. A bucket allows additional services, such as AI services, connect to the volume data contained in those buckets.

```sql
INSERT INTO azure_isv.netapp.buckets (
properties,
resource_group_name,
account_name,
pool_name,
volume_name,
bucket_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ pool_name }}',
'{{ volume_name }}',
'{{ bucket_name }}',
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
- name: buckets
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the buckets resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the buckets resource.
    - name: pool_name
      value: "{{ pool_name }}"
      description: Required parameter for the buckets resource.
    - name: volume_name
      value: "{{ volume_name }}"
      description: Required parameter for the buckets resource.
    - name: bucket_name
      value: "{{ bucket_name }}"
      description: Required parameter for the buckets resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the buckets resource.
    - name: properties
      description: |
        Bucket properties.
      value:
        path: "{{ path }}"
        fileSystemUser:
          nfsUser:
            userId: {{ userId }}
            groupId: {{ groupId }}
          cifsUser:
            username: "{{ username }}"
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        server:
          fqdn: "{{ fqdn }}"
          certificateCommonName: "{{ certificateCommonName }}"
          certificateExpiryDate: "{{ certificateExpiryDate }}"
          ipAddress: "{{ ipAddress }}"
          certificateObject: "{{ certificateObject }}"
          onCertificateConflictAction: "{{ onCertificateConflictAction }}"
        permissions: "{{ permissions }}"
        akvDetails:
          certificateAkvDetails:
            certificateKeyVaultUri: "{{ certificateKeyVaultUri }}"
            certificateName: "{{ certificateName }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
          credentialsAkvDetails:
            credentialsKeyVaultUri: "{{ credentialsKeyVaultUri }}"
            secretName: "{{ secretName }}"
            userAssignedIdentity: "{{ userAssignedIdentity }}"
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

Updates the details of a volume bucket.

```sql
UPDATE azure_isv.netapp.buckets
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND bucket_name = '{{ bucket_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Creates or updates a bucket for a volume. A bucket allows additional services, such as AI services, connect to the volume data contained in those buckets.

```sql
REPLACE azure_isv.netapp.buckets
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND bucket_name = '{{ bucket_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Delete a volume's bucket.

```sql
DELETE FROM azure_isv.netapp.buckets
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND pool_name = '{{ pool_name }}' --required
AND volume_name = '{{ volume_name }}' --required
AND bucket_name = '{{ bucket_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate_credentials"
    values={[
        { label: 'generate_credentials', value: 'generate_credentials' },
        { label: 'generate_akv_credentials', value: 'generate_akv_credentials' },
        { label: 'refresh_certificate', value: 'refresh_certificate' }
    ]}
>
<TabItem value="generate_credentials">

Generate the access key and secret key used for accessing the specified volume bucket. Also return expiry date and time of key pair (in UTC).

```sql
EXEC azure_isv.netapp.buckets.generate_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@bucket_name='{{ bucket_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyPairExpiryDays": {{ keyPairExpiryDays }}
}'
;
```
</TabItem>
<TabItem value="generate_akv_credentials">

Generate the access key and secret key used for accessing the specified volume bucket and store in Azure Key Vault.

```sql
EXEC azure_isv.netapp.buckets.generate_akv_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@bucket_name='{{ bucket_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keyPairExpiryDays": {{ keyPairExpiryDays }}
}'
;
```
</TabItem>
<TabItem value="refresh_certificate">

This operation will fetch the certificate from Azure Key Vault and install it on the bucket server.

```sql
EXEC azure_isv.netapp.buckets.refresh_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@pool_name='{{ pool_name }}' --required, 
@volume_name='{{ volume_name }}' --required, 
@bucket_name='{{ bucket_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
