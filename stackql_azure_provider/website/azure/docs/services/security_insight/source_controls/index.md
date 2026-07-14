--- 
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - security_insight
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

Creates, updates, deletes, gets or lists a <code>source_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="source_controls" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_insight.source_controls" /></td></tr>
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
    <td><CopyableCode code="contentTypes" /></td>
    <td><code>array</code></td>
    <td>Array of source control content types. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the source control.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the source control. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastDeploymentInfo" /></td>
    <td><code>object</code></td>
    <td>Information regarding the latest deployment for the source control.</td>
</tr>
<tr>
    <td><CopyableCode code="pullRequest" /></td>
    <td><code>object</code></td>
    <td>Information regarding the pull request of the source control.</td>
</tr>
<tr>
    <td><CopyableCode code="repoType" /></td>
    <td><code>string</code></td>
    <td>The repository type of the source control. Required. Known values are: "Github" and "AzureDevOps". (Github, AzureDevOps)</td>
</tr>
<tr>
    <td><CopyableCode code="repository" /></td>
    <td><code>object</code></td>
    <td>Repository metadata. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryAccess" /></td>
    <td><code>object</code></td>
    <td>Repository access credentials. This is write-only object and it never returns back to a user.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryResourceInfo" /></td>
    <td><code>object</code></td>
    <td>Information regarding the resources created in user's repository.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipal" /></td>
    <td><code>object</code></td>
    <td>Service principal metadata.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version number associated with the source control. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="workloadIdentityFederation" /></td>
    <td><code>object</code></td>
    <td>Workload Identity metadata.</td>
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
    <td><CopyableCode code="contentTypes" /></td>
    <td><code>array</code></td>
    <td>Array of source control content types. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>A description of the source control.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the source control. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastDeploymentInfo" /></td>
    <td><code>object</code></td>
    <td>Information regarding the latest deployment for the source control.</td>
</tr>
<tr>
    <td><CopyableCode code="pullRequest" /></td>
    <td><code>object</code></td>
    <td>Information regarding the pull request of the source control.</td>
</tr>
<tr>
    <td><CopyableCode code="repoType" /></td>
    <td><code>string</code></td>
    <td>The repository type of the source control. Required. Known values are: "Github" and "AzureDevOps". (Github, AzureDevOps)</td>
</tr>
<tr>
    <td><CopyableCode code="repository" /></td>
    <td><code>object</code></td>
    <td>Repository metadata. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryAccess" /></td>
    <td><code>object</code></td>
    <td>Repository access credentials. This is write-only object and it never returns back to a user.</td>
</tr>
<tr>
    <td><CopyableCode code="repositoryResourceInfo" /></td>
    <td><code>object</code></td>
    <td>Information regarding the resources created in user's repository.</td>
</tr>
<tr>
    <td><CopyableCode code="servicePrincipal" /></td>
    <td><code>object</code></td>
    <td>Service principal metadata.</td>
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
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version number associated with the source control. Known values are: "V1" and "V2". (V1, V2)</td>
</tr>
<tr>
    <td><CopyableCode code="workloadIdentityFederation" /></td>
    <td><code>object</code></td>
    <td>Workload Identity metadata.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-source_control_id"><code>source_control_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a source control byt its identifier.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all source controls, without source control items.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-source_control_id"><code>source_control_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates a source control.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-source_control_id"><code>source_control_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a source control.</td>
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
<tr id="parameter-source_control_id">
    <td><CopyableCode code="source_control_id" /></td>
    <td><code>string</code></td>
    <td>Source control Id. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the monitor workspace. Required.</td>
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

Gets a source control byt its identifier.

```sql
SELECT
id,
name,
contentTypes,
description,
displayName,
etag,
lastDeploymentInfo,
pullRequest,
repoType,
repository,
repositoryAccess,
repositoryResourceInfo,
servicePrincipal,
systemData,
type,
version,
workloadIdentityFederation
FROM azure.security_insight.source_controls
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND source_control_id = '{{ source_control_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all source controls, without source control items.

```sql
SELECT
id,
name,
contentTypes,
description,
displayName,
etag,
lastDeploymentInfo,
pullRequest,
repoType,
repository,
repositoryAccess,
repositoryResourceInfo,
servicePrincipal,
systemData,
type,
version,
workloadIdentityFederation
FROM azure.security_insight.source_controls
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
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

Creates a source control.

```sql
INSERT INTO azure.security_insight.source_controls (
properties,
etag,
resource_group_name,
workspace_name,
source_control_id,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ etag }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ source_control_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: source_controls
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the source_controls resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the source_controls resource.
    - name: source_control_id
      value: "{{ source_control_id }}"
      description: Required parameter for the source_controls resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the source_controls resource.
    - name: properties
      description: |
        source control properties. Required.
      value:
        id: "{{ id }}"
        version: "{{ version }}"
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        repoType: "{{ repoType }}"
        contentTypes:
          - "{{ contentTypes }}"
        repository:
          url: "{{ url }}"
          branch: "{{ branch }}"
          displayUrl: "{{ displayUrl }}"
          deploymentLogsUrl: "{{ deploymentLogsUrl }}"
        servicePrincipal:
          id: "{{ id }}"
          tenantId: "{{ tenantId }}"
          appId: "{{ appId }}"
          credentialsExpireOn: "{{ credentialsExpireOn }}"
        workloadIdentityFederation:
          id: "{{ id }}"
          tenantId: "{{ tenantId }}"
          appId: "{{ appId }}"
          subject: "{{ subject }}"
          issuer: "{{ issuer }}"
        repositoryAccess:
          kind: "{{ kind }}"
          code: "{{ code }}"
          state: "{{ state }}"
          clientId: "{{ clientId }}"
          token: "{{ token }}"
          installationId: "{{ installationId }}"
        repositoryResourceInfo:
          webhook:
            webhookId: "{{ webhookId }}"
            webhookUrl: "{{ webhookUrl }}"
            webhookSecretUpdateTime: "{{ webhookSecretUpdateTime }}"
            rotateWebhookSecret: {{ rotateWebhookSecret }}
          gitHubResourceInfo:
            appInstallationId: "{{ appInstallationId }}"
          azureDevOpsResourceInfo:
            pipelineId: "{{ pipelineId }}"
            serviceConnectionId: "{{ serviceConnectionId }}"
        lastDeploymentInfo:
          deploymentFetchStatus: "{{ deploymentFetchStatus }}"
          deployment:
            deploymentId: "{{ deploymentId }}"
            deploymentState: "{{ deploymentState }}"
            deploymentResult: "{{ deploymentResult }}"
            deploymentTime: "{{ deploymentTime }}"
            deploymentLogsUrl: "{{ deploymentLogsUrl }}"
          message: "{{ message }}"
        pullRequest:
          url: "{{ url }}"
          state: "{{ state }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
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

Delete a source control.

```sql
DELETE FROM azure.security_insight.source_controls
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND source_control_id = '{{ source_control_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
