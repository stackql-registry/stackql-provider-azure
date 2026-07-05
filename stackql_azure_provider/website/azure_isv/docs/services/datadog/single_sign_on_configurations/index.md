--- 
title: single_sign_on_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - single_sign_on_configurations
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

Creates, updates, deletes, gets or lists a <code>single_sign_on_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="single_sign_on_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.single_sign_on_configurations" /></td></tr>
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
    <td>ARM id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="enterpriseAppId" /></td>
    <td><code>string</code></td>
    <td>The Id of the Enterprise App used for Single sign-on.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="singleSignOnState" /></td>
    <td><code>string</code></td>
    <td>Various states of the SSO resource. Known values are: "Initial", "Enable", "Disable", and "Existing".</td>
</tr>
<tr>
    <td><CopyableCode code="singleSignOnUrl" /></td>
    <td><code>string</code></td>
    <td>The login URL specific to this Datadog Organization.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>ARM id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="enterpriseAppId" /></td>
    <td><code>string</code></td>
    <td>The Id of the Enterprise App used for Single sign-on.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="singleSignOnState" /></td>
    <td><code>string</code></td>
    <td>Various states of the SSO resource. Known values are: "Initial", "Enable", "Disable", and "Existing".</td>
</tr>
<tr>
    <td><CopyableCode code="singleSignOnUrl" /></td>
    <td><code>string</code></td>
    <td>The login URL specific to this Datadog Organization.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the datadog single sign-on resource for the given Monitor. Gets the datadog single sign-on resource for the given Monitor.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the single sign-on configurations for a given monitor resource. List the single sign-on configurations for a given monitor resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Configures single-sign-on for this resource. Configures single-sign-on for this resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-monitor_name"><code>monitor_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Configures single-sign-on for this resource. Configures single-sign-on for this resource.</td>
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
<tr id="parameter-configuration_name">
    <td><CopyableCode code="configuration_name" /></td>
    <td><code>string</code></td>
    <td>Configuration name. Required.</td>
</tr>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the datadog single sign-on resource for the given Monitor. Gets the datadog single sign-on resource for the given Monitor.

```sql
SELECT
id,
name,
enterpriseAppId,
provisioningState,
singleSignOnState,
singleSignOnUrl,
systemData,
type
FROM azure_isv.datadog.single_sign_on_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND monitor_name = '{{ monitor_name }}' -- required
AND configuration_name = '{{ configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the single sign-on configurations for a given monitor resource. List the single sign-on configurations for a given monitor resource.

```sql
SELECT
id,
name,
enterpriseAppId,
provisioningState,
singleSignOnState,
singleSignOnUrl,
systemData,
type
FROM azure_isv.datadog.single_sign_on_configurations
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

Configures single-sign-on for this resource. Configures single-sign-on for this resource.

```sql
INSERT INTO azure_isv.datadog.single_sign_on_configurations (
properties,
resource_group_name,
monitor_name,
configuration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ monitor_name }}',
'{{ configuration_name }}',
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
- name: single_sign_on_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the single_sign_on_configurations resource.
    - name: monitor_name
      value: "{{ monitor_name }}"
      description: Required parameter for the single_sign_on_configurations resource.
    - name: configuration_name
      value: "{{ configuration_name }}"
      description: Required parameter for the single_sign_on_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the single_sign_on_configurations resource.
    - name: properties
      description: |
        :vartype properties: ~azure.mgmt.datadog.models.DatadogSingleSignOnProperties
      value:
        provisioningState: "{{ provisioningState }}"
        singleSignOnState: "{{ singleSignOnState }}"
        enterpriseAppId: "{{ enterpriseAppId }}"
        singleSignOnUrl: "{{ singleSignOnUrl }}"
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

Configures single-sign-on for this resource. Configures single-sign-on for this resource.

```sql
REPLACE azure_isv.datadog.single_sign_on_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND monitor_name = '{{ monitor_name }}' --required
AND configuration_name = '{{ configuration_name }}' --required
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
