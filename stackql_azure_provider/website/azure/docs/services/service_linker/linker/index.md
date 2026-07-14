--- 
title: linker
hide_title: false
hide_table_of_contents: false
keywords:
  - linker
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

Creates, updates, deletes, gets or lists a <code>linker</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="linker" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_linker.linker" /></td></tr>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-linker_name"><code>linker_name</code></a></td>
    <td></td>
    <td>Returns Linker resource for a given name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Returns list of Linkers which connects to the resource. which supports to config both application and target service during the resource provision.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-linker_name"><code>linker_name</code></a></td>
    <td></td>
    <td>Create or update Linker resource.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-linker_name"><code>linker_name</code></a></td>
    <td></td>
    <td>Operation to update an existing Linker.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-linker_name"><code>linker_name</code></a></td>
    <td></td>
    <td>Create or update Linker resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-linker_name"><code>linker_name</code></a></td>
    <td></td>
    <td>Delete a Linker.</td>
</tr>
<tr>
    <td><a href="#list_configurations"><CopyableCode code="list_configurations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-linker_name"><code>linker_name</code></a></td>
    <td></td>
    <td>list source configurations for a Linker.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-linker_name"><code>linker_name</code></a></td>
    <td></td>
    <td>Validate a Linker.</td>
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
<tr id="parameter-linker_name">
    <td><CopyableCode code="linker_name" /></td>
    <td><code>string</code></td>
    <td>The name Linker resource. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource to be connected. Required.</td>
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

Returns Linker resource for a given name.

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
FROM azure.service_linker.linker
WHERE resource_uri = '{{ resource_uri }}' -- required
AND linker_name = '{{ linker_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Returns list of Linkers which connects to the resource. which supports to config both application and target service during the resource provision.

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
FROM azure.service_linker.linker
WHERE resource_uri = '{{ resource_uri }}' -- required
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

Create or update Linker resource.

```sql
INSERT INTO azure.service_linker.linker (
properties,
resource_uri,
linker_name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ linker_name }}'
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
- name: linker
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the linker resource.
    - name: linker_name
      value: "{{ linker_name }}"
      description: Required parameter for the linker resource.
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

Operation to update an existing Linker.

```sql
UPDATE azure.service_linker.linker
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND linker_name = '{{ linker_name }}' --required
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

Create or update Linker resource.

```sql
REPLACE azure.service_linker.linker
SET 
properties = '{{ properties }}'
WHERE 
resource_uri = '{{ resource_uri }}' --required
AND linker_name = '{{ linker_name }}' --required
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

Delete a Linker.

```sql
DELETE FROM azure.service_linker.linker
WHERE resource_uri = '{{ resource_uri }}' --required
AND linker_name = '{{ linker_name }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_configurations"
    values={[
        { label: 'list_configurations', value: 'list_configurations' },
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="list_configurations">

list source configurations for a Linker.

```sql
EXEC azure.service_linker.linker.list_configurations 
@resource_uri='{{ resource_uri }}' --required, 
@linker_name='{{ linker_name }}' --required
;
```
</TabItem>
<TabItem value="validate">

Validate a Linker.

```sql
EXEC azure.service_linker.linker.validate 
@resource_uri='{{ resource_uri }}' --required, 
@linker_name='{{ linker_name }}' --required
;
```
</TabItem>
</Tabs>
