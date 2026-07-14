--- 
title: source_control_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_configurations
  - kubernetes_configuration
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

Creates, updates, deletes, gets or lists a <code>source_control_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="source_control_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.source_control_configurations" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceStatus" /></td>
    <td><code>object</code></td>
    <td>Compliance Status of the Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationProtectedSettings" /></td>
    <td><code>object</code></td>
    <td>Name-value pairs of protected configuration settings for the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHelmOperator" /></td>
    <td><code>boolean</code></td>
    <td>Option to enable Helm Operator for this git configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="helmOperatorProperties" /></td>
    <td><code>object</code></td>
    <td>Properties for Helm operator.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorInstanceName" /></td>
    <td><code>string</code></td>
    <td>Instance name of the operator - identifying the specific configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorNamespace" /></td>
    <td><code>string</code></td>
    <td>The namespace to which this operator is installed to. Maximum of 253 lower case alphanumeric characters, hyphen and period only.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorParams" /></td>
    <td><code>string</code></td>
    <td>Any Parameters for the Operator instance in string format.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorScope" /></td>
    <td><code>string</code></td>
    <td>Scope at which the operator will be installed. Known values are: "cluster" and "namespace".</td>
</tr>
<tr>
    <td><CopyableCode code="operatorType" /></td>
    <td><code>string</code></td>
    <td>Type of the operator. "Flux"</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource provider. Known values are: "Accepted", "Deleting", "Running", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public Key associated with this SourceControl configuration (either generated within the cluster or provided by the user).</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryUrl" /></td>
    <td><code>string</code></td>
    <td>Url of the SourceControl Repository.</td>
</tr>
<tr>
    <td><CopyableCode code="sshKnownHostsContents" /></td>
    <td><code>string</code></td>
    <td>Base64-encoded known_hosts contents containing public SSH keys required to access private Git instances.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.</td>
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
    <td><CopyableCode code="complianceStatus" /></td>
    <td><code>object</code></td>
    <td>Compliance Status of the Configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="configurationProtectedSettings" /></td>
    <td><code>object</code></td>
    <td>Name-value pairs of protected configuration settings for the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="enableHelmOperator" /></td>
    <td><code>boolean</code></td>
    <td>Option to enable Helm Operator for this git configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="helmOperatorProperties" /></td>
    <td><code>object</code></td>
    <td>Properties for Helm operator.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorInstanceName" /></td>
    <td><code>string</code></td>
    <td>Instance name of the operator - identifying the specific configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorNamespace" /></td>
    <td><code>string</code></td>
    <td>The namespace to which this operator is installed to. Maximum of 253 lower case alphanumeric characters, hyphen and period only.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorParams" /></td>
    <td><code>string</code></td>
    <td>Any Parameters for the Operator instance in string format.</td>
</tr>
<tr>
    <td><CopyableCode code="operatorScope" /></td>
    <td><code>string</code></td>
    <td>Scope at which the operator will be installed. Known values are: "cluster" and "namespace".</td>
</tr>
<tr>
    <td><CopyableCode code="operatorType" /></td>
    <td><code>string</code></td>
    <td>Type of the operator. "Flux"</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the resource provider. Known values are: "Accepted", "Deleting", "Running", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public Key associated with this SourceControl configuration (either generated within the cluster or provided by the user).</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryUrl" /></td>
    <td><code>string</code></td>
    <td>Url of the SourceControl Repository.</td>
</tr>
<tr>
    <td><CopyableCode code="sshKnownHostsContents" /></td>
    <td><code>string</code></td>
    <td>Base64-encoded known_hosts contents containing public SSH keys required to access private Git instances.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-source_control_configuration_name"><code>source_control_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets details of the Source Control Configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Source Control Configurations.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-source_control_configuration_name"><code>source_control_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Kubernetes Source Control Configuration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-source_control_configuration_name"><code>source_control_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Kubernetes Source Control Configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-source_control_configuration_name"><code>source_control_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This will delete the YAML file used to set up the Source control configuration, thus stopping future sync from the source repo.</td>
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
<tr id="parameter-cluster_name">
    <td><CopyableCode code="cluster_name" /></td>
    <td><code>string</code></td>
    <td>The name of the kubernetes cluster. Required.</td>
