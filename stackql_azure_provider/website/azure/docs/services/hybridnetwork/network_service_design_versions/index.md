--- 
title: network_service_design_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_service_design_versions
  - hybridnetwork
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

Creates, updates, deletes, gets or lists a <code>network_service_design_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_service_design_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybridnetwork.network_service_design_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_network_service_design_group', value: 'list_by_network_service_design_group' }
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
    <td><CopyableCode code="configurationGroupSchemaReferences" /></td>
    <td><code>object</code></td>
    <td>The configuration schemas to used to define the values.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The network service design version description.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nfvisFromSite" /></td>
    <td><code>object</code></td>
    <td>The nfvis from the site.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network service design version resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceElementTemplates" /></td>
    <td><code>array</code></td>
    <td>List of resource element template.</td>
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
    <td><CopyableCode code="versionState" /></td>
    <td><code>string</code></td>
    <td>The network service design version state. Known values are: "Unknown", "Preview", "Active", "Deprecated", "Validating", and "ValidationFailed".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_network_service_design_group">

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
    <td><CopyableCode code="configurationGroupSchemaReferences" /></td>
    <td><code>object</code></td>
    <td>The configuration schemas to used to define the values.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The network service design version description.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="nfvisFromSite" /></td>
    <td><code>object</code></td>
    <td>The nfvis from the site.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the network service design version resource. Known values are: "Unknown", "Succeeded", "Accepted", "Deleting", "Failed", "Canceled", "Deleted", and "Converging".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceElementTemplates" /></td>
    <td><code>array</code></td>
    <td>List of resource element template.</td>
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
    <td><CopyableCode code="versionState" /></td>
    <td><code>string</code></td>
    <td>The network service design version state. Known values are: "Unknown", "Preview", "Active", "Deprecated", "Validating", and "ValidationFailed".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-network_service_design_group_name"><code>network_service_design_group_name</code></a>, <a href="#parameter-network_service_design_version_name"><code>network_service_design_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a network service design version.</td>
</tr>
<tr>
    <td><a href="#list_by_network_service_design_group"><CopyableCode code="list_by_network_service_design_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-network_service_design_group_name"><code>network_service_design_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about a list of network service design versions under a network service design group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-network_service_design_group_name"><code>network_service_design_group_name</code></a>, <a href="#parameter-network_service_design_version_name"><code>network_service_design_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a network service design version.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-network_service_design_group_name"><code>network_service_design_group_name</code></a>, <a href="#parameter-network_service_design_version_name"><code>network_service_design_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a network service design version resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-network_service_design_group_name"><code>network_service_design_group_name</code></a>, <a href="#parameter-network_service_design_version_name"><code>network_service_design_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a network service design version.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-network_service_design_group_name"><code>network_service_design_group_name</code></a>, <a href="#parameter-network_service_design_version_name"><code>network_service_design_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified network service design version.</td>
</tr>
<tr>
    <td><a href="#update_state"><CopyableCode code="update_state" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-publisher_name"><code>publisher_name</code></a>, <a href="#parameter-network_service_design_group_name"><code>network_service_design_group_name</code></a>, <a href="#parameter-network_service_design_version_name"><code>network_service_design_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update network service design version state.</td>
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
<tr id="parameter-network_service_design_group_name">
    <td><CopyableCode code="network_service_design_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network service design group. Required.</td>
</tr>
<tr id="parameter-network_service_design_version_name">
    <td><CopyableCode code="network_service_design_version_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network service design version. The name should conform to the SemVer 2.0.0 specification: https://semver.org/spec/v2.0.0.html. Required.</td>
</tr>
<tr id="parameter-publisher_name">
    <td><CopyableCode code="publisher_name" /></td>
    <td><code>string</code></td>
    <td>The name of the publisher. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
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
        { label: 'list_by_network_service_design_group', value: 'list_by_network_service_design_group' }
    ]}
>
<TabItem value="get">

Gets information about a network service design version.

```sql
SELECT
id,
name,
configurationGroupSchemaReferences,
description,
location,
nfvisFromSite,
provisioningState,
resourceElementTemplates,
systemData,
tags,
type,
versionState
FROM azure.hybridnetwork.network_service_design_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND network_service_design_group_name = '{{ network_service_design_group_name }}' -- required
AND network_service_design_version_name = '{{ network_service_design_version_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_network_service_design_group">

Gets information about a list of network service design versions under a network service design group.

```sql
SELECT
id,
name,
configurationGroupSchemaReferences,
description,
location,
nfvisFromSite,
provisioningState,
resourceElementTemplates,
systemData,
tags,
type,
versionState
FROM azure.hybridnetwork.network_service_design_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND publisher_name = '{{ publisher_name }}' -- required
AND network_service_design_group_name = '{{ network_service_design_group_name }}' -- required
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

Creates or updates a network service design version.

```sql
INSERT INTO azure.hybridnetwork.network_service_design_versions (
tags,
location,
properties,
resource_group_name,
publisher_name,
network_service_design_group_name,
network_service_design_version_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ publisher_name }}',
'{{ network_service_design_group_name }}',
'{{ network_service_design_version_name }}',
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
- name: network_service_design_versions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_service_design_versions resource.
    - name: publisher_name
      value: "{{ publisher_name }}"
      description: Required parameter for the network_service_design_versions resource.
    - name: network_service_design_group_name
      value: "{{ network_service_design_group_name }}"
      description: Required parameter for the network_service_design_versions resource.
    - name: network_service_design_version_name
      value: "{{ network_service_design_version_name }}"
      description: Required parameter for the network_service_design_versions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_service_design_versions resource.
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
        network service design version properties.
      value:
        provisioningState: "{{ provisioningState }}"
        versionState: "{{ versionState }}"
        description: "{{ description }}"
        configurationGroupSchemaReferences: "{{ configurationGroupSchemaReferences }}"
        nfvisFromSite: "{{ nfvisFromSite }}"
        resourceElementTemplates:
          - name: "{{ name }}"
            type: "{{ type }}"
            dependsOnProfile:
              installDependsOn:
                - "{{ installDependsOn }}"
              uninstallDependsOn:
                - "{{ uninstallDependsOn }}"
              updateDependsOn:
                - "{{ updateDependsOn }}"
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

Updates a network service design version resource.

```sql
UPDATE azure.hybridnetwork.network_service_design_versions
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND network_service_design_group_name = '{{ network_service_design_group_name }}' --required
AND network_service_design_version_name = '{{ network_service_design_version_name }}' --required
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


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a network service design version.

```sql
REPLACE azure.hybridnetwork.network_service_design_versions
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND network_service_design_group_name = '{{ network_service_design_group_name }}' --required
AND network_service_design_version_name = '{{ network_service_design_version_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

Deletes the specified network service design version.

```sql
DELETE FROM azure.hybridnetwork.network_service_design_versions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND publisher_name = '{{ publisher_name }}' --required
AND network_service_design_group_name = '{{ network_service_design_group_name }}' --required
AND network_service_design_version_name = '{{ network_service_design_version_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="update_state"
    values={[
        { label: 'update_state', value: 'update_state' }
    ]}
>
<TabItem value="update_state">

Update network service design version state.

```sql
EXEC azure.hybridnetwork.network_service_design_versions.update_state 
@resource_group_name='{{ resource_group_name }}' --required, 
@publisher_name='{{ publisher_name }}' --required, 
@network_service_design_group_name='{{ network_service_design_group_name }}' --required, 
@network_service_design_version_name='{{ network_service_design_version_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"versionState": "{{ versionState }}"
}'
;
```
</TabItem>
</Tabs>
