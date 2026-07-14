--- 
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - iot_hub
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.certificates" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_iot_hub', value: 'list_by_iot_hub' }
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
    <td><code>string</code></td>
    <td>The certificate content.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>The certificate's create date and time.</td>
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
    <td><CopyableCode code="policyResourceId" /></td>
    <td><code>string</code></td>
    <td>The reference to policy stored in Azure Device Registry (ADR).</td>
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
<TabItem value="list_by_iot_hub">

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
    <td><CopyableCode code="value" /></td>
    <td><code>array</code></td>
    <td>The array of Certificate objects.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the certificate. Returns the certificate.</td>
</tr>
<tr>
    <td><a href="#list_by_iot_hub"><CopyableCode code="list_by_iot_hub" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the certificate list. Returns the list of certificates.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upload the certificate to the IoT hub. Adds new or replaces existing certificate.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Upload the certificate to the IoT hub. Adds new or replaces existing certificate.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete an X509 certificate. Deletes an existing X509 certificate or does nothing if it does not exist.</td>
</tr>
<tr>
    <td><a href="#generate_verification_code"><CopyableCode code="generate_verification_code" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate verification code for proof of possession flow. Generates verification code for proof of possession flow. The verification code will be used to generate a leaf certificate.</td>
</tr>
<tr>
    <td><a href="#verify"><CopyableCode code="verify" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-certificate_name"><code>certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Verify certificate's private key possession. Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate.</td>
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
    <td>The name of the certificate. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the IoT hub. Required.</td>
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
        { label: 'list_by_iot_hub', value: 'list_by_iot_hub' }
    ]}
>
<TabItem value="get">

Get the certificate. Returns the certificate.

```sql
SELECT
id,
name,
certificate,
created,
etag,
expiry,
isVerified,
policyResourceId,
subject,
systemData,
thumbprint,
type,
updated
FROM azure.iot_hub.certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND certificate_name = '{{ certificate_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_iot_hub">

Get the certificate list. Returns the list of certificates.

```sql
SELECT
value
FROM azure.iot_hub.certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Upload the certificate to the IoT hub. Adds new or replaces existing certificate.

```sql
INSERT INTO azure.iot_hub.certificates (
properties,
resource_group_name,
resource_name,
certificate_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
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
- name: certificates
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the certificates resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the certificates resource.
    - name: certificate_name
      value: "{{ certificate_name }}"
      description: Required parameter for the certificates resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the certificates resource.
    - name: properties
      description: |
        The description of an X509 CA Certificate.
      value:
        subject: "{{ subject }}"
        expiry: "{{ expiry }}"
        thumbprint: "{{ thumbprint }}"
        isVerified: {{ isVerified }}
        created: "{{ created }}"
        updated: "{{ updated }}"
        certificate: "{{ certificate }}"
        policyResourceId: "{{ policyResourceId }}"
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

Upload the certificate to the IoT hub. Adds new or replaces existing certificate.

```sql
REPLACE azure.iot_hub.certificates
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
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

Delete an X509 certificate. Deletes an existing X509 certificate or does nothing if it does not exist.

```sql
DELETE FROM azure.iot_hub.certificates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND certificate_name = '{{ certificate_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="generate_verification_code"
    values={[
        { label: 'generate_verification_code', value: 'generate_verification_code' },
        { label: 'verify', value: 'verify' }
    ]}
>
<TabItem value="generate_verification_code">

Generate verification code for proof of possession flow. Generates verification code for proof of possession flow. The verification code will be used to generate a leaf certificate.

```sql
EXEC azure.iot_hub.certificates.generate_verification_code 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@certificate_name='{{ certificate_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="verify">

Verify certificate's private key possession. Verifies the certificate's private key possession by providing the leaf cert issued by the verifying pre uploaded certificate.

```sql
EXEC azure.iot_hub.certificates.verify 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@certificate_name='{{ certificate_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"certificate": "{{ certificate }}"
}'
;
```
</TabItem>
</Tabs>
