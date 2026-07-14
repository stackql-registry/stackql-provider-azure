--- 
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - app_platform
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.app_platform.deployments" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_for_cluster', value: 'list_for_cluster' }
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Deployment is active.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentSettings" /></td>
    <td><code>object</code></td>
    <td>Deployment settings of the Deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>Collection of instances belong to the Deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Deployment. Known values are: "Creating", "Updating", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the Deployment resource.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Uploaded source information of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the Deployment. Known values are: "Stopped" and "Running".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Deployment is active.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentSettings" /></td>
    <td><code>object</code></td>
    <td>Deployment settings of the Deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>Collection of instances belong to the Deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Deployment. Known values are: "Creating", "Updating", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the Deployment resource.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Uploaded source information of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the Deployment. Known values are: "Stopped" and "Running".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_for_cluster">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="active" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the Deployment is active.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentSettings" /></td>
    <td><code>object</code></td>
    <td>Deployment settings of the Deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>Collection of instances belong to the Deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Deployment. Known values are: "Creating", "Updating", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Sku of the Deployment resource.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>Uploaded source information of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Status of the Deployment. Known values are: "Stopped" and "Running".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Deployment and its properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all resources in an App.</td>
</tr>
<tr>
    <td><a href="#list_for_cluster"><CopyableCode code="list_for_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>List deployments for a certain service.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Deployment or update an exiting Deployment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to update an exiting Deployment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Deployment or update an exiting Deployment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to delete a Deployment.</td>
</tr>
<tr>
    <td><a href="#get_remote_debugging_config"><CopyableCode code="get_remote_debugging_config" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get remote debugging config.</td>
</tr>
<tr>
    <td><a href="#get_log_file_url"><CopyableCode code="get_log_file_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get deployment log file URL.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start the deployment.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stop the deployment.</td>
</tr>
<tr>
    <td><a href="#restart"><CopyableCode code="restart" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Restart the deployment.</td>
</tr>
<tr>
    <td><a href="#enable_remote_debugging"><CopyableCode code="enable_remote_debugging" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Enable remote debugging.</td>
</tr>
<tr>
    <td><a href="#disable_remote_debugging"><CopyableCode code="disable_remote_debugging" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable remote debugging.</td>
</tr>
<tr>
    <td><a href="#generate_heap_dump"><CopyableCode code="generate_heap_dump" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate Heap Dump.</td>
</tr>
<tr>
    <td><a href="#generate_thread_dump"><CopyableCode code="generate_thread_dump" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate Thread Dump.</td>
</tr>
<tr>
    <td><a href="#start_jfr"><CopyableCode code="start_jfr" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Start JFR.</td>
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
<tr id="parameter-app_name">
    <td><CopyableCode code="app_name" /></td>
    <td><code>string</code></td>
    <td>The name of the App resource. Required.</td>
</tr>
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Deployment resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Service resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_for_cluster', value: 'list_for_cluster' }
    ]}
>
<TabItem value="get">

Get a Deployment and its properties.

```sql
SELECT
id,
name,
active,
deploymentSettings,
instances,
provisioningState,
sku,
source,
status,
systemData,
type
FROM azure_extras.app_platform.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND app_name = '{{ app_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Handles requests to list all resources in an App.

```sql
SELECT
id,
name,
active,
deploymentSettings,
instances,
provisioningState,
sku,
source,
status,
systemData,
type
FROM azure_extras.app_platform.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND app_name = '{{ app_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_for_cluster">

List deployments for a certain service.

