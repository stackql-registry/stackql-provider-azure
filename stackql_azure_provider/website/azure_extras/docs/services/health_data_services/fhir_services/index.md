--- 
title: fhir_services
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_services
  - health_data_services
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>fhir_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="fhir_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.health_data_services.fhir_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
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
    <td><CopyableCode code="acrConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service Azure container registry configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service authentication configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="corsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service Cors configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption settings of the FHIR service.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>An etag associated with the resource, used for optimistic concurrency when editing it.</td>
</tr>
<tr>
    <td><CopyableCode code="eventState" /></td>
    <td><code>string</code></td>
    <td>Fhir Service event support status. Known values are: "Disabled", "Enabled", and "Updating". (Disabled, Enabled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="exportConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service export configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Setting indicating whether the service has a managed identity associated with it.</td>
</tr>
<tr>
    <td><CopyableCode code="implementationGuidesConfiguration" /></td>
    <td><code>object</code></td>
    <td>Implementation Guides configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="importConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service import configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the service. Known values are: "fhir-Stu3" and "fhir-R4". (fhir-Stu3, fhir-R4)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The common properties for any location based resource, tracked or proxy.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections that are set up for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Deleting", "Succeeded", "Creating", "Accepted", "Verifying", "Updating", "Failed", "Canceled", "Deprovisioned", "Moving", "Suspended", "Warned", and "SystemMaintenance". (Deleting, Succeeded, Creating, Accepted, Verifying, Updating, Failed, Canceled, Deprovisioned, Moving, Suspended, Warned, SystemMaintenance)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Control permission for data plane traffic coming from public networks while private endpoint is enabled. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceVersionPolicyConfiguration" /></td>
    <td><code>object</code></td>
    <td>Determines tracking of history for resources.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The common properties of tracked resources in the service.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_workspace">

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
    <td><CopyableCode code="acrConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service Azure container registry configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="authenticationConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service authentication configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="corsConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service Cors configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="encryption" /></td>
    <td><code>object</code></td>
    <td>The encryption settings of the FHIR service.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>An etag associated with the resource, used for optimistic concurrency when editing it.</td>
</tr>
<tr>
    <td><CopyableCode code="eventState" /></td>
    <td><code>string</code></td>
    <td>Fhir Service event support status. Known values are: "Disabled", "Enabled", and "Updating". (Disabled, Enabled, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="exportConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service export configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Setting indicating whether the service has a managed identity associated with it.</td>
</tr>
<tr>
    <td><CopyableCode code="implementationGuidesConfiguration" /></td>
    <td><code>object</code></td>
    <td>Implementation Guides configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="importConfiguration" /></td>
    <td><code>object</code></td>
    <td>Fhir Service import configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the service. Known values are: "fhir-Stu3" and "fhir-R4". (fhir-Stu3, fhir-R4)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The common properties for any location based resource, tracked or proxy.</td>
</tr>
<tr>
    <td><CopyableCode code="privateEndpointConnections" /></td>
    <td><code>array</code></td>
    <td>The list of private endpoint connections that are set up for this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state. Known values are: "Deleting", "Succeeded", "Creating", "Accepted", "Verifying", "Updating", "Failed", "Canceled", "Deprovisioned", "Moving", "Suspended", "Warned", and "SystemMaintenance". (Deleting, Succeeded, Creating, Accepted, Verifying, Updating, Failed, Canceled, Deprovisioned, Moving, Suspended, Warned, SystemMaintenance)</td>
</tr>
<tr>
    <td><CopyableCode code="publicNetworkAccess" /></td>
    <td><code>string</code></td>
    <td>Control permission for data plane traffic coming from public networks while private endpoint is enabled. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceVersionPolicyConfiguration" /></td>
    <td><code>object</code></td>
    <td>Determines tracking of history for resources.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The common properties of tracked resources in the service.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-fhir_service_name"><code>fhir_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the properties of the specified FHIR Service.</td>
</tr>
<tr>
    <td><a href="#list_by_workspace"><CopyableCode code="list_by_workspace" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all FHIR Services for the given workspace.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-fhir_service_name"><code>fhir_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a FHIR Service resource with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fhir_service_name"><code>fhir_service_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Patch FHIR Service details.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-fhir_service_name"><code>fhir_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a FHIR Service resource with the specified parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-fhir_service_name"><code>fhir_service_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a FHIR Service.</td>
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
<tr id="parameter-fhir_service_name">
    <td><CopyableCode code="fhir_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of FHIR Service resource. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of workspace resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_workspace', value: 'list_by_workspace' }
    ]}
>
<TabItem value="get">

Gets the properties of the specified FHIR Service.

