--- 
title: support_tickets_no_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - support_tickets_no_subscription
  - support
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

Creates, updates, deletes, gets or lists a <code>support_tickets_no_subscription</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="support_tickets_no_subscription" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.support_tickets_no_subscription" /></td></tr>
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
    <td>Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="advancedDiagnosticConsent" /></td>
    <td><code>string</code></td>
    <td>Advanced diagnostic consent to be updated on the support ticket. Required. Known values are: "Yes" and "No".</td>
</tr>
<tr>
    <td><CopyableCode code="contactDetails" /></td>
    <td><code>object</code></td>
    <td>Contact information of the user requesting to create a support ticket. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when the support ticket was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the question or issue. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentId" /></td>
    <td><code>string</code></td>
    <td>Enrollment Id associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="fileWorkspaceName" /></td>
    <td><code>string</code></td>
    <td>File workspace name.</td>
</tr>
<tr>
    <td><CopyableCode code="isTemporaryTicket" /></td>
    <td><code>string</code></td>
    <td>This property indicates if support ticket is a temporary ticket. Known values are: "Yes" and "No".</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when the support ticket was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="problemClassificationDisplayName" /></td>
    <td><code>string</code></td>
    <td>Localized name of problem classification.</td>
</tr>
<tr>
    <td><CopyableCode code="problemClassificationId" /></td>
    <td><code>string</code></td>
    <td>Each Azure service has its own set of issue categories, also known as problem classification. This parameter is the unique Id for the type of problem you are experiencing. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="problemScopingQuestions" /></td>
    <td><code>string</code></td>
    <td>Problem scoping questions associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="problemStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when the problem started.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaTicketDetails" /></td>
    <td><code>object</code></td>
    <td>Additional ticket details associated with a quota support ticket request.</td>
</tr>
<tr>
    <td><CopyableCode code="require24X7Response" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if this requires a 24x7 response from Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryConsent" /></td>
    <td><code>array</code></td>
    <td>This property indicates secondary consents for the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceDisplayName" /></td>
    <td><code>string</code></td>
    <td>Localized name of the Azure service.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceId" /></td>
    <td><code>string</code></td>
    <td>This is the resource Id of the Azure service resource associated with the support ticket. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevelAgreement" /></td>
    <td><code>object</code></td>
    <td>Service Level Agreement information for this support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>A value that indicates the urgency of the case, which in turn determines the response time according to the service level agreement of the technical support plan you have with Azure. Note: 'Highest critical impact', also known as the 'Emergency - Severe impact' level in the Azure portal is reserved only for our Premium customers. Required. Known values are: "minimal", "moderate", "critical", and "highestcriticalimpact".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportEngineer" /></td>
    <td><code>object</code></td>
    <td>Information about the support engineer working on this support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlanDisplayName" /></td>
    <td><code>string</code></td>
    <td>Support plan type associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlanId" /></td>
    <td><code>string</code></td>
    <td>Support plan id associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlanType" /></td>
    <td><code>string</code></td>
    <td>Support plan type associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportTicketId" /></td>
    <td><code>string</code></td>
    <td>System generated support ticket Id that is unique.</td>
</tr>
<tr>
    <td><CopyableCode code="technicalTicketDetails" /></td>
    <td><code>object</code></td>
    <td>Additional ticket details associated with a technical support ticket request.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Title of the support ticket. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the resource 'Microsoft.Support/supportTickets'.</td>
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
    <td>Id of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="advancedDiagnosticConsent" /></td>
    <td><code>string</code></td>
    <td>Advanced diagnostic consent to be updated on the support ticket. Required. Known values are: "Yes" and "No".</td>
</tr>
<tr>
    <td><CopyableCode code="contactDetails" /></td>
    <td><code>object</code></td>
    <td>Contact information of the user requesting to create a support ticket. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when the support ticket was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Detailed description of the question or issue. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="enrollmentId" /></td>
    <td><code>string</code></td>
    <td>Enrollment Id associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="fileWorkspaceName" /></td>
    <td><code>string</code></td>
    <td>File workspace name.</td>
</tr>
<tr>
    <td><CopyableCode code="isTemporaryTicket" /></td>
    <td><code>string</code></td>
    <td>This property indicates if support ticket is a temporary ticket. Known values are: "Yes" and "No".</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when the support ticket was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="problemClassificationDisplayName" /></td>
    <td><code>string</code></td>
    <td>Localized name of problem classification.</td>
</tr>
<tr>
    <td><CopyableCode code="problemClassificationId" /></td>
    <td><code>string</code></td>
    <td>Each Azure service has its own set of issue categories, also known as problem classification. This parameter is the unique Id for the type of problem you are experiencing. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="problemScopingQuestions" /></td>
    <td><code>string</code></td>
    <td>Problem scoping questions associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="problemStartTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time in UTC (ISO 8601 format) when the problem started.</td>
