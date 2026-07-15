--- 
title: solution_template_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - solution_template_versions
  - workload_orchestration
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

Creates, updates, deletes, gets or lists a <code>solution_template_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="solution_template_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.workload_orchestration.solution_template_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_solution_template', value: 'list_by_solution_template' }
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
    <td><CopyableCode code="configurations" /></td>
    <td><code>string</code></td>
    <td>Config expressions for this solution version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="orchestratorType" /></td>
    <td><code>string</code></td>
    <td>Orchestrator type. "TO" (TO)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of resource. Known values are: "Succeeded", "Failed", "Canceled", "Initialized", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, Initialized, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="specification" /></td>
    <td><code>object</code></td>
    <td>App components spec. Required.</td>
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
<TabItem value="list_by_solution_template">

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
    <td><CopyableCode code="configurations" /></td>
    <td><code>string</code></td>
    <td>Config expressions for this solution version. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>If eTag is provided in the response body, it may also be provided as a header per the normal etag convention. Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.</td>
</tr>
<tr>
    <td><CopyableCode code="orchestratorType" /></td>
    <td><code>string</code></td>
    <td>Orchestrator type. "TO" (TO)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of resource. Known values are: "Succeeded", "Failed", "Canceled", "Initialized", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, Initialized, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="specification" /></td>
    <td><code>object</code></td>
    <td>App components spec. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_template_name"><code>solution_template_name</code></a>, <a href="#parameter-solution_template_version_name"><code>solution_template_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Solution Template Version Resource.</td>
</tr>
<tr>
    <td><a href="#list_by_solution_template"><CopyableCode code="list_by_solution_template" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_template_name"><code>solution_template_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Solution Template Version Resources.</td>
</tr>
<tr>
    <td><a href="#bulk_deploy_solution"><CopyableCode code="bulk_deploy_solution" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_template_name"><code>solution_template_name</code></a>, <a href="#parameter-solution_template_version_name"><code>solution_template_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targets"><code>targets</code></a></td>
    <td></td>
    <td>Post request for bulk deploy.</td>
</tr>
<tr>
    <td><a href="#bulk_publish_solution"><CopyableCode code="bulk_publish_solution" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-solution_template_name"><code>solution_template_name</code></a>, <a href="#parameter-solution_template_version_name"><code>solution_template_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-targets"><code>targets</code></a></td>
    <td></td>
    <td>Post request for bulk publish.</td>
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
<tr id="parameter-solution_template_name">
    <td><CopyableCode code="solution_template_name" /></td>
    <td><code>string</code></td>
    <td>The name of the SolutionTemplate. Required.</td>
</tr>
<tr id="parameter-solution_template_version_name">
    <td><CopyableCode code="solution_template_version_name" /></td>
    <td><code>string</code></td>
    <td>The name of the SolutionTemplateVersion. Required.</td>
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
        { label: 'list_by_solution_template', value: 'list_by_solution_template' }
    ]}
>
<TabItem value="get">

Get a Solution Template Version Resource.

```sql
SELECT
id,
name,
configurations,
eTag,
orchestratorType,
provisioningState,
specification,
systemData,
type
FROM azure.workload_orchestration.solution_template_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND solution_template_name = '{{ solution_template_name }}' -- required
AND solution_template_version_name = '{{ solution_template_version_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_solution_template">

List Solution Template Version Resources.

```sql
SELECT
id,
name,
configurations,
eTag,
orchestratorType,
provisioningState,
specification,
systemData,
type
FROM azure.workload_orchestration.solution_template_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND solution_template_name = '{{ solution_template_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="bulk_deploy_solution"
    values={[
        { label: 'bulk_deploy_solution', value: 'bulk_deploy_solution' },
        { label: 'bulk_publish_solution', value: 'bulk_publish_solution' }
    ]}
>
<TabItem value="bulk_deploy_solution">

Post request for bulk deploy.

```sql
EXEC azure.workload_orchestration.solution_template_versions.bulk_deploy_solution 
@resource_group_name='{{ resource_group_name }}' --required, 
@solution_template_name='{{ solution_template_name }}' --required, 
@solution_template_version_name='{{ solution_template_version_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targets": "{{ targets }}"
}'
;
```
</TabItem>
<TabItem value="bulk_publish_solution">

Post request for bulk publish.

```sql
EXEC azure.workload_orchestration.solution_template_versions.bulk_publish_solution 
@resource_group_name='{{ resource_group_name }}' --required, 
@solution_template_name='{{ solution_template_name }}' --required, 
@solution_template_version_name='{{ solution_template_version_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"targets": "{{ targets }}", 
"solutionInstanceName": "{{ solutionInstanceName }}", 
"solutionDependencies": "{{ solutionDependencies }}"
}'
;
```
</TabItem>
</Tabs>
