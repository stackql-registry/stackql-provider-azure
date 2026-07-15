--- 
title: ledger
hide_title: false
hide_table_of_contents: false
keywords:
  - ledger
  - confidential_ledger
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

Creates, updates, deletes, gets or lists a <code>ledger</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="ledger" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.confidential_ledger.ledger" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="aadBasedSecurityPrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of all AAD based Security Principals.</td>
</tr>
<tr>
    <td><CopyableCode code="certBasedSecurityPrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of all cert based Security Principals.</td>
</tr>
<tr>
    <td><CopyableCode code="identityServiceUri" /></td>
    <td><code>string</code></td>
    <td>Endpoint for accessing network identity.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerInternalNamespace" /></td>
    <td><code>string</code></td>
    <td>Internal namespace for the Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerName" /></td>
    <td><code>string</code></td>
    <td>Unique name for the Confidential Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerType" /></td>
    <td><code>string</code></td>
    <td>Type of Confidential Ledger. Known values are: "Unknown", "Public", and "Private".</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerUri" /></td>
    <td><code>string</code></td>
    <td>Endpoint for calling Ledger Service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure location where the Confidential Ledger is running.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of Ledger Resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Additional tags for Confidential Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="aadBasedSecurityPrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of all AAD based Security Principals.</td>
</tr>
<tr>
    <td><CopyableCode code="certBasedSecurityPrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of all cert based Security Principals.</td>
</tr>
<tr>
    <td><CopyableCode code="identityServiceUri" /></td>
    <td><code>string</code></td>
    <td>Endpoint for accessing network identity.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerInternalNamespace" /></td>
    <td><code>string</code></td>
    <td>Internal namespace for the Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerName" /></td>
    <td><code>string</code></td>
    <td>Unique name for the Confidential Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerType" /></td>
    <td><code>string</code></td>
    <td>Type of Confidential Ledger. Known values are: "Unknown", "Public", and "Private".</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerUri" /></td>
    <td><code>string</code></td>
    <td>Endpoint for calling Ledger Service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure location where the Confidential Ledger is running.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of Ledger Resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Additional tags for Confidential Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the Resource.</td>
</tr>
<tr>
    <td><CopyableCode code="aadBasedSecurityPrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of all AAD based Security Principals.</td>
</tr>
<tr>
    <td><CopyableCode code="certBasedSecurityPrincipals" /></td>
    <td><code>array</code></td>
    <td>Array of all cert based Security Principals.</td>
</tr>
<tr>
    <td><CopyableCode code="identityServiceUri" /></td>
    <td><code>string</code></td>
    <td>Endpoint for accessing network identity.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerInternalNamespace" /></td>
    <td><code>string</code></td>
    <td>Internal namespace for the Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerName" /></td>
    <td><code>string</code></td>
    <td>Unique name for the Confidential Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerType" /></td>
    <td><code>string</code></td>
    <td>Type of Confidential Ledger. Known values are: "Unknown", "Public", and "Private".</td>
</tr>
<tr>
    <td><CopyableCode code="ledgerUri" /></td>
    <td><code>string</code></td>
    <td>Endpoint for calling Ledger Service.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure location where the Confidential Ledger is running.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of Ledger Resource. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Creating", "Deleting", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Additional tags for Confidential Ledger.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ledger_name"><code>ledger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves information about a Confidential Ledger resource. Retrieves the properties of a Confidential Ledger.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves information about all Confidential Ledger resources under the given subscription and resource group. Retrieves the properties of all Confidential Ledgers.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Retrieves information about all Confidential Ledger resources under the given subscription. Retrieves the properties of all Confidential Ledgers.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ledger_name"><code>ledger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a Confidential Ledger. Creates a Confidential Ledger with the specified ledger parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ledger_name"><code>ledger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update Confidential Ledger properties. Updates properties of Confidential Ledger.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-ledger_name"><code>ledger_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Confidential Ledger resource. Deletes an existing Confidential Ledger.</td>
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
<tr id="parameter-ledger_name">
    <td><CopyableCode code="ledger_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Confidential Ledger. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the list operation. eg. $filter=ledgerType eq 'Public'. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Retrieves information about a Confidential Ledger resource. Retrieves the properties of a Confidential Ledger.

```sql
SELECT
id,
name,
aadBasedSecurityPrincipals,
certBasedSecurityPrincipals,
identityServiceUri,
ledgerInternalNamespace,
ledgerName,
ledgerType,
ledgerUri,
location,
provisioningState,
systemData,
tags,
type
FROM azure.confidential_ledger.ledger
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND ledger_name = '{{ ledger_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Retrieves information about all Confidential Ledger resources under the given subscription and resource group. Retrieves the properties of all Confidential Ledgers.

```sql
SELECT
id,
name,
aadBasedSecurityPrincipals,
certBasedSecurityPrincipals,
identityServiceUri,
ledgerInternalNamespace,
ledgerName,
ledgerType,
ledgerUri,
location,
provisioningState,
systemData,
tags,
type
FROM azure.confidential_ledger.ledger
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
;
```
</TabItem>
<TabItem value="list_by_subscription">

Retrieves information about all Confidential Ledger resources under the given subscription. Retrieves the properties of all Confidential Ledgers.

```sql
SELECT
id,
name,
aadBasedSecurityPrincipals,
certBasedSecurityPrincipals,
identityServiceUri,
ledgerInternalNamespace,
ledgerName,
ledgerType,
ledgerUri,
location,
provisioningState,
systemData,
tags,
type
FROM azure.confidential_ledger.ledger
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
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

Creates a Confidential Ledger. Creates a Confidential Ledger with the specified ledger parameters.

```sql
INSERT INTO azure.confidential_ledger.ledger (
location,
tags,
properties,
resource_group_name,
ledger_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ ledger_name }}',
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
- name: ledger
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the ledger resource.
    - name: ledger_name
      value: "{{ ledger_name }}"
      description: Required parameter for the ledger resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the ledger resource.
    - name: location
      value: "{{ location }}"
      description: |
        The Azure location where the Confidential Ledger is running.
    - name: tags
      value: "{{ tags }}"
      description: |
        Additional tags for Confidential Ledger.
    - name: properties
      description: |
        Properties of Confidential Ledger Resource.
      value:
        ledgerName: "{{ ledgerName }}"
        ledgerUri: "{{ ledgerUri }}"
        identityServiceUri: "{{ identityServiceUri }}"
        ledgerInternalNamespace: "{{ ledgerInternalNamespace }}"
        ledgerType: "{{ ledgerType }}"
        provisioningState: "{{ provisioningState }}"
        aadBasedSecurityPrincipals:
          - principalId: "{{ principalId }}"
            tenantId: "{{ tenantId }}"
            ledgerRoleName: "{{ ledgerRoleName }}"
        certBasedSecurityPrincipals:
          - cert: "{{ cert }}"
            ledgerRoleName: "{{ ledgerRoleName }}"
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

Update Confidential Ledger properties. Updates properties of Confidential Ledger.

```sql
UPDATE azure.confidential_ledger.ledger
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND ledger_name = '{{ ledger_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes a Confidential Ledger resource. Deletes an existing Confidential Ledger.

```sql
DELETE FROM azure.confidential_ledger.ledger
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND ledger_name = '{{ ledger_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
