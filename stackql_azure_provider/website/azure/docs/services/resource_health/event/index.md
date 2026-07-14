--- 
title: event
hide_title: false
hide_table_of_contents: false
keywords:
  - event
  - resource_health
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

Creates, updates, deletes, gets or lists an <code>event</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="event" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_health.event" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_subscription_id_and_tracking_id"
    values={[
        { label: 'get_by_subscription_id_and_tracking_id', value: 'get_by_subscription_id_and_tracking_id' },
        { label: 'get_by_tenant_id_and_tracking_id', value: 'get_by_tenant_id_and_tracking_id' }
    ]}
>
<TabItem value="get_by_subscription_id_and_tracking_id">

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
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information.</td>
</tr>
<tr>
    <td><CopyableCode code="article" /></td>
    <td><code>object</code></td>
    <td>Article of event.</td>
</tr>
<tr>
    <td><CopyableCode code="billingId" /></td>
    <td><code>string</code></td>
    <td>Billing identifier information.</td>
</tr>
<tr>
    <td><CopyableCode code="currencyType" /></td>
    <td><code>string</code></td>
    <td>Billing currency type information. Example: USD, CAD.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Contains the communication message for the event, that could include summary, root cause and other details. Use fetchEventDetails endpoint to get description of sensitive events.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td>duration in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="enableChatWithUs" /></td>
    <td><code>boolean</code></td>
    <td>Tells if we want to enable or disable Microsoft Support for this event.</td>
</tr>
<tr>
    <td><CopyableCode code="enableMicrosoftSupport" /></td>
    <td><code>boolean</code></td>
    <td>Tells if we want to enable or disable Microsoft Support for this event.</td>
</tr>
<tr>
    <td><CopyableCode code="eventLevel" /></td>
    <td><code>string</code></td>
    <td>Level of event. Known values are: "Critical", "Error", "Warning", and "Informational". (Critical, Error, Warning, Informational)</td>
</tr>
<tr>
    <td><CopyableCode code="eventSource" /></td>
    <td><code>string</code></td>
    <td>Source of event. Known values are: "ResourceHealth" and "ServiceHealth". (ResourceHealth, ServiceHealth)</td>
</tr>
<tr>
    <td><CopyableCode code="eventSubType" /></td>
    <td><code>string</code></td>
    <td>Sub-type of event. Known values are: "Retirement", "ForeignExchangeRateChange", "Underbilling", "Overbilling", "PriceChanges", "TaxChanges", "MeterIDChanges", and "UnauthorizedPartyAbuse". (Retirement, ForeignExchangeRateChange, Underbilling, Overbilling, PriceChanges, TaxChanges, MeterIDChanges, UnauthorizedPartyAbuse)</td>
</tr>
<tr>
    <td><CopyableCode code="eventTags" /></td>
    <td><code>array</code></td>
    <td>A list of metadata tags associated with the event. Possible values include: -Action Recommended: Action may be required by you to avoid possible disruptions or mitigate risks for your services. It is recommended to evaluate these actions and the potential impact on your services. * False Positive: After investigation, we've determined your service is healthy and service issues did not impact your services as originally communicated. * Preliminary PIR: For our largest, most impactful service issues a Preliminary Post Incident Review (PIR) is published generally within 72 hours of mitigation, to summarize what we have learned so far from the still-in-progress investigation. * Final PIR: For service issues, a Final Post Incident Review (PIR) may be published to provide additional details or learnings. Sometimes this requires us to complete an internal retrospective, generally within 14 days of mitigation.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>Type of event. Known values are: "ServiceIssue", "PlannedMaintenance", "HealthAdvisory", "RCA", "EmergingIssues", "SecurityAdvisory", and "Billing". (ServiceIssue, PlannedMaintenance, HealthAdvisory, RCA, EmergingIssues, SecurityAdvisory, Billing)</td>
