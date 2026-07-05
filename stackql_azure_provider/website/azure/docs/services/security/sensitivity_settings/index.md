--- 
title: sensitivity_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - sensitivity_settings
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

Creates, updates, deletes, gets or lists a <code>sensitivity_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sensitivity_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.sensitivity_settings" /></td></tr>
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
    <td><CopyableCode code="mipInformation" /></td>
    <td><code>object</code></td>
    <td>Microsoft information protection built-in and custom information types, labels, and integration status.</td>
</tr>
<tr>
    <td><CopyableCode code="sensitiveInfoTypesIds" /></td>
    <td><code>array</code></td>
    <td>List of selected sensitive info types' IDs.</td>
</tr>
<tr>
    <td><CopyableCode code="sensitivityThresholdLabelId" /></td>
    <td><code>string</code></td>
    <td>The id of the sensitivity threshold label. Any label at or above this rank will be considered sensitive.</td>
</tr>
<tr>
    <td><CopyableCode code="sensitivityThresholdLabelOrder" /></td>
    <td><code>number</code></td>
    <td>The order of the sensitivity threshold label. Any label at or above this order will be considered sensitive. If set to -1, sensitivity by labels is turned off.</td>
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
    <td></td>
    <td></td>
    <td>Gets data sensitivity settings for sensitive data discovery.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-sensitiveInfoTypesIds"><code>sensitiveInfoTypesIds</code></a></td>
    <td></td>
    <td>Create or update data sensitivity settings for sensitive data discovery.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-sensitiveInfoTypesIds"><code>sensitiveInfoTypesIds</code></a></td>
    <td></td>
    <td>Create or update data sensitivity settings for sensitive data discovery.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td></td>
    <td>Gets a list with a single sensitivity settings resource.</td>
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

Gets data sensitivity settings for sensitive data discovery.

```sql
SELECT
id,
name,
mipInformation,
sensitiveInfoTypesIds,
sensitivityThresholdLabelId,
sensitivityThresholdLabelOrder,
systemData,
type
FROM azure.security.sensitivity_settings
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

Create or update data sensitivity settings for sensitive data discovery.

```sql
INSERT INTO azure.security.sensitivity_settings (
sensitiveInfoTypesIds,
sensitivityThresholdLabelOrder,
sensitivityThresholdLabelId
)
SELECT 
'{{ sensitiveInfoTypesIds }}' /* required */,
{{ sensitivityThresholdLabelOrder }},
'{{ sensitivityThresholdLabelId }}'
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
- name: sensitivity_settings
  props:
    - name: sensitiveInfoTypesIds
      value:
        - "{{ sensitiveInfoTypesIds }}"
      description: |
        List of selected sensitive info types' IDs. Required.
    - name: sensitivityThresholdLabelOrder
      value: {{ sensitivityThresholdLabelOrder }}
      description: |
        The order of the sensitivity threshold label. Any label at or above this order will be considered sensitive. If set to -1, sensitivity by labels is turned off.
    - name: sensitivityThresholdLabelId
      value: "{{ sensitivityThresholdLabelId }}"
      description: |
        The id of the sensitivity threshold label. Any label at or above this rank will be considered sensitive.
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

Create or update data sensitivity settings for sensitive data discovery.

```sql
REPLACE azure.security.sensitivity_settings
SET 
sensitiveInfoTypesIds = '{{ sensitiveInfoTypesIds }}',
sensitivityThresholdLabelOrder = {{ sensitivityThresholdLabelOrder }},
sensitivityThresholdLabelId = '{{ sensitivityThresholdLabelId }}'
WHERE 
sensitiveInfoTypesIds = '{{ sensitiveInfoTypesIds }}' --required
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
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

Gets a list with a single sensitivity settings resource.

```sql
EXEC azure.security.sensitivity_settings.list_raw 

;
```
</TabItem>
</Tabs>
