--- 
title: capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - capabilities
  - sql
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

Creates, updates, deletes, gets or lists a <code>capabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="capabilities" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.capabilities" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_location"
    values={[
        { label: 'list_by_location', value: 'list_by_location' }
    ]}
>
<TabItem value="list_by_location">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The location name.</td>
</tr>
<tr>
    <td><CopyableCode code="isZoneResilientProvisioningAllowed" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not the subscription is allowed to provision zone resilient resources.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason for the capability not being available.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the capability. Known values are: "Visible", "Available", "Default", and "Disabled". (Visible, Available, Default, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="supportedJobAgentVersions" /></td>
    <td><code>array</code></td>
    <td>The list of supported job agent versions.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedManagedInstanceVersions" /></td>
    <td><code>array</code></td>
    <td>The list of supported managed instance versions.</td>
</tr>
<tr>
    <td><CopyableCode code="supportedServerVersions" /></td>
    <td><code>array</code></td>
    <td>The list of supported server versions.</td>
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
    <td><a href="#list_by_location"><CopyableCode code="list_by_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location_name"><code>location_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-include"><code>include</code></a></td>
    <td>Gets the subscription capabilities available for the specified location.</td>
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
<tr id="parameter-location_name">
    <td><CopyableCode code="location_name" /></td>
    <td><code>string</code></td>
    <td>The location name whose capabilities are retrieved. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-include">
    <td><CopyableCode code="include" /></td>
    <td><code>string</code></td>
    <td>If specified, restricts the response to only include the selected item. Known values are: "supportedEditions", "supportedElasticPoolEditions", "supportedManagedInstanceVersions", "supportedInstancePoolEditions", "supportedManagedInstanceEditions", and "supportedJobAgentVersions". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_location"
    values={[
        { label: 'list_by_location', value: 'list_by_location' }
    ]}
>
<TabItem value="list_by_location">

Gets the subscription capabilities available for the specified location.

```sql
SELECT
name,
isZoneResilientProvisioningAllowed,
reason,
status,
supportedJobAgentVersions,
supportedManagedInstanceVersions,
supportedServerVersions
FROM azure.sql.capabilities
WHERE location_name = '{{ location_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND include = '{{ include }}'
;
```
</TabItem>
</Tabs>