</tr>
<tr id="parameter-cluster_resource_name">
    <td><CopyableCode code="cluster_resource_name" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes cluster resource name - i.e. managedClusters, connectedClusters, provisionedClusters. Required.</td>
</tr>
<tr id="parameter-cluster_rp">
    <td><CopyableCode code="cluster_rp" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes cluster RP - i.e. Microsoft.ContainerService, Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-source_control_configuration_name">
    <td><CopyableCode code="source_control_configuration_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Source Control Configuration. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets details of the Source Control Configuration.

```sql
SELECT
id,
name,
complianceStatus,
configurationProtectedSettings,
enableHelmOperator,
helmOperatorProperties,
operatorInstanceName,
operatorNamespace,
operatorParams,
operatorScope,
operatorType,
provisioningState,
repositoryPublicKey,
repositoryUrl,
sshKnownHostsContents,
systemData,
type
FROM azure.kubernetes_configuration.source_control_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_rp = '{{ cluster_rp }}' -- required
AND cluster_resource_name = '{{ cluster_resource_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND source_control_configuration_name = '{{ source_control_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Source Control Configurations.

```sql
SELECT
id,
name,
complianceStatus,
configurationProtectedSettings,
enableHelmOperator,
helmOperatorProperties,
operatorInstanceName,
operatorNamespace,
operatorParams,
operatorScope,
operatorType,
provisioningState,
repositoryPublicKey,
repositoryUrl,
sshKnownHostsContents,
systemData,
type
FROM azure.kubernetes_configuration.source_control_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_rp = '{{ cluster_rp }}' -- required
AND cluster_resource_name = '{{ cluster_resource_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
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

Create a new Kubernetes Source Control Configuration.

```sql
INSERT INTO azure.kubernetes_configuration.source_control_configurations (
properties,
resource_group_name,
cluster_rp,
cluster_resource_name,
cluster_name,
source_control_configuration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_rp }}',
'{{ cluster_resource_name }}',
'{{ cluster_name }}',
'{{ source_control_configuration_name }}',
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
- name: source_control_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the source_control_configurations resource.
    - name: cluster_rp
      value: "{{ cluster_rp }}"
      description: Required parameter for the source_control_configurations resource.
    - name: cluster_resource_name
      value: "{{ cluster_resource_name }}"
      description: Required parameter for the source_control_configurations resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the source_control_configurations resource.
    - name: source_control_configuration_name
      value: "{{ source_control_configuration_name }}"
      description: Required parameter for the source_control_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the source_control_configurations resource.
    - name: properties
      value:
        repositoryUrl: "{{ repositoryUrl }}"
        operatorNamespace: "{{ operatorNamespace }}"
        operatorInstanceName: "{{ operatorInstanceName }}"
        operatorType: "{{ operatorType }}"
        operatorParams: "{{ operatorParams }}"
        configurationProtectedSettings: "{{ configurationProtectedSettings }}"
        operatorScope: "{{ operatorScope }}"
        sshKnownHostsContents: "{{ sshKnownHostsContents }}"
        enableHelmOperator: {{ enableHelmOperator }}
        helmOperatorProperties:
          chartVersion: "{{ chartVersion }}"
          chartValues: "{{ chartValues }}"
`}</CodeBlock>

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

Create a new Kubernetes Source Control Configuration.

```sql
REPLACE azure.kubernetes_configuration.source_control_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_rp = '{{ cluster_rp }}' --required
AND cluster_resource_name = '{{ cluster_resource_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND source_control_configuration_name = '{{ source_control_configuration_name }}' --required
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

This will delete the YAML file used to set up the Source control configuration, thus stopping future sync from the source repo.

```sql
DELETE FROM azure.kubernetes_configuration.source_control_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_rp = '{{ cluster_rp }}' --required
AND cluster_resource_name = '{{ cluster_resource_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND source_control_configuration_name = '{{ source_control_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