</tr>
<tr>
    <td><CopyableCode code="quotaTicketDetails" /></td>
    <td><code>object</code></td>
    <td>Additional ticket details associated with a quota support ticket request.</td>
</tr>
<tr>
    <td><CopyableCode code="require24X7Response" /></td>
    <td><code>boolean</code></td>
    <td>Indicates if this requires a 24x7 response from Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryConsent" /></td>
    <td><code>array</code></td>
    <td>This property indicates secondary consents for the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceDisplayName" /></td>
    <td><code>string</code></td>
    <td>Localized name of the Azure service.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceId" /></td>
    <td><code>string</code></td>
    <td>This is the resource Id of the Azure service resource associated with the support ticket. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceLevelAgreement" /></td>
    <td><code>object</code></td>
    <td>Service Level Agreement information for this support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>A value that indicates the urgency of the case, which in turn determines the response time according to the service level agreement of the technical support plan you have with Azure. Note: 'Highest critical impact', also known as the 'Emergency - Severe impact' level in the Azure portal is reserved only for our Premium customers. Required. Known values are: "minimal", "moderate", "critical", and "highestcriticalimpact".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportEngineer" /></td>
    <td><code>object</code></td>
    <td>Information about the support engineer working on this support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlanDisplayName" /></td>
    <td><code>string</code></td>
    <td>Support plan type associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlanId" /></td>
    <td><code>string</code></td>
    <td>Support plan id associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportPlanType" /></td>
    <td><code>string</code></td>
    <td>Support plan type associated with the support ticket.</td>
</tr>
<tr>
    <td><CopyableCode code="supportTicketId" /></td>
    <td><code>string</code></td>
    <td>System generated support ticket Id that is unique.</td>
</tr>
<tr>
    <td><CopyableCode code="technicalTicketDetails" /></td>
    <td><code>object</code></td>
    <td>Additional ticket details associated with a technical support ticket request.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>Title of the support ticket. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Type of the resource 'Microsoft.Support/supportTickets'.</td>
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
    <td><a href="#parameter-support_ticket_name"><code>support_ticket_name</code></a></td>
    <td></td>
    <td>Gets details for a specific support ticket. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Lists all the support tickets. You can also filter the support tickets by Status, CreatedDate, , ServiceId, and ProblemClassificationId using the $filter parameter. Output will be a paged result with nextLink, using which you can retrieve the next set of support tickets. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-support_ticket_name"><code>support_ticket_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a new support ticket for Billing, and Subscription Management issues. Learn the `prerequisites `_ required to create a support ticket.Always call the Services and ProblemClassifications API to get the most recent set of services and problem categories required for support ticket creation.Adding attachments is not currently supported via the API. To add a file to an existing support ticket, visit the `Manage support ticket `_ page in the Azure portal, select the support ticket, and use the file upload control to add a new file.Providing consent to share diagnostic information with Azure support is currently not supported via the API. The Azure support engineer working on your ticket will reach out to you for consent if your issue requires gathering diagnostic information from your Azure resources..</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-support_ticket_name"><code>support_ticket_name</code></a></td>
    <td></td>
    <td>This API allows you to update the severity level, ticket status, and your contact information in the support ticket.Note: The severity levels cannot be changed if a support ticket is actively being worked upon by an Azure support engineer. In such a case, contact your support engineer to request severity update by adding a new communication using the Communications API.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-type"><code>type</code></a></td>
    <td></td>
    <td>Check the availability of a resource name. This API should be used to check the uniqueness of the name for support ticket creation for the selected subscription.</td>
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
<tr id="parameter-support_ticket_name">
    <td><CopyableCode code="support_ticket_name" /></td>
    <td><code>string</code></td>
    <td>Support ticket name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. We support 'odata v4.0' filter semantics.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of values to return in the collection. Default is 25 and max is 100. Default value is None.</td>
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

Gets details for a specific support ticket. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error.

```sql
SELECT
id,
name,
advancedDiagnosticConsent,
contactDetails,
createdDate,
description,
enrollmentId,
fileWorkspaceName,
isTemporaryTicket,
modifiedDate,
problemClassificationDisplayName,
problemClassificationId,
problemScopingQuestions,
problemStartTime,
quotaTicketDetails,
require24X7Response,
secondaryConsent,
serviceDisplayName,
serviceId,
serviceLevelAgreement,
severity,
status,
supportEngineer,
supportPlanDisplayName,
supportPlanId,
supportPlanType,
supportTicketId,
technicalTicketDetails,
title,
type
FROM azure.support.support_tickets_no_subscription
WHERE support_ticket_name = '{{ support_ticket_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the support tickets. You can also filter the support tickets by Status, CreatedDate, , ServiceId, and ProblemClassificationId using the $filter parameter. Output will be a paged result with nextLink, using which you can retrieve the next set of support tickets. Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error.

```sql
SELECT
id,
name,
advancedDiagnosticConsent,
contactDetails,
createdDate,
description,
enrollmentId,
fileWorkspaceName,
isTemporaryTicket,
modifiedDate,
problemClassificationDisplayName,
problemClassificationId,
problemScopingQuestions,
problemStartTime,
quotaTicketDetails,
require24X7Response,
secondaryConsent,
serviceDisplayName,
serviceId,
serviceLevelAgreement,
severity,
status,
supportEngineer,
supportPlanDisplayName,
supportPlanId,
supportPlanType,
supportTicketId,
technicalTicketDetails,
title,
type
FROM azure.support.support_tickets_no_subscription
WHERE $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
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

