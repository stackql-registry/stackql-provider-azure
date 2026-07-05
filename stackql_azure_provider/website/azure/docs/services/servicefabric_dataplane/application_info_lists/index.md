--- 
title: application_info_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - application_info_lists
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists an <code>application_info_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="application_info_lists" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.application_info_lists" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_application_info_list"
    values={[
        { label: 'get_application_info_list', value: 'get_application_info_list' }
    ]}
>
<TabItem value="get_application_info_list">

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
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Items" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#get_application_info_list"><CopyableCode code="get_application_info_list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ApplicationDefinitionKindFilter"><code>ApplicationDefinitionKindFilter</code></a>, <a href="#parameter-ApplicationTypeName"><code>ApplicationTypeName</code></a>, <a href="#parameter-ExcludeApplicationParameters"><code>ExcludeApplicationParameters</code></a>, <a href="#parameter-ContinuationToken"><code>ContinuationToken</code></a>, <a href="#parameter-MaxResults"><code>MaxResults</code></a>, <a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Gets the list of applications created in the Service Fabric cluster that match the specified filters. Gets the information about the applications that were created or in the process of being created in the Service Fabric cluster and match the specified filters. The response includes the name, type, status, parameters, and other details about the application. If the applications do not fit in a page, one page of results is returned as well as a continuation token, which can be used to get the next page. Filters ApplicationTypeName and ApplicationDefinitionKindFilter cannot be specified at the same time.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
</tr>
<tr id="parameter-ApplicationDefinitionKindFilter">
    <td><CopyableCode code="ApplicationDefinitionKindFilter" /></td>
    <td><code>integer</code></td>
    <td>Used to filter on ApplicationDefinitionKind, which is the mechanism used to define a Service Fabric application. - Default - Default value, which performs the same function as selecting "All". The value is 0. - All - Filter that matches input with any ApplicationDefinitionKind value. The value is 65535. - ServiceFabricApplicationDescription - Filter that matches input with ApplicationDefinitionKind value ServiceFabricApplicationDescription. The value is 1. - Compose - Filter that matches input with ApplicationDefinitionKind value Compose. The value is 2.</td>
</tr>
<tr id="parameter-ApplicationTypeName">
    <td><CopyableCode code="ApplicationTypeName" /></td>
    <td><code>string</code></td>
    <td>The application type name used to filter the applications to query for. This value should not contain the application type version.</td>
</tr>
<tr id="parameter-ContinuationToken">
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td>The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.</td>
</tr>
<tr id="parameter-ExcludeApplicationParameters">
    <td><CopyableCode code="ExcludeApplicationParameters" /></td>
    <td><code>boolean</code></td>
    <td>The flag that specifies whether application parameters will be excluded from the result.</td>
</tr>
<tr id="parameter-MaxResults">
    <td><CopyableCode code="MaxResults" /></td>
    <td><code>integer (int64)</code></td>
    <td>The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_application_info_list"
    values={[
        { label: 'get_application_info_list', value: 'get_application_info_list' }
    ]}
>
<TabItem value="get_application_info_list">

Gets the list of applications created in the Service Fabric cluster that match the specified filters. Gets the information about the applications that were created or in the process of being created in the Service Fabric cluster and match the specified filters. The response includes the name, type, status, parameters, and other details about the application. If the applications do not fit in a page, one page of results is returned as well as a continuation token, which can be used to get the next page. Filters ApplicationTypeName and ApplicationDefinitionKindFilter cannot be specified at the same time.

```sql
SELECT
ContinuationToken,
Items
FROM azure.servicefabric_dataplane.application_info_lists
WHERE endpoint = '{{ endpoint }}' -- required
AND ApplicationDefinitionKindFilter = '{{ ApplicationDefinitionKindFilter }}'
AND ApplicationTypeName = '{{ ApplicationTypeName }}'
AND ExcludeApplicationParameters = '{{ ExcludeApplicationParameters }}'
AND ContinuationToken = '{{ ContinuationToken }}'
AND MaxResults = '{{ MaxResults }}'
AND timeout = '{{ timeout }}'
;
```
</TabItem>
</Tabs>
