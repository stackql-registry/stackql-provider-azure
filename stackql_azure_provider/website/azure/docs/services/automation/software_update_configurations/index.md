--- 
title: software_update_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - software_update_configurations
  - automation
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

Creates, updates, deletes, gets or lists a <code>software_update_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="software_update_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.software_update_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_name"
    values={[
        { label: 'get_by_name', value: 'get_by_name' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_name">

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
    <td><CopyableCode code="createdBy" /></td>
    <td><code>string</code></td>
    <td>CreatedBy property, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of the resource, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Details of provisioning error.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedBy" /></td>
    <td><code>string</code></td>
    <td>LastModifiedBy property, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time resource was modified, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state for the software update configuration, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduleInfo" /></td>
    <td><code>object</code></td>
    <td>Schedule information for the Software update configuration. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tasks" /></td>
    <td><code>object</code></td>
    <td>Tasks information for the Software update configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateConfiguration" /></td>
    <td><code>object</code></td>
    <td>update specific properties for the Software update configuration. Required.</td>
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
    <td>Resource Id of the software update configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of the software update configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of the software update configuration, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="frequency" /></td>
    <td><code>string</code></td>
    <td>execution frequency of the schedule associated with the software update configuration. Known values are: "OneTime", "Day", "Hour", "Week", "Month", and "Minute". (OneTime, Day, Hour, Week, Month, Minute)</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Last time software update configuration was modified, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="nextRun" /></td>
    <td><code>string (date-time)</code></td>
    <td>ext run time of the update.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state for the software update configuration, which only appears in the response.</td>
</tr>
<tr>
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>the start time of the update.</td>
</tr>
<tr>
    <td><CopyableCode code="tasks" /></td>
    <td><code>object</code></td>
    <td>Pre and Post Tasks defined.</td>
</tr>
<tr>
    <td><CopyableCode code="updateConfiguration" /></td>
    <td><code>object</code></td>
    <td>Update specific properties of the software update configuration.</td>
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
    <td><a href="#get_by_name"><CopyableCode code="get_by_name" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-software_update_configuration_name"><code>software_update_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Get a single software update configuration by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Get all software update configurations for the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-software_update_configuration_name"><code>software_update_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>Create a new software update configuration with the name given in the URI.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-automation_account_name"><code>automation_account_name</code></a>, <a href="#parameter-software_update_configuration_name"><code>software_update_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-clientRequestId"><code>clientRequestId</code></a></td>
    <td>delete a specific software update configuration.</td>
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
<tr id="parameter-automation_account_name">
    <td><CopyableCode code="automation_account_name" /></td>
    <td><code>string</code></td>
    <td>The name of the automation account. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-software_update_configuration_name">
    <td><CopyableCode code="software_update_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name of the software update configuration to be created. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
<tr id="parameter-clientRequestId">
    <td><CopyableCode code="clientRequestId" /></td>
    <td><code>string</code></td>
    <td>Identifies this specific client request. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_name"
    values={[
        { label: 'get_by_name', value: 'get_by_name' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_name">

Get a single software update configuration by name.

```sql
SELECT
id,
name,
createdBy,
creationTime,
error,
lastModifiedBy,
lastModifiedTime,
provisioningState,
scheduleInfo,
systemData,
tasks,
type,
updateConfiguration
FROM azure.automation.software_update_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND software_update_configuration_name = '{{ software_update_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND clientRequestId = '{{ clientRequestId }}'
;
```
</TabItem>
<TabItem value="list">

Get all software update configurations for the account.

```sql
SELECT
id,
name,
creationTime,
frequency,
lastModifiedTime,
nextRun,
provisioningState,
startTime,
tasks,
updateConfiguration
FROM azure.automation.software_update_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND automation_account_name = '{{ automation_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND clientRequestId = '{{ clientRequestId }}'
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

Create a new software update configuration with the name given in the URI.

```sql
INSERT INTO azure.automation.software_update_configurations (
properties,
resource_group_name,
automation_account_name,
software_update_configuration_name,
subscription_id,
clientRequestId
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ automation_account_name }}',
'{{ software_update_configuration_name }}',
'{{ subscription_id }}',
'{{ clientRequestId }}'
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
- name: software_update_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the software_update_configurations resource.
    - name: automation_account_name
      value: "{{ automation_account_name }}"
      description: Required parameter for the software_update_configurations resource.
    - name: software_update_configuration_name
      value: "{{ software_update_configuration_name }}"
      description: Required parameter for the software_update_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the software_update_configurations resource.
    - name: properties
      description: |
        Software update configuration properties. Required.
      value:
        updateConfiguration:
          operatingSystem: "{{ operatingSystem }}"
          windows:
            includedUpdateClassifications: "{{ includedUpdateClassifications }}"
            excludedKbNumbers:
              - "{{ excludedKbNumbers }}"
            includedKbNumbers:
              - "{{ includedKbNumbers }}"
            rebootSetting: "{{ rebootSetting }}"
          linux:
            includedPackageClassifications: "{{ includedPackageClassifications }}"
            excludedPackageNameMasks:
              - "{{ excludedPackageNameMasks }}"
            includedPackageNameMasks:
              - "{{ includedPackageNameMasks }}"
            rebootSetting: "{{ rebootSetting }}"
          duration: "{{ duration }}"
          azureVirtualMachines:
            - "{{ azureVirtualMachines }}"
          nonAzureComputerNames:
            - "{{ nonAzureComputerNames }}"
          targets:
            azureQueries:
              - scope: "{{ scope }}"
                locations: "{{ locations }}"
                tagSettings:
                  tags: "{{ tags }}"
                  filterOperator: "{{ filterOperator }}"
            nonAzureQueries:
              - functionAlias: "{{ functionAlias }}"
                workspaceId: "{{ workspaceId }}"
        scheduleInfo:
          startTime: "{{ startTime }}"
          startTimeOffsetMinutes: {{ startTimeOffsetMinutes }}
          expiryTime: "{{ expiryTime }}"
          expiryTimeOffsetMinutes: {{ expiryTimeOffsetMinutes }}
          isEnabled: {{ isEnabled }}
          nextRun: "{{ nextRun }}"
          nextRunOffsetMinutes: {{ nextRunOffsetMinutes }}
          interval: {{ interval }}
          frequency: "{{ frequency }}"
          timeZone: "{{ timeZone }}"
          advancedSchedule:
            weekDays:
              - "{{ weekDays }}"
            monthDays:
              - {{ monthDays }}
            monthlyOccurrences:
              - occurrence: {{ occurrence }}
                day: "{{ day }}"
          creationTime: "{{ creationTime }}"
          lastModifiedTime: "{{ lastModifiedTime }}"
          description: "{{ description }}"
        provisioningState: "{{ provisioningState }}"
        error:
          code: "{{ code }}"
          message: "{{ message }}"
        creationTime: "{{ creationTime }}"
        createdBy: "{{ createdBy }}"
        lastModifiedTime: "{{ lastModifiedTime }}"
        lastModifiedBy: "{{ lastModifiedBy }}"
        tasks:
          preTask:
            parameters: "{{ parameters }}"
            source: "{{ source }}"
          postTask:
            parameters: "{{ parameters }}"
            source: "{{ source }}"
    - name: clientRequestId
      value: "{{ clientRequestId }}"
      description: Identifies this specific client request. Default value is None.
      description: Identifies this specific client request. Default value is None.
`}</CodeBlock>

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

delete a specific software update configuration.

```sql
DELETE FROM azure.automation.software_update_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND automation_account_name = '{{ automation_account_name }}' --required
AND software_update_configuration_name = '{{ software_update_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND clientRequestId = '{{ clientRequestId }}'
;
```
</TabItem>
</Tabs>
