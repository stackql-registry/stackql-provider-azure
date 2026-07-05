--- 
title: service_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_configurations
  - hybridconnectivity
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

Creates, updates, deletes, gets or lists a <code>service_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridconnectivity.service_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_endpoint_resource', value: 'list_by_endpoint_resource' }
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
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port on which service is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Succeeded", "Creating", "Updating", "Failed", and "Canceled". (Succeeded, Creating, Updating, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the connectivity endpoint (optional).</td>
</tr>
<tr>
    <td><CopyableCode code="serviceName" /></td>
    <td><code>string</code></td>
    <td>Name of the service. Required. Known values are: "SSH" and "WAC". (SSH, WAC)</td>
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
<TabItem value="list_by_endpoint_resource">

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
    <td><CopyableCode code="port" /></td>
    <td><code>integer</code></td>
    <td>The port on which service is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Succeeded", "Creating", "Updating", "Failed", and "Canceled". (Succeeded, Creating, Updating, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceId" /></td>
    <td><code>string</code></td>
    <td>The resource Id of the connectivity endpoint (optional).</td>
</tr>
<tr>
    <td><CopyableCode code="serviceName" /></td>
    <td><code>string</code></td>
    <td>Name of the service. Required. Known values are: "SSH" and "WAC". (SSH, WAC)</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-service_configuration_name"><code>service_configuration_name</code></a></td>
    <td></td>
    <td>Gets the details about the service to the resource.</td>
</tr>
<tr>
    <td><a href="#list_by_endpoint_resource"><CopyableCode code="list_by_endpoint_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a></td>
    <td></td>
    <td>Lists of all the services associated with endpoint resource. API to enumerate registered services in service configurations under a Endpoint Resource.</td>
</tr>
<tr>
    <td><a href="#create_orupdate"><CopyableCode code="create_orupdate" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-service_configuration_name"><code>service_configuration_name</code></a></td>
    <td></td>
    <td>Create or update a service in serviceConfiguration for the endpoint resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-service_configuration_name"><code>service_configuration_name</code></a></td>
    <td></td>
    <td>Update the service details in the service configurations of the target resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-service_configuration_name"><code>service_configuration_name</code></a></td>
    <td></td>
    <td>Deletes the service details to the target resource.</td>
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
<tr id="parameter-endpoint_name">
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The endpoint name. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-service_configuration_name">
    <td><CopyableCode code="service_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The service name. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_endpoint_resource', value: 'list_by_endpoint_resource' }
    ]}
>
<TabItem value="get">

Gets the details about the service to the resource.

```sql
SELECT
id,
name,
port,
provisioningState,
resourceId,
serviceName,
systemData,
type
FROM azure.hybridconnectivity.service_configurations
WHERE resource_uri = '{{ resource_uri }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
AND service_configuration_name = '{{ service_configuration_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_endpoint_resource">

Lists of all the services associated with endpoint resource. API to enumerate registered services in service configurations under a Endpoint Resource.

```sql
SELECT
id,
name,
port,
provisioningState,
resourceId,
serviceName,
systemData,
type
FROM azure.hybridconnectivity.service_configurations
WHERE resource_uri = '{{ resource_uri }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_orupdate"
    values={[
        { label: 'create_orupdate', value: 'create_orupdate' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_orupdate">

Create or update a service in serviceConfiguration for the endpoint resource.

```sql
INSERT INTO azure.hybridconnectivity.service_configurations (
properties,
resource_uri,
endpoint_name,
service_configuration_name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ endpoint_name }}',
'{{ service_configuration_name }}'
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
- name: service_configurations
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the service_configurations resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the service_configurations resource.
    - name: service_configuration_name
      value: "{{ service_configuration_name }}"
      description: Required parameter for the service_configurations resource.
    - name: properties
      description: |
        The service configuration properties.
      value:
        serviceName: "{{ serviceName }}"
        resourceId: "{{ resourceId }}"
        port: {{ port }}
        provisioningState: "{{ provisioningState }}"
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

Update the service details in the service configurations of the target resource.

```sql
UPDATE azure.hybridconnectivity.service_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND service_configuration_name = '{{ service_configuration_name }}' --required
RETURNING
id,
name,
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

Deletes the service details to the target resource.

```sql
DELETE FROM azure.hybridconnectivity.service_configurations
WHERE resource_uri = '{{ resource_uri }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND service_configuration_name = '{{ service_configuration_name }}' --required
;
```
</TabItem>
</Tabs>
