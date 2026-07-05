--- 
title: serverless_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_runtimes
  - informaticadatamanagement
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

Creates, updates, deletes, gets or lists a <code>serverless_runtimes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="serverless_runtimes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.informaticadatamanagement.serverless_runtimes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_informatica_organization_resource', value: 'list_by_informatica_organization_resource' }
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="advancedCustomProperties" /></td>
    <td><code>array</code></td>
    <td>String KV pairs indicating Advanced custom properties.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>Application type of the Serverless Runtime environment. Known values are: "CDI" and "CDIE".</td>
</tr>
<tr>
    <td><CopyableCode code="computeUnits" /></td>
    <td><code>string</code></td>
    <td>Compute units of the serverless runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>description of the serverless runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="executionTimeout" /></td>
    <td><code>string</code></td>
    <td>Serverless Execution timeout.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>string</code></td>
    <td>Platform type of the Serverless Runtime. "AZURE"</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessAccountLocation" /></td>
    <td><code>string</code></td>
    <td>Serverless account creation location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessRuntimeConfig" /></td>
    <td><code>object</code></td>
    <td>Serverless config properties.</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessRuntimeNetworkProfile" /></td>
    <td><code>object</code></td>
    <td>Informatica Serverless Network profile properties.</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessRuntimeTags" /></td>
    <td><code>array</code></td>
    <td>Serverless Runtime Tags.</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessRuntimeUserContextProperties" /></td>
    <td><code>object</code></td>
    <td>Serverless runtime user context properties.</td>
</tr>
<tr>
    <td><CopyableCode code="supplementaryFileLocation" /></td>
    <td><code>string</code></td>
    <td>Supplementary file location.</td>
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
<TabItem value="list_by_informatica_organization_resource">

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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="advancedCustomProperties" /></td>
    <td><code>array</code></td>
    <td>String KV pairs indicating Advanced custom properties.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>Application type of the Serverless Runtime environment. Known values are: "CDI" and "CDIE".</td>
</tr>
<tr>
    <td><CopyableCode code="computeUnits" /></td>
    <td><code>string</code></td>
    <td>Compute units of the serverless runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>description of the serverless runtime.</td>
</tr>
<tr>
    <td><CopyableCode code="executionTimeout" /></td>
    <td><code>string</code></td>
    <td>Serverless Execution timeout.</td>
</tr>
<tr>
    <td><CopyableCode code="platform" /></td>
    <td><code>string</code></td>
    <td>Platform type of the Serverless Runtime. "AZURE"</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessAccountLocation" /></td>
    <td><code>string</code></td>
    <td>Serverless account creation location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessRuntimeConfig" /></td>
    <td><code>object</code></td>
    <td>Serverless config properties.</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessRuntimeNetworkProfile" /></td>
    <td><code>object</code></td>
    <td>Informatica Serverless Network profile properties.</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessRuntimeTags" /></td>
    <td><code>array</code></td>
    <td>Serverless Runtime Tags.</td>
</tr>
<tr>
    <td><CopyableCode code="serverlessRuntimeUserContextProperties" /></td>
    <td><code>object</code></td>
    <td>Serverless runtime user context properties.</td>
</tr>
<tr>
    <td><CopyableCode code="supplementaryFileLocation" /></td>
    <td><code>string</code></td>
    <td>Supplementary file location.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-serverless_runtime_name"><code>serverless_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a InformaticaServerlessRuntimeResource.</td>
</tr>
<tr>
    <td><a href="#list_by_informatica_organization_resource"><CopyableCode code="list_by_informatica_organization_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List InformaticaServerlessRuntimeResource resources by InformaticaOrganizationResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-serverless_runtime_name"><code>serverless_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a InformaticaServerlessRuntimeResource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-serverless_runtime_name"><code>serverless_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a InformaticaServerlessRuntimeResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-serverless_runtime_name"><code>serverless_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a InformaticaServerlessRuntimeResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-serverless_runtime_name"><code>serverless_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a InformaticaServerlessRuntimeResource.</td>
</tr>
<tr>
    <td><a href="#check_dependencies"><CopyableCode code="check_dependencies" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-serverless_runtime_name"><code>serverless_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks all dependencies for a serverless runtime resource.</td>
</tr>
<tr>
    <td><a href="#serverless_resource_by_id"><CopyableCode code="serverless_resource_by_id" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-serverless_runtime_name"><code>serverless_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a serverless runtime resource by ID.</td>
</tr>
<tr>
    <td><a href="#start_failed_serverless_runtime"><CopyableCode code="start_failed_serverless_runtime" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-organization_name"><code>organization_name</code></a>, <a href="#parameter-serverless_runtime_name"><code>serverless_runtime_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts a failed runtime resource.</td>
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
<tr id="parameter-organization_name">
    <td><CopyableCode code="organization_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Organizations resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-serverless_runtime_name">
    <td><CopyableCode code="serverless_runtime_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Serverless Runtime resource. Required.</td>
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
        { label: 'list_by_informatica_organization_resource', value: 'list_by_informatica_organization_resource' }
    ]}
