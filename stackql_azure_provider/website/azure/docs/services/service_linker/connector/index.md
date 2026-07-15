--- 
title: connector
hide_title: false
hide_table_of_contents: false
keywords:
  - connector
  - service_linker
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

Creates, updates, deletes, gets or lists a <code>connector</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="connector" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_linker.connector" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_dryrun', value: 'get_dryrun' },
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="authInfo" /></td>
    <td><code>object</code></td>
    <td>The authentication type.</td>
</tr>
<tr>
    <td><CopyableCode code="clientType" /></td>
    <td><code>string</code></td>
    <td>The application client type. Known values are: "none", "dotnet", "java", "python", "go", "php", "ruby", "django", "nodejs", "springBoot", "kafka-springBoot", "jms-springBoot", and "dapr".</td>
</tr>
<tr>
    <td><CopyableCode code="configurationInfo" /></td>
    <td><code>object</code></td>
    <td>The connection information consumed by applications, including secrets, connection strings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkSolution" /></td>
    <td><code>object</code></td>
    <td>The network solution.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>connection scope in source service.</td>
</tr>
<tr>
    <td><CopyableCode code="secretStore" /></td>
    <td><code>object</code></td>
    <td>An option to store secret value in secure place.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetService" /></td>
    <td><code>object</code></td>
    <td>The target service properties.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vNetSolution" /></td>
    <td><code>object</code></td>
    <td>The VNet solution.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_dryrun">

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
    <td><CopyableCode code="operationPreviews" /></td>
    <td><code>array</code></td>
    <td>the preview of the operations for creation.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>object</code></td>
    <td>The parameters of the dryrun.</td>
</tr>
<tr>
    <td><CopyableCode code="prerequisiteResults" /></td>
    <td><code>array</code></td>
    <td>the result of the dryrun.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="authInfo" /></td>
    <td><code>object</code></td>
    <td>The authentication type.</td>
</tr>
<tr>
    <td><CopyableCode code="clientType" /></td>
    <td><code>string</code></td>
    <td>The application client type. Known values are: "none", "dotnet", "java", "python", "go", "php", "ruby", "django", "nodejs", "springBoot", "kafka-springBoot", "jms-springBoot", and "dapr".</td>
</tr>
<tr>
    <td><CopyableCode code="configurationInfo" /></td>
    <td><code>object</code></td>
    <td>The connection information consumed by applications, including secrets, connection strings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state.</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkSolution" /></td>
    <td><code>object</code></td>
    <td>The network solution.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>connection scope in source service.</td>
</tr>
<tr>
    <td><CopyableCode code="secretStore" /></td>
    <td><code>object</code></td>
    <td>An option to store secret value in secure place.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetService" /></td>
    <td><code>object</code></td>
    <td>The target service properties.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="vNetSolution" /></td>
    <td><code>object</code></td>
    <td>The VNet solution.</td>
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
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a></td>
    <td></td>
    <td>Returns Connector resource for a given name.</td>
</tr>
<tr>
    <td><a href="#get_dryrun"><CopyableCode code="get_dryrun" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-dryrun_name"><code>dryrun_name</code></a></td>
    <td></td>
    <td>get a dryrun job.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Returns list of connector which connects to the resource, which supports to config the target service during the resource provision.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a></td>
    <td></td>
    <td>Create or update Connector resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a></td>
    <td></td>
    <td>Operation to update an existing Connector.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a></td>
    <td></td>
    <td>Create or update Connector resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a></td>
    <td></td>
    <td>Delete a Connector.</td>
</tr>
<tr>
    <td><a href="#list_dryrun"><CopyableCode code="list_dryrun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>list dryrun jobs.</td>
</tr>
<tr>
    <td><a href="#create_dryrun"><CopyableCode code="create_dryrun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-dryrun_name"><code>dryrun_name</code></a></td>
    <td></td>
    <td>create a dryrun job to do necessary check before actual creation.</td>
