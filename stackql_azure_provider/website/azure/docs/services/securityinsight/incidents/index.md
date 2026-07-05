--- 
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
  - securityinsight
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

Creates, updates, deletes, gets or lists an <code>incidents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="incidents" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.securityinsight.incidents" /></td></tr>
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
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data on the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="classification" /></td>
    <td><code>string</code></td>
    <td>The reason the incident was closed. Known values are: "Undetermined", "TruePositive", "BenignPositive", and "FalsePositive". (Undetermined, TruePositive, BenignPositive, FalsePositive)</td>
</tr>
<tr>
    <td><CopyableCode code="classificationComment" /></td>
    <td><code>string</code></td>
    <td>Describes the reason the incident was closed.</td>
</tr>
<tr>
    <td><CopyableCode code="classificationReason" /></td>
    <td><code>string</code></td>
    <td>The classification reason the incident was closed with. Known values are: "SuspiciousActivity", "SuspiciousButExpected", "IncorrectAlertLogic", and "InaccurateData". (SuspiciousActivity, SuspiciousButExpected, IncorrectAlertLogic, InaccurateData)</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the incident was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="firstActivityTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the first activity in the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentNumber" /></td>
    <td><code>integer</code></td>
    <td>A sequential number.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentUrl" /></td>
    <td><code>string</code></td>
    <td>The deep-link url to the incident in Azure portal.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>array</code></td>
    <td>List of labels relevant to this incident.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActivityTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the last activity in the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time the incident was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>object</code></td>
    <td>Describes a user that the incident is assigned to.</td>
