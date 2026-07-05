--- 
title: sap_application_server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_application_server_instances
  - workloadssapvirtualinstance
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>sap_application_server_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sap_application_server_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.workloadssapvirtualinstance.sap_application_server_instances" /></td></tr>
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
    <td><CopyableCode code="dispatcherStatus" /></td>
    <td><code>string</code></td>
    <td>Application server instance dispatcher status.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the Application Instance errors.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayPort" /></td>
    <td><code>integer</code></td>
    <td>Application server instance gateway Port.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Defines the health of SAP Instances. Known values are: "Unknown", "Healthy", "Unhealthy", and "Degraded". (Unknown, Healthy, Unhealthy, Degraded)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>Application server instance SAP hostname.</td>
</tr>
<tr>
    <td><CopyableCode code="icmHttpPort" /></td>
    <td><code>integer</code></td>
    <td>Application server instance ICM HTTP Port.</td>
</tr>
<tr>
    <td><CopyableCode code="icmHttpsPort" /></td>
    <td><code>integer</code></td>
    <td>Application server instance ICM HTTPS Port.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceNo" /></td>
    <td><code>string</code></td>
    <td>Application server Instance Number.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>Application server instance SAP IP Address.</td>
</tr>
<tr>
    <td><CopyableCode code="kernelPatch" /></td>
    <td><code>string</code></td>
    <td>Application server instance SAP Kernel Patch level.</td>
</tr>
<tr>
    <td><CopyableCode code="kernelVersion" /></td>
    <td><code>string</code></td>
    <td>Application server instance SAP Kernel Version.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerDetails" /></td>
    <td><code>object</code></td>
    <td>The Load Balancer details such as LoadBalancer ID attached to Application Server Virtual Machines.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", "Failed", "Deleting", and "Canceled". (Succeeded, Updating, Creating, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Defines the SAP Instance status. Known values are: "Starting", "Running", "Stopping", "Offline", "PartiallyRunning", "Unavailable", and "SoftShutdown". (Starting, Running, Stopping, Offline, PartiallyRunning, Unavailable, SoftShutdown)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>string</code></td>
    <td>Application server Subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmDetails" /></td>
    <td><code>array</code></td>
    <td>The list of virtual machines.</td>
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
    <td><CopyableCode code="dispatcherStatus" /></td>
    <td><code>string</code></td>
    <td>Application server instance dispatcher status.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the Application Instance errors.</td>
</tr>
<tr>
    <td><CopyableCode code="gatewayPort" /></td>
    <td><code>integer</code></td>
    <td>Application server instance gateway Port.</td>
</tr>
<tr>
    <td><CopyableCode code="health" /></td>
    <td><code>string</code></td>
    <td>Defines the health of SAP Instances. Known values are: "Unknown", "Healthy", "Unhealthy", and "Degraded". (Unknown, Healthy, Unhealthy, Degraded)</td>
</tr>
<tr>
    <td><CopyableCode code="hostname" /></td>
    <td><code>string</code></td>
    <td>Application server instance SAP hostname.</td>
</tr>
<tr>
    <td><CopyableCode code="icmHttpPort" /></td>
    <td><code>integer</code></td>
    <td>Application server instance ICM HTTP Port.</td>
</tr>
<tr>
    <td><CopyableCode code="icmHttpsPort" /></td>
    <td><code>integer</code></td>
    <td>Application server instance ICM HTTPS Port.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceNo" /></td>
    <td><code>string</code></td>
    <td>Application server Instance Number.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>Application server instance SAP IP Address.</td>
</tr>
<tr>
    <td><CopyableCode code="kernelPatch" /></td>
    <td><code>string</code></td>
    <td>Application server instance SAP Kernel Patch level.</td>
</tr>
<tr>
    <td><CopyableCode code="kernelVersion" /></td>
    <td><code>string</code></td>
    <td>Application server instance SAP Kernel Version.</td>
</tr>
<tr>
    <td><CopyableCode code="loadBalancerDetails" /></td>
    <td><code>object</code></td>
    <td>The Load Balancer details such as LoadBalancer ID attached to Application Server Virtual Machines.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Creating", "Failed", "Deleting", and "Canceled". (Succeeded, Updating, Creating, Failed, Deleting, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Defines the SAP Instance status. Known values are: "Starting", "Running", "Stopping", "Offline", "PartiallyRunning", "Unavailable", and "SoftShutdown". (Starting, Running, Stopping, Offline, PartiallyRunning, Unavailable, SoftShutdown)</td>
</tr>
<tr>
    <td><CopyableCode code="subnet" /></td>
    <td><code>string</code></td>
    <td>Application server Subnet.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vmDetails" /></td>
    <td><code>array</code></td>
    <td>The list of virtual machines.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-application_instance_name"><code>application_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the SAP Application Server Instance corresponding to the Virtual Instance for SAP solutions resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the SAP Application Server Instance resources for a given Virtual Instance for SAP solutions resource.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-application_instance_name"><code>application_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Puts the SAP Application Server Instance resource. `<br />``<br />`This will be used by service only. PUT by end user will return a Bad Request error.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-application_instance_name"><code>application_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Puts the SAP Application Server Instance resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-application_instance_name"><code>application_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the SAP Application Server Instance resource. `<br />``<br />`This operation will be used by service only. Delete by end user will return a Bad Request error.</td>
