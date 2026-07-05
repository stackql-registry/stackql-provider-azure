--- 
title: managed_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_certificates
  - appcontainers
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

Creates, updates, deletes, gets or lists a <code>managed_certificates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_certificates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appcontainers.managed_certificates" /></td></tr>
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
    <td><CopyableCode code="domainControlValidation" /></td>
    <td><code>string</code></td>
    <td>Selected type of domain control validation for managed certificates. Known values are: "CNAME", "HTTP", and "TXT". (CNAME, HTTP, TXT)</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td>Any error occurred during the certificate provision.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the certificate. Known values are: "Succeeded", "Failed", "Canceled", "DeleteFailed", "Pending", and "Deleting". (Succeeded, Failed, Canceled, DeleteFailed, Pending, Deleting)</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationToken" /></td>
    <td><code>string</code></td>
    <td>A TXT token used for DNS TXT domain control validation when issuing this type of managed certificates.</td>
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
    <td><CopyableCode code="domainControlValidation" /></td>
    <td><code>string</code></td>
    <td>Selected type of domain control validation for managed certificates. Known values are: "CNAME", "HTTP", and "TXT". (CNAME, HTTP, TXT)</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>string</code></td>
    <td>Any error occurred during the certificate provision.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the certificate. Known values are: "Succeeded", "Failed", "Canceled", "DeleteFailed", "Pending", and "Deleting". (Succeeded, Failed, Canceled, DeleteFailed, Pending, Deleting)</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationToken" /></td>
    <td><code>string</code></td>
    <td>A TXT token used for DNS TXT domain control validation when issuing this type of managed certificates.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-managed_certificate_name"><code>managed_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the specified Managed Certificate. Get the specified Managed Certificate.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Managed Certificates in a given managed environment. Get the Managed Certificates in a given managed environment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-managed_certificate_name"><code>managed_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or Update a Managed Certificate. Create or Update a Managed Certificate.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-managed_certificate_name"><code>managed_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update tags of a managed certificate. Patches a managed certificate. Oly patching of tags is supported.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-managed_certificate_name"><code>managed_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or Update a Managed Certificate. Create or Update a Managed Certificate.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-environment_name"><code>environment_name</code></a>, <a href="#parameter-managed_certificate_name"><code>managed_certificate_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Managed Certificate. Deletes the specified Managed Certificate.</td>
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
<tr id="parameter-environment_name">
    <td><CopyableCode code="environment_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Environment. Required.</td>
</tr>
<tr id="parameter-managed_certificate_name">
    <td><CopyableCode code="managed_certificate_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Managed Certificate. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get the specified Managed Certificate. Get the specified Managed Certificate.

```sql
SELECT
id,
name,
domainControlValidation,
error,
location,
provisioningState,
subjectName,
systemData,
tags,
type,
validationToken
FROM azure.appcontainers.managed_certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND environment_name = '{{ environment_name }}' -- required
AND managed_certificate_name = '{{ managed_certificate_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the Managed Certificates in a given managed environment. Get the Managed Certificates in a given managed environment.

```sql
SELECT
id,
name,
domainControlValidation,
error,
location,
provisioningState,
subjectName,
systemData,
tags,
type,
validationToken
FROM azure.appcontainers.managed_certificates
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND environment_name = '{{ environment_name }}' -- required
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

Create or Update a Managed Certificate. Create or Update a Managed Certificate.

```sql
INSERT INTO azure.appcontainers.managed_certificates (
tags,
location,
properties,
resource_group_name,
environment_name,
managed_certificate_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ environment_name }}',
'{{ managed_certificate_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: managed_certificates
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the managed_certificates resource.
    - name: environment_name
      value: "{{ environment_name }}"
      description: Required parameter for the managed_certificates resource.
    - name: managed_certificate_name
      value: "{{ managed_certificate_name }}"
      description: Required parameter for the managed_certificates resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_certificates resource.
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
        provisioningState: "{{ provisioningState }}"
        subjectName: "{{ subjectName }}"
        error: "{{ error }}"
        domainControlValidation: "{{ domainControlValidation }}"
        validationToken: "{{ validationToken }}"
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

Update tags of a managed certificate. Patches a managed certificate. Oly patching of tags is supported.

```sql
UPDATE azure.appcontainers.managed_certificates
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND managed_certificate_name = '{{ managed_certificate_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or Update a Managed Certificate. Create or Update a Managed Certificate.

```sql
REPLACE azure.appcontainers.managed_certificates
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND managed_certificate_name = '{{ managed_certificate_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Deletes the specified Managed Certificate. Deletes the specified Managed Certificate.

```sql
DELETE FROM azure.appcontainers.managed_certificates
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND environment_name = '{{ environment_name }}' --required
AND managed_certificate_name = '{{ managed_certificate_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
