--- 
title: web_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - web_tests
  - applicationinsights
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

Creates, updates, deletes, gets or lists a <code>web_tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="web_tests" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.applicationinsights.web_tests" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_component', value: 'list_by_component' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="Configuration" /></td>
    <td><code>object</code></td>
    <td>An XML configuration specification for a WebTest.</td>
</tr>
<tr>
    <td><CopyableCode code="Description" /></td>
    <td><code>string</code></td>
    <td>User defined description for this WebTest.</td>
</tr>
<tr>
    <td><CopyableCode code="Enabled" /></td>
    <td><code>boolean</code></td>
    <td>Is the test actively being monitored.</td>
</tr>
<tr>
    <td><CopyableCode code="Frequency" /></td>
    <td><code>integer</code></td>
    <td>Interval in seconds between test runs for this WebTest. Default value is 300.</td>
</tr>
<tr>
    <td><CopyableCode code="Kind" /></td>
    <td><code>string</code></td>
    <td>The kind of web test this is, valid choices are ping, multistep and standard. Required. Known values are: "ping", "multistep", and "standard". (ping, multistep, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="Locations" /></td>
    <td><code>array</code></td>
    <td>A list of where to physically run the tests from to give global coverage for accessibility of your application. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>User defined name if this WebTest. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Request" /></td>
    <td><code>object</code></td>
    <td>The collection of request properties.</td>
</tr>
<tr>
    <td><CopyableCode code="RetryEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Allow for retries should this WebTest fail.</td>
</tr>
<tr>
    <td><CopyableCode code="SyntheticMonitorId" /></td>
    <td><code>string</code></td>
    <td>Unique ID of this WebTest. This is typically the same value as the Name field. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Timeout" /></td>
    <td><code>integer</code></td>
    <td>Seconds until this WebTest will timeout and fail. Default value is 30.</td>
</tr>
<tr>
    <td><CopyableCode code="ValidationRules" /></td>
    <td><code>object</code></td>
    <td>The collection of validation rule properties.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of WebTest that this web test watches. Choices are ping, multistep and standard. Known values are: "ping", "multistep", and "standard". (ping, multistep, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this component, whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_component">

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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="Configuration" /></td>
    <td><code>object</code></td>
    <td>An XML configuration specification for a WebTest.</td>
</tr>
<tr>
    <td><CopyableCode code="Description" /></td>
    <td><code>string</code></td>
    <td>User defined description for this WebTest.</td>
</tr>
<tr>
    <td><CopyableCode code="Enabled" /></td>
    <td><code>boolean</code></td>
    <td>Is the test actively being monitored.</td>
</tr>
<tr>
    <td><CopyableCode code="Frequency" /></td>
    <td><code>integer</code></td>
    <td>Interval in seconds between test runs for this WebTest. Default value is 300.</td>
</tr>
<tr>
    <td><CopyableCode code="Kind" /></td>
    <td><code>string</code></td>
    <td>The kind of web test this is, valid choices are ping, multistep and standard. Required. Known values are: "ping", "multistep", and "standard". (ping, multistep, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="Locations" /></td>
    <td><code>array</code></td>
    <td>A list of where to physically run the tests from to give global coverage for accessibility of your application. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>User defined name if this WebTest. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Request" /></td>
    <td><code>object</code></td>
    <td>The collection of request properties.</td>
</tr>
<tr>
    <td><CopyableCode code="RetryEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Allow for retries should this WebTest fail.</td>
</tr>
<tr>
    <td><CopyableCode code="SyntheticMonitorId" /></td>
    <td><code>string</code></td>
    <td>Unique ID of this WebTest. This is typically the same value as the Name field. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Timeout" /></td>
    <td><code>integer</code></td>
    <td>Seconds until this WebTest will timeout and fail. Default value is 30.</td>
</tr>
<tr>
    <td><CopyableCode code="ValidationRules" /></td>
    <td><code>object</code></td>
    <td>The collection of validation rule properties.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of WebTest that this web test watches. Choices are ping, multistep and standard. Known values are: "ping", "multistep", and "standard". (ping, multistep, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this component, whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="Configuration" /></td>
    <td><code>object</code></td>
    <td>An XML configuration specification for a WebTest.</td>
</tr>
<tr>
    <td><CopyableCode code="Description" /></td>
    <td><code>string</code></td>
    <td>User defined description for this WebTest.</td>
</tr>
<tr>
    <td><CopyableCode code="Enabled" /></td>
    <td><code>boolean</code></td>
    <td>Is the test actively being monitored.</td>
</tr>
<tr>
    <td><CopyableCode code="Frequency" /></td>
    <td><code>integer</code></td>
    <td>Interval in seconds between test runs for this WebTest. Default value is 300.</td>
</tr>
<tr>
    <td><CopyableCode code="Kind" /></td>
    <td><code>string</code></td>
    <td>The kind of web test this is, valid choices are ping, multistep and standard. Required. Known values are: "ping", "multistep", and "standard". (ping, multistep, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="Locations" /></td>
    <td><code>array</code></td>
    <td>A list of where to physically run the tests from to give global coverage for accessibility of your application. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>User defined name if this WebTest. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Request" /></td>
    <td><code>object</code></td>
    <td>The collection of request properties.</td>
</tr>
<tr>
    <td><CopyableCode code="RetryEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Allow for retries should this WebTest fail.</td>
</tr>
<tr>
    <td><CopyableCode code="SyntheticMonitorId" /></td>
    <td><code>string</code></td>
    <td>Unique ID of this WebTest. This is typically the same value as the Name field. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Timeout" /></td>
    <td><code>integer</code></td>
    <td>Seconds until this WebTest will timeout and fail. Default value is 30.</td>
</tr>
<tr>
    <td><CopyableCode code="ValidationRules" /></td>
    <td><code>object</code></td>
    <td>The collection of validation rule properties.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of WebTest that this web test watches. Choices are ping, multistep and standard. Known values are: "ping", "multistep", and "standard". (ping, multistep, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this component, whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="Configuration" /></td>
    <td><code>object</code></td>
    <td>An XML configuration specification for a WebTest.</td>
</tr>
<tr>
    <td><CopyableCode code="Description" /></td>
    <td><code>string</code></td>
    <td>User defined description for this WebTest.</td>
</tr>
<tr>
    <td><CopyableCode code="Enabled" /></td>
    <td><code>boolean</code></td>
    <td>Is the test actively being monitored.</td>
</tr>
<tr>
    <td><CopyableCode code="Frequency" /></td>
    <td><code>integer</code></td>
    <td>Interval in seconds between test runs for this WebTest. Default value is 300.</td>
</tr>
<tr>
    <td><CopyableCode code="Kind" /></td>
    <td><code>string</code></td>
    <td>The kind of web test this is, valid choices are ping, multistep and standard. Required. Known values are: "ping", "multistep", and "standard". (ping, multistep, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="Locations" /></td>
    <td><code>array</code></td>
    <td>A list of where to physically run the tests from to give global coverage for accessibility of your application. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Name" /></td>
    <td><code>string</code></td>
    <td>User defined name if this WebTest. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Request" /></td>
    <td><code>object</code></td>
    <td>The collection of request properties.</td>
</tr>
<tr>
    <td><CopyableCode code="RetryEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Allow for retries should this WebTest fail.</td>
</tr>
<tr>
    <td><CopyableCode code="SyntheticMonitorId" /></td>
    <td><code>string</code></td>
    <td>Unique ID of this WebTest. This is typically the same value as the Name field. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="Timeout" /></td>
    <td><code>integer</code></td>
    <td>Seconds until this WebTest will timeout and fail. Default value is 30.</td>
</tr>
<tr>
    <td><CopyableCode code="ValidationRules" /></td>
    <td><code>object</code></td>
    <td>The collection of validation rule properties.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of WebTest that this web test watches. Choices are ping, multistep and standard. Known values are: "ping", "multistep", and "standard". (ping, multistep, standard)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Current state of this component, whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-web_test_name"><code>web_test_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a specific Application Insights web test definition.</td>
</tr>
<tr>
    <td><a href="#list_by_component"><CopyableCode code="list_by_component" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-component_name"><code>component_name</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Application Insights web tests defined for the specified component.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Application Insights web tests defined for the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all Application Insights web test definitions for the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-web_test_name"><code>web_test_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an Application Insights web test definition.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-web_test_name"><code>web_test_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the tags associated with an Application Insights web test.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-web_test_name"><code>web_test_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates an Application Insights web test definition.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-web_test_name"><code>web_test_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Application Insights web test.</td>
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
<tr id="parameter-component_name">
    <td><CopyableCode code="component_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights component resource. Required.</td>
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
<tr id="parameter-web_test_name">
    <td><CopyableCode code="web_test_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Application Insights WebTest resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_component', value: 'list_by_component' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get a specific Application Insights web test definition.

```sql
SELECT
id,
name,
Configuration,
Description,
Enabled,
Frequency,
Kind,
Locations,
Name,
Request,
RetryEnabled,
SyntheticMonitorId,
Timeout,
ValidationRules,
kind,
location,
provisioningState,
tags,
type
FROM azure.applicationinsights.web_tests
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND web_test_name = '{{ web_test_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_component">

Get all Application Insights web tests defined for the specified component.

```sql
SELECT
id,
name,
Configuration,
Description,
Enabled,
Frequency,
Kind,
Locations,
Name,
Request,
RetryEnabled,
SyntheticMonitorId,
Timeout,
ValidationRules,
kind,
location,
provisioningState,
tags,
type
FROM azure.applicationinsights.web_tests
WHERE component_name = '{{ component_name }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all Application Insights web tests defined for the specified resource group.

```sql
SELECT
id,
name,
Configuration,
Description,
Enabled,
Frequency,
Kind,
Locations,
Name,
Request,
RetryEnabled,
SyntheticMonitorId,
Timeout,
ValidationRules,
kind,
location,
provisioningState,
tags,
type
FROM azure.applicationinsights.web_tests
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all Application Insights web test definitions for the specified subscription.

```sql
SELECT
id,
name,
Configuration,
Description,
Enabled,
Frequency,
Kind,
Locations,
Name,
Request,
RetryEnabled,
SyntheticMonitorId,
Timeout,
ValidationRules,
kind,
location,
provisioningState,
tags,
type
FROM azure.applicationinsights.web_tests
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates or updates an Application Insights web test definition.

```sql
INSERT INTO azure.applicationinsights.web_tests (
location,
tags,
kind,
properties,
resource_group_name,
web_test_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ kind }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ web_test_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: web_tests
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the web_tests resource.
    - name: web_test_name
      value: "{{ web_test_name }}"
      description: Required parameter for the web_tests resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the web_tests resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of WebTest that this web test watches. Choices are ping, multistep and standard. Known values are: "ping", "multistep", and "standard".
      valid_values: ['ping', 'multistep', 'standard']
    - name: properties
      description: |
        Metadata describing a web test for an Azure resource.
      value:
        SyntheticMonitorId: "{{ SyntheticMonitorId }}"
        Name: "{{ Name }}"
        Description: "{{ Description }}"
        Enabled: {{ Enabled }}
        Frequency: {{ Frequency }}
        Timeout: {{ Timeout }}
        Kind: "{{ Kind }}"
        RetryEnabled: {{ RetryEnabled }}
        Locations:
          - Id: "{{ Id }}"
        Configuration:
          WebTest: "{{ WebTest }}"
        provisioningState: "{{ provisioningState }}"
        Request:
          RequestUrl: "{{ RequestUrl }}"
          Headers:
            - key: "{{ key }}"
              value: "{{ value }}"
          HttpVerb: "{{ HttpVerb }}"
          RequestBody: "{{ RequestBody }}"
          ParseDependentRequests: {{ ParseDependentRequests }}
          FollowRedirects: {{ FollowRedirects }}
        ValidationRules:
          ContentValidation:
            ContentMatch: "{{ ContentMatch }}"
            IgnoreCase: {{ IgnoreCase }}
            PassIfTextFound: {{ PassIfTextFound }}
          SSLCheck: {{ SSLCheck }}
          SSLCertRemainingLifetimeCheck: {{ SSLCertRemainingLifetimeCheck }}
          ExpectedHttpStatusCode: {{ ExpectedHttpStatusCode }}
          IgnoreHttpStatusCode: {{ IgnoreHttpStatusCode }}
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates the tags associated with an Application Insights web test.

```sql
UPDATE azure.applicationinsights.web_tests
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND web_test_name = '{{ web_test_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
location,
properties,
tags,
type;
```
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

Creates or updates an Application Insights web test definition.

```sql
REPLACE azure.applicationinsights.web_tests
SET 
location = '{{ location }}',
tags = '{{ tags }}',
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND web_test_name = '{{ web_test_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
kind,
location,
properties,
tags,
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

Deletes an Application Insights web test.

```sql
DELETE FROM azure.applicationinsights.web_tests
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND web_test_name = '{{ web_test_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
