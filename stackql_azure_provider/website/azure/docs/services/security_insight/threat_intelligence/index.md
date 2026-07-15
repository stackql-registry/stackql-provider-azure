--- 
title: threat_intelligence
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_intelligence
  - security_insight
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

Creates, updates, deletes, gets or lists a <code>threat_intelligence</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="threat_intelligence" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.threat_intelligence" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="query"
    values={[
        { label: 'query', value: 'query' }
    ]}
>
<TabItem value="query">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>object</code></td>
    <td>The UserInfo of the user/entity which originally created this TI object.</td>
</tr>
<tr>
    <td><CopyableCode code="data" /></td>
    <td><code>object</code></td>
    <td>The core STIX object that this TI object represents.</td>
</tr>
<tr>
    <td><CopyableCode code="firstIngestedTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp for the first time this object was ingested.</td>
</tr>
<tr>
    <td><CopyableCode code="ingestionRulesVersion" /></td>
    <td><code>string</code></td>
    <td>The ID of the rules version that was active when this TI object was last ingested.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the TI object. Required. Known values are: "AttackPattern", "Identity", "Indicator", "Relationship", and "ThreatActor".</td>
</tr>
<tr>
    <td><CopyableCode code="lastIngestedTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp for the last time this object was ingested.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>object</code></td>
    <td>The UserInfo of the user/entity which last modified this TI object.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateMethod" /></td>
    <td><code>string</code></td>
    <td>The name of the method/application that initiated the last write to this TI object.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedDateTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp for the last time this TI object was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="relationshipHints" /></td>
    <td><code>array</code></td>
    <td>A dictionary used to help follow relationships from this object to other STIX objects. The keys are field names from the STIX object (in the 'data' field), and the values are lists of sources that can be prepended to the object ID in order to efficiently locate the target TI object.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>string</code></td>
    <td>The source name for this TI object.</td>
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
    <td><a href="#query"><CopyableCode code="query" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-ti_type"><code>ti_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all TI objects for the workspace.</td>
</tr>
<tr>
    <td><a href="#count"><CopyableCode code="count" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-ti_type"><code>ti_type</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the count of all TI objects for the workspace.</td>
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
<tr id="parameter-ti_type">
    <td><CopyableCode code="ti_type" /></td>
    <td><code>string</code></td>
    <td>TI type. "main" Required.</td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="query"
    values={[
        { label: 'query', value: 'query' }
    ]}
>
<TabItem value="query">

Gets all TI objects for the workspace.

```sql
SELECT
id,
name,
createdBy,
data,
firstIngestedTimeUtc,
ingestionRulesVersion,
kind,
lastIngestedTimeUtc,
lastModifiedBy,
lastUpdateMethod,
lastUpdatedDateTimeUtc,
relationshipHints,
source,
systemData,
type
FROM azure.security_insight.threat_intelligence
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND ti_type = '{{ ti_type }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="count"
    values={[
        { label: 'count', value: 'count' }
    ]}
>
<TabItem value="count">

Gets the count of all TI objects for the workspace.

```sql
EXEC azure.security_insight.threat_intelligence.count 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@ti_type='{{ ti_type }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