</tr>
<tr>
    <td><CopyableCode code="externalIncidentId" /></td>
    <td><code>string</code></td>
    <td>The id of the Incident.</td>
</tr>
<tr>
    <td><CopyableCode code="faqs" /></td>
    <td><code>array</code></td>
    <td>Frequently asked questions for the service health event.</td>
</tr>
<tr>
    <td><CopyableCode code="header" /></td>
    <td><code>string</code></td>
    <td>Header text of event.</td>
</tr>
<tr>
    <td><CopyableCode code="hirStage" /></td>
    <td><code>string</code></td>
    <td>Stage for HIR Document.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>array</code></td>
    <td>List services impacted by the service health event.</td>
</tr>
<tr>
    <td><CopyableCode code="impactMitigationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>It provides the Timestamp for when the health impacting event resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="impactStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>It provides the Timestamp for when the health impacting event started.</td>
</tr>
<tr>
    <td><CopyableCode code="impactType" /></td>
    <td><code>string</code></td>
    <td>The type of the impact.</td>
</tr>
<tr>
    <td><CopyableCode code="isEventSensitive" /></td>
    <td><code>boolean</code></td>
    <td>If true the event may contains sensitive data. Use the post events/&#123;trackingId&#125;/fetchEventDetails endpoint to fetch sensitive data see `https://learn.microsoft.com/en-us/azure/service-health/security-advisories-elevated-access `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isHIR" /></td>
    <td><code>boolean</code></td>
    <td>It provides information if the event is High incident rate event or not.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>It provides the Timestamp for when the health impacting event was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level of insight. Known values are: "Critical" and "Warning". (Critical, Warning)</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Useful links of event.</td>
</tr>
<tr>
    <td><CopyableCode code="newRate" /></td>
    <td><code>number</code></td>
    <td>Billing rate change information - new rate.</td>
</tr>
<tr>
    <td><CopyableCode code="oldRate" /></td>
    <td><code>number</code></td>
    <td>Billing rate change information - old rate.</td>
</tr>
<tr>
    <td><CopyableCode code="platformInitiated" /></td>
    <td><code>boolean</code></td>
    <td>Is true if the event is platform initiated.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority level of the event. Has value from 0 to 23. 0 is the highest priority. Service issue events have higher priority followed by planned maintenance and health advisory. Critical events have higher priority followed by error, warning and informational. Furthermore, active events have higher priority than resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason for the Incident.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedActions" /></td>
    <td><code>object</code></td>
    <td>Recommended actions of event.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of event. Known values are: "Active" and "Resolved". (Active, Resolved)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>Summary text of event. Use fetchEventDetails endpoint to get summary of sensitive events.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Title text of event.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_by_tenant_id_and_tracking_id">

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
    <td><CopyableCode code="additionalInformation" /></td>
    <td><code>object</code></td>
    <td>Additional information.</td>
</tr>
<tr>
    <td><CopyableCode code="article" /></td>
    <td><code>object</code></td>
    <td>Article of event.</td>
</tr>
<tr>
    <td><CopyableCode code="billingId" /></td>
    <td><code>string</code></td>
    <td>Billing identifier information.</td>
</tr>
<tr>
    <td><CopyableCode code="currencyType" /></td>
    <td><code>string</code></td>
    <td>Billing currency type information. Example: USD, CAD.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Contains the communication message for the event, that could include summary, root cause and other details. Use fetchEventDetails endpoint to get description of sensitive events.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>integer</code></td>
    <td>duration in seconds.</td>
</tr>
<tr>
    <td><CopyableCode code="enableChatWithUs" /></td>
    <td><code>boolean</code></td>
    <td>Tells if we want to enable or disable Microsoft Support for this event.</td>
</tr>
<tr>
    <td><CopyableCode code="enableMicrosoftSupport" /></td>
    <td><code>boolean</code></td>
    <td>Tells if we want to enable or disable Microsoft Support for this event.</td>
