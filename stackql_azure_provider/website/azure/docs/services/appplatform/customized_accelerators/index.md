--- 
title: customized_accelerators
hide_title: false
hide_table_of_contents: false
keywords:
  - customized_accelerators
  - appplatform
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

Creates, updates, deletes, gets or lists a <code>customized_accelerators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="customized_accelerators" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appplatform.customized_accelerators" /></td></tr>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="acceleratorTags" /></td>
    <td><code>array</code></td>
    <td>:vartype accelerator_tags: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="acceleratorType" /></td>
    <td><code>string</code></td>
    <td>Type of the customized accelerator. Known values are: "Accelerator" and "Fragment".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>:vartype description: str</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>:vartype display_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="gitRepository" /></td>
    <td><code>object</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="iconUrl" /></td>
    <td><code>string</code></td>
    <td>:vartype icon_url: str</td>
</tr>
<tr>
    <td><CopyableCode code="imports" /></td>
    <td><code>array</code></td>
    <td>Imports references all imports that this accelerator/fragment depends upon.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the customized accelerator. Known values are: "Creating", "Updating", "Succeeded", "Failed", "Deleting", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the customized accelerator resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="acceleratorTags" /></td>
    <td><code>array</code></td>
    <td>:vartype accelerator_tags: list[str]</td>
</tr>
<tr>
    <td><CopyableCode code="acceleratorType" /></td>
    <td><code>string</code></td>
    <td>Type of the customized accelerator. Known values are: "Accelerator" and "Fragment".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>:vartype description: str</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>:vartype display_name: str</td>
</tr>
<tr>
    <td><CopyableCode code="gitRepository" /></td>
    <td><code>object</code></td>
    <td>Required.</td>
</tr>
<tr>
    <td><CopyableCode code="iconUrl" /></td>
    <td><code>string</code></td>
    <td>:vartype icon_url: str</td>
</tr>
<tr>
    <td><CopyableCode code="imports" /></td>
    <td><code>array</code></td>
    <td>Imports references all imports that this accelerator/fragment depends upon.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>State of the customized accelerator. Known values are: "Creating", "Updating", "Succeeded", "Failed", "Deleting", and "Canceled".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the customized accelerator resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-application_accelerator_name"><code>application_accelerator_name</code></a>, <a href="#parameter-customized_accelerator_name"><code>customized_accelerator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the customized accelerator.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-application_accelerator_name"><code>application_accelerator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handle requests to list all customized accelerators.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-application_accelerator_name"><code>application_accelerator_name</code></a>, <a href="#parameter-customized_accelerator_name"><code>customized_accelerator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update the customized accelerator.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-application_accelerator_name"><code>application_accelerator_name</code></a>, <a href="#parameter-customized_accelerator_name"><code>customized_accelerator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update the customized accelerator.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-application_accelerator_name"><code>application_accelerator_name</code></a>, <a href="#parameter-customized_accelerator_name"><code>customized_accelerator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the customized accelerator.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-application_accelerator_name"><code>application_accelerator_name</code></a>, <a href="#parameter-customized_accelerator_name"><code>customized_accelerator_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-gitRepository"><code>gitRepository</code></a></td>
    <td></td>
    <td>Check the customized accelerator are valid.</td>
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
<tr id="parameter-application_accelerator_name">
    <td><CopyableCode code="application_accelerator_name" /></td>
    <td><code>string</code></td>
    <td>The name of the application accelerator. Required.</td>
</tr>
<tr id="parameter-customized_accelerator_name">
    <td><CopyableCode code="customized_accelerator_name" /></td>
    <td><code>string</code></td>
    <td>The name of the customized accelerator. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Service resource. Required.</td>
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

Get the customized accelerator.

```sql
SELECT
id,
name,
acceleratorTags,
acceleratorType,
description,
displayName,
gitRepository,
iconUrl,
imports,
provisioningState,
sku,
systemData,
type
FROM azure.appplatform.customized_accelerators
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND application_accelerator_name = '{{ application_accelerator_name }}' -- required
AND customized_accelerator_name = '{{ customized_accelerator_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Handle requests to list all customized accelerators.

```sql
SELECT
id,
name,
acceleratorTags,
acceleratorType,
description,
displayName,
gitRepository,
iconUrl,
imports,
provisioningState,
sku,
systemData,
type
FROM azure.appplatform.customized_accelerators
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND application_accelerator_name = '{{ application_accelerator_name }}' -- required
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

Create or update the customized accelerator.

```sql
INSERT INTO azure.appplatform.customized_accelerators (
properties,
sku,
resource_group_name,
service_name,
application_accelerator_name,
customized_accelerator_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ application_accelerator_name }}',
'{{ customized_accelerator_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
sku,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: customized_accelerators
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the customized_accelerators resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the customized_accelerators resource.
    - name: application_accelerator_name
      value: "{{ application_accelerator_name }}"
      description: Required parameter for the customized_accelerators resource.
    - name: customized_accelerator_name
      value: "{{ customized_accelerator_name }}"
      description: Required parameter for the customized_accelerators resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the customized_accelerators resource.
    - name: properties
      description: |
        Customized accelerator properties payload.
      value:
        provisioningState: "{{ provisioningState }}"
        acceleratorType: "{{ acceleratorType }}"
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        iconUrl: "{{ iconUrl }}"
        acceleratorTags:
          - "{{ acceleratorTags }}"
        imports:
          - "{{ imports }}"
        gitRepository:
          url: "{{ url }}"
          intervalInSeconds: {{ intervalInSeconds }}
          branch: "{{ branch }}"
          commit: "{{ commit }}"
          gitTag: "{{ gitTag }}"
          authSetting:
            authType: "{{ authType }}"
          subPath: "{{ subPath }}"
    - name: sku
      description: |
        Sku of the customized accelerator resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
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

Create or update the customized accelerator.

```sql
REPLACE azure.appplatform.customized_accelerators
SET 
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND application_accelerator_name = '{{ application_accelerator_name }}' --required
AND customized_accelerator_name = '{{ customized_accelerator_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
sku,
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

Delete the customized accelerator.

```sql
DELETE FROM azure.appplatform.customized_accelerators
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND application_accelerator_name = '{{ application_accelerator_name }}' --required
AND customized_accelerator_name = '{{ customized_accelerator_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="validate"
    values={[
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="validate">

Check the customized accelerator are valid.

```sql
EXEC azure.appplatform.customized_accelerators.validate 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@application_accelerator_name='{{ application_accelerator_name }}' --required, 
@customized_accelerator_name='{{ customized_accelerator_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"acceleratorType": "{{ acceleratorType }}", 
"displayName": "{{ displayName }}", 
"description": "{{ description }}", 
"iconUrl": "{{ iconUrl }}", 
"acceleratorTags": "{{ acceleratorTags }}", 
"gitRepository": "{{ gitRepository }}"
}'
;
```
</TabItem>
</Tabs>
