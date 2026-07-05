--- 
title: app_components
hide_title: false
hide_table_of_contents: false
keywords:
  - app_components
  - developer_loadtesting
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

Creates, updates, deletes, gets or lists an <code>app_components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="app_components" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.app_components" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_app_components"
    values={[
        { label: 'get_app_components', value: 'get_app_components' }
    ]}
>
<TabItem value="get_app_components">

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
    <td><CopyableCode code="components" /></td>
    <td><code>object</code></td>
    <td>Azure resource collection &#123; resource id (fully qualified resource Id e.g subscriptions/&#123;subId&#125;/resourceGroups/&#123;rg&#125;/providers/Microsoft.LoadTestService/loadtests/&#123;resName&#125;)</td>
</tr>
<tr>
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>The user that created.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>The user that last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last Modified datetime(RFC 3339 literal format).</td>
</tr>
<tr>
    <td><CopyableCode code="testId" /></td>
    <td><code>string</code></td>
    <td>Test identifier.</td>
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
    <td><a href="#get_app_components"><CopyableCode code="get_app_components" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Get associated app component (collection of azure resources) for the given test. Get associated app component (collection of azure resources) for the given test.</td>
</tr>
<tr>
    <td><a href="#create_or_update_app_components"><CopyableCode code="create_or_update_app_components" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-components"><code>components</code></a></td>
    <td></td>
    <td>Add an app component to a test. Add an app component to a test by providing the resource Id, name and type.</td>
</tr>
<tr>
    <td><a href="#create_or_update_app_components"><CopyableCode code="create_or_update_app_components" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-components"><code>components</code></a></td>
    <td></td>
    <td>Add an app component to a test. Add an app component to a test by providing the resource Id, name and type.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-test_id">
    <td><CopyableCode code="test_id" /></td>
    <td><code>string</code></td>
    <td>Unique name for the load test, must contain only lower-case alphabetic, numeric, underscore or hyphen characters. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_app_components"
    values={[
        { label: 'get_app_components', value: 'get_app_components' }
    ]}
>
<TabItem value="get_app_components">

Get associated app component (collection of azure resources) for the given test. Get associated app component (collection of azure resources) for the given test.

```sql
SELECT
components,
createdBy,
createdDateTime,
lastModifiedBy,
lastModifiedDateTime,
testId
FROM azure.developer_loadtesting.app_components
WHERE test_id = '{{ test_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_app_components"
    values={[
        { label: 'create_or_update_app_components', value: 'create_or_update_app_components' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_app_components">

Add an app component to a test. Add an app component to a test by providing the resource Id, name and type.

```sql
INSERT INTO azure.developer_loadtesting.app_components (
components,
test_id,
endpoint
)
SELECT 
'{{ components }}' /* required */,
'{{ test_id }}',
'{{ endpoint }}'
RETURNING
components,
createdBy,
createdDateTime,
lastModifiedBy,
lastModifiedDateTime,
testId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: app_components
  props:
    - name: test_id
      value: "{{ test_id }}"
      description: Required parameter for the app_components resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the app_components resource.
    - name: components
      value: "{{ components }}"
      description: |
        Azure resource collection { resource id (fully qualified resource Id e.g subscriptions/{subId}/resourceGroups/{rg}/providers/Microsoft.LoadTestService/loadtests/{resName})
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_app_components"
    values={[
        { label: 'create_or_update_app_components', value: 'create_or_update_app_components' }
    ]}
>
<TabItem value="create_or_update_app_components">

Add an app component to a test. Add an app component to a test by providing the resource Id, name and type.

```sql
REPLACE azure.developer_loadtesting.app_components
SET 
components = '{{ components }}'
WHERE 
test_id = '{{ test_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND components = '{{ components }}' --required
RETURNING
components,
createdBy,
createdDateTime,
lastModifiedBy,
lastModifiedDateTime,
testId;
```
</TabItem>
</Tabs>