```sql
SELECT
id,
name,
active,
deploymentSettings,
instances,
provisioningState,
sku,
source,
status,
systemData,
type
FROM azure_extras.app_platform.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a new Deployment or update an exiting Deployment.

```sql
INSERT INTO azure_extras.app_platform.deployments (
properties,
sku,
resource_group_name,
service_name,
app_name,
deployment_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ app_name }}',
'{{ deployment_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
sku,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: deployments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the deployments resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the deployments resource.
    - name: app_name
      value: "{{ app_name }}"
      description: Required parameter for the deployments resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the deployments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the deployments resource.
    - name: properties
      description: |
        Properties of the Deployment resource.
      value:
        source:
          type: "{{ type }}"
          version: "{{ version }}"
        deploymentSettings:
          resourceRequests:
            cpu: "{{ cpu }}"
            memory: "{{ memory }}"
          environmentVariables: "{{ environmentVariables }}"
          apms:
            - resourceId: "{{ resourceId }}"
          addonConfigs: "{{ addonConfigs }}"
          livenessProbe:
            probeAction:
              type: "{{ type }}"
            disableProbe: {{ disableProbe }}
            initialDelaySeconds: {{ initialDelaySeconds }}
            periodSeconds: {{ periodSeconds }}
            timeoutSeconds: {{ timeoutSeconds }}
            failureThreshold: {{ failureThreshold }}
            successThreshold: {{ successThreshold }}
          readinessProbe:
            probeAction:
              type: "{{ type }}"
            disableProbe: {{ disableProbe }}
            initialDelaySeconds: {{ initialDelaySeconds }}
            periodSeconds: {{ periodSeconds }}
            timeoutSeconds: {{ timeoutSeconds }}
            failureThreshold: {{ failureThreshold }}
            successThreshold: {{ successThreshold }}
          startupProbe:
            probeAction:
              type: "{{ type }}"
            disableProbe: {{ disableProbe }}
            initialDelaySeconds: {{ initialDelaySeconds }}
            periodSeconds: {{ periodSeconds }}
            timeoutSeconds: {{ timeoutSeconds }}
            failureThreshold: {{ failureThreshold }}
            successThreshold: {{ successThreshold }}
          terminationGracePeriodSeconds: {{ terminationGracePeriodSeconds }}
          containerProbeSettings:
            disableProbe: {{ disableProbe }}
        provisioningState: "{{ provisioningState }}"
        status: "{{ status }}"
        active: {{ active }}
        instances:
          - name: "{{ name }}"
            status: "{{ status }}"
            reason: "{{ reason }}"
            discoveryStatus: "{{ discoveryStatus }}"
            startTime: "{{ startTime }}"
            zone: "{{ zone }}"
    - name: sku
      description: |
        Sku of the Deployment resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        capacity: {{ capacity }}
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

Operation to update an exiting Deployment.

```sql
UPDATE azure_extras.app_platform.deployments
SET 
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
sku,
systemData,
type;
```
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

Create a new Deployment or update an exiting Deployment.

```sql
REPLACE azure_extras.app_platform.deployments
SET 
properties = '{{ properties }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
sku,
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

Operation to delete a Deployment.

```sql
DELETE FROM azure_extras.app_platform.deployments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_remote_debugging_config"
    values={[
        { label: 'get_remote_debugging_config', value: 'get_remote_debugging_config' },
        { label: 'get_log_file_url', value: 'get_log_file_url' },
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' },
        { label: 'restart', value: 'restart' },
        { label: 'enable_remote_debugging', value: 'enable_remote_debugging' },
        { label: 'disable_remote_debugging', value: 'disable_remote_debugging' },
        { label: 'generate_heap_dump', value: 'generate_heap_dump' },
        { label: 'generate_thread_dump', value: 'generate_thread_dump' },
        { label: 'start_jfr', value: 'start_jfr' }
    ]}
>
<TabItem value="get_remote_debugging_config">

Get remote debugging config.

```sql
EXEC azure_extras.app_platform.deployments.get_remote_debugging_config 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_log_file_url">

Get deployment log file URL.

```sql
EXEC azure_extras.app_platform.deployments.get_log_file_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start">

Start the deployment.

```sql
EXEC azure_extras.app_platform.deployments.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="stop">

Stop the deployment.

```sql
EXEC azure_extras.app_platform.deployments.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="restart">

Restart the deployment.

```sql
EXEC azure_extras.app_platform.deployments.restart 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable_remote_debugging">

Enable remote debugging.

```sql
EXEC azure_extras.app_platform.deployments.enable_remote_debugging 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"port": {{ port }}
}'
;
```
</TabItem>
<TabItem value="disable_remote_debugging">

Disable remote debugging.

```sql
EXEC azure_extras.app_platform.deployments.disable_remote_debugging 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_heap_dump">

Generate Heap Dump.

```sql
EXEC azure_extras.app_platform.deployments.generate_heap_dump 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"appInstance": "{{ appInstance }}", 
"filePath": "{{ filePath }}", 
"duration": "{{ duration }}"
}'
;
```
</TabItem>
<TabItem value="generate_thread_dump">

Generate Thread Dump.

```sql
EXEC azure_extras.app_platform.deployments.generate_thread_dump 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"appInstance": "{{ appInstance }}", 
"filePath": "{{ filePath }}", 
"duration": "{{ duration }}"
}'
;
```
</TabItem>
<TabItem value="start_jfr">

Start JFR.

```sql
EXEC azure_extras.app_platform.deployments.start_jfr 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@deployment_name='{{ deployment_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"appInstance": "{{ appInstance }}", 
"filePath": "{{ filePath }}", 
"duration": "{{ duration }}"
}'
;
```
</TabItem>
</Tabs>