```sql
SELECT
id,
name,
acrConfiguration,
authenticationConfiguration,
corsConfiguration,
encryption,
etag,
eventState,
exportConfiguration,
identity,
implementationGuidesConfiguration,
importConfiguration,
kind,
location,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
resourceVersionPolicyConfiguration,
systemData,
tags,
type
FROM azure_extras.health_data_services.fhir_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND fhir_service_name = '{{ fhir_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_workspace">

Lists all FHIR Services for the given workspace.

```sql
SELECT
id,
name,
acrConfiguration,
authenticationConfiguration,
corsConfiguration,
encryption,
etag,
eventState,
exportConfiguration,
identity,
implementationGuidesConfiguration,
importConfiguration,
kind,
location,
privateEndpointConnections,
provisioningState,
publicNetworkAccess,
resourceVersionPolicyConfiguration,
systemData,
tags,
type
FROM azure_extras.health_data_services.fhir_services
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
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

Creates or updates a FHIR Service resource with the specified parameters.

```sql
INSERT INTO azure_extras.health_data_services.fhir_services (
properties,
tags,
location,
etag,
identity,
kind,
resource_group_name,
workspace_name,
fhir_service_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ etag }}',
'{{ identity }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ fhir_service_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
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
- name: fhir_services
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the fhir_services resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the fhir_services resource.
    - name: fhir_service_name
      value: "{{ fhir_service_name }}"
      description: Required parameter for the fhir_services resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the fhir_services resource.
    - name: properties
      description: |
        Fhir Service configuration.
      value:
        provisioningState: "{{ provisioningState }}"
        acrConfiguration:
          loginServers:
            - "{{ loginServers }}"
          ociArtifacts:
            - loginServer: "{{ loginServer }}"
              imageName: "{{ imageName }}"
              digest: "{{ digest }}"
        authenticationConfiguration:
          authority: "{{ authority }}"
          audience: "{{ audience }}"
          smartProxyEnabled: {{ smartProxyEnabled }}
          smartIdentityProviders:
            - authority: "{{ authority }}"
              applications: "{{ applications }}"
        corsConfiguration:
          origins:
            - "{{ origins }}"
          headers:
            - "{{ headers }}"
          methods:
            - "{{ methods }}"
          maxAge: {{ maxAge }}
          allowCredentials: {{ allowCredentials }}
        exportConfiguration:
          storageAccountName: "{{ storageAccountName }}"
        privateEndpointConnections:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            systemData:
              createdBy: "{{ createdBy }}"
              createdByType: "{{ createdByType }}"
              createdAt: "{{ createdAt }}"
              lastModifiedBy: "{{ lastModifiedBy }}"
              lastModifiedByType: "{{ lastModifiedByType }}"
              lastModifiedAt: "{{ lastModifiedAt }}"
            properties:
              privateEndpoint:
                id: "{{ id }}"
              privateLinkServiceConnectionState:
                status: "{{ status }}"
                description: "{{ description }}"
                actionsRequired: "{{ actionsRequired }}"
              provisioningState: "{{ provisioningState }}"
        publicNetworkAccess: "{{ publicNetworkAccess }}"
        eventState: "{{ eventState }}"
        resourceVersionPolicyConfiguration:
          default: "{{ default }}"
          resourceTypeOverrides: "{{ resourceTypeOverrides }}"
        importConfiguration:
          integrationDataStore: "{{ integrationDataStore }}"
          initialImportMode: {{ initialImportMode }}
          enabled: {{ enabled }}
        implementationGuidesConfiguration:
          usCoreMissingData: {{ usCoreMissingData }}
        encryption:
          customerManagedKeyEncryption:
            keyEncryptionKeyUrl: "{{ keyEncryptionKeyUrl }}"
    - name: tags
      value: "{{ tags }}"
      description: |
        The common properties of tracked resources in the service.
    - name: location
      value: "{{ location }}"
      description: |
        The common properties for any location based resource, tracked or proxy.
    - name: etag
      value: "{{ etag }}"
      description: |
        An etag associated with the resource, used for optimistic concurrency when editing it.
    - name: identity
      description: |
        Setting indicating whether the service has a managed identity associated with it.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the service. Known values are: "fhir-Stu3" and "fhir-R4".
      valid_values: ['fhir-Stu3', 'fhir-R4']
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

Patch FHIR Service details.

```sql
UPDATE azure_extras.health_data_services.fhir_services
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND fhir_service_name = '{{ fhir_service_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Creates or updates a FHIR Service resource with the specified parameters.

```sql
REPLACE azure_extras.health_data_services.fhir_services
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
etag = '{{ etag }}',
identity = '{{ identity }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND fhir_service_name = '{{ fhir_service_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Deletes a FHIR Service.

```sql
DELETE FROM azure_extras.health_data_services.fhir_services
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND fhir_service_name = '{{ fhir_service_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
