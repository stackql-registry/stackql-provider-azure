--- 
title: dps_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - dps_certificate
  - iot_hub_provisioning_services
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

Creates, updates, deletes, gets or lists a <code>dps_certificate</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dps_certificate" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub_provisioning_services.dps_certificate" /></td></tr>
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
    <td><CopyableCode code="certificate" /></td>
    <td><code>string (byte)</code></td>
    <td>base-64 representation of X509 certificate .cer file or just .pem file content.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The certificate's creation date and time.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag.</td>
</tr>
<tr>
    <td><CopyableCode code="expiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>The certificate's expiration date and time.</td>
</tr>
<tr>
    <td><CopyableCode code="isVerified" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether certificate has been verified.</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td>The certificate's subject name.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>The certificate's thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The certificate's last update date and time.</td>
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
    <td><CopyableCode code="certificate" /></td>
    <td><code>string (byte)</code></td>
    <td>base-64 representation of X509 certificate .cer file or just .pem file content.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The certificate's creation date and time.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The entity tag.</td>
</tr>
<tr>
    <td><CopyableCode code="expiry" /></td>
    <td><code>string (date-time)</code></td>
    <td>The certificate's expiration date and time.</td>
</tr>
<tr>
    <td><CopyableCode code="isVerified" /></td>
    <td><code>boolean</code></td>
    <td>Determines whether certificate has been verified.</td>
</tr>
<tr>
    <td><CopyableCode code="subject" /></td>
    <td><code>string</code></td>
    <td>The certificate's subject name.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="thumbprint" /></td>
    <td><code>string</code></td>
    <td>The certificate's thumbprint.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The certificate's last update date and time.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the certificate from the provisioning service.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all the certificates tied to the provisioning service.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add new certificate or update an existing certificate.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Add new certificate or update an existing certificate.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-certificate.name"><code>certificate.name</code></a>, <a href="#parameter-certificate.rawBytes"><code>certificate.rawBytes</code></a>, <a href="#parameter-certificate.isVerified"><code>certificate.isVerified</code></a>, <a href="#parameter-certificate.purpose"><code>certificate.purpose</code></a>, <a href="#parameter-certificate.created"><code>certificate.created</code></a>, <a href="#parameter-certificate.lastUpdated"><code>certificate.lastUpdated</code></a>, <a href="#parameter-certificate.hasPrivateKey"><code>certificate.hasPrivateKey</code></a>, <a href="#parameter-certificate.nonce"><code>certificate.nonce</code></a></td>
    <td>Deletes the specified certificate associated with the Provisioning Service.</td>
</tr>
<tr>
    <td><a href="#generate_verification_code"><CopyableCode code="generate_verification_code" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-certificate.name"><code>certificate.name</code></a>, <a href="#parameter-certificate.rawBytes"><code>certificate.rawBytes</code></a>, <a href="#parameter-certificate.isVerified"><code>certificate.isVerified</code></a>, <a href="#parameter-certificate.purpose"><code>certificate.purpose</code></a>, <a href="#parameter-certificate.created"><code>certificate.created</code></a>, <a href="#parameter-certificate.lastUpdated"><code>certificate.lastUpdated</code></a>, <a href="#parameter-certificate.hasPrivateKey"><code>certificate.hasPrivateKey</code></a>, <a href="#parameter-certificate.nonce"><code>certificate.nonce</code></a></td>
    <td>Generate verification code for Proof of Possession.</td>
</tr>
<tr>
    <td><a href="#verify_certificate"><CopyableCode code="verify_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-provisioning_service_name"><code>provisioning_service_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-certificate.name"><code>certificate.name</code></a>, <a href="#parameter-certificate.rawBytes"><code>certificate.rawBytes</code></a>, <a href="#parameter-certificate.isVerified"><code>certificate.isVerified</code></a>, <a href="#parameter-certificate.purpose"><code>certificate.purpose</code></a>, <a href="#parameter-certificate.created"><code>certificate.created</code></a>, <a href="#parameter-certificate.lastUpdated"><code>certificate.lastUpdated</code></a>, <a href="#parameter-certificate.hasPrivateKey"><code>certificate.hasPrivateKey</code></a>, <a href="#parameter-certificate.nonce"><code>certificate.nonce</code></a></td>
    <td>Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate.</td>
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
    <td>Name of the certificate to retrieve. Required.</td>
</tr>
<tr id="parameter-provisioning_service_name">
    <td><CopyableCode code="provisioning_service_name" /></td>
    <td><code>string</code></td>
    <td>Name of the provisioning service to retrieve. Required.</td>
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
<tr id="parameter-certificate.created">
    <td><CopyableCode code="certificate.created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time the certificate is created. Default value is None.</td>
</tr>
<tr id="parameter-certificate.hasPrivateKey">
    <td><CopyableCode code="certificate.hasPrivateKey" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the certificate contains private key. Default value is None.</td>
</tr>
<tr id="parameter-certificate.isVerified">
    <td><CopyableCode code="certificate.isVerified" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the certificate has been verified by owner of the private key. Default value is None.</td>
</tr>
<tr id="parameter-certificate.lastUpdated">
    <td><CopyableCode code="certificate.lastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>Certificate last updated time. Default value is None.</td>
</tr>
<tr id="parameter-certificate.name">
    <td><CopyableCode code="certificate.name" /></td>
    <td><code>string</code></td>
    <td>Common Name for the certificate. Default value is None.</td>
