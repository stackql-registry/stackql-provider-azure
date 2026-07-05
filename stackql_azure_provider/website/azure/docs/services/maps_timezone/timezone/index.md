--- 
title: timezone
hide_title: false
hide_table_of_contents: false
keywords:
  - timezone
  - maps_timezone
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

Creates, updates, deletes, gets or lists a <code>timezone</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="timezone" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maps_timezone.timezone" /></td></tr>
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
    <td><a href="#get_timezone_by_id"><CopyableCode code="get_timezone_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-Accept-Language"><code>Accept-Language</code></a>, <a href="#parameter-options"><code>options</code></a>, <a href="#parameter-timeStamp"><code>timeStamp</code></a>, <a href="#parameter-transitionsFrom"><code>transitionsFrom</code></a>, <a href="#parameter-transitionsYears"><code>transitionsYears</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get the current, historical, and future time zone information for the specified IANA time zone ID. The `Get Timezone By ID` API is an HTTP `GET` request that returns current, historical, and future time zone information for the specified IANA time zone ID.</td>
</tr>
<tr>
    <td><a href="#get_timezone_by_coordinates"><CopyableCode code="get_timezone_by_coordinates" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-Accept-Language"><code>Accept-Language</code></a>, <a href="#parameter-options"><code>options</code></a>, <a href="#parameter-timeStamp"><code>timeStamp</code></a>, <a href="#parameter-transitionsFrom"><code>transitionsFrom</code></a>, <a href="#parameter-transitionsYears"><code>transitionsYears</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get the current, historical, and future time zone information for the specified latitude-longitude pair. The `Get Timezone By Coordinates` API is an HTTP `GET` request that returns current, historical, and future time zone information for a specified latitude-longitude pair. In addition, the API provides sunset and sunrise times for a given location.</td>
</tr>
<tr>
    <td><a href="#get_windows_timezone_ids"><CopyableCode code="get_windows_timezone_ids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get the list of Windows Time Zone IDs. The `Get Windows Time Zones` API is an HTTP `GET` request that returns a full list of Windows Time Zone IDs.</td>
</tr>
<tr>
    <td><a href="#get_iana_timezone_ids"><CopyableCode code="get_iana_timezone_ids" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get the list of IANA time zone IDs. The `Get IANA Time Zones` API is an HTTP `GET` request that returns a full list of Internet Assigned Numbers Authority (IANA) time zone IDs. Updates to the IANA service are reflected in the system within one day.</td>
</tr>
<tr>
    <td><a href="#get_iana_version"><CopyableCode code="get_iana_version" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get the current IANA version number. The `Get Time Zone IANA Version` API is an HTTP `GET` request that returns the current Internet Assigned Numbers Authority (IANA) version number as Metadata.</td>
</tr>
<tr>
    <td><a href="#convert_windows_timezone_to_iana"><CopyableCode code="convert_windows_timezone_to_iana" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-format"><code>format</code></a>, <a href="#parameter-query"><code>query</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-territory"><code>territory</code></a>, <a href="#parameter-x-ms-client-id"><code>x-ms-client-id</code></a></td>
    <td>Use to get the IANA ID. The `Get Windows to IANA Time Zone` API is an HTTP `GET` request that returns a corresponding Internet Assigned Numbers Authority (IANA) ID, given a valid Windows Time Zone ID. Multiple IANA IDs may be returned for a single Windows ID. It is possible to narrow these results by adding an optional territory parameter.</td>
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
<tr id="parameter-format">
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>Desired format of the response. Only `json` format is supported. "json" Default value is "json".</td>
</tr>
<tr id="parameter-query">
    <td><CopyableCode code="query" /></td>
    <td><code>string</code></td>
    <td>The Windows time zone ID. Required.</td>
</tr>
<tr id="parameter-Accept-Language">
    <td><CopyableCode code="Accept-Language" /></td>
    <td><code>string</code></td>
    <td>Specifies the language code in which the timezone names should be returned. If no language code is provided, the response will be in "EN". Please refer to `Supported Languages `_ for details. Default value is None.</td>
</tr>
<tr id="parameter-options">
    <td><CopyableCode code="options" /></td>
    <td><code>string</code></td>
    <td>Alternatively, use alias "o". Options available for types of information returned in the result. Known values are: "none", "zoneInfo", "transitions", and "all". Default value is None.</td>
</tr>
<tr id="parameter-territory">
    <td><CopyableCode code="territory" /></td>
    <td><code>string</code></td>
    <td>Windows Time Zone territory code. Default value is None.</td>
