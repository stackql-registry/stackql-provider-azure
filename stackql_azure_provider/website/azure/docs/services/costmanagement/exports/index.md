--- 
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
  - costmanagement
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

Creates, updates, deletes, gets or lists an <code>exports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="exports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.costmanagement.exports" /></td></tr>
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
    <td><CopyableCode code="compressionMode" /></td>
    <td><code>string</code></td>
    <td>Allow customers to select compress data for exports. This setting will enable destination file compression scheme at runtime. By default set to None. Gzip is for csv and snappy for parquet. Known values are: "gzip", "snappy", and "none". (gzip, snappy, none)</td>
</tr>
<tr>
    <td><CopyableCode code="dataOverwriteBehavior" /></td>
    <td><code>string</code></td>
    <td>Allow customers to select overwrite data(OverwritePreviousReport) for exports. This setting will enable overwrite data for the same month in customer storage account. By default set to CreateNewReport. Known values are: "OverwritePreviousReport" and "CreateNewReport". (OverwritePreviousReport, CreateNewReport)</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Has the definition for the export. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryInfo" /></td>
    <td><code>object</code></td>
    <td>Has delivery information for the export. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="exportDescription" /></td>
    <td><code>string</code></td>
    <td>The export description set by customer at time of export creation/update.</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>The format of the export being delivered. Known values are: "Csv" and "Parquet". (Csv, Parquet)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity associated with Export.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the Export's managed identity. Only required when utilizing managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="nextRunTimeEstimate" /></td>
    <td><code>string (date-time)</code></td>
    <td>If the export has an active schedule, provides an estimate of the next run time.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionData" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, exported data will be partitioned by size and placed in a blob directory together with a manifest file.</td>
</tr>
<tr>
    <td><CopyableCode code="runHistory" /></td>
    <td><code>object</code></td>
    <td>If requested, has the most recent run history for the export.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Has schedule information for the export.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSuspensionContext" /></td>
    <td><code>object</code></td>
    <td>The export suspension reason if export is in SystemSuspended state. This is not populated currently.</td>
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
    <td><CopyableCode code="compressionMode" /></td>
    <td><code>string</code></td>
    <td>Allow customers to select compress data for exports. This setting will enable destination file compression scheme at runtime. By default set to None. Gzip is for csv and snappy for parquet. Known values are: "gzip", "snappy", and "none". (gzip, snappy, none)</td>
</tr>
<tr>
    <td><CopyableCode code="dataOverwriteBehavior" /></td>
    <td><code>string</code></td>
    <td>Allow customers to select overwrite data(OverwritePreviousReport) for exports. This setting will enable overwrite data for the same month in customer storage account. By default set to CreateNewReport. Known values are: "OverwritePreviousReport" and "CreateNewReport". (OverwritePreviousReport, CreateNewReport)</td>
</tr>
<tr>
    <td><CopyableCode code="definition" /></td>
    <td><code>object</code></td>
    <td>Has the definition for the export. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryInfo" /></td>
    <td><code>object</code></td>
    <td>Has delivery information for the export. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.</td>
</tr>
<tr>
    <td><CopyableCode code="exportDescription" /></td>
    <td><code>string</code></td>
    <td>The export description set by customer at time of export creation/update.</td>
</tr>
<tr>
    <td><CopyableCode code="format" /></td>
    <td><code>string</code></td>
    <td>The format of the export being delivered. Known values are: "Csv" and "Parquet". (Csv, Parquet)</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed identity associated with Export.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the Export's managed identity. Only required when utilizing managed identity.</td>
</tr>
<tr>
    <td><CopyableCode code="nextRunTimeEstimate" /></td>
    <td><code>string (date-time)</code></td>
    <td>If the export has an active schedule, provides an estimate of the next run time.</td>
</tr>
<tr>
    <td><CopyableCode code="partitionData" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, exported data will be partitioned by size and placed in a blob directory together with a manifest file.</td>
</tr>
<tr>
    <td><CopyableCode code="runHistory" /></td>
    <td><code>object</code></td>
    <td>If requested, has the most recent run history for the export.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>Has schedule information for the export.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSuspensionContext" /></td>
    <td><code>object</code></td>
    <td>The export suspension reason if export is in SystemSuspended state. This is not populated currently.</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-export_name"><code>export_name</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to get the export for the defined scope by export name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to list all exports at the given scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-export_name"><code>export_name</code></a></td>
    <td></td>
    <td>The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-export_name"><code>export_name</code></a></td>
    <td></td>
    <td>The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-export_name"><code>export_name</code></a></td>
    <td></td>
    <td>The operation to delete a export.</td>
</tr>
<tr>
    <td><a href="#get_execution_history"><CopyableCode code="get_execution_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-export_name"><code>export_name</code></a></td>
    <td></td>
    <td>The operation to get the run history of an export for the defined scope and export name.</td>
</tr>
<tr>
    <td><a href="#execute"><CopyableCode code="execute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-export_name"><code>export_name</code></a></td>
    <td></td>
    <td>The operation to run an export.</td>
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
<tr id="parameter-export_name">
    <td><CopyableCode code="export_name" /></td>
    <td><code>string</code></td>
    <td>Export Name. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>May be used to expand the properties within an export. Currently only 'runHistory' is supported and will return information for the last run of each export. Default value is None.</td>
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

The operation to get the export for the defined scope by export name.

