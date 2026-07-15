--- 
title: deployment_info
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_info
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

Creates, updates, deletes, gets or lists a <code>deployment_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployment_info" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.elastic.deployment_info" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td><CopyableCode code="configurationType" /></td>
    <td><code>string</code></td>
    <td>ConfigurationType Type - Applicable for Serverless only.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentUrl" /></td>
    <td><code>string</code></td>
    <td>Deployment URL of the elasticsearch in Elastic cloud deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="diskCapacity" /></td>
    <td><code>string</code></td>
    <td>Disk capacity of the elasticsearch in Elastic cloud deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="elasticsearchEndPoint" /></td>
    <td><code>string</code></td>
    <td>Elasticsearch endpoint in Elastic cloud deployment. This is either the aliased_endpoint if available, or the service_url otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceSaasInfo" /></td>
    <td><code>object</code></td>
    <td>Marketplace SaaS Info of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="memoryCapacity" /></td>
    <td><code>string</code></td>
    <td>RAM capacity of the elasticsearch in Elastic cloud deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="projectType" /></td>
    <td><code>string</code></td>
    <td>Project Type - Applicable for Serverless only.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The Elastic deployment status. Known values are: "Healthy" and "Unhealthy".</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>Version of the elasticsearch in Elastic cloud deployment.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Fetch detailed information about Elastic cloud deployments corresponding to the Elastic monitor resource. Fetch detailed information about Elastic cloud deployments corresponding to the Elastic monitor resource.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Fetch detailed information about Elastic cloud deployments corresponding to the Elastic monitor resource. Fetch detailed information about Elastic cloud deployments corresponding to the Elastic monitor resource.

```sql
SELECT
configurationType,
deploymentUrl,
diskCapacity,
elasticsearchEndPoint,
marketplaceSaasInfo,
memoryCapacity,
projectType,
status,
version
FROM azure_isv.elastic.deployment_info
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