</tr>
<tr>
    <td><CopyableCode code="eventLevel" /></td>
    <td><code>string</code></td>
    <td>Level of event. Known values are: "Critical", "Error", "Warning", and "Informational". (Critical, Error, Warning, Informational)</td>
</tr>
<tr>
    <td><CopyableCode code="eventSource" /></td>
    <td><code>string</code></td>
    <td>Source of event. Known values are: "ResourceHealth" and "ServiceHealth". (ResourceHealth, ServiceHealth)</td>
</tr>
<tr>
    <td><CopyableCode code="eventSubType" /></td>
    <td><code>string</code></td>
    <td>Sub-type of event. Known values are: "Retirement", "ForeignExchangeRateChange", "Underbilling", "Overbilling", "PriceChanges", "TaxChanges", "MeterIDChanges", and "UnauthorizedPartyAbuse". (Retirement, ForeignExchangeRateChange, Underbilling, Overbilling, PriceChanges, TaxChanges, MeterIDChanges, UnauthorizedPartyAbuse)</td>
</tr>
<tr>
    <td><CopyableCode code="eventTags" /></td>
    <td><code>array</code></td>
    <td>A list of metadata tags associated with the event. Possible values include: -Action Recommended: Action may be required by you to avoid possible disruptions or mitigate risks for your services. It is recommended to evaluate these actions and the potential impact on your services. * False Positive: After investigation, we've determined your service is healthy and service issues did not impact your services as originally communicated. * Preliminary PIR: For our largest, most impactful service issues a Preliminary Post Incident Review (PIR) is published generally within 72 hours of mitigation, to summarize what we have learned so far from the still-in-progress investigation. * Final PIR: For service issues, a Final Post Incident Review (PIR) may be published to provide additional details or learnings. Sometimes this requires us to complete an internal retrospective, generally within 14 days of mitigation.</td>
</tr>
<tr>
    <td><CopyableCode code="eventType" /></td>
    <td><code>string</code></td>
    <td>Type of event. Known values are: "ServiceIssue", "PlannedMaintenance", "HealthAdvisory", "RCA", "EmergingIssues", "SecurityAdvisory", and "Billing". (ServiceIssue, PlannedMaintenance, HealthAdvisory, RCA, EmergingIssues, SecurityAdvisory, Billing)</td>
</tr>
<tr>
    <td><CopyableCode code="externalIncidentId" /></td>
    <td><code>string</code></td>
    <td>The id of the Incident.</td>
</tr>
<tr>
    <td><CopyableCode code="faqs" /></td>
    <td><code>array</code></td>
    <td>Frequently asked questions for the service health event.</td>
</tr>
<tr>
    <td><CopyableCode code="header" /></td>
    <td><code>string</code></td>
    <td>Header text of event.</td>
</tr>
<tr>
    <td><CopyableCode code="hirStage" /></td>
    <td><code>string</code></td>
    <td>Stage for HIR Document.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>array</code></td>
    <td>List services impacted by the service health event.</td>
</tr>
<tr>
    <td><CopyableCode code="impactMitigationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>It provides the Timestamp for when the health impacting event resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="impactStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>It provides the Timestamp for when the health impacting event started.</td>
</tr>
<tr>
    <td><CopyableCode code="impactType" /></td>
    <td><code>string</code></td>
    <td>The type of the impact.</td>
</tr>
<tr>
    <td><CopyableCode code="isEventSensitive" /></td>
    <td><code>boolean</code></td>
    <td>If true the event may contains sensitive data. Use the post events/&#123;trackingId&#125;/fetchEventDetails endpoint to fetch sensitive data see `https://learn.microsoft.com/en-us/azure/service-health/security-advisories-elevated-access `_.</td>
</tr>
<tr>
    <td><CopyableCode code="isHIR" /></td>
    <td><code>boolean</code></td>
    <td>It provides information if the event is High incident rate event or not.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>It provides the Timestamp for when the health impacting event was last updated.</td>
