--- 
title: server_metrics_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - server_metrics_configs
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

Creates, updates, deletes, gets or lists a <code>server_metrics_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="server_metrics_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.developer_loadtesting.server_metrics_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_server_metrics_config"
    values={[
        { label: 'get_server_metrics_config', value: 'get_server_metrics_config' }
    ]}
>
<TabItem value="get_server_metrics_config">

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
    <td><CopyableCode code="metrics" /></td>
    <td><code>object</code></td>
    <td>Azure resource metrics collection &#123;metric id : metrics object&#125; (Refer : `https://learn.microsoft.com/en-us/rest/api/monitor/metric-definitions/list#metricdefinition `_ for metric id). Required.</td>
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
    <td><a href="#get_server_metrics_config"><CopyableCode code="get_server_metrics_config" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List server metrics configuration for the given test. List server metrics configuration for the given test.</td>
</tr>
<tr>
    <td><a href="#create_or_update_server_metrics_config"><CopyableCode code="create_or_update_server_metrics_config" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-metrics"><code>metrics</code></a></td>
    <td></td>
    <td>Configure server metrics for a test. Configure server metrics for a test.</td>
</tr>
<tr>
    <td><a href="#create_or_update_server_metrics_config"><CopyableCode code="create_or_update_server_metrics_config" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-test_id"><code>test_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-metrics"><code>metrics</code></a></td>
    <td></td>
    <td>Configure server metrics for a test. Configure server metrics for a test.</td>
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
    defaultValue="get_server_metrics_config"
    values={[
        { label: 'get_server_metrics_config', value: 'get_server_metrics_config' }
    ]}
>
<TabItem value="get_server_metrics_config">

List server metrics configuration for the given test. List server metrics configuration for the given test.

```sql
SELECT
createdBy,
createdDateTime,
lastModifiedBy,
lastModifiedDateTime,
metrics,
testId
FROM azure.developer_loadtesting.server_metrics_configs
WHERE test_id = '{{ test_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_server_metrics_config"
    values={[
        { label: 'create_or_update_server_metrics_config', value: 'create_or_update_server_metrics_config' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_server_metrics_config">

Configure server metrics for a test. Configure server metrics for a test.

```sql
INSERT INTO azure.developer_loadtesting.server_metrics_configs (
metrics,
test_id,
endpoint
)
SELECT 
'{{ metrics }}' /* required */,
'{{ test_id }}',
'{{ endpoint }}'
RETURNING
createdBy,
createdDateTime,
lastModifiedBy,
lastModifiedDateTime,
metrics,
testId
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: server_metrics_configs
  props:
    - name: test_id
      value: "{{ test_id }}"
      description: Required parameter for the server_metrics_configs resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the server_metrics_configs resource.
    - name: metrics
      value: "{{ metrics }}"
      description: |
        Azure resource metrics collection {metric id : metrics object} (Refer : \`https://learn.microsoft.com/en-us/rest/api/monitor/metric-definitions/list#metricdefinition \`_ for metric id). Required.
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_server_metrics_config"
    values={[
        { label: 'create_or_update_server_metrics_config', value: 'create_or_update_server_metrics_config' }
    ]}
>
<TabItem value="create_or_update_server_metrics_config">

Configure server metrics for a test. Configure server metrics for a test.

```sql
REPLACE azure.developer_loadtesting.server_metrics_configs
SET 
metrics = '{{ metrics }}'
WHERE 
test_id = '{{ test_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND metrics = '{{ metrics }}' --required
RETURNING
createdBy,
createdDateTime,
lastModifiedBy,
lastModifiedDateTime,
metrics,
testId;
```
</TabItem>
</Tabs>
