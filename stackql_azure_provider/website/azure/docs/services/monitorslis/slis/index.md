--- 
title: slis
hide_title: false
hide_table_of_contents: false
keywords:
  - slis
  - monitorslis
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

Creates, updates, deletes, gets or lists a <code>slis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="slis" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitorslis.slis" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
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
    <td><CopyableCode code="baselineProperties" /></td>
    <td><code>object</code></td>
    <td>Defines the SLO baseline associated with the SLI. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Specifies the category of the SLI, used to classify signals such as Availability and Latency. Required. Known values are: "Availability" and "Latency". (Availability, Latency)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A user-provided description of the SLI, with a maximum length of 1000 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationAmwAccounts" /></td>
    <td><code>array</code></td>
    <td>Destination AMW accounts. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationMetrics" /></td>
    <td><code>array</code></td>
    <td>The destination Azure Monitor Workspace (AMW) accounts where the SLI emits metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAlert" /></td>
    <td><code>boolean</code></td>
    <td>A flag to determine whether alert is enabled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationType" /></td>
    <td><code>string</code></td>
    <td>Determines how the SLI is evaluated—either based on request counts or time windows. Required. Known values are: "WindowBased" and "RequestBased". (WindowBased, RequestBased)</td>
</tr>
<tr>
    <td><CopyableCode code="executionState" /></td>
    <td><code>object</code></td>
    <td>Indicates the current execution status of the SLI resource in ARM responses.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Indicates the provisioning status of the last operation. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sliProperties" /></td>
    <td><code>object</code></td>
    <td>Defines the SLI properties associated with the SLI. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="streamingRuleId" /></td>
    <td><code>string</code></td>
    <td>The streaming rule Id associated with the Sli resource.</td>
</tr>
<tr>
    <td><CopyableCode code="streamingRuleLastUpdatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The streaming rule last updated timestamp associated with the Sli resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_parent">

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
    <td><CopyableCode code="baselineProperties" /></td>
    <td><code>object</code></td>
    <td>Defines the SLO baseline associated with the SLI. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>Specifies the category of the SLI, used to classify signals such as Availability and Latency. Required. Known values are: "Availability" and "Latency". (Availability, Latency)</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A user-provided description of the SLI, with a maximum length of 1000 characters. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationAmwAccounts" /></td>
    <td><code>array</code></td>
    <td>Destination AMW accounts. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="destinationMetrics" /></td>
    <td><code>array</code></td>
    <td>The destination Azure Monitor Workspace (AMW) accounts where the SLI emits metrics.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAlert" /></td>
    <td><code>boolean</code></td>
    <td>A flag to determine whether alert is enabled. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluationType" /></td>
    <td><code>string</code></td>
    <td>Determines how the SLI is evaluated—either based on request counts or time windows. Required. Known values are: "WindowBased" and "RequestBased". (WindowBased, RequestBased)</td>
</tr>
<tr>
    <td><CopyableCode code="executionState" /></td>
    <td><code>object</code></td>
    <td>Indicates the current execution status of the SLI resource in ARM responses.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Indicates the provisioning status of the last operation. Known values are: "Succeeded", "Failed", and "Canceled". (Succeeded, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="sliProperties" /></td>
    <td><code>object</code></td>
    <td>Defines the SLI properties associated with the SLI. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="streamingRuleId" /></td>
    <td><code>string</code></td>
    <td>The streaming rule Id associated with the Sli resource.</td>
</tr>
<tr>
    <td><CopyableCode code="streamingRuleLastUpdatedTimestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The streaming rule last updated timestamp associated with the Sli resource.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
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
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-sli_name"><code>sli_name</code></a></td>
    <td></td>
    <td>Gets an SLI resource.</td>
</tr>
<tr>
    <td><a href="#list_by_parent"><CopyableCode code="list_by_parent" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a></td>
    <td></td>
    <td>Lists all SLI resources under a parent resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-sli_name"><code>sli_name</code></a></td>
    <td></td>
    <td>Creates or updates an SLI resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-sli_name"><code>sli_name</code></a></td>
    <td></td>
    <td>Creates or updates an SLI resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-service_group_name"><code>service_group_name</code></a>, <a href="#parameter-sli_name"><code>sli_name</code></a></td>
    <td></td>
    <td>Deletes an SLI resource.</td>
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
<tr id="parameter-service_group_name">
    <td><CopyableCode code="service_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the service group. Required.</td>
</tr>
<tr id="parameter-sli_name">
    <td><CopyableCode code="sli_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SLI that is given by the user. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_parent', value: 'list_by_parent' }
    ]}
>
<TabItem value="get">

Gets an SLI resource.

