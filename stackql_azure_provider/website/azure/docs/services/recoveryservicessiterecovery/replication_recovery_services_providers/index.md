--- 
title: replication_recovery_services_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_recovery_services_providers
  - recoveryservicessiterecovery
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

Creates, updates, deletes, gets or lists a <code>replication_recovery_services_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="replication_recovery_services_providers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recoveryservicessiterecovery.replication_recovery_services_providers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_replication_fabrics', value: 'list_by_replication_fabrics' },
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
    <td><CopyableCode code="allowedScenarios" /></td>
    <td><code>array</code></td>
    <td>The scenarios allowed on this provider.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The authentication identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="biosId" /></td>
    <td><code>string</code></td>
    <td>The Bios Id.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>A value indicating whether DRA is responsive.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneAuthenticationIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The data plane authentication identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="draIdentifier" /></td>
    <td><code>string</code></td>
    <td>The DRA Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricType" /></td>
    <td><code>string</code></td>
    <td>Type of the site.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrorDetails" /></td>
    <td><code>array</code></td>
    <td>The recovery services provider health error details.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartBeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when last heartbeat was sent by the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="machineId" /></td>
    <td><code>string</code></td>
    <td>The machine Id.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The machine name.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemCount" /></td>
    <td><code>integer</code></td>
    <td>Number of protected VMs currently managed by the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersion" /></td>
    <td><code>string</code></td>
    <td>The provider version.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionDetails" /></td>
    <td><code>object</code></td>
    <td>The provider version details.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionExpiryDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date of the version.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionState" /></td>
    <td><code>string</code></td>
    <td>DRA version status.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAccessIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The resource access identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="serverVersion" /></td>
    <td><code>string</code></td>
    <td>The fabric provider.</td>
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
<TabItem value="list_by_replication_fabrics">

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
    <td><CopyableCode code="allowedScenarios" /></td>
    <td><code>array</code></td>
    <td>The scenarios allowed on this provider.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The authentication identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="biosId" /></td>
    <td><code>string</code></td>
    <td>The Bios Id.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>A value indicating whether DRA is responsive.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneAuthenticationIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The data plane authentication identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="draIdentifier" /></td>
    <td><code>string</code></td>
    <td>The DRA Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricType" /></td>
    <td><code>string</code></td>
    <td>Type of the site.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrorDetails" /></td>
    <td><code>array</code></td>
    <td>The recovery services provider health error details.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartBeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when last heartbeat was sent by the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="machineId" /></td>
    <td><code>string</code></td>
    <td>The machine Id.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The machine name.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemCount" /></td>
    <td><code>integer</code></td>
    <td>Number of protected VMs currently managed by the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersion" /></td>
    <td><code>string</code></td>
    <td>The provider version.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionDetails" /></td>
    <td><code>object</code></td>
    <td>The provider version details.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionExpiryDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date of the version.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionState" /></td>
    <td><code>string</code></td>
    <td>DRA version status.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAccessIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The resource access identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="serverVersion" /></td>
    <td><code>string</code></td>
    <td>The fabric provider.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedScenarios" /></td>
    <td><code>array</code></td>
    <td>The scenarios allowed on this provider.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The authentication identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="biosId" /></td>
    <td><code>string</code></td>
    <td>The Bios Id.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStatus" /></td>
    <td><code>string</code></td>
    <td>A value indicating whether DRA is responsive.</td>
</tr>
<tr>
    <td><CopyableCode code="dataPlaneAuthenticationIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The data plane authentication identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="draIdentifier" /></td>
    <td><code>string</code></td>
    <td>The DRA Id.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricFriendlyName" /></td>
    <td><code>string</code></td>
    <td>The fabric friendly name.</td>
</tr>
<tr>
    <td><CopyableCode code="fabricType" /></td>
    <td><code>string</code></td>
    <td>Type of the site.</td>
