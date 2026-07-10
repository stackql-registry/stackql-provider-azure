--- 
title: mesh_application
hide_title: false
hide_table_of_contents: false
keywords:
  - mesh_application
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>mesh_application</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="mesh_application" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.mesh_application" /></td></tr>
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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="debugParams" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>Describes the diagnostics options available.</td>
</tr>
<tr>
    <td><CopyableCode code="healthState" /></td>
    <td><code>string</code></td>
    <td>Describes the health state of an application resource. Possible values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Information describing the identities associated with this application. All required parameters must be populated in order to send to Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceNames" /></td>
    <td><code>array</code></td>
    <td>Names of the services in the application.</td>
</tr>
<tr>
    <td><CopyableCode code="services" /></td>
    <td><code>array</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the application. Possible values include: 'Unknown', 'Ready', 'Upgrading', 'Creating', 'Deleting', 'Failed'</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Gives additional information about the current status of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="unhealthyEvaluation" /></td>
    <td><code>string</code></td>
    <td>When the application's health state is not 'Ok', this additional details from service fabric Health Manager for the user to know why the application is marked unhealthy.</td>
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
    <td><CopyableCode code="ContinuationToken" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="Items" /></td>
    <td><code>array</code></td>
    <td></td>
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
    <td><a href="#parameter-application_resource_name"><code>application_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the Application resource with the given name. Gets the information about the Application resource with the given name. The information include the description and other properties of the Application.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Lists all the application resources. Gets the information about all application resources in a given resource group. The information include the description and other properties of the Application.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-application_resource_name"><code>application_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates or updates a Application resource. Creates a Application resource with the specified name, description and properties. If Application resource with the same name exists, then it is updated with the specified description and properties.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-application_resource_name"><code>application_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Creates or updates a Application resource. Creates a Application resource with the specified name, description and properties. If Application resource with the same name exists, then it is updated with the specified description and properties.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-application_resource_name"><code>application_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes the Application resource. Deletes the Application resource identified by the name.</td>
</tr>
<tr>
    <td><a href="#get_upgrade_progress"><CopyableCode code="get_upgrade_progress" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-application_resource_name"><code>application_resource_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets the progress of the latest upgrade performed on this application resource. Gets the upgrade progress information about the Application resource with the given name. The information include percentage of completion and other upgrade state information of the Application resource.</td>
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
<tr id="parameter-application_resource_name">
    <td><CopyableCode code="application_resource_name" /></td>
    <td><code>string</code></td>
    <td>The identity of the application.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
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

Gets the Application resource with the given name. Gets the information about the Application resource with the given name. The information include the description and other properties of the Application.

```sql
SELECT
name,
debugParams,
description,
diagnostics,
healthState,
identity,
serviceNames,
services,
status,
statusDetails,
unhealthyEvaluation
FROM azure.servicefabric_dataplane.mesh_application
WHERE application_resource_name = '{{ application_resource_name }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all the application resources. Gets the information about all application resources in a given resource group. The information include the description and other properties of the Application.

```sql
SELECT
ContinuationToken,
Items
FROM azure.servicefabric_dataplane.mesh_application
WHERE endpoint = '{{ endpoint }}' -- required
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

Creates or updates a Application resource. Creates a Application resource with the specified name, description and properties. If Application resource with the same name exists, then it is updated with the specified description and properties.

