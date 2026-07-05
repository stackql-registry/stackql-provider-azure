--- 
title: child_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - child_resources
  - resourcehealth
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

Creates, updates, deletes, gets or lists a <code>child_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="child_resources" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resourcehealth.child_resources" /></td></tr>
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
    <td><CopyableCode code="id" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager Identity for the availabilityStatuses resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>:vartype name: str</td>
</tr>
<tr>
    <td><CopyableCode code="articleId" /></td>
    <td><code>string</code></td>
    <td>The Article Id.</td>
</tr>
<tr>
    <td><CopyableCode code="availabilityState" /></td>
    <td><code>string</code></td>
    <td>Availability status of the resource. When it is null, this availabilityStatus object represents an availability impacting event. Known values are: "Available", "Unavailable", "Degraded", and "Unknown". (Available, Unavailable, Degraded, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>When a context field is set to Platform, this field will reflect if the event was planned or unplanned. If the context field does not have a value of Platform, then this field will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="context" /></td>
    <td><code>string</code></td>
    <td>When an event is created, it can either be triggered by a customer or the platform of the resource and this field will illustrate that. This field is connected to the category field in this object.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedStatus" /></td>
    <td><code>string</code></td>
    <td>Details of the availability status.</td>
</tr>
<tr>
    <td><CopyableCode code="healthEventCategory" /></td>
    <td><code>string</code></td>
    <td>In case of an availability impacting event, it describes the category of a PlatformInitiated health impacting event. Examples are Planned, Unplanned etc.</td>
</tr>
<tr>
    <td><CopyableCode code="healthEventCause" /></td>
    <td><code>string</code></td>
    <td>In case of an availability impacting event, it describes where the health impacting event was originated. Examples are PlatformInitiated, UserInitiated etc.</td>
</tr>
<tr>
    <td><CopyableCode code="healthEventId" /></td>
    <td><code>string</code></td>
    <td>It is a unique Id that identifies the event.</td>
</tr>
<tr>
    <td><CopyableCode code="healthEventType" /></td>
    <td><code>string</code></td>
    <td>In case of an availability impacting event, it describes when the health impacting event was originated. Examples are Lifecycle, Downtime, Fault Analysis etc.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Manager geo location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="occuredTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for when last change in health status occurred.</td>
</tr>
<tr>
    <td><CopyableCode code="reasonChronicity" /></td>
    <td><code>string</code></td>
    <td>Chronicity of the availability transition. Known values are: "Transient" and "Persistent". (Transient, Persistent)</td>
</tr>
<tr>
    <td><CopyableCode code="reasonType" /></td>
    <td><code>string</code></td>
    <td>When the resource's availabilityState is Unavailable, it describes where the health impacting event was originated. Examples are planned, unplanned, user initiated or an outage etc.</td>
</tr>
<tr>
    <td><CopyableCode code="recentlyResolved" /></td>
    <td><code>object</code></td>
    <td>An annotation describing a change in the availabilityState to Available from Unavailable with a reasonType of type Unplanned.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedActions" /></td>
    <td><code>array</code></td>
    <td>Lists actions the user can take based on the current availabilityState of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="reportedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp for when the health was last checked.</td>
</tr>
<tr>
    <td><CopyableCode code="resolutionETA" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the resource's availabilityState is Unavailable and the reasonType is not User Initiated, it provides the date and time for when the issue is expected to be resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="rootCauseAttributionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>When the resource's availabilityState is Unavailable, it provides the Timestamp for when the health impacting event was received.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceImpactingEvents" /></td>
    <td><code>array</code></td>
    <td>Lists the service impacting events that may be affecting the health of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>Summary description of the availability status.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Title description of the availability status.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Microsoft.ResourceHealth/AvailabilityStatuses.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists the all the children and its current health status for a parent resource. Use the nextLink property in the response to get the next page of children current health.</td>
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
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Setting $expand=recommendedactions in url query expands the recommendedactions in the response. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. For more information please see `https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN `_. Default value is None.</td>
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

Lists the all the children and its current health status for a parent resource. Use the nextLink property in the response to get the next page of children current health.

```sql
SELECT
id,
name,
articleId,
availabilityState,
category,
context,
detailedStatus,
healthEventCategory,
healthEventCause,
healthEventId,
healthEventType,
location,
occuredTime,
reasonChronicity,
reasonType,
recentlyResolved,
recommendedActions,
reportedTime,
resolutionETA,
rootCauseAttributionTime,
serviceImpactingEvents,
summary,
title,
type
FROM azure.resourcehealth.child_resources
WHERE resource_uri = '{{ resource_uri }}' -- required
AND $filter = '{{ $filter }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>