```sql
SELECT
id,
name,
baselineProperties,
category,
description,
destinationAmwAccounts,
destinationMetrics,
enableAlert,
evaluationType,
executionState,
identity,
provisioningState,
sliProperties,
streamingRuleId,
streamingRuleLastUpdatedTimestamp,
systemData,
type
FROM azure.monitorslis.slis
WHERE service_group_name = '{{ service_group_name }}' -- required
AND sli_name = '{{ sli_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_parent">

Lists all SLI resources under a parent resource.

```sql
SELECT
id,
name,
baselineProperties,
category,
description,
destinationAmwAccounts,
destinationMetrics,
enableAlert,
evaluationType,
executionState,
identity,
provisioningState,
sliProperties,
streamingRuleId,
streamingRuleLastUpdatedTimestamp,
systemData,
type
FROM azure.monitorslis.slis
WHERE service_group_name = '{{ service_group_name }}' -- required
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

Creates or updates an SLI resource.

```sql
INSERT INTO azure.monitorslis.slis (
properties,
identity,
service_group_name,
sli_name
)
SELECT 
'{{ properties }}',
'{{ identity }}',
'{{ service_group_name }}',
'{{ sli_name }}'
RETURNING
id,
name,
identity,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: slis
  props:
    - name: service_group_name
      value: "{{ service_group_name }}"
      description: Required parameter for the slis resource.
    - name: sli_name
      value: "{{ sli_name }}"
      description: Required parameter for the slis resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        description: "{{ description }}"
        category: "{{ category }}"
        evaluationType: "{{ evaluationType }}"
        executionState:
          state: "{{ state }}"
          message: "{{ message }}"
        destinationAmwAccounts:
          - resourceId: "{{ resourceId }}"
            identity: "{{ identity }}"
        destinationMetrics:
          - metricNamespace: "{{ metricNamespace }}"
            metricName: "{{ metricName }}"
        baselineProperties:
          baseline:
            value: {{ value }}
            evaluationPeriodDays: {{ evaluationPeriodDays }}
            evaluationCalculationType: "{{ evaluationCalculationType }}"
        streamingRuleId: "{{ streamingRuleId }}"
        streamingRuleLastUpdatedTimestamp: "{{ streamingRuleLastUpdatedTimestamp }}"
        enableAlert: {{ enableAlert }}
        sliProperties:
          goodSignals:
            signalSources:
              - signalSourceId: "{{ signalSourceId }}"
                sourceAmwAccountManagedIdentity: "{{ sourceAmwAccountManagedIdentity }}"
                sourceAmwAccountResourceId: "{{ sourceAmwAccountResourceId }}"
                metricNamespace: "{{ metricNamespace }}"
                metricName: "{{ metricName }}"
                filters: "{{ filters }}"
                spatialAggregation:
                  type: "{{ type }}"
                  dimensions: "{{ dimensions }}"
                temporalAggregation:
                  type: "{{ type }}"
                  windowSizeMinutes: {{ windowSizeMinutes }}
            signalFormula: "{{ signalFormula }}"
          totalSignals:
            signalSources:
              - signalSourceId: "{{ signalSourceId }}"
                sourceAmwAccountManagedIdentity: "{{ sourceAmwAccountManagedIdentity }}"
                sourceAmwAccountResourceId: "{{ sourceAmwAccountResourceId }}"
                metricNamespace: "{{ metricNamespace }}"
                metricName: "{{ metricName }}"
                filters: "{{ filters }}"
                spatialAggregation:
                  type: "{{ type }}"
                  dimensions: "{{ dimensions }}"
                temporalAggregation:
                  type: "{{ type }}"
                  windowSizeMinutes: {{ windowSizeMinutes }}
            signalFormula: "{{ signalFormula }}"
          signals:
            signalSources:
              - signalSourceId: "{{ signalSourceId }}"
                sourceAmwAccountManagedIdentity: "{{ sourceAmwAccountManagedIdentity }}"
                sourceAmwAccountResourceId: "{{ sourceAmwAccountResourceId }}"
                metricNamespace: "{{ metricNamespace }}"
                metricName: "{{ metricName }}"
                filters: "{{ filters }}"
                spatialAggregation:
                  type: "{{ type }}"
                  dimensions: "{{ dimensions }}"
                temporalAggregation:
                  type: "{{ type }}"
                  windowSizeMinutes: {{ windowSizeMinutes }}
            signalFormula: "{{ signalFormula }}"
          windowUptimeCriteria:
            target: {{ target }}
            comparator: "{{ comparator }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Creates or updates an SLI resource.

```sql
REPLACE azure.monitorslis.slis
SET 
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
service_group_name = '{{ service_group_name }}' --required
AND sli_name = '{{ sli_name }}' --required
RETURNING
id,
name,
identity,
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

Deletes an SLI resource.

```sql
DELETE FROM azure.monitorslis.slis
WHERE service_group_name = '{{ service_group_name }}' --required
AND sli_name = '{{ sli_name }}' --required
;
```
</TabItem>
</Tabs>