</tr>
<tr>
    <td><CopyableCode code="friendlyName" /></td>
    <td><code>string</code></td>
    <td>Friendly name of the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="healthErrorDetails" /></td>
    <td><code>array</code></td>
    <td>The recovery services provider health error details.</td>
</tr>
<tr>
    <td><CopyableCode code="lastHeartBeat" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when last heartbeat was sent by the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource Location.</td>
</tr>
<tr>
    <td><CopyableCode code="machineId" /></td>
    <td><code>string</code></td>
    <td>The machine Id.</td>
</tr>
<tr>
    <td><CopyableCode code="machineName" /></td>
    <td><code>string</code></td>
    <td>The machine name.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedItemCount" /></td>
    <td><code>integer</code></td>
    <td>Number of protected VMs currently managed by the DRA.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersion" /></td>
    <td><code>string</code></td>
    <td>The provider version.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionDetails" /></td>
    <td><code>object</code></td>
    <td>The provider version details.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionExpiryDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>Expiry date of the version.</td>
</tr>
<tr>
    <td><CopyableCode code="providerVersionState" /></td>
    <td><code>string</code></td>
    <td>DRA version status.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAccessIdentityDetails" /></td>
    <td><code>object</code></td>
    <td>The resource access identity details.</td>
</tr>
<tr>
    <td><CopyableCode code="serverVersion" /></td>
    <td><code>string</code></td>
    <td>The fabric provider.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the details of a recovery services provider. Gets the details of registered recovery services provider.</td>
</tr>
<tr>
    <td><a href="#list_by_replication_fabrics"><CopyableCode code="list_by_replication_fabrics" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of registered recovery services providers for the fabric. Lists the registered recovery services providers for the specified fabric.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of registered recovery services providers in the vault. This is a view only api. Lists the registered recovery services providers in the vault.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Adds a recovery services provider. The operation to add a recovery services provider.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes provider from fabric. Note: Deleting provider for any fabric other than SingleHost is unsupported. To maintain backward compatibility for released clients the object "deleteRspInput" is used (if the object is empty we assume that it is old client and continue the old behavior). The operation to removes/delete(unregister) a recovery services provider from the vault.</td>
</tr>
<tr>
    <td><a href="#purge"><CopyableCode code="purge" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Purges recovery service provider from fabric. The operation to purge(force delete) a recovery services provider from the vault.</td>
</tr>
<tr>
    <td><a href="#refresh_provider"><CopyableCode code="refresh_provider" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-fabric_name"><code>fabric_name</code></a>, <a href="#parameter-provider_name"><code>provider_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Refresh details from the recovery services provider. The operation to refresh the information from the recovery services provider.</td>
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
<tr id="parameter-fabric_name">
    <td><CopyableCode code="fabric_name" /></td>
    <td><code>string</code></td>
    <td>Fabric name. Required.</td>
