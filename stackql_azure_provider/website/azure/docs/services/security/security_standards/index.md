--- 
title: security_standards
hide_title: false
hide_table_of_contents: false
keywords:
  - security_standards
  - security
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

Creates, updates, deletes, gets or lists a <code>security_standards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="security_standards" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.security_standards" /></td></tr>
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
    <td><CopyableCode code="assessments" /></td>
    <td><code>array</code></td>
    <td>List of assessment keys to apply to standard scope.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudProviders" /></td>
    <td><code>array</code></td>
    <td>List of all standard supported clouds.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the standard.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the standard, equivalent to the standardId.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The security standard metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The policy set definition id associated with the standard.</td>
</tr>
<tr>
    <td><CopyableCode code="standardType" /></td>
    <td><code>string</code></td>
    <td>Standard type (Custom or Default or Compliance only currently). Known values are: "Custom", "Default", and "Compliance". (Custom, Default, Compliance)</td>
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
    <td><CopyableCode code="assessments" /></td>
    <td><code>array</code></td>
    <td>List of assessment keys to apply to standard scope.</td>
</tr>
<tr>
    <td><CopyableCode code="cloudProviders" /></td>
    <td><code>array</code></td>
    <td>List of all standard supported clouds.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the standard.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the standard, equivalent to the standardId.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The security standard metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="policySetDefinitionId" /></td>
    <td><code>string</code></td>
    <td>The policy set definition id associated with the standard.</td>
</tr>
<tr>
    <td><CopyableCode code="standardType" /></td>
    <td><code>string</code></td>
    <td>Standard type (Custom or Default or Compliance only currently). Known values are: "Custom", "Default", and "Compliance". (Custom, Default, Compliance)</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-standard_id"><code>standard_id</code></a></td>
    <td></td>
    <td>Get a specific security standard for the requested scope by standardId.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get a list of all relevant security standards over a scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-standard_id"><code>standard_id</code></a></td>
    <td></td>
    <td>Creates or updates a security standard over a given scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-standard_id"><code>standard_id</code></a></td>
    <td></td>
    <td>Creates or updates a security standard over a given scope.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-standard_id"><code>standard_id</code></a></td>
    <td></td>
    <td>Delete a security standard over a given scope.</td>
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
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-standard_id">
    <td><CopyableCode code="standard_id" /></td>
    <td><code>string</code></td>
    <td>The Security Standard key - unique key for the standard type. Required.</td>
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

Get a specific security standard for the requested scope by standardId.

```sql
SELECT
id,
name,
assessments,
cloudProviders,
description,
displayName,
metadata,
policySetDefinitionId,
standardType,
systemData,
type
FROM azure.security.security_standards
WHERE scope = '{{ scope }}' -- required
AND standard_id = '{{ standard_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of all relevant security standards over a scope.

```sql
SELECT
id,
name,
assessments,
cloudProviders,
description,
displayName,
metadata,
policySetDefinitionId,
standardType,
systemData,
type
FROM azure.security.security_standards
WHERE scope = '{{ scope }}' -- required
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

Creates or updates a security standard over a given scope.

```sql
INSERT INTO azure.security.security_standards (
properties,
scope,
standard_id
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ standard_id }}'
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
- name: security_standards
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the security_standards resource.
    - name: standard_id
      value: "{{ standard_id }}"
      description: Required parameter for the security_standards resource.
    - name: properties
      description: |
        Properties of a security standard.
      value:
        displayName: "{{ displayName }}"
        standardType: "{{ standardType }}"
        description: "{{ description }}"
        assessments:
          - assessmentKey: "{{ assessmentKey }}"
        cloudProviders:
          - "{{ cloudProviders }}"
        policySetDefinitionId: "{{ policySetDefinitionId }}"
        metadata:
          createdBy: "{{ createdBy }}"
          createdOn: "{{ createdOn }}"
          lastUpdatedBy: "{{ lastUpdatedBy }}"
          lastUpdatedOn: "{{ lastUpdatedOn }}"
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

Creates or updates a security standard over a given scope.

```sql
REPLACE azure.security.security_standards
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND standard_id = '{{ standard_id }}' --required
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

Delete a security standard over a given scope.

```sql
DELETE FROM azure.security.security_standards
WHERE scope = '{{ scope }}' --required
AND standard_id = '{{ standard_id }}' --required
;
```
</TabItem>
</Tabs>
