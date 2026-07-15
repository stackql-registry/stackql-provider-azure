--- 
title: service_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_configurations
  - ai_personalizer
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

Creates, updates, deletes, gets or lists a <code>service_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_personalizer.service_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#update_service_configuration"><CopyableCode code="update_service_configuration" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Update Service Configuration. Update the Personalizer service configuration.</td>
</tr>
<tr>
    <td><a href="#get_service_configuration"><CopyableCode code="get_service_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Service Configuration. Get the Personalizer service configuration.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `Endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `UPDATE` examples

<Tabs
    defaultValue="update_service_configuration"
    values={[
        { label: 'update_service_configuration', value: 'update_service_configuration' }
    ]}
>
<TabItem value="update_service_configuration">

Update Service Configuration. Update the Personalizer service configuration.

```sql
UPDATE azure.ai_personalizer.service_configurations
SET 
-- No updatable properties
WHERE 
endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_service_configuration"
    values={[
        { label: 'get_service_configuration', value: 'get_service_configuration' }
    ]}
>
<TabItem value="get_service_configuration">

Service Configuration. Get the Personalizer service configuration.

```sql
EXEC azure.ai_personalizer.service_configurations.get_service_configuration 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
