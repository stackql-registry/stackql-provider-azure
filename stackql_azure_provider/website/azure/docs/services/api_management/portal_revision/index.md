--- 
title: portal_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - portal_revision
  - api_management
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

Creates, updates, deletes, gets or lists a <code>portal_revision</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="portal_revision" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.portal_revision" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service', value: 'list_by_service' }
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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Portal's revision creation date and time.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Portal revision description.</td>
</tr>
<tr>
    <td><CopyableCode code="isCurrent" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the portal's revision is public.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the portal's revision. Known values are: "pending", "publishing", "completed", and "failed". (pending, publishing, completed, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Portal revision publishing status details.</td>
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
<tr>
    <td><CopyableCode code="updatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last updated date and time.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_service">

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
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Portal's revision creation date and time.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Portal revision description.</td>
</tr>
<tr>
    <td><CopyableCode code="isCurrent" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if the portal's revision is public.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the portal's revision. Known values are: "pending", "publishing", "completed", and "failed". (pending, publishing, completed, failed)</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Portal revision publishing status details.</td>
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
<tr>
    <td><CopyableCode code="updatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last updated date and time.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-portal_revision_id"><code>portal_revision_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the developer portal's revision specified by its identifier.</td>
</tr>
<tr>
    <td><a href="#list_by_service"><CopyableCode code="list_by_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skip"><code>$skip</code></a></td>
    <td>Lists developer portal's revisions.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-portal_revision_id"><code>portal_revision_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new developer portal's revision by running the portal's publishing. The `isCurrent` property indicates if the revision is publicly accessible.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-portal_revision_id"><code>portal_revision_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the description of specified portal revision or makes it current.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-portal_revision_id"><code>portal_revision_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new developer portal's revision by running the portal's publishing. The `isCurrent` property indicates if the revision is publicly accessible.</td>
</tr>
<tr>
    <td><a href="#get_entity_tag"><CopyableCode code="get_entity_tag" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-portal_revision_id"><code>portal_revision_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the developer portal revision specified by its identifier.</td>
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
<tr id="parameter-portal_revision_id">
    <td><CopyableCode code="portal_revision_id" /></td>
    <td><code>string</code></td>
    <td>Portal revision identifier. Must be unique in the current API Management service instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>| Field | Supported operators | Supported functions | |-------------|------------------------|-----------------------------------| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |isCurrent | eq, ne | |. Default value is None.</td>
</tr>
<tr id="parameter-$skip">
    <td><CopyableCode code="$skip" /></td>
    <td><code>integer</code></td>
    <td>Number of records to skip. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of records to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_service', value: 'list_by_service' }
    ]}
>
<TabItem value="get">

Gets the developer portal's revision specified by its identifier.

```sql
SELECT
id,
name,
createdDateTime,
description,
isCurrent,
provisioningState,
status,
statusDetails,
systemData,
type,
updatedDateTime
FROM azure.api_management.portal_revision
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND portal_revision_id = '{{ portal_revision_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_service">

Lists developer portal's revisions.

```sql
SELECT
id,
name,
createdDateTime,
description,
isCurrent,
provisioningState,
status,
statusDetails,
systemData,
type,
updatedDateTime
FROM azure.api_management.portal_revision
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skip = '{{ $skip }}'
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

Creates a new developer portal's revision by running the portal's publishing. The `isCurrent` property indicates if the revision is publicly accessible.

```sql
INSERT INTO azure.api_management.portal_revision (
properties,
resource_group_name,
service_name,
portal_revision_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ portal_revision_id }}',
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
- name: portal_revision
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the portal_revision resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the portal_revision resource.
    - name: portal_revision_id
      value: "{{ portal_revision_id }}"
      description: Required parameter for the portal_revision resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the portal_revision resource.
    - name: properties
      description: |
        Properties of the portal revisions.
      value:
        description: "{{ description }}"
        statusDetails: "{{ statusDetails }}"
        status: "{{ status }}"
        isCurrent: {{ isCurrent }}
        createdDateTime: "{{ createdDateTime }}"
        updatedDateTime: "{{ updatedDateTime }}"
        provisioningState: "{{ provisioningState }}"
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

Updates the description of specified portal revision or makes it current.

```sql
UPDATE azure.api_management.portal_revision
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND portal_revision_id = '{{ portal_revision_id }}' --required
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

Creates a new developer portal's revision by running the portal's publishing. The `isCurrent` property indicates if the revision is publicly accessible.

```sql
REPLACE azure.api_management.portal_revision
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND portal_revision_id = '{{ portal_revision_id }}' --required
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


## Lifecycle Methods

<Tabs
    defaultValue="get_entity_tag"
    values={[
        { label: 'get_entity_tag', value: 'get_entity_tag' }
    ]}
>
<TabItem value="get_entity_tag">

Gets the developer portal revision specified by its identifier.

```sql
EXEC azure.api_management.portal_revision.get_entity_tag 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@portal_revision_id='{{ portal_revision_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