Creates a new support ticket for Billing, and Subscription Management issues. Learn the `prerequisites `_ required to create a support ticket.Always call the Services and ProblemClassifications API to get the most recent set of services and problem categories required for support ticket creation.Adding attachments is not currently supported via the API. To add a file to an existing support ticket, visit the `Manage support ticket `_ page in the Azure portal, select the support ticket, and use the file upload control to add a new file.Providing consent to share diagnostic information with Azure support is currently not supported via the API. The Azure support engineer working on your ticket will reach out to you for consent if your issue requires gathering diagnostic information from your Azure resources..

```sql
INSERT INTO azure.support.support_tickets_no_subscription (
properties,
support_ticket_name
)
SELECT 
'{{ properties }}' /* required */,
'{{ support_ticket_name }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: support_tickets_no_subscription
  props:
    - name: support_ticket_name
      value: "{{ support_ticket_name }}"
      description: Required parameter for the support_tickets_no_subscription resource.
    - name: properties
      value:
        supportTicketId: "{{ supportTicketId }}"
        description: "{{ description }}"
        problemClassificationId: "{{ problemClassificationId }}"
        severity: "{{ severity }}"
        enrollmentId: "{{ enrollmentId }}"
        require24X7Response: {{ require24X7Response }}
        advancedDiagnosticConsent: "{{ advancedDiagnosticConsent }}"
        problemScopingQuestions: "{{ problemScopingQuestions }}"
        supportPlanId: "{{ supportPlanId }}"
        contactDetails:
          firstName: "{{ firstName }}"
          lastName: "{{ lastName }}"
          preferredContactMethod: "{{ preferredContactMethod }}"
          primaryEmailAddress: "{{ primaryEmailAddress }}"
          additionalEmailAddresses:
            - "{{ additionalEmailAddresses }}"
          phoneNumber: "{{ phoneNumber }}"
          preferredTimeZone: "{{ preferredTimeZone }}"
          country: "{{ country }}"
          preferredSupportLanguage: "{{ preferredSupportLanguage }}"
        serviceLevelAgreement:
          startTime: "{{ startTime }}"
          expirationTime: "{{ expirationTime }}"
          slaMinutes: {{ slaMinutes }}
        supportEngineer:
          emailAddress: "{{ emailAddress }}"
        title: "{{ title }}"
        problemStartTime: "{{ problemStartTime }}"
        serviceId: "{{ serviceId }}"
        fileWorkspaceName: "{{ fileWorkspaceName }}"
        technicalTicketDetails:
          resourceId: "{{ resourceId }}"
        quotaTicketDetails:
          quotaChangeRequestSubType: "{{ quotaChangeRequestSubType }}"
          quotaChangeRequestVersion: "{{ quotaChangeRequestVersion }}"
          quotaChangeRequests:
            - region: "{{ region }}"
              payload: "{{ payload }}"
        secondaryConsent:
          - userConsent: "{{ userConsent }}"
            type: "{{ type }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

This API allows you to update the severity level, ticket status, and your contact information in the support ticket.Note: The severity levels cannot be changed if a support ticket is actively being worked upon by an Azure support engineer. In such a case, contact your support engineer to request severity update by adding a new communication using the Communications API.

```sql
UPDATE azure.support.support_tickets_no_subscription
SET 
severity = '{{ severity }}',
status = '{{ status }}',
contactDetails = '{{ contactDetails }}',
advancedDiagnosticConsent = '{{ advancedDiagnosticConsent }}',
secondaryConsent = '{{ secondaryConsent }}'
WHERE 
support_ticket_name = '{{ support_ticket_name }}' --required
RETURNING
id,
name,
properties,
type;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_name_availability"
    values={[
        { label: 'check_name_availability', value: 'check_name_availability' }
    ]}
>
<TabItem value="check_name_availability">

Check the availability of a resource name. This API should be used to check the uniqueness of the name for support ticket creation for the selected subscription.

```sql
EXEC azure.support.support_tickets_no_subscription.check_name_availability 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