</tr>
<tr>
    <td><a href="#start"><CopyableCode code="start" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-application_instance_name"><code>application_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts the SAP Application Server Instance.</td>
</tr>
<tr>
    <td><a href="#stop"><CopyableCode code="stop" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_virtual_instance_name"><code>sap_virtual_instance_name</code></a>, <a href="#parameter-application_instance_name"><code>application_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Stops the SAP Application Server Instance.</td>
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
<tr id="parameter-application_instance_name">
    <td><CopyableCode code="application_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of SAP Application Server instance resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sap_virtual_instance_name">
    <td><CopyableCode code="sap_virtual_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Virtual Instances for SAP solutions resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
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

Gets the SAP Application Server Instance corresponding to the Virtual Instance for SAP solutions resource.

```sql
SELECT
id,
name,
dispatcherStatus,
errors,
gatewayPort,
health,
hostname,
icmHttpPort,
icmHttpsPort,
instanceNo,
ipAddress,
kernelPatch,
kernelVersion,
loadBalancerDetails,
location,
provisioningState,
status,
subnet,
systemData,
tags,
type,
vmDetails
FROM azure_isv.workloadssapvirtualinstance.sap_application_server_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_virtual_instance_name = '{{ sap_virtual_instance_name }}' -- required
AND application_instance_name = '{{ application_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the SAP Application Server Instance resources for a given Virtual Instance for SAP solutions resource.

```sql
SELECT
id,
name,
dispatcherStatus,
errors,
gatewayPort,
health,
hostname,
icmHttpPort,
icmHttpsPort,
instanceNo,
ipAddress,
kernelPatch,
kernelVersion,
loadBalancerDetails,
location,
provisioningState,
status,
subnet,
systemData,
tags,
type,
vmDetails
FROM azure_isv.workloadssapvirtualinstance.sap_application_server_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_virtual_instance_name = '{{ sap_virtual_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Puts the SAP Application Server Instance resource. `<br />``<br />`This will be used by service only. PUT by end user will return a Bad Request error.

```sql
INSERT INTO azure_isv.workloadssapvirtualinstance.sap_application_server_instances (
tags,
location,
properties,
resource_group_name,
sap_virtual_instance_name,
application_instance_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sap_virtual_instance_name }}',
'{{ application_instance_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: sap_application_server_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sap_application_server_instances resource.
    - name: sap_virtual_instance_name
      value: "{{ sap_virtual_instance_name }}"
      description: Required parameter for the sap_application_server_instances resource.
    - name: application_instance_name
      value: "{{ application_instance_name }}"
      description: Required parameter for the sap_application_server_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sap_application_server_instances resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        instanceNo: "{{ instanceNo }}"
        subnet: "{{ subnet }}"
        hostname: "{{ hostname }}"
        kernelVersion: "{{ kernelVersion }}"
        kernelPatch: "{{ kernelPatch }}"
        ipAddress: "{{ ipAddress }}"
        gatewayPort: {{ gatewayPort }}
        icmHttpPort: {{ icmHttpPort }}
        icmHttpsPort: {{ icmHttpsPort }}
        dispatcherStatus: "{{ dispatcherStatus }}"
        loadBalancerDetails:
          id: "{{ id }}"
        vmDetails:
          - type: "{{ type }}"
            virtualMachineId: "{{ virtualMachineId }}"
            storageDetails: "{{ storageDetails }}"
        status: "{{ status }}"
        health: "{{ health }}"
        provisioningState: "{{ provisioningState }}"
        errors:
          properties:
            code: "{{ code }}"
            message: "{{ message }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                details: "{{ details }}"
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

Puts the SAP Application Server Instance resource.

```sql
UPDATE azure_isv.workloadssapvirtualinstance.sap_application_server_instances
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sap_virtual_instance_name = '{{ sap_virtual_instance_name }}' --required
AND application_instance_name = '{{ application_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
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

Deletes the SAP Application Server Instance resource. `<br />``<br />`This operation will be used by service only. Delete by end user will return a Bad Request error.

```sql
DELETE FROM azure_isv.workloadssapvirtualinstance.sap_application_server_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sap_virtual_instance_name = '{{ sap_virtual_instance_name }}' --required
AND application_instance_name = '{{ application_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start"
    values={[
        { label: 'start', value: 'start' },
        { label: 'stop', value: 'stop' }
    ]}
>
<TabItem value="start">

Starts the SAP Application Server Instance.

```sql
EXEC azure_isv.workloadssapvirtualinstance.sap_application_server_instances.start 
@resource_group_name='{{ resource_group_name }}' --required, 
@sap_virtual_instance_name='{{ sap_virtual_instance_name }}' --required, 
@application_instance_name='{{ application_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"startVm": {{ startVm }}
}'
;
```
</TabItem>
<TabItem value="stop">

Stops the SAP Application Server Instance.

```sql
EXEC azure_isv.workloadssapvirtualinstance.sap_application_server_instances.stop 
@resource_group_name='{{ resource_group_name }}' --required, 
@sap_virtual_instance_name='{{ sap_virtual_instance_name }}' --required, 
@application_instance_name='{{ application_instance_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"softStopTimeoutSeconds": {{ softStopTimeoutSeconds }}, 
"deallocateVm": {{ deallocateVm }}
}'
;
```
</TabItem>
</Tabs>
