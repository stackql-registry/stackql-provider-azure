--- 
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - hdinsight
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

Creates, updates, deletes, gets or lists an <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="applications" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.applications" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_azure_async_operation_status"
    values={[
        { label: 'get_azure_async_operation_status', value: 'get_azure_async_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list_by_cluster', value: 'list_by_cluster' }
    ]}
>
<TabItem value="get_azure_async_operation_status">

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
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>The error message associated with the cluster creation.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>The async operation state. Known values are: "InProgress", "Succeeded", and "Failed". (InProgress, Succeeded, Failed)</td>
</tr>
</tbody>
</table>
</TabItem>
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
    <td><CopyableCode code="applicationState" /></td>
    <td><code>string</code></td>
    <td>The application state.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>The application type.</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>The list of roles in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string</code></td>
    <td>The application create date time.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsEndpoints" /></td>
    <td><code>array</code></td>
    <td>The list of application HTTPS endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="installScriptActions" /></td>
    <td><code>array</code></td>
    <td>The list of install script actions.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceIdentifier" /></td>
    <td><code>string</code></td>
    <td>The marketplace identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConfigurations" /></td>
    <td><code>array</code></td>
    <td>The private link configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="sshEndpoints" /></td>
    <td><code>array</code></td>
    <td>The list of application SSH endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uninstallScriptActions" /></td>
    <td><code>array</code></td>
    <td>The list of uninstall script actions.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_cluster">

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
    <td><CopyableCode code="applicationState" /></td>
    <td><code>string</code></td>
    <td>The application state.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationType" /></td>
    <td><code>string</code></td>
    <td>The application type.</td>
</tr>
<tr>
    <td><CopyableCode code="computeProfile" /></td>
    <td><code>object</code></td>
    <td>The list of roles in the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDate" /></td>
    <td><code>string</code></td>
    <td>The application create date time.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>The ETag for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsEndpoints" /></td>
    <td><code>array</code></td>
    <td>The list of application HTTPS endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="installScriptActions" /></td>
    <td><code>array</code></td>
    <td>The list of install script actions.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceIdentifier" /></td>
    <td><code>string</code></td>
    <td>The marketplace identifier.</td>
</tr>
<tr>
    <td><CopyableCode code="privateLinkConfigurations" /></td>
    <td><code>array</code></td>
    <td>The private link configurations.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the application.</td>
</tr>
<tr>
    <td><CopyableCode code="sshEndpoints" /></td>
    <td><code>array</code></td>
    <td>The list of application SSH endpoints.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags for the application.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="uninstallScriptActions" /></td>
    <td><code>array</code></td>
    <td>The list of uninstall script actions.</td>
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
    <td><a href="#get_azure_async_operation_status"><CopyableCode code="get_azure_async_operation_status" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the async operation status.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets properties of the specified application.</td>
</tr>
<tr>
    <td><a href="#list_by_cluster"><CopyableCode code="list_by_cluster" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the applications for the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates applications for the HDInsight cluster.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-application_name"><code>application_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified application on the HDInsight cluster.</td>
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
<tr id="parameter-application_name">
    <td><CopyableCode code="application_name" /></td>
    <td><code>string</code></td>
    <td>The constant value for the application name. Required.</td>
</tr>
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the cluster. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The long running operation id. Required.</td>
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
    defaultValue="get_azure_async_operation_status"
    values={[
        { label: 'get_azure_async_operation_status', value: 'get_azure_async_operation_status' },
        { label: 'get', value: 'get' },
        { label: 'list_by_cluster', value: 'list_by_cluster' }
    ]}
>
<TabItem value="get_azure_async_operation_status">

Gets the async operation status.

```sql
SELECT
error,
status
FROM azure.hdinsight.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND application_name = '{{ application_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets properties of the specified application.

```sql
SELECT
id,
name,
applicationState,
applicationType,
computeProfile,
createdDate,
errors,
etag,
httpsEndpoints,
installScriptActions,
marketplaceIdentifier,
privateLinkConfigurations,
provisioningState,
sshEndpoints,
systemData,
tags,
type,
uninstallScriptActions
FROM azure.hdinsight.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND application_name = '{{ application_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_cluster">