</tr>
<tr>
    <td><CopyableCode code="level" /></td>
    <td><code>string</code></td>
    <td>Level of insight. Known values are: "Critical" and "Warning". (Critical, Warning)</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>array</code></td>
    <td>Useful links of event.</td>
</tr>
<tr>
    <td><CopyableCode code="newRate" /></td>
    <td><code>number</code></td>
    <td>Billing rate change information - new rate.</td>
</tr>
<tr>
    <td><CopyableCode code="oldRate" /></td>
    <td><code>number</code></td>
    <td>Billing rate change information - old rate.</td>
</tr>
<tr>
    <td><CopyableCode code="platformInitiated" /></td>
    <td><code>boolean</code></td>
    <td>Is true if the event is platform initiated.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority level of the event. Has value from 0 to 23. 0 is the highest priority. Service issue events have higher priority followed by planned maintenance and health advisory. Critical events have higher priority followed by error, warning and informational. Furthermore, active events have higher priority than resolved.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason for the Incident.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendedActions" /></td>
    <td><code>object</code></td>
    <td>Recommended actions of event.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Current status of event. Known values are: "Active" and "Resolved". (Active, Resolved)</td>
</tr>
<tr>
    <td><CopyableCode code="summary" /></td>
    <td><code>string</code></td>
    <td>Summary text of event. Use fetchEventDetails endpoint to get summary of sensitive events.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Title text of event.</td>
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
    <td><a href="#get_by_subscription_id_and_tracking_id"><CopyableCode code="get_by_subscription_id_and_tracking_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-event_tracking_id"><code>event_tracking_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-queryStartTime"><code>queryStartTime</code></a></td>
    <td>Service health event in the subscription by event tracking id.</td>
</tr>
<tr>
    <td><a href="#get_by_tenant_id_and_tracking_id"><CopyableCode code="get_by_tenant_id_and_tracking_id" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-event_tracking_id"><code>event_tracking_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-queryStartTime"><code>queryStartTime</code></a></td>
    <td>Service health event in the tenant by event tracking id.</td>
</tr>
<tr>
    <td><a href="#fetch_details_by_subscription_id_and_tracking_id"><CopyableCode code="fetch_details_by_subscription_id_and_tracking_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-event_tracking_id"><code>event_tracking_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Service health event details in the subscription by event tracking id. This can be used to fetch sensitive properties for Security Advisory events. Please see `https://learn.microsoft.com/en-us/azure/service-health/security-advisories-elevated-access `_.</td>
</tr>
<tr>
    <td><a href="#fetch_billling_communication_details_by_subscription_id_and_tracking_id"><CopyableCode code="fetch_billling_communication_details_by_subscription_id_and_tracking_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-event_tracking_id"><code>event_tracking_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Service health event details specific in the subscription by event tracking id. This can be used to fetch sensitive properties for Billing event type.</td>
</tr>
<tr>
    <td><a href="#fetch_details_by_tenant_id_and_tracking_id"><CopyableCode code="fetch_details_by_tenant_id_and_tracking_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-event_tracking_id"><code>event_tracking_id</code></a></td>
    <td></td>
    <td>Service health event details in the tenant by event tracking id. This can be used to fetch sensitive properties for Security Advisory events. Please see `https://learn.microsoft.com/en-us/azure/service-health/security-advisories-elevated-access `_.</td>
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
<tr id="parameter-event_tracking_id">
    <td><CopyableCode code="event_tracking_id" /></td>
    <td><code>string</code></td>
    <td>Event Id which uniquely identifies ServiceHealth event. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. For more information please see `https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN `_. Default value is None.</td>
