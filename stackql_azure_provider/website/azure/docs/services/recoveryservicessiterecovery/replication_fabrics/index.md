--- 
title: replication_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_fabrics
  - recoveryservicessiterecovery
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

Creates, updates, deletes, gets or lists a <code>replication_fabrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_fabrics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicessiterecovery.replication_fabrics" /></td></tr>
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
    <td><CopyableCode code="bcdrState" /></td>
    <td><code>string</code></td>
    <td>BCDR state of the fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="customDetails" /></td>
    <td><code>object</code></td>
    <td>Fabric specific settings.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionDetails" /></td>
    <td><code>object</code></td>
    <td>Encryption details for the fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Health of fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrorDetails" /></td>
    <td><code>array</code></td>
    <td>Fabric health error details.</td>
</tr>
<tr>
    <td><CopyableCode code="internalIdentifier" /></td>
    <td><code>string</code></td>
    <td>Dra Registration Id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="rolloverEncryptionDetails" /></td>
    <td><code>object</code></td>
    <td>Rollover encryption details for the fabric.</td>
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
    <td><CopyableCode code="bcdrState" /></td>
    <td><code>string</code></td>
    <td>BCDR state of the fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="customDetails" /></td>
    <td><code>object</code></td>
    <td>Fabric specific settings.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionDetails" /></td>
    <td><code>object</code></td>
    <td>Encryption details for the fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Health of fabric.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrorDetails" /></td>
    <td><code>array</code></td>
    <td>Fabric health error details.</td>
</tr>
<tr>
    <td><CopyableCode code="internalIdentifier" /></td>
    <td><code>string</code></td>
    <td>Dra Registration Id.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="rolloverEncryptionDetails" /></td>
    <td><code>object</code></td>
    <td>Rollover encryption details for the fabric.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets the details of an ASR fabric. Gets the details of an Azure Site Recovery fabric.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of ASR fabrics. Gets a list of the Azure Site Recovery fabrics in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an Azure Site Recovery fabric. The operation to create an Azure Site Recovery fabric (for e.g. Hyper-V site).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the site. The operation to delete or remove an Azure Site Recovery fabric.</td>
</tr>
<tr>
    <td><a href="#purge"><CopyableCode code="purge" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Purges the site. The operation to purge(force delete) an Azure Site Recovery fabric.</td>
</tr>
<tr>
    <td><a href="#check_consistency"><CopyableCode code="check_consistency" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the consistency of the ASR fabric. The operation to perform a consistency check on the fabric.</td>
</tr>
<tr>
    <td><a href="#migrate_to_aad"><CopyableCode code="migrate_to_aad" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Migrates the site to AAD. The operation to migrate an Azure Site Recovery fabric to AAD.</td>
</tr>
<tr>
    <td><a href="#reassociate_gateway"><CopyableCode code="reassociate_gateway" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Perform failover of the process server. The operation to move replications from a process server to another process server.</td>
</tr>
<tr>
    <td><a href="#renew_certificate"><CopyableCode code="renew_certificate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Renews certificate for the fabric. Renews the connection certificate for the ASR replication fabric.</td>
</tr>
<tr>
    <td><a href="#remove_infra"><CopyableCode code="remove_infra" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Removes the appliance's infrastructure under the fabric. Removes the appliance's infrastructure under the fabric.</td>
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
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>Fabric name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the recovery services vault. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>OData filter options. Default value is None.</td>
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

Gets the details of an ASR fabric. Gets the details of an Azure Site Recovery fabric.

```sql
SELECT
id,
name,
bcdrState,
customDetails,
encryptionDetails,
friendlyName,
health,
healthErrorDetails,
internalIdentifier,
location,
rolloverEncryptionDetails,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_fabrics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list">

Gets the list of ASR fabrics. Gets a list of the Azure Site Recovery fabrics in the vault.

```sql
SELECT
id,
name,
bcdrState,
customDetails,
encryptionDetails,
friendlyName,
health,
healthErrorDetails,
internalIdentifier,
location,
rolloverEncryptionDetails,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_fabrics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Creates an Azure Site Recovery fabric. The operation to create an Azure Site Recovery fabric (for e.g. Hyper-V site).

```sql
INSERT INTO azure.recoveryservicessiterecovery.replication_fabrics (
properties,
resource_group_name,
resource_name,
fabric_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ fabric_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: replication_fabrics
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_fabrics resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_fabrics resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the replication_fabrics resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_fabrics resource.
    - name: properties
      description: |
        Fabric creation input.
      value:
        customDetails:
          instanceType: "{{ instanceType }}"
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

Deletes the site. The operation to delete or remove an Azure Site Recovery fabric.

```sql
DELETE FROM azure.recoveryservicessiterecovery.replication_fabrics
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="purge"
    values={[
        { label: 'purge', value: 'purge' },
        { label: 'check_consistency', value: 'check_consistency' },
        { label: 'migrate_to_aad', value: 'migrate_to_aad' },
        { label: 'reassociate_gateway', value: 'reassociate_gateway' },
        { label: 'renew_certificate', value: 'renew_certificate' },
        { label: 'remove_infra', value: 'remove_infra' }
    ]}
>
<TabItem value="purge">

Purges the site. The operation to purge(force delete) an Azure Site Recovery fabric.

```sql
EXEC azure.recoveryservicessiterecovery.replication_fabrics.purge 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_consistency">

Checks the consistency of the ASR fabric. The operation to perform a consistency check on the fabric.

```sql
EXEC azure.recoveryservicessiterecovery.replication_fabrics.check_consistency 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migrate_to_aad">

Migrates the site to AAD. The operation to migrate an Azure Site Recovery fabric to AAD.

```sql
EXEC azure.recoveryservicessiterecovery.replication_fabrics.migrate_to_aad 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="reassociate_gateway">

Perform failover of the process server. The operation to move replications from a process server to another process server.

```sql
EXEC azure.recoveryservicessiterecovery.replication_fabrics.reassociate_gateway 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="renew_certificate">

Renews certificate for the fabric. Renews the connection certificate for the ASR replication fabric.

```sql
EXEC azure.recoveryservicessiterecovery.replication_fabrics.renew_certificate 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="remove_infra">

Removes the appliance's infrastructure under the fabric. Removes the appliance's infrastructure under the fabric.

```sql
EXEC azure.recoveryservicessiterecovery.replication_fabrics.remove_infra 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
