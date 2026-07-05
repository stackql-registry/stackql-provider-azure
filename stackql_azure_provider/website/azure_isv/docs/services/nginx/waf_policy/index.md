--- 
title: waf_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - waf_policy
  - nginx
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

Creates, updates, deletes, gets or lists a <code>waf_policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="waf_policy" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.nginx.waf_policy" /></td></tr>
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
    <td><CopyableCode code="applyingState" /></td>
    <td><code>object</code></td>
    <td>Nginx Deployment Waf Policy Applying Status.</td>
</tr>
<tr>
    <td><CopyableCode code="compilingState" /></td>
    <td><code>object</code></td>
    <td>Nginx Deployment Waf Policy Compiling Status.</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>string (byte)</code></td>
    <td>The byte content of the Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="filepath" /></td>
    <td><code>string</code></td>
    <td>The file path where the Policy is to be saved.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified". (Accepted, Creating, Updating, Deleting, Succeeded, Failed, Canceled, Deleted, NotSpecified)</td>
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
    <td>:vartype id: str</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>:vartype name: str</td>
</tr>
<tr>
    <td><CopyableCode code="applyingState" /></td>
    <td><code>object</code></td>
    <td>Nginx Deployment Waf Policy Applying Status.</td>
</tr>
<tr>
    <td><CopyableCode code="compilingState" /></td>
    <td><code>object</code></td>
    <td>Nginx Deployment Waf Policy Compiling Status.</td>
</tr>
<tr>
    <td><CopyableCode code="filepath" /></td>
    <td><code>string</code></td>
    <td>:vartype filepath: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified". (Accepted, Creating, Updating, Deleting, Succeeded, Failed, Canceled, Deleted, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>:vartype type: str</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-waf_policy_name"><code>waf_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the Nginx Waf Policy of given Nginx deployment.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Waf Policies of given Nginx deployment.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-waf_policy_name"><code>waf_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update the Nginx Waf Policy for given Nginx deployment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-waf_policy_name"><code>waf_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reset the Nginx Waf Policy of given Nginx deployment to default.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The name of targeted NGINX deployment. Required.</td>
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
<tr id="parameter-waf_policy_name">
    <td><CopyableCode code="waf_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of Waf Policy. Required.</td>
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

Get the Nginx Waf Policy of given Nginx deployment.

```sql
SELECT
id,
name,
applyingState,
compilingState,
content,
filepath,
provisioningState,
systemData,
type
FROM azure_isv.nginx.waf_policy
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND waf_policy_name = '{{ waf_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Waf Policies of given Nginx deployment.

```sql
SELECT
id,
name,
applyingState,
compilingState,
filepath,
provisioningState,
systemData,
type
FROM azure_isv.nginx.waf_policy
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
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

Create or update the Nginx Waf Policy for given Nginx deployment.

```sql
INSERT INTO azure_isv.nginx.waf_policy (
properties,
resource_group_name,
deployment_name,
waf_policy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ deployment_name }}',
'{{ waf_policy_name }}',
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
- name: waf_policy
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the waf_policy resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the waf_policy resource.
    - name: waf_policy_name
      value: "{{ waf_policy_name }}"
      description: Required parameter for the waf_policy resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the waf_policy resource.
    - name: properties
      description: |
        Nginx Deployment Waf Policy Properties.
      value:
        provisioningState: "{{ provisioningState }}"
        content: "{{ content }}"
        filepath: "{{ filepath }}"
        compilingState:
          code: "{{ code }}"
          displayStatus: "{{ displayStatus }}"
          time: "{{ time }}"
        applyingState:
          code: "{{ code }}"
          displayStatus: "{{ displayStatus }}"
          time: "{{ time }}"
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

Reset the Nginx Waf Policy of given Nginx deployment to default.

```sql
DELETE FROM azure_isv.nginx.waf_policy
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND waf_policy_name = '{{ waf_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
