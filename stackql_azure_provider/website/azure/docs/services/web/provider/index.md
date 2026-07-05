--- 
title: provider
hide_title: false
hide_table_of_contents: false
keywords:
  - provider
  - web
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

Creates, updates, deletes, gets or lists a <code>provider</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="provider" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.provider" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_function_app_stacks_for_location"
    values={[
        { label: 'get_function_app_stacks_for_location', value: 'get_function_app_stacks_for_location' },
        { label: 'get_available_stacks_on_prem', value: 'get_available_stacks_on_prem' },
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="get_function_app_stacks_for_location">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="displayText" /></td>
    <td><code>string</code></td>
    <td>Function App stack (display only).</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Function App stack location.</td>
</tr>
<tr>
    <td><CopyableCode code="majorVersions" /></td>
    <td><code>array</code></td>
    <td>List of major versions available.</td>
</tr>
<tr>
    <td><CopyableCode code="preferredOs" /></td>
    <td><code>string</code></td>
    <td>Function App stack preferred OS. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="value" /></td>
    <td><code>string</code></td>
    <td>Function App stack name.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_available_stacks_on_prem">

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
    <td>Resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource Name.</td>
</tr>
<tr>
    <td><CopyableCode code="dependency" /></td>
    <td><code>string</code></td>
    <td>Application stack dependency.</td>
</tr>
<tr>
    <td><CopyableCode code="display" /></td>
    <td><code>string</code></td>
    <td>Application stack display name.</td>
</tr>
<tr>
    <td><CopyableCode code="frameworks" /></td>
    <td><code>array</code></td>
    <td>List of frameworks associated with application stack.</td>
</tr>
<tr>
    <td><CopyableCode code="isDeprecated" /></td>
    <td><code>array</code></td>
    <td>true if this is the stack is deprecated; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="majorVersions" /></td>
    <td><code>array</code></td>
    <td>List of major versions available.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_operations">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>:vartype name: str</td>
</tr>
<tr>
    <td><CopyableCode code="display" /></td>
    <td><code>object</code></td>
    <td>Meta data about operation used for display in portal.</td>
</tr>
<tr>
    <td><CopyableCode code="isDataAction" /></td>
    <td><code>boolean</code></td>
    <td>:vartype is_data_action: bool</td>
</tr>
<tr>
    <td><CopyableCode code="origin" /></td>
    <td><code>string</code></td>
    <td>:vartype origin: str</td>
</tr>
<tr>
    <td><CopyableCode code="serviceSpecification" /></td>
    <td><code>object</code></td>
    <td>Resource metrics service provided by Microsoft.Insights resource provider.</td>
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
    <td><a href="#get_function_app_stacks_for_location"><CopyableCode code="get_function_app_stacks_for_location" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-stackOsType"><code>stackOsType</code></a></td>
    <td>Get available Function app frameworks and their versions for location. Description for Get available Function app frameworks and their versions for location.</td>
</tr>
<tr>
    <td><a href="#get_available_stacks_on_prem"><CopyableCode code="get_available_stacks_on_prem" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-osTypeSelected"><code>osTypeSelected</code></a></td>
    <td>Get available application frameworks and their versions. Description for Get available application frameworks and their versions.</td>
</tr>
<tr>
    <td><a href="#list_operations"><CopyableCode code="list_operations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions. Description for Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions.</td>
</tr>
<tr>
    <td><a href="#get_available_stacks"><CopyableCode code="get_available_stacks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td><a href="#parameter-osTypeSelected"><code>osTypeSelected</code></a></td>
    <td>Get available application frameworks and their versions. Description for Get available application frameworks and their versions.</td>
</tr>
<tr>
    <td><a href="#get_function_app_stacks"><CopyableCode code="get_function_app_stacks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td><a href="#parameter-stackOsType"><code>stackOsType</code></a></td>
    <td>Get available Function app frameworks and their versions. Description for Get available Function app frameworks and their versions.</td>
</tr>
<tr>
    <td><a href="#get_web_app_stacks_for_location"><CopyableCode code="get_web_app_stacks_for_location" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a></td>
    <td><a href="#parameter-stackOsType"><code>stackOsType</code></a></td>
    <td>Get available Web app frameworks and their versions for location. Description for Get available Web app frameworks and their versions for location.</td>
</tr>
<tr>
    <td><a href="#get_web_app_stacks"><CopyableCode code="get_web_app_stacks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td></td>
    <td><a href="#parameter-stackOsType"><code>stackOsType</code></a></td>
    <td>Get available Web app frameworks and their versions. Description for Get available Web app frameworks and their versions.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-osTypeSelected">
    <td><CopyableCode code="osTypeSelected" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Windows", "Linux", "WindowsFunctions", "LinuxFunctions", and "All". Default value is None.</td>
</tr>
<tr id="parameter-stackOsType">
    <td><CopyableCode code="stackOsType" /></td>
    <td><code>string</code></td>
    <td>Stack OS Type. Known values are: "Windows", "Linux", and "All". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_function_app_stacks_for_location"
    values={[
        { label: 'get_function_app_stacks_for_location', value: 'get_function_app_stacks_for_location' },
        { label: 'get_available_stacks_on_prem', value: 'get_available_stacks_on_prem' },
        { label: 'list_operations', value: 'list_operations' }
    ]}
>
<TabItem value="get_function_app_stacks_for_location">

Get available Function app frameworks and their versions for location. Description for Get available Function app frameworks and their versions for location.

```sql
SELECT
id,
name,
displayText,
kind,
location,
majorVersions,
preferredOs,
type,
value
FROM azure.web.provider
WHERE location = '{{ location }}' -- required
AND stackOsType = '{{ stackOsType }}'
;
```
</TabItem>
<TabItem value="get_available_stacks_on_prem">

Get available application frameworks and their versions. Description for Get available application frameworks and their versions.

```sql
SELECT
id,
name,
dependency,
display,
frameworks,
isDeprecated,
kind,
majorVersions,
type
FROM azure.web.provider
WHERE subscription_id = '{{ subscription_id }}' -- required
AND osTypeSelected = '{{ osTypeSelected }}'
;
```
</TabItem>
<TabItem value="list_operations">

Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions. Description for Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions.

```sql
SELECT
name,
display,
isDataAction,
origin,
serviceSpecification
FROM azure.web.provider
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_available_stacks"
    values={[
        { label: 'get_available_stacks', value: 'get_available_stacks' },
        { label: 'get_function_app_stacks', value: 'get_function_app_stacks' },
        { label: 'get_web_app_stacks_for_location', value: 'get_web_app_stacks_for_location' },
        { label: 'get_web_app_stacks', value: 'get_web_app_stacks' }
    ]}
>
<TabItem value="get_available_stacks">

Get available application frameworks and their versions. Description for Get available application frameworks and their versions.

```sql
EXEC azure.web.provider.get_available_stacks 
@osTypeSelected='{{ osTypeSelected }}'
;
```
</TabItem>
<TabItem value="get_function_app_stacks">

Get available Function app frameworks and their versions. Description for Get available Function app frameworks and their versions.

```sql
EXEC azure.web.provider.get_function_app_stacks 
@stackOsType='{{ stackOsType }}'
;
```
</TabItem>
<TabItem value="get_web_app_stacks_for_location">

Get available Web app frameworks and their versions for location. Description for Get available Web app frameworks and their versions for location.

```sql
EXEC azure.web.provider.get_web_app_stacks_for_location 
@location='{{ location }}' --required, 
@stackOsType='{{ stackOsType }}'
;
```
</TabItem>
<TabItem value="get_web_app_stacks">

Get available Web app frameworks and their versions. Description for Get available Web app frameworks and their versions.

```sql
EXEC azure.web.provider.get_web_app_stacks 
@stackOsType='{{ stackOsType }}'
;
```
</TabItem>
</Tabs>
