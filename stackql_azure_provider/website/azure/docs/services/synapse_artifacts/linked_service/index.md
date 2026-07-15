--- 
title: linked_service
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_service
  - synapse_artifacts
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

Creates, updates, deletes, gets or lists a <code>linked_service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="linked_service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse_artifacts.linked_service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_linked_service"
    values={[
        { label: 'get_linked_service', value: 'get_linked_service' },
        { label: 'get_linked_services_by_workspace', value: 'get_linked_services_by_workspace' }
    ]}
>
<TabItem value="get_linked_service">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the linked service.</td>
</tr>
<tr>
    <td><CopyableCode code="connectVia" /></td>
    <td><code>object</code></td>
    <td>The integration runtime reference.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Linked service description.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Parameters for linked service.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the linked service.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_linked_services_by_workspace">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="" /></td>
    <td><code>object</code></td>
    <td>Unmatched properties from the message are deserialized to this collection.</td>
</tr>
<tr>
    <td><CopyableCode code="annotations" /></td>
    <td><code>array</code></td>
    <td>List of tags that can be used for describing the linked service.</td>
</tr>
<tr>
    <td><CopyableCode code="connectVia" /></td>
    <td><code>object</code></td>
    <td>The integration runtime reference.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Linked service description.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource Etag.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>Parameters for linked service.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the linked service.</td>
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
    <td><a href="#get_linked_service"><CopyableCode code="get_linked_service" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-linked_service_name"><code>linked_service_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-If-None-Match"><code>If-None-Match</code></a></td>
    <td>Gets a linked service.</td>
</tr>
<tr>
    <td><a href="#get_linked_services_by_workspace"><CopyableCode code="get_linked_services_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists linked services.</td>
</tr>
<tr>
    <td><a href="#create_or_update_linked_service"><CopyableCode code="create_or_update_linked_service" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-linked_service_name"><code>linked_service_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a linked service.</td>
</tr>
<tr>
    <td><a href="#create_or_update_linked_service"><CopyableCode code="create_or_update_linked_service" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-linked_service_name"><code>linked_service_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td><a href="#parameter-If-Match"><code>If-Match</code></a></td>
    <td>Creates or updates a linked service.</td>
</tr>
<tr>
    <td><a href="#delete_linked_service"><CopyableCode code="delete_linked_service" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-linked_service_name"><code>linked_service_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a linked service.</td>
</tr>
<tr>
    <td><a href="#rename_linked_service"><CopyableCode code="rename_linked_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-linked_service_name"><code>linked_service_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Renames a linked service.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-linked_service_name">
    <td><CopyableCode code="linked_service_name" /></td>
    <td><code>string</code></td>
    <td>The linked service name. Required.</td>
</tr>
<tr id="parameter-If-Match">
    <td><CopyableCode code="If-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the linkedService entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.</td>
</tr>
<tr id="parameter-If-None-Match">
    <td><CopyableCode code="If-None-Match" /></td>
    <td><code>string</code></td>
    <td>ETag of the linked service entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_linked_service"
    values={[
        { label: 'get_linked_service', value: 'get_linked_service' },
        { label: 'get_linked_services_by_workspace', value: 'get_linked_services_by_workspace' }
    ]}
>
<TabItem value="get_linked_service">

Gets a linked service.

```sql
SELECT
id,
name,
,
annotations,
connectVia,
description,
etag,
parameters,
type,
version
FROM azure.synapse_artifacts.linked_service
WHERE linked_service_name = '{{ linked_service_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND If-None-Match = '{{ If-None-Match }}'
;
```
</TabItem>
<TabItem value="get_linked_services_by_workspace">

Lists linked services.

```sql
SELECT
id,
name,
,
annotations,
connectVia,
description,
etag,
parameters,
type,
version
FROM azure.synapse_artifacts.linked_service
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_linked_service"
    values={[
        { label: 'create_or_update_linked_service', value: 'create_or_update_linked_service' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_linked_service">

Creates or updates a linked service.

```sql
INSERT INTO azure.synapse_artifacts.linked_service (
,
type,
version,
connectVia,
description,
parameters,
annotations,
linked_service_name,
endpoint,
If-Match
)
SELECT 
'{{  }}',
'{{ type }}' /* required */,
'{{ version }}',
'{{ connectVia }}',
'{{ description }}',
'{{ parameters }}',
'{{ annotations }}',
'{{ linked_service_name }}',
'{{ endpoint }}',
'{{ If-Match }}'
RETURNING
id,
name,
etag,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: linked_service
  props:
    - name: linked_service_name
      value: "{{ linked_service_name }}"
      description: Required parameter for the linked_service resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the linked_service resource.
    - name: 
      value: "{{  }}"
      description: |
        Unmatched properties from the message are deserialized to this collection.
    - name: type
      value: "{{ type }}"
      description: |
        Type of linked service. Required.
    - name: version
      value: "{{ version }}"
      description: |
        Version of the linked service.
    - name: connectVia
      description: |
        The integration runtime reference.
      value:
        type: "{{ type }}"
        referenceName: "{{ referenceName }}"
        parameters: "{{ parameters }}"
    - name: description
      value: "{{ description }}"
      description: |
        Linked service description.
    - name: parameters
      value: "{{ parameters }}"
      description: |
        Parameters for linked service.
    - name: annotations
      value: "{{ annotations }}"
      description: |
        List of tags that can be used for describing the linked service.
    - name: If-Match
      value: "{{ If-Match }}"
      description: ETag of the linkedService entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
      description: ETag of the linkedService entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_linked_service"
    values={[
        { label: 'create_or_update_linked_service', value: 'create_or_update_linked_service' }
    ]}
>
<TabItem value="create_or_update_linked_service">

Creates or updates a linked service.

```sql
REPLACE azure.synapse_artifacts.linked_service
SET 
 = '{{  }}',
type = '{{ type }}',
version = '{{ version }}',
connectVia = '{{ connectVia }}',
description = '{{ description }}',
parameters = '{{ parameters }}',
annotations = '{{ annotations }}'
WHERE 
linked_service_name = '{{ linked_service_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND type = '{{ type }}' --required
AND If-Match = '{{ If-Match}}'
RETURNING
id,
name,
etag,
properties,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_linked_service"
    values={[
        { label: 'delete_linked_service', value: 'delete_linked_service' }
    ]}
>
<TabItem value="delete_linked_service">

Deletes a linked service.

```sql
DELETE FROM azure.synapse_artifacts.linked_service
WHERE linked_service_name = '{{ linked_service_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="rename_linked_service"
    values={[
        { label: 'rename_linked_service', value: 'rename_linked_service' }
    ]}
>
<TabItem value="rename_linked_service">

Renames a linked service.

```sql
EXEC azure.synapse_artifacts.linked_service.rename_linked_service 
@linked_service_name='{{ linked_service_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
