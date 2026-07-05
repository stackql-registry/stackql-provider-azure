--- 
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - cdn
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing additional properties for profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="frontDoorId" /></td>
    <td><code>string</code></td>
    <td>The Id of the frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the profile. Used by portal to differentiate traditional CDN profile and new AFD profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logScrubbing" /></td>
    <td><code>object</code></td>
    <td>Defines rules that scrub sensitive fields in the Azure Front Door profile logs.</td>
</tr>
<tr>
    <td><CopyableCode code="originResponseTimeoutSeconds" /></td>
    <td><code>integer</code></td>
    <td>Send and receive timeout on forwarding request to the origin. When timeout is reached, the request fails and returns.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the profile. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the profile. Known values are: "Creating", "Active", "Deleting", "Disabled", "Migrating", "Migrated", "PendingMigrationCommit", "CommittingMigration", and "AbortingMigration". (Creating, Active, Deleting, Disabled, Migrating, Migrated, PendingMigrationCommit, CommittingMigration, AbortingMigration)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The pricing tier (defines Azure Front Door Standard or Premium or a CDN provider, feature list and rate) of the profile. Required.</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing additional properties for profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="frontDoorId" /></td>
    <td><code>string</code></td>
    <td>The Id of the frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the profile. Used by portal to differentiate traditional CDN profile and new AFD profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logScrubbing" /></td>
    <td><code>object</code></td>
    <td>Defines rules that scrub sensitive fields in the Azure Front Door profile logs.</td>
</tr>
<tr>
    <td><CopyableCode code="originResponseTimeoutSeconds" /></td>
    <td><code>integer</code></td>
    <td>Send and receive timeout on forwarding request to the origin. When timeout is reached, the request fails and returns.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the profile. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the profile. Known values are: "Creating", "Active", "Deleting", "Disabled", "Migrating", "Migrated", "PendingMigrationCommit", "CommittingMigration", and "AbortingMigration". (Creating, Active, Deleting, Disabled, Migrating, Migrated, PendingMigrationCommit, CommittingMigration, AbortingMigration)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The pricing tier (defines Azure Front Door Standard or Premium or a CDN provider, feature list and rate) of the profile. Required.</td>
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
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing additional properties for profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="frontDoorId" /></td>
    <td><code>string</code></td>
    <td>The Id of the frontdoor.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of the profile. Used by portal to differentiate traditional CDN profile and new AFD profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logScrubbing" /></td>
    <td><code>object</code></td>
    <td>Defines rules that scrub sensitive fields in the Azure Front Door profile logs.</td>
</tr>
<tr>
    <td><CopyableCode code="originResponseTimeoutSeconds" /></td>
    <td><code>integer</code></td>
    <td>Send and receive timeout on forwarding request to the origin. When timeout is reached, the request fails and returns.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the profile. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the profile. Known values are: "Creating", "Active", "Deleting", "Disabled", "Migrating", "Migrated", "PendingMigrationCommit", "CommittingMigration", and "AbortingMigration". (Creating, Active, Deleting, Disabled, Migrating, Migrated, PendingMigrationCommit, CommittingMigration, AbortingMigration)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The pricing tier (defines Azure Front Door Standard or Premium or a CDN provider, feature list and rate) of the profile. Required.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within an Azure subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Creates a new Azure Front Door Standard or Azure Front Door Premium or CDN profile with a profile name under the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified parameters. Deleting a profile will result in the deletion of all of the sub-resources including endpoints, origins and custom domains.</td>
</tr>
<tr>
    <td><a href="#list_supported_optimization_types"><CopyableCode code="list_supported_optimization_types" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the supported optimization types for the current profile. A user can create an endpoint with an optimization type from the listed values.</td>
</tr>
<tr>
    <td><a href="#list_resource_usage"><CopyableCode code="list_resource_usage" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the quota and actual usage of endpoints under the given Azure Front Door Standard or Azure Front Door Premium or CDN profile.</td>
