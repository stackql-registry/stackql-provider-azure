--- 
title: job_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - job_schedules
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

Creates, updates, deletes, gets or lists a <code>job_schedules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="job_schedules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.job_schedules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_job_schedule"
    values={[
        { label: 'get_job_schedule', value: 'get_job_schedule' },
        { label: 'list_job_schedules', value: 'list_job_schedules' }
    ]}
>
<TabItem value="get_job_schedule">

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
    <td>A string that uniquely identifies the schedule within the Account. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Job Schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the Job Schedule. This is an opaque string. You can use it to detect whether the Job Schedule has changed between requests. In particular, you can be pass the ETag with an Update Job Schedule request to specify that your changes should take effect only if nobody else has modified the schedule in the meantime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="executionInfo" /></td>
    <td><code>object</code></td>
    <td>Information about Jobs that have been and will be run under this schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="jobSpecification" /></td>
    <td><code>object</code></td>
    <td>The details of the Jobs to be created on this schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the Job Schedule. This is the last time at which the schedule level data, such as the Job specification or recurrence information, changed. It does not factor in job-level changes such as new Jobs being created or Jobs changing state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>A list of name-value pairs associated with the schedule as metadata. The Batch service does not assign any meaning to metadata; it is solely for the use of user code.</td>
