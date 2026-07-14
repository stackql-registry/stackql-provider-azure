--- 
title: open_shift_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - open_shift_clusters
  - red_hat_openshift
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

Creates, updates, deletes, gets or lists an <code>open_shift_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="open_shift_clusters" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.red_hat_openshift.open_shift_clusters" /></td></tr>
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
    <td><CopyableCode code="apiserverProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster API server profile.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster profile.</td>
</tr>
<tr>
    <td><CopyableCode code="consoleProfile" /></td>
    <td><code>object</code></td>
    <td>The console profile.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressProfiles" /></td>
    <td><code>array</code></td>
    <td>The cluster ingress profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="masterProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster master profile.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster network profile.</td>
</tr>
<tr>
    <td><CopyableCode code="platformWorkloadIdentityProfile" /></td>
    <td><code>object</code></td>
    <td>The workload identity profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The cluster provisioning state. Known values are: "AdminUpdating", "Canceled", "Creating", "Deleting", "Failed", "Succeeded", and "Updating". (AdminUpdating, Canceled, Creating, Deleting, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster service principal profile.</td>
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
    <td><CopyableCode code="workerProfiles" /></td>
    <td><code>array</code></td>
    <td>The cluster worker profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="workerProfilesStatus" /></td>
    <td><code>array</code></td>
    <td>The cluster worker profiles status.</td>
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
    <td><CopyableCode code="apiserverProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster API server profile.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster profile.</td>
</tr>
<tr>
    <td><CopyableCode code="consoleProfile" /></td>
    <td><code>object</code></td>
    <td>The console profile.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressProfiles" /></td>
    <td><code>array</code></td>
    <td>The cluster ingress profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="masterProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster master profile.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster network profile.</td>
</tr>
<tr>
    <td><CopyableCode code="platformWorkloadIdentityProfile" /></td>
    <td><code>object</code></td>
    <td>The workload identity profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The cluster provisioning state. Known values are: "AdminUpdating", "Canceled", "Creating", "Deleting", "Failed", "Succeeded", and "Updating". (AdminUpdating, Canceled, Creating, Deleting, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster service principal profile.</td>
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
    <td><CopyableCode code="workerProfiles" /></td>
    <td><code>array</code></td>
    <td>The cluster worker profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="workerProfilesStatus" /></td>
    <td><code>array</code></td>
    <td>The cluster worker profiles status.</td>
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
    <td><CopyableCode code="apiserverProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster API server profile.</td>
</tr>
<tr>
    <td><CopyableCode code="clusterProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster profile.</td>
</tr>
<tr>
    <td><CopyableCode code="consoleProfile" /></td>
    <td><code>object</code></td>
    <td>The console profile.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The managed service identities assigned to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressProfiles" /></td>
    <td><code>array</code></td>
    <td>The cluster ingress profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="masterProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster master profile.</td>
</tr>
<tr>
    <td><CopyableCode code="networkProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster network profile.</td>
</tr>
<tr>
    <td><CopyableCode code="platformWorkloadIdentityProfile" /></td>
    <td><code>object</code></td>
    <td>The workload identity profile.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The cluster provisioning state. Known values are: "AdminUpdating", "Canceled", "Creating", "Deleting", "Failed", "Succeeded", and "Updating". (AdminUpdating, Canceled, Creating, Deleting, Failed, Succeeded, Updating)</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipalProfile" /></td>
    <td><code>object</code></td>
    <td>The cluster service principal profile.</td>
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
    <td><CopyableCode code="workerProfiles" /></td>
    <td><code>array</code></td>
    <td>The cluster worker profiles.</td>
</tr>
<tr>
    <td><CopyableCode code="workerProfilesStatus" /></td>
    <td><code>array</code></td>
    <td>The cluster worker profiles status.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns properties of a OpenShift cluster.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists OpenShift clusters in the specified subscription and resource group. The operation returns properties of each OpenShift cluster.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists OpenShift clusters in the specified subscription. The operation returns properties of each OpenShift cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns properties of a OpenShift cluster.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns properties of a OpenShift cluster.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns properties of a OpenShift cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns nothing.</td>
</tr>
<tr>
    <td><a href="#list_admin_credentials"><CopyableCode code="list_admin_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists admin kubeconfig of an OpenShift cluster with the specified subscription, resource group and resource name. The operation returns the admin kubeconfig.</td>
</tr>
<tr>
    <td><a href="#list_credentials"><CopyableCode code="list_credentials" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-resource_name"><code>resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists credentials of an OpenShift cluster with the specified subscription, resource group and resource name. The operation returns the credentials.</td>
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
<tr id="parameter-resource_name">
    <td><CopyableCode code="resource_name" /></td>
    <td><code>string</code></td>
    <td>The name of the OpenShift cluster resource. Required.</td>
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

Gets a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns properties of a OpenShift cluster.

```sql
SELECT
id,
name,
apiserverProfile,
clusterProfile,
consoleProfile,
identity,
ingressProfiles,
location,
masterProfile,
networkProfile,
platformWorkloadIdentityProfile,
provisioningState,
servicePrincipalProfile,
systemData,
tags,
type,
workerProfiles,
workerProfilesStatus
FROM azure.red_hat_openshift.open_shift_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND resource_name = '{{ resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists OpenShift clusters in the specified subscription and resource group. The operation returns properties of each OpenShift cluster.

```sql
SELECT
id,
name,
apiserverProfile,
clusterProfile,
consoleProfile,
identity,
ingressProfiles,
location,
masterProfile,
networkProfile,
platformWorkloadIdentityProfile,
provisioningState,
servicePrincipalProfile,
systemData,
tags,
type,
workerProfiles,
workerProfilesStatus
FROM azure.red_hat_openshift.open_shift_clusters
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists OpenShift clusters in the specified subscription. The operation returns properties of each OpenShift cluster.

```sql
SELECT
id,
name,
apiserverProfile,
clusterProfile,
consoleProfile,
identity,
ingressProfiles,
location,
masterProfile,
networkProfile,
platformWorkloadIdentityProfile,
provisioningState,
servicePrincipalProfile,
systemData,
tags,
type,
workerProfiles,
workerProfilesStatus
FROM azure.red_hat_openshift.open_shift_clusters
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

Creates or updates a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns properties of a OpenShift cluster.

```sql
INSERT INTO azure.red_hat_openshift.open_shift_clusters (
tags,
location,
properties,
identity,
resource_group_name,
resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ resource_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: open_shift_clusters
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the open_shift_clusters resource.
    - name: resource_name
      value: "{{ resource_name }}"
      description: Required parameter for the open_shift_clusters resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the open_shift_clusters resource.
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
        The cluster properties.
      value:
        provisioningState: "{{ provisioningState }}"
        clusterProfile:
          pullSecret: "{{ pullSecret }}"
          domain: "{{ domain }}"
          version: "{{ version }}"
          resourceGroupId: "{{ resourceGroupId }}"
          fipsValidatedModules: "{{ fipsValidatedModules }}"
          oidcIssuer: "{{ oidcIssuer }}"
        consoleProfile:
          url: "{{ url }}"
        servicePrincipalProfile:
          clientId: "{{ clientId }}"
          clientSecret: "{{ clientSecret }}"
        platformWorkloadIdentityProfile:
          upgradeableTo: "{{ upgradeableTo }}"
          platformWorkloadIdentities: "{{ platformWorkloadIdentities }}"
        networkProfile:
          podCidr: "{{ podCidr }}"
          serviceCidr: "{{ serviceCidr }}"
          outboundType: "{{ outboundType }}"
          loadBalancerProfile:
            managedOutboundIps:
              count: {{ count }}
            effectiveOutboundIps:
              - id: "{{ id }}"
          preconfiguredNSG: "{{ preconfiguredNSG }}"
        masterProfile:
          vmSize: "{{ vmSize }}"
          subnetId: "{{ subnetId }}"
          encryptionAtHost: "{{ encryptionAtHost }}"
          diskEncryptionSetId: "{{ diskEncryptionSetId }}"
        workerProfiles:
          - name: "{{ name }}"
            vmSize: "{{ vmSize }}"
            diskSizeGB: {{ diskSizeGB }}
            subnetId: "{{ subnetId }}"
            count: {{ count }}
            encryptionAtHost: "{{ encryptionAtHost }}"
            diskEncryptionSetId: "{{ diskEncryptionSetId }}"
        workerProfilesStatus:
          - name: "{{ name }}"
            vmSize: "{{ vmSize }}"
            diskSizeGB: {{ diskSizeGB }}
            subnetId: "{{ subnetId }}"
            count: {{ count }}
            encryptionAtHost: "{{ encryptionAtHost }}"
            diskEncryptionSetId: "{{ diskEncryptionSetId }}"
        apiserverProfile:
          visibility: "{{ visibility }}"
          url: "{{ url }}"
          ip: "{{ ip }}"
        ingressProfiles:
          - name: "{{ name }}"
            visibility: "{{ visibility }}"
            ip: "{{ ip }}"
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

Creates or updates a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns properties of a OpenShift cluster.

```sql
UPDATE azure.red_hat_openshift.open_shift_clusters
SET 
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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

Creates or updates a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns properties of a OpenShift cluster.

```sql
REPLACE azure.red_hat_openshift.open_shift_clusters
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Deletes a OpenShift cluster with the specified subscription, resource group and resource name. The operation returns nothing.

```sql
DELETE FROM azure.red_hat_openshift.open_shift_clusters
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND resource_name = '{{ resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_admin_credentials"
    values={[
        { label: 'list_admin_credentials', value: 'list_admin_credentials' },
        { label: 'list_credentials', value: 'list_credentials' }
    ]}
>
<TabItem value="list_admin_credentials">

Lists admin kubeconfig of an OpenShift cluster with the specified subscription, resource group and resource name. The operation returns the admin kubeconfig.

```sql
EXEC azure.red_hat_openshift.open_shift_clusters.list_admin_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_credentials">

Lists credentials of an OpenShift cluster with the specified subscription, resource group and resource name. The operation returns the credentials.

```sql
EXEC azure.red_hat_openshift.open_shift_clusters.list_credentials 
@resource_group_name='{{ resource_group_name }}' --required, 
@resource_name='{{ resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