</tr>
<tr>
    <td><a href="#migration_commit"><CopyableCode code="migration_commit" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Commit the migrated Azure Frontdoor(Standard/Premium) profile.</td>
</tr>
<tr>
    <td><a href="#generate_sso_uri"><CopyableCode code="generate_sso_uri" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generates a dynamic SSO URI used to sign in to the CDN supplemental portal. Supplemental portal is used to configure advanced feature capabilities that are not yet available in the Azure portal, such as core reports in a standard profile; rules engine, advanced HTTP reports, and real-time stats and alerts in a premium profile. The SSO URI changes approximately every 10 minutes.</td>
</tr>
<tr>
    <td><a href="#cdn_can_migrate_to_afd"><CopyableCode code="cdn_can_migrate_to_afd" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks if CDN profile can be migrated to Azure Frontdoor(Standard/Premium) profile.</td>
</tr>
<tr>
    <td><a href="#cdn_migrate_to_afd"><CopyableCode code="cdn_migrate_to_afd" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Migrate the CDN profile to Azure Frontdoor(Standard/Premium) profile. This step prepares the profile for migration and will be followed by Commit to finalize the migration.</td>
</tr>
<tr>
    <td><a href="#migration_abort"><CopyableCode code="migration_abort" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Abort the migration to Azure Frontdoor Premium/Standard.</td>
</tr>
<tr>
    <td><a href="#can_migrate"><CopyableCode code="can_migrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-classicResourceReference"><code>classicResourceReference</code></a></td>
    <td></td>
    <td>Checks if CDN profile can be migrated to Azure Frontdoor(Standard/Premium) profile.</td>
</tr>
<tr>
    <td><a href="#migrate"><CopyableCode code="migrate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-sku"><code>sku</code></a>, <a href="#parameter-classicResourceReference"><code>classicResourceReference</code></a>, <a href="#parameter-profileName"><code>profileName</code></a></td>
    <td></td>
    <td>Migrate the CDN profile to Azure Frontdoor(Standard/Premium) profile. The change need to be committed after this.</td>
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
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets an Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group.

```sql
SELECT
id,
name,
extendedProperties,
frontDoorId,
identity,
kind,
location,
logScrubbing,
originResponseTimeoutSeconds,
provisioningState,
resourceState,
sku,
systemData,
tags,
type
FROM azure.cdn.profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within a resource group.

```sql
SELECT
id,
name,
extendedProperties,
frontDoorId,
identity,
kind,
location,
logScrubbing,
originResponseTimeoutSeconds,
provisioningState,
resourceState,
sku,
systemData,
tags,
type
FROM azure.cdn.profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all of the Azure Front Door Standard, Azure Front Door Premium, and CDN profiles within an Azure subscription.

```sql
SELECT
id,
name,
extendedProperties,
frontDoorId,
identity,
kind,
location,
logScrubbing,
originResponseTimeoutSeconds,
provisioningState,
resourceState,
sku,
systemData,
tags,
type
FROM azure.cdn.profiles
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Creates a new Azure Front Door Standard or Azure Front Door Premium or CDN profile with a profile name under the specified subscription and resource group.

```sql
INSERT INTO azure.cdn.profiles (
tags,
location,
properties,
sku,
identity,
resource_group_name,
profile_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ sku }}' /* required */,
'{{ identity }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
kind,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: profiles
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the profiles resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the profiles resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the profiles resource.
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
        The JSON object that contains the properties required to create a profile.
      value:
        resourceState: "{{ resourceState }}"
        provisioningState: "{{ provisioningState }}"
        extendedProperties: "{{ extendedProperties }}"
        frontDoorId: "{{ frontDoorId }}"
        originResponseTimeoutSeconds: {{ originResponseTimeoutSeconds }}
        logScrubbing:
          state: "{{ state }}"
          scrubbingRules:
            - matchVariable: "{{ matchVariable }}"
              selectorMatchOperator: "{{ selectorMatchOperator }}"
              selector: "{{ selector }}"
              state: "{{ state }}"
    - name: sku
      description: |
        The pricing tier (defines Azure Front Door Standard or Premium or a CDN provider, feature list and rate) of the profile. Required.
      value:
        name: "{{ name }}"
    - name: identity
      description: |
        The managed service identities assigned to this resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Updates an existing Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group.

