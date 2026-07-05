--- 
title: flux_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - flux_configurations
  - kubernetesconfiguration_fluxconfigurations
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

Creates, updates, deletes, gets or lists a <code>flux_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="flux_configurations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetesconfiguration_fluxconfigurations.flux_configurations" /></td></tr>
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
    <td><CopyableCode code="azureBlob" /></td>
    <td><code>object</code></td>
    <td>Parameters to reconcile to the AzureBlob source kind type.</td>
</tr>
<tr>
    <td><CopyableCode code="bucket" /></td>
    <td><code>object</code></td>
    <td>Parameters to reconcile to the Bucket source kind type.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Combined status of the Flux Kubernetes resources created by the fluxConfiguration or created by the managed objects. Known values are: "Compliant", "Non-Compliant", "Pending", "Suspended", and "Unknown". (Compliant, Non-Compliant, Pending, Suspended, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="configurationProtectedSettings" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs of protected configuration settings for the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>Error message returned to the user in the case of provisioning failure.</td>
</tr>
<tr>
    <td><CopyableCode code="gitRepository" /></td>
    <td><code>object</code></td>
    <td>Parameters to reconcile to the GitRepository source kind type.</td>
</tr>
<tr>
    <td><CopyableCode code="kustomizations" /></td>
    <td><code>object</code></td>
    <td>Array of kustomizations used to reconcile the artifact pulled by the source type on the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace to which this configuration is installed to. Maximum of 253 lower case alphanumeric characters, hyphen and period only.</td>
</tr>
<tr>
    <td><CopyableCode code="ociRepository" /></td>
    <td><code>object</code></td>
    <td>Parameters to reconcile to the OCIRepository source kind type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the creation of the fluxConfiguration. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="reconciliationWaitDuration" /></td>
    <td><code>string</code></td>
    <td>Maximum duration to wait for flux configuration reconciliation. E.g PT1H, PT5M, P1D.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public Key associated with this fluxConfiguration (either generated within the cluster or provided by the user).</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope at which the operator will be installed. Known values are: "cluster" and "namespace". (cluster, namespace)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceKind" /></td>
    <td><code>string</code></td>
    <td>Source Kind to pull the configuration data from. Known values are: "GitRepository", "Bucket", "AzureBlob", and "OCIRepository". (GitRepository, Bucket, AzureBlob, OCIRepository)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSyncedCommitId" /></td>
    <td><code>string</code></td>
    <td>Branch and/or SHA of the source commit synced with the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceUpdatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Datetime the fluxConfiguration synced its source on the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="statusUpdatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Datetime the fluxConfiguration synced its status on the cluster with Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>Statuses of the Flux Kubernetes resources created by the fluxConfiguration or created by the managed objects provisioned by the fluxConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="suspend" /></td>
    <td><code>boolean</code></td>
    <td>Whether this configuration should suspend its reconciliation of its kustomizations and sources.</td>
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
<tr>
    <td><CopyableCode code="waitForReconciliation" /></td>
    <td><code>boolean</code></td>
    <td>Whether flux configuration deployment should wait for cluster to reconcile the kustomizations.</td>
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
    <td><CopyableCode code="azureBlob" /></td>
    <td><code>object</code></td>
    <td>Parameters to reconcile to the AzureBlob source kind type.</td>
</tr>
<tr>
    <td><CopyableCode code="bucket" /></td>
    <td><code>object</code></td>
    <td>Parameters to reconcile to the Bucket source kind type.</td>
</tr>
<tr>
    <td><CopyableCode code="complianceState" /></td>
    <td><code>string</code></td>
    <td>Combined status of the Flux Kubernetes resources created by the fluxConfiguration or created by the managed objects. Known values are: "Compliant", "Non-Compliant", "Pending", "Suspended", and "Unknown". (Compliant, Non-Compliant, Pending, Suspended, Unknown)</td>
</tr>
<tr>
    <td><CopyableCode code="configurationProtectedSettings" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs of protected configuration settings for the configuration.</td>
</tr>
<tr>
    <td><CopyableCode code="errorMessage" /></td>
    <td><code>string</code></td>
    <td>Error message returned to the user in the case of provisioning failure.</td>
</tr>
<tr>
    <td><CopyableCode code="gitRepository" /></td>
    <td><code>object</code></td>
    <td>Parameters to reconcile to the GitRepository source kind type.</td>
</tr>
<tr>
    <td><CopyableCode code="kustomizations" /></td>
    <td><code>object</code></td>
    <td>Array of kustomizations used to reconcile the artifact pulled by the source type on the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="namespace" /></td>
    <td><code>string</code></td>
    <td>The namespace to which this configuration is installed to. Maximum of 253 lower case alphanumeric characters, hyphen and period only.</td>
</tr>
<tr>
    <td><CopyableCode code="ociRepository" /></td>
    <td><code>object</code></td>
    <td>Parameters to reconcile to the OCIRepository source kind type.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Status of the creation of the fluxConfiguration. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Updating", and "Deleting". (Succeeded, Failed, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="reconciliationWaitDuration" /></td>
    <td><code>string</code></td>
    <td>Maximum duration to wait for flux configuration reconciliation. E.g PT1H, PT5M, P1D.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryPublicKey" /></td>
    <td><code>string</code></td>
    <td>Public Key associated with this fluxConfiguration (either generated within the cluster or provided by the user).</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>Scope at which the operator will be installed. Known values are: "cluster" and "namespace". (cluster, namespace)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceKind" /></td>
    <td><code>string</code></td>
    <td>Source Kind to pull the configuration data from. Known values are: "GitRepository", "Bucket", "AzureBlob", and "OCIRepository". (GitRepository, Bucket, AzureBlob, OCIRepository)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceSyncedCommitId" /></td>
    <td><code>string</code></td>
    <td>Branch and/or SHA of the source commit synced with the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="sourceUpdatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Datetime the fluxConfiguration synced its source on the cluster.</td>
</tr>
<tr>
    <td><CopyableCode code="statusUpdatedAt" /></td>
    <td><code>string (date-time)</code></td>
    <td>Datetime the fluxConfiguration synced its status on the cluster with Azure.</td>
</tr>
<tr>
    <td><CopyableCode code="statuses" /></td>
    <td><code>array</code></td>
    <td>Statuses of the Flux Kubernetes resources created by the fluxConfiguration or created by the managed objects provisioned by the fluxConfiguration.</td>
</tr>
<tr>
    <td><CopyableCode code="suspend" /></td>
    <td><code>boolean</code></td>
    <td>Whether this configuration should suspend its reconciliation of its kustomizations and sources.</td>
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
<tr>
    <td><CopyableCode code="waitForReconciliation" /></td>
    <td><code>boolean</code></td>
    <td>Whether flux configuration deployment should wait for cluster to reconcile the kustomizations.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-flux_configuration_name"><code>flux_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets details of the Flux Configuration.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all Flux Configurations.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-flux_configuration_name"><code>flux_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Kubernetes Flux Configuration.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-flux_configuration_name"><code>flux_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing Kubernetes Flux Configuration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-flux_configuration_name"><code>flux_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new Kubernetes Flux Configuration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_rp"><code>cluster_rp</code></a>, <a href="#parameter-cluster_resource_name"><code>cluster_resource_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-flux_configuration_name"><code>flux_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceDelete"><code>forceDelete</code></a></td>
    <td>This will delete the YAML file used to set up the Flux Configuration, thus stopping future sync from the source repo.</td>
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
    <td>The Kubernetes cluster resource name - i.e. managedClusters, connectedClusters, provisionedClusters, appliances. Required.</td>
</tr>
<tr id="parameter-cluster_rp">
    <td><CopyableCode code="cluster_rp" /></td>
    <td><code>string</code></td>
    <td>The Kubernetes cluster RP - i.e. Microsoft.ContainerService, Microsoft.Kubernetes, Microsoft.HybridContainerService. Required.</td>
</tr>
<tr id="parameter-flux_configuration_name">
    <td><CopyableCode code="flux_configuration_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Flux Configuration. Required.</td>
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
<tr id="parameter-forceDelete">
    <td><CopyableCode code="forceDelete" /></td>
    <td><code>boolean</code></td>
    <td>Delete the extension resource in Azure - not the normal asynchronous delete. Default value is None.</td>
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

Gets details of the Flux Configuration.

```sql
SELECT
id,
name,
azureBlob,
bucket,
complianceState,
configurationProtectedSettings,
errorMessage,
gitRepository,
kustomizations,
namespace,
ociRepository,
provisioningState,
reconciliationWaitDuration,
repositoryPublicKey,
scope,
sourceKind,
sourceSyncedCommitId,
sourceUpdatedAt,
statusUpdatedAt,
statuses,
suspend,
systemData,
type,
waitForReconciliation
FROM azure.kubernetesconfiguration_fluxconfigurations.flux_configurations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_rp = '{{ cluster_rp }}' -- required
AND cluster_resource_name = '{{ cluster_resource_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND flux_configuration_name = '{{ flux_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all Flux Configurations.

```sql
SELECT
id,
name,
azureBlob,
bucket,
complianceState,
configurationProtectedSettings,
errorMessage,
gitRepository,
kustomizations,
namespace,
ociRepository,
provisioningState,
reconciliationWaitDuration,
repositoryPublicKey,
scope,
sourceKind,
sourceSyncedCommitId,
sourceUpdatedAt,
statusUpdatedAt,
statuses,
suspend,
systemData,
type,
waitForReconciliation
FROM azure.kubernetesconfiguration_fluxconfigurations.flux_configurations
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

Create a new Kubernetes Flux Configuration.

```sql
INSERT INTO azure.kubernetesconfiguration_fluxconfigurations.flux_configurations (
properties,
resource_group_name,
cluster_rp,
cluster_resource_name,
cluster_name,
flux_configuration_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_rp }}',
'{{ cluster_resource_name }}',
'{{ cluster_name }}',
'{{ flux_configuration_name }}',
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
- name: flux_configurations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the flux_configurations resource.
    - name: cluster_rp
      value: "{{ cluster_rp }}"
      description: Required parameter for the flux_configurations resource.
    - name: cluster_resource_name
      value: "{{ cluster_resource_name }}"
      description: Required parameter for the flux_configurations resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the flux_configurations resource.
    - name: flux_configuration_name
      value: "{{ flux_configuration_name }}"
      description: Required parameter for the flux_configurations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the flux_configurations resource.
    - name: properties
      description: |
        Properties to create a Flux Configuration resource.
      value:
        scope: "{{ scope }}"
        namespace: "{{ namespace }}"
        sourceKind: "{{ sourceKind }}"
        suspend: {{ suspend }}
        gitRepository:
          url: "{{ url }}"
          timeoutInSeconds: {{ timeoutInSeconds }}
          syncIntervalInSeconds: {{ syncIntervalInSeconds }}
          repositoryRef:
            branch: "{{ branch }}"
            tag: "{{ tag }}"
            semver: "{{ semver }}"
            commit: "{{ commit }}"
          sshKnownHosts: "{{ sshKnownHosts }}"
          httpsUser: "{{ httpsUser }}"
          httpsCACert: "{{ httpsCACert }}"
          localAuthRef: "{{ localAuthRef }}"
          provider: "{{ provider }}"
        bucket:
          url: "{{ url }}"
          bucketName: "{{ bucketName }}"
          insecure: {{ insecure }}
          timeoutInSeconds: {{ timeoutInSeconds }}
          syncIntervalInSeconds: {{ syncIntervalInSeconds }}
          accessKey: "{{ accessKey }}"
          localAuthRef: "{{ localAuthRef }}"
        azureBlob:
          url: "{{ url }}"
          containerName: "{{ containerName }}"
          timeoutInSeconds: {{ timeoutInSeconds }}
          syncIntervalInSeconds: {{ syncIntervalInSeconds }}
          servicePrincipal:
            clientId: "{{ clientId }}"
            tenantId: "{{ tenantId }}"
            clientSecret: "{{ clientSecret }}"
            clientCertificate: "{{ clientCertificate }}"
            clientCertificatePassword: "{{ clientCertificatePassword }}"
            clientCertificateSendChain: {{ clientCertificateSendChain }}
          accountKey: "{{ accountKey }}"
          sasToken: "{{ sasToken }}"
          managedIdentity:
            clientId: "{{ clientId }}"
          localAuthRef: "{{ localAuthRef }}"
        ociRepository:
          url: "{{ url }}"
          timeoutInSeconds: {{ timeoutInSeconds }}
          syncIntervalInSeconds: {{ syncIntervalInSeconds }}
          repositoryRef:
            tag: "{{ tag }}"
            semver: "{{ semver }}"
            digest: "{{ digest }}"
          layerSelector:
            mediaType: "{{ mediaType }}"
            operation: "{{ operation }}"
          verify:
            provider: "{{ provider }}"
            verificationConfig: "{{ verificationConfig }}"
            matchOidcIdentity:
              - issuer: "{{ issuer }}"
                subject: "{{ subject }}"
          insecure: {{ insecure }}
          useWorkloadIdentity: {{ useWorkloadIdentity }}
          serviceAccountName: "{{ serviceAccountName }}"
          tlsConfig:
            clientCertificate: "{{ clientCertificate }}"
            privateKey: "{{ privateKey }}"
            caCertificate: "{{ caCertificate }}"
          localAuthRef: "{{ localAuthRef }}"
        kustomizations: "{{ kustomizations }}"
        configurationProtectedSettings: "{{ configurationProtectedSettings }}"
        statuses:
          - name: "{{ name }}"
            namespace: "{{ namespace }}"
            kind: "{{ kind }}"
            complianceState: "{{ complianceState }}"
            appliedBy:
              name: "{{ name }}"
              namespace: "{{ namespace }}"
            statusConditions: "{{ statusConditions }}"
            helmReleaseProperties:
              lastRevisionApplied: {{ lastRevisionApplied }}
              helmChartRef:
                name: "{{ name }}"
                namespace: "{{ namespace }}"
              failureCount: {{ failureCount }}
              installFailureCount: {{ installFailureCount }}
              upgradeFailureCount: {{ upgradeFailureCount }}
        repositoryPublicKey: "{{ repositoryPublicKey }}"
        sourceSyncedCommitId: "{{ sourceSyncedCommitId }}"
        sourceUpdatedAt: "{{ sourceUpdatedAt }}"
        statusUpdatedAt: "{{ statusUpdatedAt }}"
        waitForReconciliation: {{ waitForReconciliation }}
        reconciliationWaitDuration: "{{ reconciliationWaitDuration }}"
        complianceState: "{{ complianceState }}"
        provisioningState: "{{ provisioningState }}"
        errorMessage: "{{ errorMessage }}"
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

Update an existing Kubernetes Flux Configuration.

```sql
UPDATE azure.kubernetesconfiguration_fluxconfigurations.flux_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_rp = '{{ cluster_rp }}' --required
AND cluster_resource_name = '{{ cluster_resource_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND flux_configuration_name = '{{ flux_configuration_name }}' --required
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

Create a new Kubernetes Flux Configuration.

```sql
REPLACE azure.kubernetesconfiguration_fluxconfigurations.flux_configurations
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_rp = '{{ cluster_rp }}' --required
AND cluster_resource_name = '{{ cluster_resource_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND flux_configuration_name = '{{ flux_configuration_name }}' --required
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

This will delete the YAML file used to set up the Flux Configuration, thus stopping future sync from the source repo.

```sql
DELETE FROM azure.kubernetesconfiguration_fluxconfigurations.flux_configurations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_rp = '{{ cluster_rp }}' --required
AND cluster_resource_name = '{{ cluster_resource_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND flux_configuration_name = '{{ flux_configuration_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceDelete = '{{ forceDelete }}'
;
```
</TabItem>
</Tabs>
