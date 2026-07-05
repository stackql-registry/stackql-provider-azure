--- 
title: create_and_associate_pl_filter
hide_title: false
hide_table_of_contents: false
keywords:
  - create_and_associate_pl_filter
  - elastic
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>create_and_associate_pl_filter</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="create_and_associate_pl_filter" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.create_and_associate_pl_filter" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-privateEndpointGuid"><code>privateEndpointGuid</code></a>, <a href="#parameter-privateEndpointName"><code>privateEndpointName</code></a></td>
    <td>Create and associate a PL filter with your Elastic monitor resource to control and manage network traffic. Create and associate a PL filter with your Elastic monitor resource to control and manage network traffic.</td>
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
<tr id="parameter-monitor_name">
    <td><CopyableCode code="monitor_name" /></td>
    <td><code>string</code></td>
    <td>Monitor resource name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the traffic filter. Default value is None.</td>
</tr>
<tr id="parameter-privateEndpointGuid">
    <td><CopyableCode code="privateEndpointGuid" /></td>
    <td><code>string</code></td>
    <td>Guid of the private endpoint. Default value is None.</td>
</tr>
<tr id="parameter-privateEndpointName">
    <td><CopyableCode code="privateEndpointName" /></td>
    <td><code>string</code></td>
    <td>Name of the private endpoint. Default value is None.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create and associate a PL filter with your Elastic monitor resource to control and manage network traffic. Create and associate a PL filter with your Elastic monitor resource to control and manage network traffic.

```sql
INSERT INTO azure_isv.elastic.create_and_associate_pl_filter (
resource_group_name,
monitor_name,
subscription_id,
name,
privateEndpointGuid,
privateEndpointName
)
SELECT 
'{{ resource_group_name }}',
'{{ monitor_name }}',
'{{ subscription_id }}',
'{{ name }}',
'{{ privateEndpointGuid }}',
'{{ privateEndpointName }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: create_and_associate_pl_filter
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the create_and_associate_pl_filter resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the create_and_associate_pl_filter resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the create_and_associate_pl_filter resource.
    - name: name
      value: "{{ name }}"
      description: Name of the traffic filter. Default value is None.
      description: Name of the traffic filter. Default value is None.
    - name: privateEndpointGuid
      value: "{{ privateEndpointGuid }}"
      description: Guid of the private endpoint. Default value is None.
      description: Guid of the private endpoint. Default value is None.
    - name: privateEndpointName
      value: "{{ privateEndpointName }}"
      description: Name of the private endpoint. Default value is None.
      description: Name of the private endpoint. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>