</tr>
<tr>
    <td><CopyableCode code="previousState" /></td>
    <td><code>string</code></td>
    <td>The previous state of the Job Schedule. This property is not present if the Job Schedule is in its initial active state. Known values are: "active", "completed", "disabled", "terminating", and "deleting". (active, completed, disabled, terminating, deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="previousStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Job Schedule entered its previous state. This property is not present if the Job Schedule is in its initial active state.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>The schedule according to which Jobs will be created. All times are fixed respective to UTC and are not impacted by daylight saving time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Job Schedule. Required. Known values are: "active", "completed", "disabled", "terminating", and "deleting". (active, completed, disabled, terminating, deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Job Schedule entered the current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
    <td>The lifetime resource usage statistics for the Job Schedule. The statistics may not be immediately available. The Batch service performs periodic roll-up of statistics. The typical delay is about 30 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Job Schedule. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_job_schedules">

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
    <td>A string that uniquely identifies the schedule within the Account. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation time of the Job Schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name for the schedule.</td>
</tr>
<tr>
    <td><CopyableCode code="eTag" /></td>
    <td><code>string</code></td>
    <td>The ETag of the Job Schedule. This is an opaque string. You can use it to detect whether the Job Schedule has changed between requests. In particular, you can be pass the ETag with an Update Job Schedule request to specify that your changes should take effect only if nobody else has modified the schedule in the meantime. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="executionInfo" /></td>
    <td><code>object</code></td>
    <td>Information about Jobs that have been and will be run under this schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="jobSpecification" /></td>
    <td><code>object</code></td>
    <td>The details of the Jobs to be created on this schedule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModified" /></td>
    <td><code>string (date-time)</code></td>
    <td>The last modified time of the Job Schedule. This is the last time at which the schedule level data, such as the Job specification or recurrence information, changed. It does not factor in job-level changes such as new Jobs being created or Jobs changing state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>array</code></td>
    <td>A list of name-value pairs associated with the schedule as metadata. The Batch service does not assign any meaning to metadata; it is solely for the use of user code.</td>
</tr>
<tr>
    <td><CopyableCode code="previousState" /></td>
    <td><code>string</code></td>
    <td>The previous state of the Job Schedule. This property is not present if the Job Schedule is in its initial active state. Known values are: "active", "completed", "disabled", "terminating", and "deleting". (active, completed, disabled, terminating, deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="previousStateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Job Schedule entered its previous state. This property is not present if the Job Schedule is in its initial active state.</td>
</tr>
<tr>
    <td><CopyableCode code="schedule" /></td>
    <td><code>object</code></td>
    <td>The schedule according to which Jobs will be created. All times are fixed respective to UTC and are not impacted by daylight saving time.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The current state of the Job Schedule. Required. Known values are: "active", "completed", "disabled", "terminating", and "deleting". (active, completed, disabled, terminating, deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="stateTransitionTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The time at which the Job Schedule entered the current state. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stats" /></td>
    <td><code>object</code></td>
    <td>The lifetime resource usage statistics for the Job Schedule. The statistics may not be immediately available. The Batch service performs periodic roll-up of statistics. The typical delay is about 30 minutes.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>The URL of the Job Schedule. Required.</td>
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
    <td><a href="#get_job_schedule"><CopyableCode code="get_job_schedule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-job_schedule_id"><code>job_schedule_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets information about the specified Job Schedule.</td>
</tr>
<tr>
    <td><a href="#list_job_schedules"><CopyableCode code="list_job_schedules" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-maxresults"><code>maxresults</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Lists all of the Job Schedules in the specified Account. Lists all of the Job Schedules in the specified Account.</td>
</tr>
<tr>
    <td><a href="#create_job_schedule"><CopyableCode code="create_job_schedule" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-id"><code>id</code></a>, <a href="#parameter-schedule"><code>schedule</code></a>, <a href="#parameter-jobSpecification"><code>jobSpecification</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Creates a Job Schedule to the specified Account. Creates a Job Schedule to the specified Account.</td>
</tr>
<tr>
    <td><a href="#update_job_schedule"><CopyableCode code="update_job_schedule" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-job_schedule_id"><code>job_schedule_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a>, <a href="#parameter-If-Modified-Since"><code>If-Modified-Since</code></a>, <a href="#parameter-If-Unmodified-Since"><code>If-Unmodified-Since</code></a></td>
    <td>Updates the properties of the specified Job Schedule. This replaces only the Job Schedule properties specified in the request. For example, if the schedule property is not specified with this request, then the Batch service will keep the existing schedule. Changes to a Job Schedule only impact Jobs created by the schedule after the update has taken place; currently running Jobs are unaffected.</td>
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
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-job_schedule_id">
    <td><CopyableCode code="job_schedule_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Job Schedule to update. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>array</code></td>
    <td>An OData $expand clause. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>An OData $filter clause. For more information on constructing this filter, see `https://learn.microsoft.com/rest/api/batchservice/odata-filters-in-batch#list-job-schedules `_. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>array</code></td>
    <td>An OData $select clause. Default value is None.</td>
</tr>
<tr id="parameter-If-Modified-Since">
    <td><CopyableCode code="If-Modified-Since" /></td>
    <td><code>string</code></td>
    <td>A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time. Default value is None.</td>
</tr>
<tr id="parameter-If-Unmodified-Since">
    <td><CopyableCode code="If-Unmodified-Since" /></td>
    <td><code>string</code></td>
    <td>A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time. Default value is None.</td>
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
    defaultValue="get_job_schedule"
    values={[
        { label: 'get_job_schedule', value: 'get_job_schedule' },
        { label: 'list_job_schedules', value: 'list_job_schedules' }
    ]}
>
<TabItem value="get_job_schedule">

Gets information about the specified Job Schedule.

```sql
SELECT
id,
creationTime,
displayName,
eTag,
executionInfo,
jobSpecification,
lastModified,
metadata,
previousState,
previousStateTransitionTime,
schedule,
state,
stateTransitionTime,
stats,
url
FROM azure.batch_dataplane.job_schedules
WHERE job_schedule_id = '{{ job_schedule_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND If-Modified-Since = '{{ If-Modified-Since }}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_job_schedules">

Lists all of the Job Schedules in the specified Account. Lists all of the Job Schedules in the specified Account.

```sql
SELECT
id,
creationTime,
displayName,
eTag,
executionInfo,
jobSpecification,
lastModified,
metadata,
previousState,
previousStateTransitionTime,
schedule,
state,
stateTransitionTime,
stats,
url
FROM azure.batch_dataplane.job_schedules
WHERE endpoint = '{{ endpoint }}' -- required
AND timeOut = '{{ timeOut }}'
AND ocp-date = '{{ ocp-date }}'
AND maxresults = '{{ maxresults }}'
AND $filter = '{{ $filter }}'
AND $select = '{{ $select }}'
AND $expand = '{{ $expand }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_job_schedule"
    values={[
        { label: 'create_job_schedule', value: 'create_job_schedule' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_job_schedule">

Creates a Job Schedule to the specified Account. Creates a Job Schedule to the specified Account.

```sql
INSERT INTO azure.batch_dataplane.job_schedules (
id,
displayName,
schedule,
jobSpecification,
metadata,
endpoint,
timeOut,
ocp-date
)
SELECT 
'{{ id }}' /* required */,
'{{ displayName }}',
'{{ schedule }}' /* required */,
'{{ jobSpecification }}' /* required */,
'{{ metadata }}',
'{{ endpoint }}',
'{{ timeOut }}',
'{{ ocp-date }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: job_schedules
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the job_schedules resource.
    - name: id
      value: "{{ id }}"
      description: |
        A string that uniquely identifies the schedule within the Account. The ID can contain any combination of alphanumeric characters including hyphens and underscores, and cannot contain more than 64 characters. The ID is case-preserving and case-insensitive (that is, you may not have two IDs within an Account that differ only by case). Required.
    - name: displayName
      value: "{{ displayName }}"
      description: |
        The display name for the schedule. The display name need not be unique and can contain any Unicode characters up to a maximum length of 1024.
    - name: schedule
      description: |
        The schedule according to which Jobs will be created. All times are fixed respective to UTC and are not impacted by daylight saving time. Required.
      value:
        doNotRunUntil: "{{ doNotRunUntil }}"
        doNotRunAfter: "{{ doNotRunAfter }}"
        startWindow: "{{ startWindow }}"
        recurrenceInterval: "{{ recurrenceInterval }}"
    - name: jobSpecification
      description: |
        The details of the Jobs to be created on this schedule. Required.
      value:
        priority: {{ priority }}
        allowTaskPreemption: {{ allowTaskPreemption }}
        maxParallelTasks: {{ maxParallelTasks }}
        displayName: "{{ displayName }}"
        usesTaskDependencies: {{ usesTaskDependencies }}
        onAllTasksComplete: "{{ onAllTasksComplete }}"
        onTaskFailure: "{{ onTaskFailure }}"
        networkConfiguration:
          subnetId: "{{ subnetId }}"
          skipWithdrawFromVNet: {{ skipWithdrawFromVNet }}
        constraints:
          maxWallClockTime: "{{ maxWallClockTime }}"
          maxTaskRetryCount: {{ maxTaskRetryCount }}
        jobManagerTask:
          id: "{{ id }}"
          displayName: "{{ displayName }}"
          commandLine: "{{ commandLine }}"
          containerSettings:
            containerRunOptions: "{{ containerRunOptions }}"
            imageName: "{{ imageName }}"
            registry:
              username: "{{ username }}"
              password: "{{ password }}"
              registryServer: "{{ registryServer }}"
              identityReference:
                resourceId: "{{ resourceId }}"
            workingDirectory: "{{ workingDirectory }}"
            containerHostBatchBindMounts:
              - source: "{{ source }}"
                isReadOnly: {{ isReadOnly }}
          resourceFiles:
            - autoStorageContainerName: "{{ autoStorageContainerName }}"
              storageContainerUrl: "{{ storageContainerUrl }}"
              httpUrl: "{{ httpUrl }}"
              blobPrefix: "{{ blobPrefix }}"
              filePath: "{{ filePath }}"
              fileMode: "{{ fileMode }}"
              identityReference:
                resourceId: "{{ resourceId }}"
          outputFiles:
            - filePattern: "{{ filePattern }}"
              destination:
                container:
                  path: "{{ path }}"
                  containerUrl: "{{ containerUrl }}"
                  identityReference: "{{ identityReference }}"
                  uploadHeaders: "{{ uploadHeaders }}"
              uploadOptions:
                uploadCondition: "{{ uploadCondition }}"
          environmentSettings:
            - name: "{{ name }}"
              value: "{{ value }}"
          constraints:
            maxWallClockTime: "{{ maxWallClockTime }}"
            retentionTime: "{{ retentionTime }}"
            maxTaskRetryCount: {{ maxTaskRetryCount }}
          requiredSlots: {{ requiredSlots }}
          killJobOnCompletion: {{ killJobOnCompletion }}
          userIdentity:
            username: "{{ username }}"
            autoUser:
              scope: "{{ scope }}"
              elevationLevel: "{{ elevationLevel }}"
          runExclusive: {{ runExclusive }}
          applicationPackageReferences:
            - applicationId: "{{ applicationId }}"
              version: "{{ version }}"
          allowLowPriorityNode: {{ allowLowPriorityNode }}
        jobPreparationTask:
          id: "{{ id }}"
          commandLine: "{{ commandLine }}"
          containerSettings:
            containerRunOptions: "{{ containerRunOptions }}"
            imageName: "{{ imageName }}"
            registry:
              username: "{{ username }}"
              password: "{{ password }}"
              registryServer: "{{ registryServer }}"
              identityReference:
                resourceId: "{{ resourceId }}"
            workingDirectory: "{{ workingDirectory }}"
            containerHostBatchBindMounts:
              - source: "{{ source }}"
                isReadOnly: {{ isReadOnly }}
          resourceFiles:
            - autoStorageContainerName: "{{ autoStorageContainerName }}"
              storageContainerUrl: "{{ storageContainerUrl }}"
              httpUrl: "{{ httpUrl }}"
              blobPrefix: "{{ blobPrefix }}"
              filePath: "{{ filePath }}"
              fileMode: "{{ fileMode }}"
              identityReference:
                resourceId: "{{ resourceId }}"
          environmentSettings:
            - name: "{{ name }}"
              value: "{{ value }}"
          constraints:
            maxWallClockTime: "{{ maxWallClockTime }}"
            retentionTime: "{{ retentionTime }}"
            maxTaskRetryCount: {{ maxTaskRetryCount }}
          waitForSuccess: {{ waitForSuccess }}
          userIdentity:
            username: "{{ username }}"
            autoUser:
              scope: "{{ scope }}"
              elevationLevel: "{{ elevationLevel }}"
          rerunOnNodeRebootAfterSuccess: {{ rerunOnNodeRebootAfterSuccess }}
        jobReleaseTask:
          id: "{{ id }}"
          commandLine: "{{ commandLine }}"
          containerSettings:
            containerRunOptions: "{{ containerRunOptions }}"
            imageName: "{{ imageName }}"
            registry:
              username: "{{ username }}"
              password: "{{ password }}"
              registryServer: "{{ registryServer }}"
              identityReference:
                resourceId: "{{ resourceId }}"
            workingDirectory: "{{ workingDirectory }}"
            containerHostBatchBindMounts:
              - source: "{{ source }}"
                isReadOnly: {{ isReadOnly }}
          resourceFiles:
            - autoStorageContainerName: "{{ autoStorageContainerName }}"
              storageContainerUrl: "{{ storageContainerUrl }}"
              httpUrl: "{{ httpUrl }}"
              blobPrefix: "{{ blobPrefix }}"
              filePath: "{{ filePath }}"
              fileMode: "{{ fileMode }}"
              identityReference:
                resourceId: "{{ resourceId }}"
          environmentSettings:
            - name: "{{ name }}"
              value: "{{ value }}"
          maxWallClockTime: "{{ maxWallClockTime }}"
          retentionTime: "{{ retentionTime }}"
          userIdentity:
            username: "{{ username }}"
            autoUser:
              scope: "{{ scope }}"
              elevationLevel: "{{ elevationLevel }}"
        commonEnvironmentSettings:
          - name: "{{ name }}"
            value: "{{ value }}"
        poolInfo:
          poolId: "{{ poolId }}"
          autoPoolSpecification:
            autoPoolIdPrefix: "{{ autoPoolIdPrefix }}"
            poolLifetimeOption: "{{ poolLifetimeOption }}"
            keepAlive: {{ keepAlive }}
            pool:
              displayName: "{{ displayName }}"
              vmSize: "{{ vmSize }}"
              virtualMachineConfiguration:
                imageReference: "{{ imageReference }}"
                nodeAgentSKUId: "{{ nodeAgentSKUId }}"
                windowsConfiguration: "{{ windowsConfiguration }}"
                dataDisks: "{{ dataDisks }}"
                licenseType: "{{ licenseType }}"
                containerConfiguration: "{{ containerConfiguration }}"
                diskEncryptionConfiguration: "{{ diskEncryptionConfiguration }}"
                nodePlacementConfiguration: "{{ nodePlacementConfiguration }}"
                extensions: "{{ extensions }}"
                osDisk: "{{ osDisk }}"
                securityProfile: "{{ securityProfile }}"
                serviceArtifactReference: "{{ serviceArtifactReference }}"
              taskSlotsPerNode: {{ taskSlotsPerNode }}
              taskSchedulingPolicy:
                jobDefaultOrder: "{{ jobDefaultOrder }}"
                nodeFillType: "{{ nodeFillType }}"
              resizeTimeout: "{{ resizeTimeout }}"
              targetDedicatedNodes: {{ targetDedicatedNodes }}
              targetLowPriorityNodes: {{ targetLowPriorityNodes }}
              enableAutoScale: {{ enableAutoScale }}
              autoScaleFormula: "{{ autoScaleFormula }}"
              autoScaleEvaluationInterval: "{{ autoScaleEvaluationInterval }}"
              enableInterNodeCommunication: {{ enableInterNodeCommunication }}
              networkConfiguration:
                subnetId: "{{ subnetId }}"
                dynamicVNetAssignmentScope: "{{ dynamicVNetAssignmentScope }}"
                endpointConfiguration: "{{ endpointConfiguration }}"
                publicIPAddressConfiguration: "{{ publicIPAddressConfiguration }}"
                enableAcceleratedNetworking: {{ enableAcceleratedNetworking }}
              startTask:
                commandLine: "{{ commandLine }}"
                containerSettings: "{{ containerSettings }}"
                resourceFiles: "{{ resourceFiles }}"
                environmentSettings: "{{ environmentSettings }}"
                userIdentity: "{{ userIdentity }}"
                maxTaskRetryCount: {{ maxTaskRetryCount }}
                waitForSuccess: {{ waitForSuccess }}
              applicationPackageReferences:
                - applicationId: "{{ applicationId }}"
                  version: "{{ version }}"
              userAccounts:
                - name: "{{ name }}"
                  password: "{{ password }}"
                  elevationLevel: "{{ elevationLevel }}"
                  linuxUserConfiguration:
                    uid: {{ uid }}
                    gid: {{ gid }}
                    sshPrivateKey: "{{ sshPrivateKey }}"
                  windowsUserConfiguration:
                    loginMode: "{{ loginMode }}"
              metadata:
                - name: "{{ name }}"
                  value: "{{ value }}"
              mountConfiguration:
                - azureBlobFileSystemConfiguration:
                    accountName: "{{ accountName }}"
                    containerName: "{{ containerName }}"
                    accountKey: "{{ accountKey }}"
                    sasKey: "{{ sasKey }}"
                    blobfuseOptions: "{{ blobfuseOptions }}"
                    relativeMountPath: "{{ relativeMountPath }}"
                    identityReference: "{{ identityReference }}"
                  nfsMountConfiguration:
                    source: "{{ source }}"
                    relativeMountPath: "{{ relativeMountPath }}"
                    mountOptions: "{{ mountOptions }}"
                  cifsMountConfiguration:
                    username: "{{ username }}"
                    source: "{{ source }}"
                    relativeMountPath: "{{ relativeMountPath }}"
                    mountOptions: "{{ mountOptions }}"
                    password: "{{ password }}"
                  azureFileShareConfiguration:
                    accountName: "{{ accountName }}"
                    accountKey: "{{ accountKey }}"
                    azureFileUrl: "{{ azureFileUrl }}"
                    relativeMountPath: "{{ relativeMountPath }}"
                    mountOptions: "{{ mountOptions }}"
              upgradePolicy:
                mode: "{{ mode }}"
                automaticOSUpgradePolicy: "{{ automaticOSUpgradePolicy }}"
                rollingUpgradePolicy: "{{ rollingUpgradePolicy }}"
        metadata:
          - name: "{{ name }}"
            value: "{{ value }}"
    - name: metadata
      description: |
        A list of name-value pairs associated with the schedule as metadata. The Batch service does not assign any meaning to metadata; it is solely for the use of user code.
      value:
        - name: "{{ name }}"
          value: "{{ value }}"
    - name: timeOut
      value: {{ timeOut }}
      description: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.
      description: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds. If the value is larger than 30, the default will be used instead.". Default value is None.
    - name: ocp-date
      value: "{{ ocp-date }}"
      description: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.
      description: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly. Default value is None.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_job_schedule"
    values={[
        { label: 'update_job_schedule', value: 'update_job_schedule' }
    ]}
>
<TabItem value="update_job_schedule">

Updates the properties of the specified Job Schedule. This replaces only the Job Schedule properties specified in the request. For example, if the schedule property is not specified with this request, then the Batch service will keep the existing schedule. Changes to a Job Schedule only impact Jobs created by the schedule after the update has taken place; currently running Jobs are unaffected.

```sql
UPDATE azure.batch_dataplane.job_schedules
SET 
schedule = '{{ schedule }}',
jobSpecification = '{{ jobSpecification }}',
metadata = '{{ metadata }}'
WHERE 
job_schedule_id = '{{ job_schedule_id }}' --required
AND endpoint = '{{ endpoint }}' --required
AND timeOut = '{{ timeOut}}'
AND ocp-date = '{{ ocp-date}}'
AND If-Modified-Since = '{{ If-Modified-Since}}'
AND If-Unmodified-Since = '{{ If-Unmodified-Since}}';
```
</TabItem>
</Tabs>