</tr>
<tr>
    <td><a href="#update_dryrun"><CopyableCode code="update_dryrun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-dryrun_name"><code>dryrun_name</code></a></td>
    <td></td>
    <td>update a dryrun job to do necessary check before actual creation.</td>
</tr>
<tr>
    <td><a href="#delete_dryrun"><CopyableCode code="delete_dryrun" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-dryrun_name"><code>dryrun_name</code></a></td>
    <td></td>
    <td>delete a dryrun job.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a></td>
    <td></td>
    <td>Validate a Connector.</td>
</tr>
<tr>
    <td><a href="#generate_configurations"><CopyableCode code="generate_configurations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-connector_name"><code>connector_name</code></a></td>
    <td></td>
    <td>Generate configurations for a Connector.</td>
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
<tr id="parameter-connector_name">
    <td><CopyableCode code="connector_name" /></td>
    <td><code>string</code></td>
    <td>The name of resource. Required.</td>
</tr>
<tr id="parameter-dryrun_name">
    <td><CopyableCode code="dryrun_name" /></td>
    <td><code>string</code></td>
    <td>The name of dryrun. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of Azure region. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the target subscription. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'get_dryrun', value: 'get_dryrun' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Returns Connector resource for a given name.

```sql
SELECT
id,
name,
authInfo,
clientType,
configurationInfo,
provisioningState,
publicNetworkSolution,
scope,
secretStore,
systemData,
targetService,
type,
vNetSolution
FROM azure.service_linker.connector
WHERE subscription_id = '{{ subscription_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND location = '{{ location }}' -- required
AND connector_name = '{{ connector_name }}' -- required
;
```
</TabItem>
<TabItem value="get_dryrun">

get a dryrun job.

```sql
SELECT
id,
name,
operationPreviews,
parameters,
prerequisiteResults,
provisioningState,
systemData,
type
FROM azure.service_linker.connector
WHERE subscription_id = '{{ subscription_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND location = '{{ location }}' -- required
AND dryrun_name = '{{ dryrun_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns list of connector which connects to the resource, which supports to config the target service during the resource provision.

```sql
SELECT
id,
name,
authInfo,
clientType,
configurationInfo,
provisioningState,
publicNetworkSolution,
scope,
secretStore,
systemData,
targetService,
type,
vNetSolution
FROM azure.service_linker.connector
WHERE subscription_id = '{{ subscription_id }}' -- required
AND resource_group_name = '{{ resource_group_name }}' -- required
AND location = '{{ location }}' -- required
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

Create or update Connector resource.

```sql
INSERT INTO azure.service_linker.connector (
properties,
subscription_id,
resource_group_name,
location,
connector_name
)
SELECT 
'{{ properties }}',
'{{ subscription_id }}',
'{{ resource_group_name }}',
'{{ location }}',
'{{ connector_name }}'
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
- name: connector
  props:
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the connector resource.
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the connector resource.
    - name: location
      value: "{{ location }}"
      description: Required parameter for the connector resource.
    - name: connector_name
      value: "{{ connector_name }}"
      description: Required parameter for the connector resource.
    - name: properties
      value:
        targetService:
          type: "{{ type }}"
        authInfo:
          authType: "{{ authType }}"
          authMode: "{{ authMode }}"
        clientType: "{{ clientType }}"
        vNetSolution:
          type: "{{ type }}"
          deleteOrUpdateBehavior: "{{ deleteOrUpdateBehavior }}"
        secretStore:
          keyVaultId: "{{ keyVaultId }}"
          keyVaultSecretName: "{{ keyVaultSecretName }}"
        scope: "{{ scope }}"
        publicNetworkSolution:
          deleteOrUpdateBehavior: "{{ deleteOrUpdateBehavior }}"
          action: "{{ action }}"
          firewallRules:
            ipRanges:
              - "{{ ipRanges }}"
            azureServices: "{{ azureServices }}"
            callerClientIP: "{{ callerClientIP }}"
        configurationInfo:
          deleteOrUpdateBehavior: "{{ deleteOrUpdateBehavior }}"
          action: "{{ action }}"
          customizedKeys: "{{ customizedKeys }}"
          daprProperties:
            version: "{{ version }}"
            componentType: "{{ componentType }}"
            secretStoreComponent: "{{ secretStoreComponent }}"
            metadata:
              - name: "{{ name }}"
                value: "{{ value }}"
                secretRef: "{{ secretRef }}"
                description: "{{ description }}"
                required: "{{ required }}"
            scopes:
              - "{{ scopes }}"
            runtimeVersion: "{{ runtimeVersion }}"
            bindingComponentDirection: "{{ bindingComponentDirection }}"
          additionalConfigurations: "{{ additionalConfigurations }}"
          additionalConnectionStringProperties: "{{ additionalConnectionStringProperties }}"
          configurationStore:
            appConfigurationId: "{{ appConfigurationId }}"
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

Operation to update an existing Connector.

```sql
UPDATE azure.service_linker.connector
SET 
properties = '{{ properties }}'
WHERE 
subscription_id = '{{ subscription_id }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND location = '{{ location }}' --required
AND connector_name = '{{ connector_name }}' --required
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