>
<TabItem value="get">

Get a InformaticaServerlessRuntimeResource.

```sql
SELECT
id,
name,
advancedCustomProperties,
applicationType,
computeUnits,
description,
executionTimeout,
platform,
provisioningState,
serverlessAccountLocation,
serverlessRuntimeConfig,
serverlessRuntimeNetworkProfile,
serverlessRuntimeTags,
serverlessRuntimeUserContextProperties,
supplementaryFileLocation,
systemData,
type
FROM azure_isv.informaticadatamanagement.serverless_runtimes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND organization_name = '{{ organization_name }}' -- required
AND serverless_runtime_name = '{{ serverless_runtime_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_informatica_organization_resource">

List InformaticaServerlessRuntimeResource resources by InformaticaOrganizationResource.

```sql
SELECT
id,
name,
advancedCustomProperties,
applicationType,
computeUnits,
description,
executionTimeout,
platform,
provisioningState,
serverlessAccountLocation,
serverlessRuntimeConfig,
serverlessRuntimeNetworkProfile,
serverlessRuntimeTags,
serverlessRuntimeUserContextProperties,
supplementaryFileLocation,
systemData,
type
FROM azure_isv.informaticadatamanagement.serverless_runtimes
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND organization_name = '{{ organization_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a InformaticaServerlessRuntimeResource.

```sql
INSERT INTO azure_isv.informaticadatamanagement.serverless_runtimes (
properties,
resource_group_name,
organization_name,
serverless_runtime_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ organization_name }}',
'{{ serverless_runtime_name }}',
'{{ subscription_id }}'
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
- name: serverless_runtimes
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the serverless_runtimes resource.
    - name: organization_name
      value: "{{ organization_name }}"
      description: Required parameter for the serverless_runtimes resource.
    - name: serverless_runtime_name
      value: "{{ serverless_runtime_name }}"
      description: Required parameter for the serverless_runtimes resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the serverless_runtimes resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        description: "{{ description }}"
        platform: "{{ platform }}"
        applicationType: "{{ applicationType }}"
        computeUnits: "{{ computeUnits }}"
        executionTimeout: "{{ executionTimeout }}"
        serverlessAccountLocation: "{{ serverlessAccountLocation }}"
        serverlessRuntimeNetworkProfile:
          networkInterfaceConfiguration:
            vnetId: "{{ vnetId }}"
            subnetId: "{{ subnetId }}"
            vnetResourceGuid: "{{ vnetResourceGuid }}"
        advancedCustomProperties:
          - key: "{{ key }}"
            value: "{{ value }}"
        supplementaryFileLocation: "{{ supplementaryFileLocation }}"
        serverlessRuntimeConfig:
          cdiConfigProps:
            - engineName: "{{ engineName }}"
              engineVersion: "{{ engineVersion }}"
              applicationConfigs: "{{ applicationConfigs }}"
          cdieConfigProps:
            - engineName: "{{ engineName }}"
              engineVersion: "{{ engineVersion }}"
              applicationConfigs: "{{ applicationConfigs }}"
        serverlessRuntimeTags:
          - name: "{{ name }}"
            value: "{{ value }}"
        serverlessRuntimeUserContextProperties:
          userContextToken: "{{ userContextToken }}"
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

Update a InformaticaServerlessRuntimeResource.

```sql
UPDATE azure_isv.informaticadatamanagement.serverless_runtimes
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND serverless_runtime_name = '{{ serverless_runtime_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
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

Create a InformaticaServerlessRuntimeResource.

```sql
REPLACE azure_isv.informaticadatamanagement.serverless_runtimes
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND serverless_runtime_name = '{{ serverless_runtime_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
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

Delete a InformaticaServerlessRuntimeResource.

```sql
DELETE FROM azure_isv.informaticadatamanagement.serverless_runtimes
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND organization_name = '{{ organization_name }}' --required
AND serverless_runtime_name = '{{ serverless_runtime_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_dependencies"
    values={[
        { label: 'check_dependencies', value: 'check_dependencies' },
        { label: 'serverless_resource_by_id', value: 'serverless_resource_by_id' },
        { label: 'start_failed_serverless_runtime', value: 'start_failed_serverless_runtime' }
    ]}
>
<TabItem value="check_dependencies">

Checks all dependencies for a serverless runtime resource.

```sql
EXEC azure_isv.informaticadatamanagement.serverless_runtimes.check_dependencies 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@serverless_runtime_name='{{ serverless_runtime_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="serverless_resource_by_id">

Returns a serverless runtime resource by ID.

```sql
EXEC azure_isv.informaticadatamanagement.serverless_runtimes.serverless_resource_by_id 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@serverless_runtime_name='{{ serverless_runtime_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="start_failed_serverless_runtime">

Starts a failed runtime resource.

```sql
EXEC azure_isv.informaticadatamanagement.serverless_runtimes.start_failed_serverless_runtime 
@resource_group_name='{{ resource_group_name }}' --required, 
@organization_name='{{ organization_name }}' --required, 
@serverless_runtime_name='{{ serverless_runtime_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
