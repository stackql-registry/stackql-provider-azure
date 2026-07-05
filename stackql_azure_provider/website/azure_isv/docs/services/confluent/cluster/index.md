--- 
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
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

Creates, updates, deletes, gets or lists a <code>cluster</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cluster" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.confluent.cluster" /></td></tr>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create confluent clusters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create confluent clusters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-environment_id"><code>environment_id</code></a>, <a href="#parameter-cluster_id"><code>cluster_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete confluent cluster by id.</td>
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

Create confluent clusters.

```sql
INSERT INTO azure_isv.confluent.cluster (
kind,
properties,
resource_group_name,
organization_name,
environment_id,
cluster_id,
subscription_id
)
SELECT 
'{{ kind }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ organization_name }}',
'{{ environment_id }}',
'{{ cluster_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: cluster
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cluster resource.
    - name: organization_name
      value: "{{ organization_name }}"
      description: Required parameter for the cluster resource.
    - name: environment_id
      value: "{{ environment_id }}"
      description: Required parameter for the cluster resource.
    - name: cluster_id
      value: "{{ cluster_id }}"
      description: Required parameter for the cluster resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cluster resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Type of cluster.
    - name: properties
      description: |
        Cluster Properties.
      value:
        metadata:
          self: "{{ self }}"
          resourceName: "{{ resourceName }}"
          createdTimestamp: "{{ createdTimestamp }}"
          updatedTimestamp: "{{ updatedTimestamp }}"
          deletedTimestamp: "{{ deletedTimestamp }}"
        spec:
          name: "{{ name }}"
          availability: "{{ availability }}"
          cloud: "{{ cloud }}"
          zone: "{{ zone }}"
          package: "{{ package }}"
          region: "{{ region }}"
          kafkaBootstrapEndpoint: "{{ kafkaBootstrapEndpoint }}"
          httpEndpoint: "{{ httpEndpoint }}"
          apiEndpoint: "{{ apiEndpoint }}"
          config:
            kind: "{{ kind }}"
          environment:
            id: "{{ id }}"
            environment: "{{ environment }}"
            related: "{{ related }}"
            resourceName: "{{ resourceName }}"
          network:
            id: "{{ id }}"
            environment: "{{ environment }}"
            related: "{{ related }}"
            resourceName: "{{ resourceName }}"
          byok:
            id: "{{ id }}"
            related: "{{ related }}"
            resourceName: "{{ resourceName }}"
        status:
          phase: "{{ phase }}"
          cku: {{ cku }}
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

Create confluent clusters.

```sql
REPLACE azure_isv.confluent.cluster
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND environment_id = '{{ environment_id }}' --required
AND cluster_id = '{{ cluster_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
type;
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

Delete confluent cluster by id.

```sql
DELETE FROM azure_isv.confluent.cluster
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND environment_id = '{{ environment_id }}' --required
AND cluster_id = '{{ cluster_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