</tr>
<tr id="parameter-provider_name">
    <td><CopyableCode code="provider_name" /></td>
    <td><code>string</code></td>
    <td>Recovery services provider name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Vault. Required.</td>
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
        { label: 'list_by_replication_fabrics', value: 'list_by_replication_fabrics' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets the details of a recovery services provider. Gets the details of registered recovery services provider.

```sql
SELECT
id,
name,
allowedScenarios,
authenticationIdentityDetails,
biosId,
connectionStatus,
dataPlaneAuthenticationIdentityDetails,
draIdentifier,
fabricFriendlyName,
fabricType,
friendlyName,
healthErrorDetails,
lastHeartBeat,
location,
machineId,
machineName,
protectedItemCount,
providerVersion,
providerVersionDetails,
providerVersionExpiryDate,
providerVersionState,
resourceAccessIdentityDetails,
serverVersion,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_recovery_services_providers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND provider_name = '{{ provider_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_replication_fabrics">

Gets the list of registered recovery services providers for the fabric. Lists the registered recovery services providers for the specified fabric.

```sql
SELECT
id,
name,
allowedScenarios,
authenticationIdentityDetails,
biosId,
connectionStatus,
dataPlaneAuthenticationIdentityDetails,
draIdentifier,
fabricFriendlyName,
fabricType,
friendlyName,
healthErrorDetails,
lastHeartBeat,
location,
machineId,
machineName,
protectedItemCount,
providerVersion,
providerVersionDetails,
providerVersionExpiryDate,
providerVersionState,
resourceAccessIdentityDetails,
serverVersion,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_recovery_services_providers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND fabric_name = '{{ fabric_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets the list of registered recovery services providers in the vault. This is a view only api. Lists the registered recovery services providers in the vault.

```sql
SELECT
id,
name,
allowedScenarios,
authenticationIdentityDetails,
biosId,
connectionStatus,
dataPlaneAuthenticationIdentityDetails,
draIdentifier,
fabricFriendlyName,
fabricType,
friendlyName,
healthErrorDetails,
lastHeartBeat,
location,
machineId,
machineName,
protectedItemCount,
providerVersion,
providerVersionDetails,
providerVersionExpiryDate,
providerVersionState,
resourceAccessIdentityDetails,
serverVersion,
systemData,
type
FROM azure.recoveryservicessiterecovery.replication_recovery_services_providers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
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

Adds a recovery services provider. The operation to add a recovery services provider.

```sql
INSERT INTO azure.recoveryservicessiterecovery.replication_recovery_services_providers (
properties,
resource_group_name,
resource_name,
fabric_name,
provider_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ fabric_name }}',
'{{ provider_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: replication_recovery_services_providers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the replication_recovery_services_providers resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the replication_recovery_services_providers resource.
    - name: fabric_name
      value: "{{ fabric_name }}"
      description: Required parameter for the replication_recovery_services_providers resource.
    - name: provider_name
      value: "{{ provider_name }}"
      description: Required parameter for the replication_recovery_services_providers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the replication_recovery_services_providers resource.
    - name: properties
      description: |
        The properties of an add provider request. Required.
      value:
        machineName: "{{ machineName }}"
        machineId: "{{ machineId }}"
        biosId: "{{ biosId }}"
        authenticationIdentityInput:
          tenantId: "{{ tenantId }}"
          applicationId: "{{ applicationId }}"
          objectId: "{{ objectId }}"
          audience: "{{ audience }}"
          aadAuthority: "{{ aadAuthority }}"
        resourceAccessIdentityInput:
          tenantId: "{{ tenantId }}"
          applicationId: "{{ applicationId }}"
          objectId: "{{ objectId }}"
          audience: "{{ audience }}"
          aadAuthority: "{{ aadAuthority }}"
        dataPlaneAuthenticationIdentityInput:
          tenantId: "{{ tenantId }}"
          applicationId: "{{ applicationId }}"
          objectId: "{{ objectId }}"
          audience: "{{ audience }}"
          aadAuthority: "{{ aadAuthority }}"
`}</CodeBlock>

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

Deletes provider from fabric. Note: Deleting provider for any fabric other than SingleHost is unsupported. To maintain backward compatibility for released clients the object "deleteRspInput" is used (if the object is empty we assume that it is old client and continue the old behavior). The operation to removes/delete(unregister) a recovery services provider from the vault.

```sql
DELETE FROM azure.recoveryservicessiterecovery.replication_recovery_services_providers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND fabric_name = '{{ fabric_name }}' --required
AND provider_name = '{{ provider_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="purge"
    values={[
        { label: 'purge', value: 'purge' },
        { label: 'refresh_provider', value: 'refresh_provider' }
    ]}
>
<TabItem value="purge">

Purges recovery service provider from fabric. The operation to purge(force delete) a recovery services provider from the vault.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_services_providers.purge 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@provider_name='{{ provider_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="refresh_provider">

Refresh details from the recovery services provider. The operation to refresh the information from the recovery services provider.

```sql
EXEC azure.recoveryservicessiterecovery.replication_recovery_services_providers.refresh_provider 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@fabric_name='{{ fabric_name }}' --required, 
@provider_name='{{ provider_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