```sql
SELECT
id,
name,
compressionMode,
dataOverwriteBehavior,
definition,
deliveryInfo,
eTag,
exportDescription,
format,
identity,
location,
nextRunTimeEstimate,
partitionData,
runHistory,
schedule,
systemData,
systemSuspensionContext,
type
FROM azure.costmanagement.exports
WHERE scope = '{{ scope }}' -- required
AND export_name = '{{ export_name }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

The operation to list all exports at the given scope.

```sql
SELECT
id,
name,
compressionMode,
dataOverwriteBehavior,
definition,
deliveryInfo,
eTag,
exportDescription,
format,
identity,
location,
nextRunTimeEstimate,
partitionData,
runHistory,
schedule,
systemData,
systemSuspensionContext,
type
FROM azure.costmanagement.exports
WHERE scope = '{{ scope }}' -- required
AND $expand = '{{ $expand }}'
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

The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

```sql
INSERT INTO azure.costmanagement.exports (
properties,
identity,
location,
eTag,
scope,
export_name
)
SELECT 
'{{ properties }}',
'{{ identity }}',
'{{ location }}',
'{{ eTag }}',
'{{ scope }}',
'{{ export_name }}'
RETURNING
id,
name,
eTag,
identity,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: exports
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the exports resource.
    - name: export_name
      value: "{{ export_name }}"
      description: Required parameter for the exports resource.
    - name: properties
      description: |
        The properties of the export.
      value:
        format: "{{ format }}"
        deliveryInfo:
          destination:
            type: "{{ type }}"
            resourceId: "{{ resourceId }}"
            container: "{{ container }}"
            rootFolderPath: "{{ rootFolderPath }}"
            sasToken: "{{ sasToken }}"
            storageAccount: "{{ storageAccount }}"
        definition:
          type: "{{ type }}"
          timeframe: "{{ timeframe }}"
          timePeriod:
            from: "{{ from }}"
            to: "{{ to }}"
          dataSet:
            granularity: "{{ granularity }}"
            configuration:
              columns:
                - "{{ columns }}"
              dataVersion: "{{ dataVersion }}"
              filters:
                - name: "{{ name }}"
                  value: "{{ value }}"
        runHistory:
          value:
            - id: "{{ id }}"
              name: "{{ name }}"
              type: "{{ type }}"
              eTag: "{{ eTag }}"
              properties:
                executionType: "{{ executionType }}"
                status: "{{ status }}"
                submittedBy: "{{ submittedBy }}"
                submittedTime: "{{ submittedTime }}"
                processingStartTime: "{{ processingStartTime }}"
                processingEndTime: "{{ processingEndTime }}"
                startDate: "{{ startDate }}"
                endDate: "{{ endDate }}"
                fileName: "{{ fileName }}"
                manifestFile: "{{ manifestFile }}"
                runSettings:
                  format: "{{ format }}"
                  deliveryInfo: "{{ deliveryInfo }}"
                  definition: "{{ definition }}"
                  runHistory: "{{ runHistory }}"
                  partitionData: {{ partitionData }}
                  dataOverwriteBehavior: "{{ dataOverwriteBehavior }}"
                  compressionMode: "{{ compressionMode }}"
                  exportDescription: "{{ exportDescription }}"
                  nextRunTimeEstimate: "{{ nextRunTimeEstimate }}"
                  systemSuspensionContext: "{{ systemSuspensionContext }}"
                error:
                  code: "{{ code }}"
                  message: "{{ message }}"
        partitionData: {{ partitionData }}
        dataOverwriteBehavior: "{{ dataOverwriteBehavior }}"
        compressionMode: "{{ compressionMode }}"
        exportDescription: "{{ exportDescription }}"
        nextRunTimeEstimate: "{{ nextRunTimeEstimate }}"
        systemSuspensionContext:
          suspensionCode: "{{ suspensionCode }}"
          suspensionReason: "{{ suspensionReason }}"
          suspensionTime: "{{ suspensionTime }}"
        schedule:
          status: "{{ status }}"
          recurrence: "{{ recurrence }}"
          recurrencePeriod:
            from: "{{ from }}"
            to: "{{ to }}"
    - name: identity
      description: |
        The managed identity associated with Export.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
    - name: location
      value: "{{ location }}"
      description: |
        The location of the Export's managed identity. Only required when utilizing managed identity.
    - name: eTag
      value: "{{ eTag }}"
      description: |
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
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

The operation to create or update a export. Update operation requires latest eTag to be set in the request. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

```sql
REPLACE azure.costmanagement.exports
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
location = '{{ location }}',
eTag = '{{ eTag }}'
WHERE 
scope = '{{ scope }}' --required
AND export_name = '{{ export_name }}' --required
RETURNING
id,
name,
eTag,
identity,
location,
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

The operation to delete a export.

```sql
DELETE FROM azure.costmanagement.exports
WHERE scope = '{{ scope }}' --required
AND export_name = '{{ export_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_execution_history"
    values={[
        { label: 'get_execution_history', value: 'get_execution_history' },
        { label: 'execute', value: 'execute' }
    ]}
>
<TabItem value="get_execution_history">

The operation to get the run history of an export for the defined scope and export name.

```sql
EXEC azure.costmanagement.exports.get_execution_history 
@scope='{{ scope }}' --required, 
@export_name='{{ export_name }}' --required
;
```
</TabItem>
<TabItem value="execute">

The operation to run an export.

```sql
EXEC azure.costmanagement.exports.execute 
@scope='{{ scope }}' --required, 
@export_name='{{ export_name }}' --required 
@@json=
'{
"timePeriod": "{{ timePeriod }}"
}'
;
```
</TabItem>
</Tabs>
