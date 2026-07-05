--- 
title: tag_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_rules
  - datadog
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

Creates, updates, deletes, gets or lists a <code>tag_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tag_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.tag_rules" /></td></tr>
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
    <td>The id of the rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="automuting" /></td>
    <td><code>boolean</code></td>
    <td>Configuration to enable/disable auto-muting flag.</td>
</tr>
<tr>
    <td><CopyableCode code="logRules" /></td>
    <td><code>object</code></td>
    <td>Set of rules for sending logs for the Monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="metricRules" /></td>
    <td><code>object</code></td>
    <td>Set of rules for sending metrics for the Monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the rule set.</td>
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
    <td>The id of the rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the rule set.</td>
</tr>
<tr>
    <td><CopyableCode code="automuting" /></td>
    <td><code>boolean</code></td>
    <td>Configuration to enable/disable auto-muting flag.</td>
</tr>
<tr>
    <td><CopyableCode code="logRules" /></td>
    <td><code>object</code></td>
    <td>Set of rules for sending logs for the Monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="metricRules" /></td>
    <td><code>object</code></td>
    <td>Set of rules for sending metrics for the Monitor resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the rule set.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a tag rule set for a given monitor resource. Get a tag rule set for a given monitor resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the tag rules for a given monitor resource. List the tag rules for a given monitor resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a tag rule set for a given monitor resource. Create or update a tag rule set for a given monitor resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-rule_set_name"><code>rule_set_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a tag rule set for a given monitor resource. Create or update a tag rule set for a given monitor resource.</td>
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
<tr id="parameter-rule_set_name">
    <td><CopyableCode code="rule_set_name" /></td>
    <td><code>string</code></td>
    <td>Rule set name. Required.</td>
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

Get a tag rule set for a given monitor resource. Get a tag rule set for a given monitor resource.

```sql
SELECT
id,
name,
automuting,
logRules,
metricRules,
provisioningState,
systemData,
type
FROM azure_isv.datadog.tag_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND rule_set_name = '{{ rule_set_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the tag rules for a given monitor resource. List the tag rules for a given monitor resource.

```sql
SELECT
id,
name,
automuting,
logRules,
metricRules,
provisioningState,
systemData,
type
FROM azure_isv.datadog.tag_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
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

Create or update a tag rule set for a given monitor resource. Create or update a tag rule set for a given monitor resource.

```sql
INSERT INTO azure_isv.datadog.tag_rules (
properties,
resource_group_name,
monitor_name,
rule_set_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ monitor_name }}',
'{{ rule_set_name }}',
'{{ subscription_id }}'
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
- name: tag_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the tag_rules resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the tag_rules resource.
    - name: rule_set_name
      value: "{{ rule_set_name }}"
      description: Required parameter for the tag_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the tag_rules resource.
    - name: properties
      description: |
        Definition of the properties for a TagRules resource.
      value:
        provisioningState: "{{ provisioningState }}"
        logRules:
          sendAadLogs: {{ sendAadLogs }}
          sendSubscriptionLogs: {{ sendSubscriptionLogs }}
          sendResourceLogs: {{ sendResourceLogs }}
          filteringTags:
            - name: "{{ name }}"
              value: "{{ value }}"
              action: "{{ action }}"
        metricRules:
          filteringTags:
            - name: "{{ name }}"
              value: "{{ value }}"
              action: "{{ action }}"
        automuting: {{ automuting }}
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

Create or update a tag rule set for a given monitor resource. Create or update a tag rule set for a given monitor resource.

```sql
REPLACE azure_isv.datadog.tag_rules
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND rule_set_name = '{{ rule_set_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