</tr>
<tr id="parameter-timeStamp">
    <td><CopyableCode code="timeStamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>Alternatively, use alias "stamp", or "s". Reference time, if omitted, the API will use the machine time serving the request. Default value is None.</td>
</tr>
<tr id="parameter-transitionsFrom">
    <td><CopyableCode code="transitionsFrom" /></td>
    <td><code>string (date-time)</code></td>
    <td>Alternatively, use alias "tf". The start date from which daylight savings time (DST) transitions are requested, only applies when "options" = all or "options" = transitions. Default value is None.</td>
</tr>
<tr id="parameter-transitionsYears">
    <td><CopyableCode code="transitionsYears" /></td>
    <td><code>integer</code></td>
    <td>Alternatively, use alias "ty". The number of years from "transitionsFrom" for which DST transitions are requested, only applies when "options" = all or "options" = transitions. Default value is None.</td>
</tr>
<tr id="parameter-x-ms-client-id">
    <td><CopyableCode code="x-ms-client-id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="get_timezone_by_id"
    values={[
        { label: 'get_timezone_by_id', value: 'get_timezone_by_id' },
        { label: 'get_timezone_by_coordinates', value: 'get_timezone_by_coordinates' },
        { label: 'get_windows_timezone_ids', value: 'get_windows_timezone_ids' },
        { label: 'get_iana_timezone_ids', value: 'get_iana_timezone_ids' },
        { label: 'get_iana_version', value: 'get_iana_version' },
        { label: 'convert_windows_timezone_to_iana', value: 'convert_windows_timezone_to_iana' }
    ]}
>
<TabItem value="get_timezone_by_id">

Use to get the current, historical, and future time zone information for the specified IANA time zone ID. The `Get Timezone By ID` API is an HTTP `GET` request that returns current, historical, and future time zone information for the specified IANA time zone ID.

```sql
EXEC azure.maps_timezone.timezone.get_timezone_by_id 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@Accept-Language='{{ Accept-Language }}', 
@options='{{ options }}', 
@timeStamp='{{ timeStamp }}', 
@transitionsFrom='{{ transitionsFrom }}', 
@transitionsYears='{{ transitionsYears }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_timezone_by_coordinates">

Use to get the current, historical, and future time zone information for the specified latitude-longitude pair. The `Get Timezone By Coordinates` API is an HTTP `GET` request that returns current, historical, and future time zone information for a specified latitude-longitude pair. In addition, the API provides sunset and sunrise times for a given location.

```sql
EXEC azure.maps_timezone.timezone.get_timezone_by_coordinates 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@Accept-Language='{{ Accept-Language }}', 
@options='{{ options }}', 
@timeStamp='{{ timeStamp }}', 
@transitionsFrom='{{ transitionsFrom }}', 
@transitionsYears='{{ transitionsYears }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_windows_timezone_ids">

Use to get the list of Windows Time Zone IDs. The `Get Windows Time Zones` API is an HTTP `GET` request that returns a full list of Windows Time Zone IDs.

```sql
EXEC azure.maps_timezone.timezone.get_windows_timezone_ids 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_iana_timezone_ids">

Use to get the list of IANA time zone IDs. The `Get IANA Time Zones` API is an HTTP `GET` request that returns a full list of Internet Assigned Numbers Authority (IANA) time zone IDs. Updates to the IANA service are reflected in the system within one day.

```sql
EXEC azure.maps_timezone.timezone.get_iana_timezone_ids 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="get_iana_version">

Use to get the current IANA version number. The `Get Time Zone IANA Version` API is an HTTP `GET` request that returns the current Internet Assigned Numbers Authority (IANA) version number as Metadata.

```sql
EXEC azure.maps_timezone.timezone.get_iana_version 
@format='{{ format }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
<TabItem value="convert_windows_timezone_to_iana">

Use to get the IANA ID. The `Get Windows to IANA Time Zone` API is an HTTP `GET` request that returns a corresponding Internet Assigned Numbers Authority (IANA) ID, given a valid Windows Time Zone ID. Multiple IANA IDs may be returned for a single Windows ID. It is possible to narrow these results by adding an optional territory parameter.

```sql
EXEC azure.maps_timezone.timezone.convert_windows_timezone_to_iana 
@format='{{ format }}' --required, 
@query='{{ query }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@territory='{{ territory }}', 
@x-ms-client-id='{{ x-ms-client-id }}'
;
```
</TabItem>
</Tabs>