```sql
UPDATE azure.cdn.profiles
SET 
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
kind,
location,
properties,
sku,
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

Deletes an existing Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified parameters. Deleting a profile will result in the deletion of all of the sub-resources including endpoints, origins and custom domains.

```sql
DELETE FROM azure.cdn.profiles
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_supported_optimization_types"
    values={[
        { label: 'list_supported_optimization_types', value: 'list_supported_optimization_types' },
        { label: 'list_resource_usage', value: 'list_resource_usage' },
        { label: 'migration_commit', value: 'migration_commit' },
        { label: 'generate_sso_uri', value: 'generate_sso_uri' },
        { label: 'cdn_can_migrate_to_afd', value: 'cdn_can_migrate_to_afd' },
        { label: 'cdn_migrate_to_afd', value: 'cdn_migrate_to_afd' },
        { label: 'migration_abort', value: 'migration_abort' },
        { label: 'can_migrate', value: 'can_migrate' },
        { label: 'migrate', value: 'migrate' }
    ]}
>
<TabItem value="list_supported_optimization_types">

Gets the supported optimization types for the current profile. A user can create an endpoint with an optimization type from the listed values.

```sql
EXEC azure.cdn.profiles.list_supported_optimization_types 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_resource_usage">

Checks the quota and actual usage of endpoints under the given Azure Front Door Standard or Azure Front Door Premium or CDN profile.

```sql
EXEC azure.cdn.profiles.list_resource_usage 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="migration_commit">

Commit the migrated Azure Frontdoor(Standard/Premium) profile.

```sql
EXEC azure.cdn.profiles.migration_commit 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate_sso_uri">

Generates a dynamic SSO URI used to sign in to the CDN supplemental portal. Supplemental portal is used to configure advanced feature capabilities that are not yet available in the Azure portal, such as core reports in a standard profile; rules engine, advanced HTTP reports, and real-time stats and alerts in a premium profile. The SSO URI changes approximately every 10 minutes.

```sql
EXEC azure.cdn.profiles.generate_sso_uri 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cdn_can_migrate_to_afd">

Checks if CDN profile can be migrated to Azure Frontdoor(Standard/Premium) profile.

```sql
EXEC azure.cdn.profiles.cdn_can_migrate_to_afd 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="cdn_migrate_to_afd">

Migrate the CDN profile to Azure Frontdoor(Standard/Premium) profile. This step prepares the profile for migration and will be followed by Commit to finalize the migration.

```sql
EXEC azure.cdn.profiles.cdn_migrate_to_afd 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sku": "{{ sku }}", 
"migrationEndpointMappings": "{{ migrationEndpointMappings }}"
}'
;
```
</TabItem>
<TabItem value="migration_abort">

Abort the migration to Azure Frontdoor Premium/Standard.

```sql
EXEC azure.cdn.profiles.migration_abort 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="can_migrate">

Checks if CDN profile can be migrated to Azure Frontdoor(Standard/Premium) profile.

```sql
EXEC azure.cdn.profiles.can_migrate 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"classicResourceReference": "{{ classicResourceReference }}"
}'
;
```
</TabItem>
<TabItem value="migrate">

Migrate the CDN profile to Azure Frontdoor(Standard/Premium) profile. The change need to be committed after this.

```sql
EXEC azure.cdn.profiles.migrate 
@resource_group_name='{{ resource_group_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"sku": "{{ sku }}", 
"classicResourceReference": "{{ classicResourceReference }}", 
"profileName": "{{ profileName }}", 
"migrationWebApplicationFirewallMappings": "{{ migrationWebApplicationFirewallMappings }}"
}'
;
```
</TabItem>
</Tabs>
