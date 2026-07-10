--- 
title: threat_intelligence_indicator
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_intelligence_indicator
  - securityinsight
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

Creates, updates, deletes, gets or lists a <code>threat_intelligence_indicator</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="threat_intelligence_indicator" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.securityinsight.threat_intelligence_indicator" /></td></tr>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. "indicator"</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>View a threat intelligence indicator by name.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Update a threat Intelligence indicator.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a threat intelligence indicator.</td>
</tr>
<tr>
    <td><a href="#append_tags"><CopyableCode code="append_tags" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Append tags to a threat intelligence indicator.</td>
</tr>
<tr>
    <td><a href="#replace_tags"><CopyableCode code="replace_tags" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Replace tags added to a threat intelligence indicator.</td>
</tr>
<tr>
    <td><a href="#create_indicator"><CopyableCode code="create_indicator" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Create a new threat intelligence indicator.</td>
</tr>
<tr>
    <td><a href="#query_indicators"><CopyableCode code="query_indicators" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Query threat intelligence indicators as per filtering criteria.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Threat intelligence indicator name field. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the monitor workspace. Required.</td>
</tr>
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

View a threat intelligence indicator by name.

```sql
SELECT
id,
name,
etag,
kind,
systemData,
type
FROM azure.securityinsight.threat_intelligence_indicator
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Update a threat Intelligence indicator.

```sql
INSERT INTO azure.securityinsight.threat_intelligence_indicator (
kind,
etag,
properties,
resource_group_name,
workspace_name,
name,
subscription_id
)
SELECT 
'{{ kind }}' /* required */,
'{{ etag }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: threat_intelligence_indicator
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the threat_intelligence_indicator resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the threat_intelligence_indicator resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the threat_intelligence_indicator resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the threat_intelligence_indicator resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Required. Entity represents threat intelligence indicator in the system.
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
    - name: properties
      description: |
        Threat Intelligence Entity properties.
      value:
        additionalData: "{{ additionalData }}"
        friendlyName: "{{ friendlyName }}"
        threatIntelligenceTags:
          - "{{ threatIntelligenceTags }}"
        lastUpdatedTimeUtc: "{{ lastUpdatedTimeUtc }}"
        source: "{{ source }}"
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        indicatorTypes:
          - "{{ indicatorTypes }}"
        pattern: "{{ pattern }}"
        patternType: "{{ patternType }}"
        patternVersion: "{{ patternVersion }}"
        killChainPhases:
          - killChainName: "{{ killChainName }}"
            phaseName: "{{ phaseName }}"
        parsedPattern:
          - patternTypeKey: "{{ patternTypeKey }}"
            patternTypeValues: "{{ patternTypeValues }}"
        externalId: "{{ externalId }}"
        createdByRef: "{{ createdByRef }}"
        defanged: {{ defanged }}
        externalLastUpdatedTimeUtc: "{{ externalLastUpdatedTimeUtc }}"
        externalReferences:
          - description: "{{ description }}"
            externalId: "{{ externalId }}"
            sourceName: "{{ sourceName }}"
            url: "{{ url }}"
            hashes: "{{ hashes }}"
        granularMarkings:
          - language: "{{ language }}"
            markingRef: {{ markingRef }}
            selectors: "{{ selectors }}"
        labels:
          - "{{ labels }}"
        revoked: {{ revoked }}
        confidence: {{ confidence }}
        objectMarkingRefs:
          - "{{ objectMarkingRefs }}"
        language: "{{ language }}"
        threatTypes:
          - "{{ threatTypes }}"
        validFrom: "{{ validFrom }}"
        validUntil: "{{ validUntil }}"
        created: "{{ created }}"
        modified: "{{ modified }}"
        extensions: "{{ extensions }}"
`}</CodeBlock>

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

Delete a threat intelligence indicator.

```sql
DELETE FROM azure.securityinsight.threat_intelligence_indicator
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="append_tags"
    values={[
        { label: 'append_tags', value: 'append_tags' },
        { label: 'replace_tags', value: 'replace_tags' },
        { label: 'create_indicator', value: 'create_indicator' },
        { label: 'query_indicators', value: 'query_indicators' }
    ]}
>
<TabItem value="append_tags">

Append tags to a threat intelligence indicator.

```sql
EXEC azure.securityinsight.threat_intelligence_indicator.append_tags 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"threatIntelligenceTags": "{{ threatIntelligenceTags }}"
}'
;
```
</TabItem>
<TabItem value="replace_tags">

Replace tags added to a threat intelligence indicator.

```sql
EXEC azure.securityinsight.threat_intelligence_indicator.replace_tags 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@name='{{ name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"etag": "{{ etag }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="create_indicator">

Create a new threat intelligence indicator.

```sql
EXEC azure.securityinsight.threat_intelligence_indicator.create_indicator 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"etag": "{{ etag }}", 
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="query_indicators">

Query threat intelligence indicators as per filtering criteria.

```sql
EXEC azure.securityinsight.threat_intelligence_indicator.query_indicators 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"pageSize": {{ pageSize }}, 
"minConfidence": {{ minConfidence }}, 
"maxConfidence": {{ maxConfidence }}, 
"minValidUntil": "{{ minValidUntil }}", 
"maxValidUntil": "{{ maxValidUntil }}", 
"includeDisabled": {{ includeDisabled }}, 
"sortBy": "{{ sortBy }}", 
"sources": "{{ sources }}", 
"patternTypes": "{{ patternTypes }}", 
"threatTypes": "{{ threatTypes }}", 
"ids": "{{ ids }}", 
"keywords": "{{ keywords }}", 
"skipToken": "{{ skipToken }}"
}'
;
```
</TabItem>
</Tabs>
