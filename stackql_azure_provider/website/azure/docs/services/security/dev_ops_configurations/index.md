--- 
title: dev_ops_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_ops_configurations
  - security
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

Creates, updates, deletes, gets or lists a <code>dev_ops_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="dev_ops_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.dev_ops_configurations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="agentlessConfiguration" /></td>
    <td><code>object</code></td>
    <td>Details about Agentless configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="authorization" /></td>
    <td><code>object</code></td>
    <td>Authorization payload.</td>
</tr>
<tr>
    <td><CopyableCode code="autoDiscovery" /></td>
    <td><code>string</code></td>
    <td>AutoDiscovery states. Known values are: "Disabled", "Enabled", and "NotApplicable". (Disabled, Enabled, NotApplicable)</td>
</tr>
<tr>
    <td><CopyableCode code="capabilities" /></td>
    <td><code>array</code></td>
    <td>List of capabilities assigned to the DevOps configuration during the discovery process.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource. Pending - Provisioning pending. Failed - Provisioning failed. Succeeded - Successful provisioning. Canceled - Provisioning canceled. PendingDeletion - Deletion pending. DeletionSuccess - Deletion successful. DeletionFailure - Deletion failure. Known values are: "Succeeded", "Failed", "Canceled", "Pending", "PendingDeletion", "DeletionSuccess", and "DeletionFailure". (Succeeded, Failed, Canceled, Pending, PendingDeletion, DeletionSuccess, DeletionFailure)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatusMessage" /></td>
    <td><code>string</code></td>
    <td>Gets the resource status message.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningStatusUpdateTimeUtc" /></td>
    <td><code>string (date-time)</code></td>
    <td>Gets the time when resource was last checked.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="topLevelInventoryList" /></td>
    <td><code>array</code></td>
    <td>List of top-level inventory to select when AutoDiscovery is disabled. This field is ignored when AutoDiscovery is enabled.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a DevOps Configuration. Gets a DevOps Configuration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a DevOps Configuration. Creates or updates a DevOps Configuration.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a DevOps Configuration. Updates a DevOps Configuration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a DevOps Configuration. Creates or updates a DevOps Configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a DevOps Connector. Deletes a DevOps Connector.</td>
</tr>
<tr>
    <td><a href="#list_raw"><CopyableCode code="list_raw" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List DevOps Configurations. List DevOps Configurations.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-security_connector_name">
    <td><CopyableCode code="security_connector_name" /></td>
    <td><code>string</code></td>
    <td>The security connector name. Required.</td>
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
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets a DevOps Configuration. Gets a DevOps Configuration.

```sql
SELECT
id,
name,
agentlessConfiguration,
authorization,
autoDiscovery,
capabilities,
provisioningState,
provisioningStatusMessage,
provisioningStatusUpdateTimeUtc,
systemData,
topLevelInventoryList,
type
FROM azure.security.dev_ops_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND security_connector_name = '{{ security_connector_name }}' -- required
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

Creates or updates a DevOps Configuration. Creates or updates a DevOps Configuration.

```sql
INSERT INTO azure.security.dev_ops_configurations (
properties,
resource_group_name,
security_connector_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ security_connector_name }}',
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
- name: dev_ops_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the dev_ops_configurations resource.
    - name: security_connector_name
      value: "{{ security_connector_name }}"
      description: Required parameter for the dev_ops_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the dev_ops_configurations resource.
    - name: properties
      description: |
        DevOps Configuration properties.
      value:
        provisioningStatusMessage: "{{ provisioningStatusMessage }}"
        provisioningStatusUpdateTimeUtc: "{{ provisioningStatusUpdateTimeUtc }}"
        provisioningState: "{{ provisioningState }}"
        authorization:
          code: "{{ code }}"
        autoDiscovery: "{{ autoDiscovery }}"
        topLevelInventoryList:
          - "{{ topLevelInventoryList }}"
        capabilities:
          - name: "{{ name }}"
            value: "{{ value }}"
        agentlessConfiguration:
          agentlessEnabled: "{{ agentlessEnabled }}"
          agentlessAutoDiscovery: "{{ agentlessAutoDiscovery }}"
          scanners:
            - "{{ scanners }}"
          inventoryListType: "{{ inventoryListType }}"
          inventoryList:
            - inventoryKind: "{{ inventoryKind }}"
              value: "{{ value }}"
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

Updates a DevOps Configuration. Updates a DevOps Configuration.

```sql
UPDATE azure.security.dev_ops_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND security_connector_name = '{{ security_connector_name }}' --required
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

Creates or updates a DevOps Configuration. Creates or updates a DevOps Configuration.

```sql
REPLACE azure.security.dev_ops_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND security_connector_name = '{{ security_connector_name }}' --required
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

Deletes a DevOps Connector. Deletes a DevOps Connector.

```sql
DELETE FROM azure.security.dev_ops_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND security_connector_name = '{{ security_connector_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_raw"
    values={[
        { label: 'list_raw', value: 'list_raw' }
    ]}
>
<TabItem value="list_raw">

List DevOps Configurations. List DevOps Configurations.

```sql
EXEC azure.security.dev_ops_configurations.list_raw 
@resource_group_name='{{ resource_group_name }}' --required, 
@security_connector_name='{{ security_connector_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