</tr>
<tr>
    <td><CopyableCode code="providerIncidentId" /></td>
    <td><code>string</code></td>
    <td>The incident ID assigned by the incident provider.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>The name of the source provider that generated the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="relatedAnalyticRuleIds" /></td>
    <td><code>array</code></td>
    <td>List of resource ids of Analytic rules related to the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The severity of the incident. Required. Known values are: "High", "Medium", "Low", and "Informational". (High, Medium, Low, Informational)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the incident. Required. Known values are: "New", "Active", and "Closed". (New, Active, Closed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="teamInformation" /></td>
    <td><code>object</code></td>
    <td>Describes a team for the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title of the incident. Required.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data on the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="classification" /></td>
    <td><code>string</code></td>
    <td>The reason the incident was closed. Known values are: "Undetermined", "TruePositive", "BenignPositive", and "FalsePositive". (Undetermined, TruePositive, BenignPositive, FalsePositive)</td>
</tr>
<tr>
    <td><CopyableCode code="classificationComment" /></td>
    <td><code>string</code></td>
    <td>Describes the reason the incident was closed.</td>
</tr>
<tr>
    <td><CopyableCode code="classificationReason" /></td>
    <td><code>string</code></td>
    <td>The classification reason the incident was closed with. Known values are: "SuspiciousActivity", "SuspiciousButExpected", "IncorrectAlertLogic", and "InaccurateData". (SuspiciousActivity, SuspiciousButExpected, IncorrectAlertLogic, InaccurateData)</td>
</tr>
<tr>
    <td><CopyableCode code="createdTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time the incident was created.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="firstActivityTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the first activity in the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentNumber" /></td>
    <td><code>integer</code></td>
    <td>A sequential number.</td>
</tr>
<tr>
    <td><CopyableCode code="incidentUrl" /></td>
    <td><code>string</code></td>
    <td>The deep-link url to the incident in Azure portal.</td>
</tr>
<tr>
    <td><CopyableCode code="labels" /></td>
    <td><code>array</code></td>
    <td>List of labels relevant to this incident.</td>
</tr>
<tr>
    <td><CopyableCode code="lastActivityTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time of the last activity in the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last time the incident was updated.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>object</code></td>
    <td>Describes a user that the incident is assigned to.</td>
</tr>
<tr>
    <td><CopyableCode code="providerIncidentId" /></td>
    <td><code>string</code></td>
    <td>The incident ID assigned by the incident provider.</td>
</tr>
<tr>
    <td><CopyableCode code="providerName" /></td>
    <td><code>string</code></td>
    <td>The name of the source provider that generated the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="relatedAnalyticRuleIds" /></td>
    <td><code>array</code></td>
    <td>List of resource ids of Analytic rules related to the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="severity" /></td>
    <td><code>string</code></td>
    <td>The severity of the incident. Required. Known values are: "High", "Medium", "Low", and "Informational". (High, Medium, Low, Informational)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The status of the incident. Required. Known values are: "New", "Active", and "Closed". (New, Active, Closed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="teamInformation" /></td>
    <td><code>object</code></td>
    <td>Describes a team for the incident.</td>
</tr>
<tr>
    <td><CopyableCode code="title" /></td>
    <td><code>string</code></td>
    <td>The title of the incident. Required.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-incident_id"><code>incident_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a given incident.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Gets all incidents.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-incident_id"><code>incident_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an incident.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-incident_id"><code>incident_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates an incident.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-incident_id"><code>incident_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a given incident.</td>
</tr>
<tr>
    <td><a href="#list_alerts"><CopyableCode code="list_alerts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-incident_id"><code>incident_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all alerts for an incident.</td>
</tr>
<tr>
    <td><a href="#list_bookmarks"><CopyableCode code="list_bookmarks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-incident_id"><code>incident_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all bookmarks for an incident.</td>
</tr>
<tr>
    <td><a href="#list_entities"><CopyableCode code="list_entities" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-incident_id"><code>incident_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all entities for an incident.</td>
</tr>
<tr>
    <td><a href="#run_playbook"><CopyableCode code="run_playbook" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-incident_identifier"><code>incident_identifier</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-logicAppsResourceId"><code>logicAppsResourceId</code></a></td>
    <td></td>
    <td>Triggers playbook on a specific incident.</td>
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
<tr id="parameter-incident_id">
    <td><CopyableCode code="incident_id" /></td>
    <td><code>string</code></td>
    <td>Incident ID. Required.</td>
</tr>
<tr id="parameter-incident_identifier">
    <td><CopyableCode code="incident_identifier" /></td>
    <td><code>string</code></td>
    <td>The incident identifier. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Filters the results, based on a Boolean condition. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Sorts the results. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Returns only the first n results. Optional. Default value is None.</td>
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

Gets a given incident.

```sql
SELECT
id,
name,
additionalData,
classification,
classificationComment,
classificationReason,
createdTimeUtc,
description,
etag,
firstActivityTimeUtc,
incidentNumber,
incidentUrl,
labels,
lastActivityTimeUtc,
lastModifiedTimeUtc,
owner,
providerIncidentId,
providerName,
relatedAnalyticRuleIds,
severity,
status,
systemData,
teamInformation,
title,
type
FROM azure.securityinsight.incidents
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND incident_id = '{{ incident_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all incidents.

```sql
SELECT
id,
name,
additionalData,
classification,
classificationComment,
classificationReason,
createdTimeUtc,
description,
etag,
firstActivityTimeUtc,
incidentNumber,
incidentUrl,
labels,
lastActivityTimeUtc,
lastModifiedTimeUtc,
owner,
providerIncidentId,
providerName,
relatedAnalyticRuleIds,
severity,
status,
systemData,
teamInformation,
title,
type
FROM azure.securityinsight.incidents
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Creates or updates an incident.

```sql
INSERT INTO azure.securityinsight.incidents (
properties,
etag,
resource_group_name,
workspace_name,
incident_id,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ incident_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: incidents
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the incidents resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the incidents resource.
    - name: incident_id
      value: "{{ incident_id }}"
      description: Required parameter for the incidents resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the incidents resource.
    - name: properties
      description: |
        Incident properties.
      value:
        title: "{{ title }}"
        description: "{{ description }}"
        severity: "{{ severity }}"
        status: "{{ status }}"
        classification: "{{ classification }}"
        classificationReason: "{{ classificationReason }}"
        classificationComment: "{{ classificationComment }}"
        owner:
          email: "{{ email }}"
          assignedTo: "{{ assignedTo }}"
          objectId: "{{ objectId }}"
          userPrincipalName: "{{ userPrincipalName }}"
          ownerType: "{{ ownerType }}"
        labels:
          - labelName: "{{ labelName }}"
            labelType: "{{ labelType }}"
        firstActivityTimeUtc: "{{ firstActivityTimeUtc }}"
        lastActivityTimeUtc: "{{ lastActivityTimeUtc }}"
        lastModifiedTimeUtc: "{{ lastModifiedTimeUtc }}"
        createdTimeUtc: "{{ createdTimeUtc }}"
        incidentNumber: {{ incidentNumber }}
        additionalData:
          alertsCount: {{ alertsCount }}
          bookmarksCount: {{ bookmarksCount }}
          commentsCount: {{ commentsCount }}
          alertProductNames:
            - "{{ alertProductNames }}"
          tactics:
            - "{{ tactics }}"
          techniques:
            - "{{ techniques }}"
          providerIncidentUrl: "{{ providerIncidentUrl }}"
          mergedIncidentNumber: "{{ mergedIncidentNumber }}"
          mergedIncidentUrl: "{{ mergedIncidentUrl }}"
        relatedAnalyticRuleIds:
          - "{{ relatedAnalyticRuleIds }}"
        incidentUrl: "{{ incidentUrl }}"
        providerName: "{{ providerName }}"
        providerIncidentId: "{{ providerIncidentId }}"
        teamInformation:
          teamId: "{{ teamId }}"
          primaryChannelUrl: "{{ primaryChannelUrl }}"
          teamCreationTimeUtc: "{{ teamCreationTimeUtc }}"
          name: "{{ name }}"
          description: "{{ description }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
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

Creates or updates an incident.

```sql
REPLACE azure.securityinsight.incidents
SET 
properties = '{{ properties }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND incident_id = '{{ incident_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
properties,
systemData,
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

Deletes a given incident.

```sql
DELETE FROM azure.securityinsight.incidents
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND incident_id = '{{ incident_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_alerts"
    values={[
        { label: 'list_alerts', value: 'list_alerts' },
        { label: 'list_bookmarks', value: 'list_bookmarks' },
        { label: 'list_entities', value: 'list_entities' },
        { label: 'run_playbook', value: 'run_playbook' }
    ]}
>
<TabItem value="list_alerts">

Gets all alerts for an incident.

```sql
EXEC azure.securityinsight.incidents.list_alerts 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@incident_id='{{ incident_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_bookmarks">

Gets all bookmarks for an incident.

```sql
EXEC azure.securityinsight.incidents.list_bookmarks 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@incident_id='{{ incident_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_entities">

Gets all entities for an incident.

```sql
EXEC azure.securityinsight.incidents.list_entities 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@incident_id='{{ incident_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="run_playbook">

Triggers playbook on a specific incident.

```sql
EXEC azure.securityinsight.incidents.run_playbook 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@incident_identifier='{{ incident_identifier }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"tenantId": "{{ tenantId }}", 
"logicAppsResourceId": "{{ logicAppsResourceId }}"
}'
;
```
</TabItem>
</Tabs>
