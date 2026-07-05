--- 
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - nginx
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.nginx.deployments" /></td></tr>
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
    <td><CopyableCode code="autoUpgradeProfile" /></td>
    <td><code>object</code></td>
    <td>Autoupgrade settings of a deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dataplaneApiEndpoint" /></td>
    <td><code>string</code></td>
    <td>Dataplane API endpoint for the caller to update the NGINX state of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDiagnosticsSupport" /></td>
    <td><code>boolean</code></td>
    <td>:vartype enable_diagnostics_support: bool</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logging" /></td>
    <td><code>object</code></td>
    <td>Nginx Logging.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Nginx Network Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="nginxAppProtect" /></td>
    <td><code>object</code></td>
    <td>Settings for NGINX App Protect (NAP).</td>
</tr>
<tr>
    <td><CopyableCode code="nginxVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype nginx_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified". (Accepted, Creating, Updating, Deleting, Succeeded, Failed, Canceled, Deleted, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="scalingProperties" /></td>
    <td><code>object</code></td>
    <td>Information on how the deployment will be scaled.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Resource Sku.</td>
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
    <td><CopyableCode code="userProfile" /></td>
    <td><code>object</code></td>
    <td>Nginx Deployment User Profile.</td>
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
    <td><CopyableCode code="autoUpgradeProfile" /></td>
    <td><code>object</code></td>
    <td>Autoupgrade settings of a deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dataplaneApiEndpoint" /></td>
    <td><code>string</code></td>
    <td>Dataplane API endpoint for the caller to update the NGINX state of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDiagnosticsSupport" /></td>
    <td><code>boolean</code></td>
    <td>:vartype enable_diagnostics_support: bool</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logging" /></td>
    <td><code>object</code></td>
    <td>Nginx Logging.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Nginx Network Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="nginxAppProtect" /></td>
    <td><code>object</code></td>
    <td>Settings for NGINX App Protect (NAP).</td>
</tr>
<tr>
    <td><CopyableCode code="nginxVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype nginx_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified". (Accepted, Creating, Updating, Deleting, Succeeded, Failed, Canceled, Deleted, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="scalingProperties" /></td>
    <td><code>object</code></td>
    <td>Information on how the deployment will be scaled.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Resource Sku.</td>
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
    <td><CopyableCode code="userProfile" /></td>
    <td><code>object</code></td>
    <td>Nginx Deployment User Profile.</td>
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
    <td><CopyableCode code="autoUpgradeProfile" /></td>
    <td><code>object</code></td>
    <td>Autoupgrade settings of a deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="dataplaneApiEndpoint" /></td>
    <td><code>string</code></td>
    <td>Dataplane API endpoint for the caller to update the NGINX state of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="enableDiagnosticsSupport" /></td>
    <td><code>boolean</code></td>
    <td>:vartype enable_diagnostics_support: bool</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Identity Properties.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>string</code></td>
    <td>The IP address of the deployment.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="logging" /></td>
    <td><code>object</code></td>
    <td>Nginx Logging.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>Nginx Network Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="nginxAppProtect" /></td>
    <td><code>object</code></td>
    <td>Settings for NGINX App Protect (NAP).</td>
</tr>
<tr>
    <td><CopyableCode code="nginxVersion" /></td>
    <td><code>string</code></td>
    <td>:vartype nginx_version: str</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning State. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified". (Accepted, Creating, Updating, Deleting, Succeeded, Failed, Canceled, Deleted, NotSpecified)</td>
</tr>
<tr>
    <td><CopyableCode code="scalingProperties" /></td>
    <td><code>object</code></td>
    <td>Information on how the deployment will be scaled.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Resource Sku.</td>
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
    <td><CopyableCode code="userProfile" /></td>
    <td><code>object</code></td>
    <td>Nginx Deployment User Profile.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the NGINX deployment.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all NGINX deployments under the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the NGINX deployments resources.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the NGINX deployment.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update the NGINX deployment.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update the NGINX deployment.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the NGINX deployment resource.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The name of targeted NGINX deployment. Required.</td>
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

Get the NGINX deployment.

```sql
SELECT
id,
name,
autoUpgradeProfile,
dataplaneApiEndpoint,
enableDiagnosticsSupport,
identity,
ipAddress,
location,
logging,
networkProfile,
nginxAppProtect,
nginxVersion,
provisioningState,
scalingProperties,
sku,
systemData,
tags,
type,
userProfile
FROM azure_isv.nginx.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List all NGINX deployments under the specified resource group.

```sql
SELECT
id,
name,
autoUpgradeProfile,
dataplaneApiEndpoint,
enableDiagnosticsSupport,
identity,
ipAddress,
location,
logging,
networkProfile,
nginxAppProtect,
nginxVersion,
provisioningState,
scalingProperties,
sku,
systemData,
tags,
type,
userProfile
FROM azure_isv.nginx.deployments
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the NGINX deployments resources.

```sql
SELECT
id,
name,
autoUpgradeProfile,
dataplaneApiEndpoint,
enableDiagnosticsSupport,
identity,
ipAddress,
location,
logging,
networkProfile,
nginxAppProtect,
nginxVersion,
provisioningState,
scalingProperties,
sku,
systemData,
tags,
type,
userProfile
FROM azure_isv.nginx.deployments
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create or update the NGINX deployment.

```sql
INSERT INTO azure_isv.nginx.deployments (
tags,
location,
properties,
identity,
sku,
resource_group_name,
deployment_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ sku }}',
'{{ resource_group_name }}',
'{{ deployment_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: deployments
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the deployments resource.
    - name: deployment_name
      value: "{{ deployment_name }}"
      description: Required parameter for the deployments resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the deployments resource.
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
        Nginx Deployment Properties.
      value:
        provisioningState: "{{ provisioningState }}"
        nginxVersion: "{{ nginxVersion }}"
        networkProfile:
          frontEndIPConfiguration:
            publicIPAddresses:
              - id: "{{ id }}"
            privateIPAddresses:
              - privateIPAddress: "{{ privateIPAddress }}"
                privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                subnetId: "{{ subnetId }}"
          networkInterfaceConfiguration:
            subnetId: "{{ subnetId }}"
        ipAddress: "{{ ipAddress }}"
        enableDiagnosticsSupport: {{ enableDiagnosticsSupport }}
        logging:
          storageAccount:
            accountName: "{{ accountName }}"
            containerName: "{{ containerName }}"
        scalingProperties:
          capacity: {{ capacity }}
          autoScaleSettings:
            profiles:
              - name: "{{ name }}"
                capacity:
                  min: {{ min }}
                  max: {{ max }}
        autoUpgradeProfile:
          upgradeChannel: "{{ upgradeChannel }}"
        userProfile:
          preferredEmail: "{{ preferredEmail }}"
        nginxAppProtect:
          webApplicationFirewallSettings:
            activationState: "{{ activationState }}"
          webApplicationFirewallStatus:
            wafRelease: "{{ wafRelease }}"
            attackSignaturesPackage:
              version: "{{ version }}"
              revisionDatetime: "{{ revisionDatetime }}"
            botSignaturesPackage:
              version: "{{ version }}"
              revisionDatetime: "{{ revisionDatetime }}"
            threatCampaignsPackage:
              version: "{{ version }}"
              revisionDatetime: "{{ revisionDatetime }}"
            componentVersions:
              wafEngineVersion: "{{ wafEngineVersion }}"
              wafNginxVersion: "{{ wafNginxVersion }}"
        dataplaneApiEndpoint: "{{ dataplaneApiEndpoint }}"
    - name: identity
      description: |
        Identity Properties.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: sku
      description: |
        Resource Sku.
      value:
        name: "{{ name }}"
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

Update the NGINX deployment.

```sql
UPDATE azure_isv.nginx.deployments
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
sku,
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

Create or update the NGINX deployment.

```sql
REPLACE azure_isv.nginx.deployments
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Delete the NGINX deployment resource.

```sql
DELETE FROM azure_isv.nginx.deployments
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND deployment_name = '{{ deployment_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
