--- 
title: certificate_object_local_rulestack
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_object_local_rulestack
  - paloaltonetworksngfw
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

Creates, updates, deletes, gets or lists a <code>certificate_object_local_rulestack</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_object_local_rulestack" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworksngfw.certificate_object_local_rulestack" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_local_rulestacks', value: 'list_by_local_rulestacks' }
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
    <td><CopyableCode code="auditComment" /></td>
    <td><code>string</code></td>
    <td>comment for this object.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateSelfSigned" /></td>
    <td><code>string</code></td>
    <td>use certificate self signed. Required. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="certificateSignerResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of certificate signer, to be populated only when certificateSelfSigned is false.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>user description for this object.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>read only string representing last create or update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
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
<TabItem value="list_by_local_rulestacks">

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
    <td><CopyableCode code="auditComment" /></td>
    <td><code>string</code></td>
    <td>comment for this object.</td>
</tr>
<tr>
    <td><CopyableCode code="certificateSelfSigned" /></td>
    <td><code>string</code></td>
    <td>use certificate self signed. Required. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="certificateSignerResourceId" /></td>
    <td><code>string</code></td>
    <td>Resource Id of certificate signer, to be populated only when certificateSelfSigned is false.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>user description for this object.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>read only string representing last create or update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a CertificateObjectLocalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#list_by_local_rulestacks"><CopyableCode code="list_by_local_rulestacks" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List CertificateObjectLocalRulestackResource resources by LocalRulestacks.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a CertificateObjectLocalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a CertificateObjectLocalRulestackResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-local_rulestack_name"><code>local_rulestack_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a CertificateObjectLocalRulestackResource.</td>
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
<tr id="parameter-local_rulestack_name">
    <td><CopyableCode code="local_rulestack_name" /></td>
    <td><code>string</code></td>
    <td>LocalRulestack resource name. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>certificate name. Required.</td>
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
        { label: 'list_by_local_rulestacks', value: 'list_by_local_rulestacks' }
    ]}
>
<TabItem value="get">

Get a CertificateObjectLocalRulestackResource.

```sql
SELECT
id,
name,
auditComment,
certificateSelfSigned,
certificateSignerResourceId,
description,
etag,
provisioningState,
systemData,
type
FROM azure_isv.paloaltonetworksngfw.certificate_object_local_rulestack
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND local_rulestack_name = '{{ local_rulestack_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_local_rulestacks">

List CertificateObjectLocalRulestackResource resources by LocalRulestacks.

```sql
SELECT
id,
name,
auditComment,
certificateSelfSigned,
certificateSignerResourceId,
description,
etag,
provisioningState,
systemData,
type
FROM azure_isv.paloaltonetworksngfw.certificate_object_local_rulestack
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND local_rulestack_name = '{{ local_rulestack_name }}' -- required
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

Create a CertificateObjectLocalRulestackResource.

```sql
INSERT INTO azure_isv.paloaltonetworksngfw.certificate_object_local_rulestack (
properties,
resource_group_name,
local_rulestack_name,
name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ local_rulestack_name }}',
'{{ name }}',
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
- name: certificate_object_local_rulestack
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the certificate_object_local_rulestack resource.
    - name: local_rulestack_name
      value: "{{ local_rulestack_name }}"
      description: Required parameter for the certificate_object_local_rulestack resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the certificate_object_local_rulestack resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the certificate_object_local_rulestack resource.
    - name: properties
      value:
        certificateSignerResourceId: "{{ certificateSignerResourceId }}"
        certificateSelfSigned: "{{ certificateSelfSigned }}"
        auditComment: "{{ auditComment }}"
        description: "{{ description }}"
        etag: "{{ etag }}"
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

Create a CertificateObjectLocalRulestackResource.

```sql
REPLACE azure_isv.paloaltonetworksngfw.certificate_object_local_rulestack
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND local_rulestack_name = '{{ local_rulestack_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
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

Delete a CertificateObjectLocalRulestackResource.

```sql
DELETE FROM azure_isv.paloaltonetworksngfw.certificate_object_local_rulestack
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND local_rulestack_name = '{{ local_rulestack_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
