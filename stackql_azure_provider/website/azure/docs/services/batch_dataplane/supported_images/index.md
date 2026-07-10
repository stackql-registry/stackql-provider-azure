--- 
title: supported_images
hide_title: false
hide_table_of_contents: false
keywords:
  - supported_images
  - batch_dataplane
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

Creates, updates, deletes, gets or lists a <code>supported_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="supported_images" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.supported_images" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_supported_images"
    values={[
        { label: 'list_supported_images', value: 'list_supported_images' }
    ]}
>
<TabItem value="list_supported_images">

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
    <td><CopyableCode code="batchSupportEndOfLife" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time when the Azure Batch service will stop accepting create Pool requests for the Image.</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>The capabilities or features which the Image supports. Not every capability of the Image is listed. Capabilities in this list are considered of special interest and are generally related to integration with other features in the Azure Batch service.</td>
</tr>
<tr>
    <td><CopyableCode code="imageReference" /></td>
    <td><code>object</code></td>
    <td>The reference to the Azure Virtual Machine's Marketplace Image. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nodeAgentSKUId" /></td>
    <td><code>string</code></td>
    <td>The ID of the Compute Node agent SKU which the Image supports. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The type of operating system (e.g. Windows or Linux) of the Image. Required. Known values are: "linux" and "windows". (linux, windows)</td>
</tr>
<tr>
    <td><CopyableCode code="verificationType" /></td>
    <td><code>string</code></td>
    <td>Whether the Azure Batch service actively verifies that the Image is compatible with the associated Compute Node agent SKU. Required. Known values are: "verified" and "unverified". (verified, unverified)</td>
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
    <td><a href="#list_supported_images"><CopyableCode code="list_supported_images" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists all Virtual Machine Images supported by the Azure Batch service. Lists all Virtual Machine Images supported by the Azure Batch service.</td>
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
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-support-images `_. Default value is None.</td>
</tr>
<tr id="parameter-maxresults">
    <td><CopyableCode code="maxresults" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of items to return in the response. A maximum of 1000 applications can be returned. Default value is None.</td>
</tr>
<tr id="parameter-ocp-date">
    <td><CopyableCode code="ocp-date" /></td>
    <td><code>string</code></td>
    <td>The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.</td>
</tr>
<tr id="parameter-timeOut">
    <td><CopyableCode code="timeOut" /></td>
    <td><code>integer</code></td>
    <td>The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_supported_images"
    values={[
        { label: 'list_supported_images', value: 'list_supported_images' }
    ]}
>
<TabItem value="list_supported_images">

Lists all Virtual Machine Images supported by the Azure Batch service. Lists all Virtual Machine Images supported by the Azure Batch service.

```sql
SELECT
batchSupportEndOfLife,
capabilities,
imageReference,
nodeAgentSKUId,
osType,
verificationType
FROM azure.batch_dataplane.supported_images
WHERE endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND maxresults = '{{ maxresults }}'
AND $filter = '{{ $filter }}'
;
```
</TabItem>
</Tabs>
