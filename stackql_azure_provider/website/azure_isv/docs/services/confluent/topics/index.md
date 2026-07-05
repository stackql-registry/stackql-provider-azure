--- 
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - confluent
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

Creates, updates, deletes, gets or lists a <code>topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="topics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.topics" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="configs" /></td>
    <td><code>object</code></td>
    <td>Config Specification of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="inputConfigs" /></td>
    <td><code>array</code></td>
    <td>Input Config Specification of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of topic.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="partitions" /></td>
    <td><code>object</code></td>
    <td>Partition Specification of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionsCount" /></td>
    <td><code>string</code></td>
    <td>Partition count of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionsReassignments" /></td>
    <td><code>object</code></td>
    <td>Partition Reassignment Specification of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationFactor" /></td>
    <td><code>string</code></td>
    <td>Replication factor of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="topicId" /></td>
    <td><code>string</code></td>
    <td>Topic Id returned by Confluent.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="configs" /></td>
    <td><code>object</code></td>
    <td>Config Specification of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="inputConfigs" /></td>
    <td><code>array</code></td>
    <td>Input Config Specification of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Type of topic.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of the record.</td>
</tr>
<tr>
    <td><CopyableCode code="partitions" /></td>
    <td><code>object</code></td>
    <td>Partition Specification of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionsCount" /></td>
    <td><code>string</code></td>
    <td>Partition count of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionsReassignments" /></td>
    <td><code>object</code></td>
    <td>Partition Reassignment Specification of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationFactor" /></td>
    <td><code>string</code></td>
    <td>Replication factor of the topic.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="topicId" /></td>
    <td><code>string</code></td>
    <td>Topic Id returned by Confluent.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get confluent topic by Name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-pageSize"><code>pageSize</code></a>, <a href="#parameter-pageToken"><code>pageToken</code></a></td>
    <td>Lists of all the topics in a clusters.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create confluent topics by Name.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-topic_name"><code>topic_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete confluent topic by name.</td>
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
<tr id="parameter-cluster_id">
    <td><CopyableCode code="cluster_id" /></td>
    <td><code>string</code></td>
    <td>Confluent kafka or schema registry cluster id. Required.</td>
</tr>
<tr id="parameter-environment_id">
    <td><CopyableCode code="environment_id" /></td>
    <td><code>string</code></td>
    <td>Confluent environment id. Required.</td>
</tr>
<tr id="parameter-organization_name">
    <td><CopyableCode code="organization_name" /></td>
    <td><code>string</code></td>
    <td>Organization resource name. Required.</td>
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
<tr id="parameter-topic_name">
    <td><CopyableCode code="topic_name" /></td>
    <td><code>string</code></td>
    <td>Confluent kafka or schema registry topic name. Required.</td>
</tr>
<tr id="parameter-pageSize">
    <td><CopyableCode code="pageSize" /></td>
    <td><code>integer</code></td>
    <td>Pagination size. Default value is None.</td>
</tr>
<tr id="parameter-pageToken">
    <td><CopyableCode code="pageToken" /></td>
    <td><code>string</code></td>
    <td>An opaque pagination token to fetch the next set of records. Default value is None.</td>
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

Get confluent topic by Name.

```sql
SELECT
id,
name,
configs,
inputConfigs,
kind,
metadata,
partitions,
partitionsCount,
partitionsReassignments,
replicationFactor,
systemData,
topicId,
type
FROM azure_isv.confluent.topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND organization_name = '{{ organization_name }}' -- required
AND environment_id = '{{ environment_id }}' -- required
AND cluster_id = '{{ cluster_id }}' -- required
AND topic_name = '{{ topic_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists of all the topics in a clusters.

```sql
SELECT
id,
name,
configs,
inputConfigs,
kind,
metadata,
partitions,
partitionsCount,
partitionsReassignments,
replicationFactor,
systemData,
topicId,
type
FROM azure_isv.confluent.topics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND organization_name = '{{ organization_name }}' -- required
AND environment_id = '{{ environment_id }}' -- required
AND cluster_id = '{{ cluster_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND pageSize = '{{ pageSize }}'
AND pageToken = '{{ pageToken }}'
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

Create confluent topics by Name.

```sql
INSERT INTO azure_isv.confluent.topics (
properties,
resource_group_name,
organization_name,
environment_id,
cluster_id,
topic_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ organization_name }}',
'{{ environment_id }}',
'{{ cluster_id }}',
'{{ topic_name }}',
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
- name: topics
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the topics resource.
    - name: organization_name
      value: "{{ organization_name }}"
      description: Required parameter for the topics resource.
    - name: environment_id
      value: "{{ environment_id }}"
      description: Required parameter for the topics resource.
    - name: cluster_id
      value: "{{ cluster_id }}"
      description: Required parameter for the topics resource.
    - name: topic_name
      value: "{{ topic_name }}"
      description: Required parameter for the topics resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the topics resource.
    - name: properties
      description: |
        Topic Properties.
      value:
        kind: "{{ kind }}"
        topicId: "{{ topicId }}"
        metadata:
          self: "{{ self }}"
          resourceName: "{{ resourceName }}"
        partitions:
          related: "{{ related }}"
        configs:
          related: "{{ related }}"
        inputConfigs:
          - name: "{{ name }}"
            value: "{{ value }}"
        partitionsReassignments:
          related: "{{ related }}"
        partitionsCount: "{{ partitionsCount }}"
        replicationFactor: "{{ replicationFactor }}"
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

Delete confluent topic by name.

```sql
DELETE FROM azure_isv.confluent.topics
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND environment_id = '{{ environment_id }}' --required
AND cluster_id = '{{ cluster_id }}' --required
AND topic_name = '{{ topic_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
