--- 
title: sensor_partner_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - sensor_partner_integrations
  - agrifood_farming
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>sensor_partner_integrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sensor_partner_integrations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood_farming.sensor_partner_integrations" /></td></tr>
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
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-sensor_partner_id"><code>sensor_partner_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or update an integration with a sensor partner.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-sensor_partner_id"><code>sensor_partner_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create or update an integration with a sensor partner.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-sensor_partner_id"><code>sensor_partner_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes a partner integration model entity.</td>
</tr>
<tr>
    <td><a href="#get_raw"><CopyableCode code="get_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sensor_partner_id"><code>sensor_partner_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets a partner integration model entity.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sensor_partner_id"><code>sensor_partner_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-minCreatedDateTime"><code>minCreatedDateTime</code></a>, <a href="#parameter-maxCreatedDateTime"><code>maxCreatedDateTime</code></a>, <a href="#parameter-minLastModifiedDateTime"><code>minLastModifiedDateTime</code></a>, <a href="#parameter-maxLastModifiedDateTime"><code>maxLastModifiedDateTime</code></a>, <a href="#parameter-skipToken"><code>skipToken</code></a></td>
    <td>Gets partner integration models.</td>
</tr>
<tr>
    <td><a href="#check_consent"><CopyableCode code="check_consent" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sensor_partner_id"><code>sensor_partner_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a>, <a href="#parameter-key"><code>key</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Checks consent for partner integration.</td>
</tr>
<tr>
    <td><a href="#generate_consent_link"><CopyableCode code="generate_consent_link" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-sensor_partner_id"><code>sensor_partner_id</code></a>, <a href="#parameter-integration_id"><code>integration_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Generates partner integration consent link.</td>
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
<tr id="parameter-integration_id">
    <td><CopyableCode code="integration_id" /></td>
    <td><code>string</code></td>
    <td>Id of the integration object. Required.</td>
</tr>
<tr id="parameter-key">
    <td><CopyableCode code="key" /></td>
    <td><code>string</code></td>
    <td>Partner integration key. Required.</td>
</tr>
<tr id="parameter-sensor_partner_id">
    <td><CopyableCode code="sensor_partner_id" /></td>
    <td><code>string</code></td>
    <td>Id of the sensor partner. Required.</td>
</tr>
<tr id="parameter-maxCreatedDateTime">
    <td><CopyableCode code="maxCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-maxLastModifiedDateTime">
    <td><CopyableCode code="maxLastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Maximum last modified date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minCreatedDateTime">
    <td><CopyableCode code="minCreatedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum creation date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-minLastModifiedDateTime">
    <td><CopyableCode code="minLastModifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Minimum last modified date of resource (inclusive). Default value is None.</td>
</tr>
<tr id="parameter-skipToken">
    <td><CopyableCode code="skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip token for getting next set of results. Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Create or update an integration with a sensor partner.

```sql
INSERT INTO azure_extras.agrifood_farming.sensor_partner_integrations (
sensor_partner_id,
integration_id,
endpoint
)
SELECT 
'{{ sensor_partner_id }}',
'{{ integration_id }}',
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sensor_partner_integrations
  props:
    - name: sensor_partner_id
      value: "{{ sensor_partner_id }}"
      description: Required parameter for the sensor_partner_integrations resource.
    - name: integration_id
      value: "{{ integration_id }}"
      description: Required parameter for the sensor_partner_integrations resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the sensor_partner_integrations resource.
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

Create or update an integration with a sensor partner.

```sql
REPLACE azure_extras.agrifood_farming.sensor_partner_integrations
SET 
-- No updatable properties
WHERE 
sensor_partner_id = '{{ sensor_partner_id }}' --required
AND integration_id = '{{ integration_id }}' --required
AND endpoint = '{{ endpoint }}' --required;
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

Deletes a partner integration model entity.

```sql
DELETE FROM azure_extras.agrifood_farming.sensor_partner_integrations
WHERE sensor_partner_id = '{{ sensor_partner_id }}' --required
AND integration_id = '{{ integration_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_raw"
    values={[
        { label: 'get_raw', value: 'get_raw' },
        { label: 'list_raw', value: 'list_raw' },
        { label: 'check_consent', value: 'check_consent' },
        { label: 'generate_consent_link', value: 'generate_consent_link' }
    ]}
>
<TabItem value="get_raw">

Gets a partner integration model entity.

```sql
EXEC azure_extras.agrifood_farming.sensor_partner_integrations.get_raw 
@sensor_partner_id='{{ sensor_partner_id }}' --required, 
@integration_id='{{ integration_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="list_raw">

Gets partner integration models.

```sql
EXEC azure_extras.agrifood_farming.sensor_partner_integrations.list_raw 
@sensor_partner_id='{{ sensor_partner_id }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@minCreatedDateTime='{{ minCreatedDateTime }}', 
@maxCreatedDateTime='{{ maxCreatedDateTime }}', 
@minLastModifiedDateTime='{{ minLastModifiedDateTime }}', 
@maxLastModifiedDateTime='{{ maxLastModifiedDateTime }}', 
@skipToken='{{ skipToken }}'
;
```
</TabItem>
<TabItem value="check_consent">

Checks consent for partner integration.

```sql
EXEC azure_extras.agrifood_farming.sensor_partner_integrations.check_consent 
@sensor_partner_id='{{ sensor_partner_id }}' --required, 
@integration_id='{{ integration_id }}' --required, 
@key='{{ key }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
<TabItem value="generate_consent_link">

Generates partner integration consent link.

```sql
EXEC azure_extras.agrifood_farming.sensor_partner_integrations.generate_consent_link 
@sensor_partner_id='{{ sensor_partner_id }}' --required, 
@integration_id='{{ integration_id }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