Lists all of the applications for the HDInsight cluster.

```sql
SELECT
id,
name,
applicationState,
applicationType,
computeProfile,
createdDate,
errors,
etag,
httpsEndpoints,
installScriptActions,
marketplaceIdentifier,
privateLinkConfigurations,
provisioningState,
sshEndpoints,
systemData,
tags,
type,
uninstallScriptActions
FROM azure.hdinsight.applications
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
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

Creates applications for the HDInsight cluster.

```sql
INSERT INTO azure.hdinsight.applications (
properties,
etag,
tags,
resource_group_name,
cluster_name,
application_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ etag }}',
'{{ tags }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ application_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: applications
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the applications resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the applications resource.
    - name: application_name
      value: "{{ application_name }}"
      description: Required parameter for the applications resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the applications resource.
    - name: properties
      description: |
        The properties of the application.
      value:
        computeProfile:
          roles:
            - name: "{{ name }}"
              minInstanceCount: {{ minInstanceCount }}
              targetInstanceCount: {{ targetInstanceCount }}
              VMGroupName: "{{ VMGroupName }}"
              autoscale:
                capacity:
                  minInstanceCount: {{ minInstanceCount }}
                  maxInstanceCount: {{ maxInstanceCount }}
                recurrence:
                  timeZone: "{{ timeZone }}"
                  schedule: "{{ schedule }}"
              hardwareProfile:
                vmSize: "{{ vmSize }}"
              osProfile:
                linuxOperatingSystemProfile:
                  username: "{{ username }}"
                  password: "{{ password }}"
                  sshProfile: "{{ sshProfile }}"
              virtualNetworkProfile:
                id: "{{ id }}"
                subnet: "{{ subnet }}"
              dataDisksGroups: "{{ dataDisksGroups }}"
              scriptActions: "{{ scriptActions }}"
              encryptDataDisks: {{ encryptDataDisks }}
        installScriptActions:
          - name: "{{ name }}"
            uri: "{{ uri }}"
            parameters: "{{ parameters }}"
            roles: "{{ roles }}"
            applicationName: "{{ applicationName }}"
        uninstallScriptActions:
          - name: "{{ name }}"
            uri: "{{ uri }}"
            parameters: "{{ parameters }}"
            roles: "{{ roles }}"
            applicationName: "{{ applicationName }}"
        httpsEndpoints:
          - accessModes: "{{ accessModes }}"
            location: "{{ location }}"
            destinationPort: {{ destinationPort }}
            publicPort: {{ publicPort }}
            privateIPAddress: "{{ privateIPAddress }}"
            subDomainSuffix: "{{ subDomainSuffix }}"
            disableGatewayAuth: {{ disableGatewayAuth }}
        sshEndpoints:
          - location: "{{ location }}"
            destinationPort: {{ destinationPort }}
            publicPort: {{ publicPort }}
            privateIPAddress: "{{ privateIPAddress }}"
        provisioningState: "{{ provisioningState }}"
        applicationType: "{{ applicationType }}"
        applicationState: "{{ applicationState }}"
        errors:
          - code: "{{ code }}"
            message: "{{ message }}"
        createdDate: "{{ createdDate }}"
        marketplaceIdentifier: "{{ marketplaceIdentifier }}"
        privateLinkConfigurations:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              groupId: "{{ groupId }}"
              provisioningState: "{{ provisioningState }}"
              ipConfigurations:
                - id: "{{ id }}"
                  name: "{{ name }}"
                  type: "{{ type }}"
                  properties:
                    provisioningState: "{{ provisioningState }}"
                    primary: {{ primary }}
                    privateIPAddress: "{{ privateIPAddress }}"
                    privateIPAllocationMethod: "{{ privateIPAllocationMethod }}"
                    subnet: "{{ subnet }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        The ETag for the application.
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags for the application.
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

Deletes the specified application on the HDInsight cluster.

```sql
DELETE FROM azure.hdinsight.applications
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND application_name = '{{ application_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