</tr>
<tr id="parameter-queryStartTime">
    <td><CopyableCode code="queryStartTime" /></td>
    <td><code>string</code></td>
    <td>Specifies from when to return events (default is 3 days), based on the lastUpdateTime property. For example, queryStartTime = 7/24/2020 OR queryStartTime=7%2F24%2F2020. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_subscription_id_and_tracking_id"
    values={[
        { label: 'get_by_subscription_id_and_tracking_id', value: 'get_by_subscription_id_and_tracking_id' },
        { label: 'get_by_tenant_id_and_tracking_id', value: 'get_by_tenant_id_and_tracking_id' }
    ]}
>
<TabItem value="get_by_subscription_id_and_tracking_id">

Service health event in the subscription by event tracking id.

```sql
SELECT
id,
name,
additionalInformation,
article,
billingId,
currencyType,
description,
duration,
enableChatWithUs,
enableMicrosoftSupport,
eventLevel,
eventSource,
eventSubType,
eventTags,
eventType,
externalIncidentId,
faqs,
header,
hirStage,
impact,
impactMitigationTime,
impactStartTime,
impactType,
isEventSensitive,
isHIR,
lastUpdateTime,
level,
links,
newRate,
oldRate,
platformInitiated,
priority,
reason,
recommendedActions,
status,
summary,
systemData,
title,
type
FROM azure.resource_health.event
WHERE event_tracking_id = '{{ event_tracking_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND queryStartTime = '{{ queryStartTime }}'
;
```
</TabItem>
<TabItem value="get_by_tenant_id_and_tracking_id">

Service health event in the tenant by event tracking id.

```sql
SELECT
id,
name,
additionalInformation,
article,
billingId,
currencyType,
description,
duration,
enableChatWithUs,
enableMicrosoftSupport,
eventLevel,
eventSource,
eventSubType,
eventTags,
eventType,
externalIncidentId,
faqs,
header,
hirStage,
impact,
impactMitigationTime,
impactStartTime,
impactType,
isEventSensitive,
isHIR,
lastUpdateTime,
level,
links,
newRate,
oldRate,
platformInitiated,
priority,
reason,
recommendedActions,
status,
summary,
systemData,
title,
type
FROM azure.resource_health.event
WHERE event_tracking_id = '{{ event_tracking_id }}' -- required
AND $filter = '{{ $filter }}'
AND queryStartTime = '{{ queryStartTime }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="fetch_details_by_subscription_id_and_tracking_id"
    values={[
        { label: 'fetch_details_by_subscription_id_and_tracking_id', value: 'fetch_details_by_subscription_id_and_tracking_id' },
        { label: 'fetch_billling_communication_details_by_subscription_id_and_tracking_id', value: 'fetch_billling_communication_details_by_subscription_id_and_tracking_id' },
        { label: 'fetch_details_by_tenant_id_and_tracking_id', value: 'fetch_details_by_tenant_id_and_tracking_id' }
    ]}
>
<TabItem value="fetch_details_by_subscription_id_and_tracking_id">

Service health event details in the subscription by event tracking id. This can be used to fetch sensitive properties for Security Advisory events. Please see `https://learn.microsoft.com/en-us/azure/service-health/security-advisories-elevated-access `_.

```sql
EXEC azure.resource_health.event.fetch_details_by_subscription_id_and_tracking_id 
@event_tracking_id='{{ event_tracking_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="fetch_billling_communication_details_by_subscription_id_and_tracking_id">

Service health event details specific in the subscription by event tracking id. This can be used to fetch sensitive properties for Billing event type.

```sql
EXEC azure.resource_health.event.fetch_billling_communication_details_by_subscription_id_and_tracking_id 
@event_tracking_id='{{ event_tracking_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="fetch_details_by_tenant_id_and_tracking_id">

Service health event details in the tenant by event tracking id. This can be used to fetch sensitive properties for Security Advisory events. Please see `https://learn.microsoft.com/en-us/azure/service-health/security-advisories-elevated-access `_.

```sql
EXEC azure.resource_health.event.fetch_details_by_tenant_id_and_tracking_id 
@event_tracking_id='{{ event_tracking_id }}' --required
;
```
</TabItem>
</Tabs>