</tr>
<tr id="parameter-certificate.nonce">
    <td><CopyableCode code="certificate.nonce" /></td>
    <td><code>string</code></td>
    <td>Random number generated to indicate Proof of Possession. Default value is None.</td>
</tr>
<tr id="parameter-certificate.purpose">
    <td><CopyableCode code="certificate.purpose" /></td>
    <td><code>string</code></td>
    <td>Describe the purpose of the certificate. Known values are: "clientAuthentication" and "serverAuthentication". Default value is None.</td>
</tr>
<tr id="parameter-certificate.rawBytes">
    <td><CopyableCode code="certificate.rawBytes" /></td>
    <td><code>string (byte)</code></td>
    <td>Raw data of certificate. Default value is None.</td>
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

Get the certificate from the provisioning service.

```sql
SELECT
id,
name,
certificate,
created,
etag,
expiry,
isVerified,
subject,
systemData,
thumbprint,
type,
updated
FROM azure.iot_hub_provisioning_services.dps_certificate
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND provisioning_service_name = '{{ provisioning_service_name }}' -- required
AND certificate_name = '{{ certificate_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all the certificates tied to the provisioning service.

```sql
SELECT
id,
name,
certificate,
created,
etag,
expiry,
isVerified,
subject,
systemData,
thumbprint,
type,
updated
FROM azure.iot_hub_provisioning_services.dps_certificate
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND provisioning_service_name = '{{ provisioning_service_name }}' -- required
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

Add new certificate or update an existing certificate.

```sql
INSERT INTO azure.iot_hub_provisioning_services.dps_certificate (
properties,
resource_group_name,
provisioning_service_name,
certificate_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ provisioning_service_name }}',
'{{ certificate_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: dps_certificate
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dps_certificate resource.
    - name: provisioning_service_name
      value: "{{ provisioning_service_name }}"
      description: Required parameter for the dps_certificate resource.
    - name: certificate_name
      value: "{{ certificate_name }}"
      description: Required parameter for the dps_certificate resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dps_certificate resource.
    - name: properties
      description: |
        properties of a certificate.
      value:
        subject: "{{ subject }}"
        expiry: "{{ expiry }}"
        thumbprint: "{{ thumbprint }}"
        isVerified: {{ isVerified }}
        certificate: "{{ certificate }}"
        created: "{{ created }}"
        updated: "{{ updated }}"
`}</CodeBlock>

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

Add new certificate or update an existing certificate.

```sql
REPLACE azure.iot_hub_provisioning_services.dps_certificate
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND provisioning_service_name = '{{ provisioning_service_name }}' --required
AND certificate_name = '{{ certificate_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Deletes the specified certificate associated with the Provisioning Service.

```sql
DELETE FROM azure.iot_hub_provisioning_services.dps_certificate
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND provisioning_service_name = '{{ provisioning_service_name }}' --required
AND certificate_name = '{{ certificate_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND certificate.name = '{{ certificate.name }}'
AND certificate.rawBytes = '{{ certificate.rawBytes }}'
AND certificate.isVerified = '{{ certificate.isVerified }}'
AND certificate.purpose = '{{ certificate.purpose }}'
AND certificate.created = '{{ certificate.created }}'
AND certificate.lastUpdated = '{{ certificate.lastUpdated }}'
AND certificate.hasPrivateKey = '{{ certificate.hasPrivateKey }}'
AND certificate.nonce = '{{ certificate.nonce }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate_verification_code"
    values={[
        { label: 'generate_verification_code', value: 'generate_verification_code' },
        { label: 'verify_certificate', value: 'verify_certificate' }
    ]}
>
<TabItem value="generate_verification_code">

Generate verification code for Proof of Possession.

```sql
EXEC azure.iot_hub_provisioning_services.dps_certificate.generate_verification_code 
@resource_group_name='{{ resource_group_name }}' --required, 
@provisioning_service_name='{{ provisioning_service_name }}' --required, 
@certificate_name='{{ certificate_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@certificate.name='{{ certificate.name }}', 
@certificate.rawBytes='{{ certificate.rawBytes }}', 
@certificate.isVerified={{ certificate.isVerified }}, 
@certificate.purpose='{{ certificate.purpose }}', 
@certificate.created='{{ certificate.created }}', 
@certificate.lastUpdated='{{ certificate.lastUpdated }}', 
@certificate.hasPrivateKey={{ certificate.hasPrivateKey }}, 
@certificate.nonce='{{ certificate.nonce }}'
;
```
</TabItem>
<TabItem value="verify_certificate">

Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate.

```sql
EXEC azure.iot_hub_provisioning_services.dps_certificate.verify_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@provisioning_service_name='{{ provisioning_service_name }}' --required, 
@certificate_name='{{ certificate_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@certificate.name='{{ certificate.name }}', 
@certificate.rawBytes='{{ certificate.rawBytes }}', 
@certificate.isVerified={{ certificate.isVerified }}, 
@certificate.purpose='{{ certificate.purpose }}', 
@certificate.created='{{ certificate.created }}', 
@certificate.lastUpdated='{{ certificate.lastUpdated }}', 
@certificate.hasPrivateKey={{ certificate.hasPrivateKey }}, 
@certificate.nonce='{{ certificate.nonce }}' 
@@json=
'{
"certificate": "{{ certificate }}"
}'
;
```
</TabItem>
</Tabs>