```sql
INSERT INTO azure.servicefabric_dataplane.mesh_application (
name,
properties,
identity,
application_resource_name,
endpoint
)
SELECT 
'{{ name }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ application_resource_name }}',
'{{ endpoint }}'
RETURNING
name,
identity,
properties
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: mesh_application
  props:
    - name: application_resource_name
      value: "{{ application_resource_name }}"
      description: Required parameter for the mesh_application resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the mesh_application resource.
    - name: name
      value: "{{ name }}"
    - name: properties
      value:
        description: "{{ description }}"
        services:
          - name: "{{ name }}"
            properties:
              osType: "{{ osType }}"
              codePackages:
                - name: "{{ name }}"
                  image: "{{ image }}"
                  imageRegistryCredential:
                    server: "{{ server }}"
                    username: "{{ username }}"
                    passwordType: "{{ passwordType }}"
                    password: "{{ password }}"
                  entryPoint: "{{ entryPoint }}"
                  commands: "{{ commands }}"
                  environmentVariables: "{{ environmentVariables }}"
                  settings: "{{ settings }}"
                  labels: "{{ labels }}"
                  endpoints: "{{ endpoints }}"
                  resources:
                    requests: "{{ requests }}"
                    limits: "{{ limits }}"
                  volumeRefs: "{{ volumeRefs }}"
                  volumes: "{{ volumes }}"
                  diagnostics:
                    enabled: {{ enabled }}
                    sinkRefs: "{{ sinkRefs }}"
                  reliableCollectionsRefs: "{{ reliableCollectionsRefs }}"
                  instanceView:
                    restartCount: {{ restartCount }}
                    currentState: "{{ currentState }}"
                    previousState: "{{ previousState }}"
                    events: "{{ events }}"
                  livenessProbe: "{{ livenessProbe }}"
                  readinessProbe: "{{ readinessProbe }}"
              networkRefs:
                - name: "{{ name }}"
                  endpointRefs: "{{ endpointRefs }}"
              diagnostics:
                enabled: {{ enabled }}
                sinkRefs:
                  - "{{ sinkRefs }}"
              description: "{{ description }}"
              replicaCount: {{ replicaCount }}
              executionPolicy:
                type: "{{ type }}"
              autoScalingPolicies:
                - name: "{{ name }}"
                  trigger:
                    kind: "{{ kind }}"
                  mechanism:
                    kind: "{{ kind }}"
              status: "{{ status }}"
              statusDetails: "{{ statusDetails }}"
              healthState: "{{ healthState }}"
              unhealthyEvaluation: "{{ unhealthyEvaluation }}"
              identityRefs:
                - name: "{{ name }}"
                  identityRef: "{{ identityRef }}"
              dnsName: "{{ dnsName }}"
        diagnostics:
          sinks:
            - name: "{{ name }}"
              description: "{{ description }}"
              kind: "{{ kind }}"
          enabled: {{ enabled }}
          defaultSinkRefs:
            - "{{ defaultSinkRefs }}"
        debugParams: "{{ debugParams }}"
    - name: identity
      description: |
        Information describing the identities associated with this application. All required parameters must be populated in order to send to Azure.
      value:
        tokenServiceEndpoint: "{{ tokenServiceEndpoint }}"
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
        principalId: "{{ principalId }}"
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

Creates or updates a Application resource. Creates a Application resource with the specified name, description and properties. If Application resource with the same name exists, then it is updated with the specified description and properties.

```sql
REPLACE azure.servicefabric_dataplane.mesh_application
SET 
name = '{{ name }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
application_resource_name = '{{ application_resource_name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND name = '{{ name }}' --required
RETURNING
name,
identity,
properties;
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

Deletes the Application resource. Deletes the Application resource identified by the name.

```sql
DELETE FROM azure.servicefabric_dataplane.mesh_application
WHERE application_resource_name = '{{ application_resource_name }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_upgrade_progress"
    values={[
        { label: 'get_upgrade_progress', value: 'get_upgrade_progress' }
    ]}
>
<TabItem value="get_upgrade_progress">

Gets the progress of the latest upgrade performed on this application resource. Gets the upgrade progress information about the Application resource with the given name. The information include percentage of completion and other upgrade state information of the Application resource.

```sql
EXEC azure.servicefabric_dataplane.mesh_application.get_upgrade_progress 
@application_resource_name='{{ application_resource_name }}' --required, 
@endpoint='{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
