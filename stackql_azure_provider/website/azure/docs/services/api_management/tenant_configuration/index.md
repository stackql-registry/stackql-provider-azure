--- 
title: tenant_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_configuration
  - api_management
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

Creates, updates, deletes, gets or lists a <code>tenant_configuration</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tenant_configuration" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tenant_configuration" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_sync_state"
    values={[
        { label: 'get_sync_state', value: 'get_sync_state' }
    ]}
>
<TabItem value="get_sync_state">

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
    <td><CopyableCode code="branch" /></td>
    <td><code>string</code></td>
    <td>The name of Git branch.</td>
</tr>
<tr>
    <td><CopyableCode code="commitId" /></td>
    <td><code>string</code></td>
    <td>The latest commit Id.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationChangeDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the latest configuration change. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.</td>
</tr>
<tr>
    <td><CopyableCode code="isExport" /></td>
    <td><code>boolean</code></td>
    <td>value indicating if last sync was save (true) or deploy (false) operation.</td>
</tr>
<tr>
    <td><CopyableCode code="isGitEnabled" /></td>
    <td><code>boolean</code></td>
    <td>value indicating whether Git configuration access is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="isSynced" /></td>
    <td><code>boolean</code></td>
    <td>value indicating if last synchronization was later than the configuration change.</td>
</tr>
<tr>
    <td><CopyableCode code="lastOperationId" /></td>
    <td><code>string</code></td>
    <td>Most recent tenant configuration operation identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="syncDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date of the latest synchronization. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.</td>
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
    <td><a href="#get_sync_state"><CopyableCode code="get_sync_state" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the status of the most recent synchronization between the configuration database and the Git repository.</td>
</tr>
<tr>
    <td><a href="#deploy"><CopyableCode code="deploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation applies changes from the specified Git branch to the configuration database. This is a long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#save"><CopyableCode code="save" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation creates a commit with the current configuration snapshot to the specified branch in the repository. This is a long running operation and could take several minutes to complete.</td>
</tr>
<tr>
    <td><a href="#validate"><CopyableCode code="validate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-configuration_name"><code>configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation validates the changes in the specified Git branch. This is a long running operation and could take several minutes to complete.</td>
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
<tr id="parameter-configuration_name">
    <td><CopyableCode code="configuration_name" /></td>
    <td><code>string</code></td>
    <td>API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number. "configuration" Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the API Management service. Required.</td>
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
    defaultValue="get_sync_state"
    values={[
        { label: 'get_sync_state', value: 'get_sync_state' }
    ]}
>
<TabItem value="get_sync_state">

Gets the status of the most recent synchronization between the configuration database and the Git repository.

```sql
SELECT
id,
name,
branch,
commitId,
configurationChangeDate,
isExport,
isGitEnabled,
isSynced,
lastOperationId,
syncDate,
systemData,
type
FROM azure.api_management.tenant_configuration
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND configuration_name = '{{ configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="deploy"
    values={[
        { label: 'deploy', value: 'deploy' },
        { label: 'save', value: 'save' },
        { label: 'validate', value: 'validate' }
    ]}
>
<TabItem value="deploy">

This operation applies changes from the specified Git branch to the configuration database. This is a long running operation and could take several minutes to complete.

```sql
EXEC azure.api_management.tenant_configuration.deploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@configuration_name='{{ configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="save">

This operation creates a commit with the current configuration snapshot to the specified branch in the repository. This is a long running operation and could take several minutes to complete.

```sql
EXEC azure.api_management.tenant_configuration.save 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@configuration_name='{{ configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
<TabItem value="validate">

This operation validates the changes in the specified Git branch. This is a long running operation and could take several minutes to complete.

```sql
EXEC azure.api_management.tenant_configuration.validate 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@configuration_name='{{ configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
