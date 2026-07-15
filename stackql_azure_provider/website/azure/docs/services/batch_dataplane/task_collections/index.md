--- 
title: task_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - task_collections
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

Creates, updates, deletes, gets or lists a <code>task_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="task_collections" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch_dataplane.task_collections" /></td></tr>
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
    <td><a href="#create_task_collection"><CopyableCode code="create_task_collection" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-job_id"><code>job_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-value"><code>value</code></a></td>
    <td><a href="#parameter-timeOut"><code>timeOut</code></a>, <a href="#parameter-ocp-date"><code>ocp-date</code></a></td>
    <td>Adds a collection of Tasks to the specified Job. Note that each Task must have a unique ID. The Batch service may not return the results for each Task in the same order the Tasks were submitted in this request. If the server times out or the connection is closed during the request, the request may have been partially or fully processed, or not at all. In such cases, the user should re-issue the request. Note that it is up to the user to correctly handle failures when re-issuing a request. For example, you should use the same Task IDs during a retry so that if the prior operation succeeded, the retry will not create extra Tasks unexpectedly. If the response contains any Tasks which failed to add, a client can retry the request. In a retry, it is most efficient to resubmit only Tasks that failed to add, and to omit Tasks that were successfully added on the first attempt. The maximum lifetime of a Task from addition to completion is 180 days. If a Task has not completed within 180 days of being added it will be terminated by the Batch service and left in whatever state it was in at that time.</td>
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
<tr id="parameter-job_id">
    <td><CopyableCode code="job_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the Job to which the Task collection is to be added. Required.</td>
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

## `INSERT` examples

<Tabs
    defaultValue="create_task_collection"
    values={[
        { label: 'create_task_collection', value: 'create_task_collection' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_task_collection">

Adds a collection of Tasks to the specified Job. Note that each Task must have a unique ID. The Batch service may not return the results for each Task in the same order the Tasks were submitted in this request. If the server times out or the connection is closed during the request, the request may have been partially or fully processed, or not at all. In such cases, the user should re-issue the request. Note that it is up to the user to correctly handle failures when re-issuing a request. For example, you should use the same Task IDs during a retry so that if the prior operation succeeded, the retry will not create extra Tasks unexpectedly. If the response contains any Tasks which failed to add, a client can retry the request. In a retry, it is most efficient to resubmit only Tasks that failed to add, and to omit Tasks that were successfully added on the first attempt. The maximum lifetime of a Task from addition to completion is 180 days. If a Task has not completed within 180 days of being added it will be terminated by the Batch service and left in whatever state it was in at that time.

```sql
INSERT INTO azure.batch_dataplane.task_collections (
value,
job_id,
endpoint,
timeOut,
ocp-date
)
SELECT 
'{{ value }}' /* required */,
'{{ job_id }}',
'{{ endpoint }}',
'{{ timeOut }}',
'{{ ocp-date }}'
RETURNING
value
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: task_collections
  props:
    - name: job_id
      value: "{{ job_id }}"
      description: Required parameter for the task_collections resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the task_collections resource.
    - name: value
      description: |
        The collection of Tasks to add. The maximum count of Tasks is 100. The total serialized size of this collection must be less than 1MB. If it is greater than 1MB (for example if each Task has 100's of resource files or environment variables), the request will fail with code 'RequestBodyTooLarge' and should be retried again with fewer Tasks. Required.
      value:
        - id: "{{ id }}"
          displayName: "{{ displayName }}"
          exitConditions:
            exitCodes:
              - code: {{ code }}
                exitOptions:
                  jobAction: "{{ jobAction }}"
                  dependencyAction: "{{ dependencyAction }}"
            exitCodeRanges:
              - start: {{ start }}
                end: {{ end }}
                exitOptions:
                  jobAction: "{{ jobAction }}"
                  dependencyAction: "{{ dependencyAction }}"
            preProcessingError:
              jobAction: "{{ jobAction }}"
              dependencyAction: "{{ dependencyAction }}"
            fileUploadError:
              jobAction: "{{ jobAction }}"
              dependencyAction: "{{ dependencyAction }}"
            default:
              jobAction: "{{ jobAction }}"
              dependencyAction: "{{ dependencyAction }}"
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
          resourceFiles: "{{ resourceFiles }}"
          outputFiles: "{{ outputFiles }}"
          environmentSettings: "{{ environmentSettings }}"
          affinityInfo:
            affinityId: "{{ affinityId }}"
          constraints:
            maxWallClockTime: "{{ maxWallClockTime }}"
            retentionTime: "{{ retentionTime }}"
            maxTaskRetryCount: {{ maxTaskRetryCount }}
          requiredSlots: {{ requiredSlots }}
          userIdentity:
            username: "{{ username }}"
            autoUser:
              scope: "{{ scope }}"
              elevationLevel: "{{ elevationLevel }}"
          multiInstanceSettings:
            numberOfInstances: {{ numberOfInstances }}
            coordinationCommandLine: "{{ coordinationCommandLine }}"
            commonResourceFiles:
              - autoStorageContainerName: "{{ autoStorageContainerName }}"
                storageContainerUrl: "{{ storageContainerUrl }}"
                httpUrl: "{{ httpUrl }}"
                blobPrefix: "{{ blobPrefix }}"
                filePath: "{{ filePath }}"
                fileMode: "{{ fileMode }}"
                identityReference:
                  resourceId: "{{ resourceId }}"
          dependsOn:
            taskIds:
              - "{{ taskIds }}"
            taskIdRanges:
              - start: {{ start }}
                end: {{ end }}
          applicationPackageReferences: "{{ applicationPackageReferences }}"
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
