--- 
title: dependency_of_relationships
hide_title: false
hide_table_of_contents: false
keywords:
  - dependency_of_relationships
  - relationships
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

Creates, updates, deletes, gets or lists a <code>dependency_of_relationships</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dependency_of_relationships" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.relationships.dependency_of_relationships" /></td></tr>
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
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the relationship. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="originInformation" /></td>
    <td><code>object</code></td>
    <td>Information about the origin of the relationship. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the relationship. Known values are: "Succeeded", "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted". (Succeeded, Failed, Canceled, Provisioning, Updating, Deleting, Accepted)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceId" /></td>
    <td><code>string</code></td>
    <td>The relationship source resource id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetId" /></td>
    <td><code>string</code></td>
    <td>The relationship target resource id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="targetTenant" /></td>
    <td><code>string</code></td>
    <td>The relationship target tenant id.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Get a DependencyOfRelationship.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create a DependencyOfRelationship.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Create a DependencyOfRelationship.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Delete a DependencyOfRelationship.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of dependencyOf relationship. Required.</td>
</tr>
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

Get a DependencyOfRelationship.

```sql
SELECT
id,
name,
metadata,
originInformation,
provisioningState,
sourceId,
systemData,
targetId,
targetTenant,
type
FROM azure.relationships.dependency_of_relationships
WHERE resource_uri = '{{ resource_uri }}' -- required
AND name = '{{ name }}' -- required
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

Create a DependencyOfRelationship.

```sql
INSERT INTO azure.relationships.dependency_of_relationships (
properties,
resource_uri,
name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ name }}'
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
- name: dependency_of_relationships
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the dependency_of_relationships resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the dependency_of_relationships resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        sourceId: "{{ sourceId }}"
        targetId: "{{ targetId }}"
        targetTenant: "{{ targetTenant }}"
        originInformation:
          relationshipOriginType: "{{ relationshipOriginType }}"
          discoveryEngine: "{{ discoveryEngine }}"
        metadata:
          sourceType: "{{ sourceType }}"
          targetType: "{{ targetType }}"
        provisioningState: "{{ provisioningState }}"
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

Create a DependencyOfRelationship.

```sql
REPLACE azure.relationships.dependency_of_relationships
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND name = '{{ name }}' --required
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

Delete a DependencyOfRelationship.

```sql
DELETE FROM azure.relationships.dependency_of_relationships
WHERE resource_uri = '{{ resource_uri }}' --required
AND name = '{{ name }}' --required
;
```
</TabItem>
</Tabs>