Create or update Connector resource.

```sql
REPLACE azure.service_linker.connector
SET 
properties = '{{ properties }}'
WHERE 
subscription_id = '{{ subscription_id }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND location = '{{ location }}' --required
AND connector_name = '{{ connector_name }}' --required
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

Delete a Connector.

```sql
DELETE FROM azure.service_linker.connector
WHERE subscription_id = '{{ subscription_id }}' --required
AND resource_group_name = '{{ resource_group_name }}' --required
AND location = '{{ location }}' --required
AND connector_name = '{{ connector_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_dryrun"
    values={[
        { label: 'list_dryrun', value: 'list_dryrun' },
        { label: 'create_dryrun', value: 'create_dryrun' },
        { label: 'update_dryrun', value: 'update_dryrun' },
        { label: 'delete_dryrun', value: 'delete_dryrun' },
        { label: 'validate', value: 'validate' },
        { label: 'generate_configurations', value: 'generate_configurations' }
    ]}
>
<TabItem value="list_dryrun">

list dryrun jobs.

```sql
EXEC azure.service_linker.connector.list_dryrun 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required
;
```
</TabItem>
<TabItem value="create_dryrun">

create a dryrun job to do necessary check before actual creation.

```sql
EXEC azure.service_linker.connector.create_dryrun 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@dryrun_name='{{ dryrun_name }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="update_dryrun">

update a dryrun job to do necessary check before actual creation.

```sql
EXEC azure.service_linker.connector.update_dryrun 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@dryrun_name='{{ dryrun_name }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="delete_dryrun">

delete a dryrun job.

```sql
EXEC azure.service_linker.connector.delete_dryrun 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@dryrun_name='{{ dryrun_name }}' --required
;
```
</TabItem>
<TabItem value="validate">

Validate a Connector.

```sql
EXEC azure.service_linker.connector.validate 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@connector_name='{{ connector_name }}' --required
;
```
</TabItem>
<TabItem value="generate_configurations">

Generate configurations for a Connector.

```sql
EXEC azure.service_linker.connector.generate_configurations 
@subscription_id='{{ subscription_id }}' --required, 
@resource_group_name='{{ resource_group_name }}' --required, 
@location='{{ location }}' --required, 
@connector_name='{{ connector_name }}' --required 
@@json=
'{
"deleteOrUpdateBehavior": "{{ deleteOrUpdateBehavior }}", 
"action": "{{ action }}", 
"customizedKeys": "{{ customizedKeys }}", 
"daprProperties": "{{ daprProperties }}", 
"additionalConfigurations": "{{ additionalConfigurations }}", 
"additionalConnectionStringProperties": "{{ additionalConnectionStringProperties }}", 
"configurationStore": "{{ configurationStore }}"
}'
;
```
</TabItem>
</Tabs>
