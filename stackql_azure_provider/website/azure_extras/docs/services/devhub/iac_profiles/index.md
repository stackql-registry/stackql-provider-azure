--- 
title: iac_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - iac_profiles
  - devhub
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

Creates, updates, deletes, gets or lists an <code>iac_profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="iac_profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.devhub.iac_profiles" /></td></tr>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="githubProfile" /></td>
    <td><code>object</code></td>
    <td>GitHub Profile of a IacProfile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stages" /></td>
    <td><code>array</code></td>
    <td>:vartype stages: list[~azure.mgmt.devhub.models.StageProperties]</td>
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
    <td><CopyableCode code="templates" /></td>
    <td><code>array</code></td>
    <td>:vartype templates: list[~azure.mgmt.devhub.models.IacTemplateProperties]</td>
</tr>
<tr>
    <td><CopyableCode code="terraformProfile" /></td>
    <td><code>object</code></td>
    <td>Terraform Profile of a IacProfile.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="githubProfile" /></td>
    <td><code>object</code></td>
    <td>GitHub Profile of a IacProfile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stages" /></td>
    <td><code>array</code></td>
    <td>:vartype stages: list[~azure.mgmt.devhub.models.StageProperties]</td>
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
    <td><CopyableCode code="templates" /></td>
    <td><code>array</code></td>
    <td>:vartype templates: list[~azure.mgmt.devhub.models.IacTemplateProperties]</td>
</tr>
<tr>
    <td><CopyableCode code="terraformProfile" /></td>
    <td><code>object</code></td>
    <td>Terraform Profile of a IacProfile.</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="githubProfile" /></td>
    <td><code>object</code></td>
    <td>GitHub Profile of a IacProfile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="stages" /></td>
    <td><code>array</code></td>
    <td>:vartype stages: list[~azure.mgmt.devhub.models.StageProperties]</td>
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
    <td><CopyableCode code="templates" /></td>
    <td><code>array</code></td>
    <td>:vartype templates: list[~azure.mgmt.devhub.models.IacTemplateProperties]</td>
</tr>
<tr>
    <td><CopyableCode code="terraformProfile" /></td>
    <td><code>object</code></td>
    <td>Terraform Profile of a IacProfile.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iac_profile_name"><code>iac_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a IacProfile. Gets a IacProfile.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of iacProfiles within a resource group. Gets a list of iacProfiles within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of IacProfiles associated with the specified subscription. Gets a list of IacProfiles associated with the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iac_profile_name"><code>iac_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a IacProfile. Creates or updates a IacProfile.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iac_profile_name"><code>iac_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates tags on a IacProfile. Updates tags on a IacProfile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iac_profile_name"><code>iac_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a IacProfile. Creates or updates a IacProfile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iac_profile_name"><code>iac_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a IacProfile. Deletes a IacProfile.</td>
</tr>
<tr>
    <td><a href="#export"><CopyableCode code="export" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iac_profile_name"><code>iac_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Export a template. Export a template.</td>
</tr>
<tr>
    <td><a href="#scale"><CopyableCode code="scale" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iac_profile_name"><code>iac_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Scale by template. Scale by template.</td>
</tr>
<tr>
    <td><a href="#sync"><CopyableCode code="sync" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-iac_profile_name"><code>iac_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Sync template. Sync template.</td>
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
<tr id="parameter-iac_profile_name">
    <td><CopyableCode code="iac_profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the IacProfile. Required.</td>
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

Gets a IacProfile. Gets a IacProfile.

```sql
SELECT
id,
name,
etag,
githubProfile,
location,
stages,
systemData,
tags,
templates,
terraformProfile,
type
FROM azure_extras.devhub.iac_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND iac_profile_name = '{{ iac_profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets a list of iacProfiles within a resource group. Gets a list of iacProfiles within a resource group.

```sql
SELECT
id,
name,
etag,
githubProfile,
location,
stages,
systemData,
tags,
templates,
terraformProfile,
type
FROM azure_extras.devhub.iac_profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of IacProfiles associated with the specified subscription. Gets a list of IacProfiles associated with the specified subscription.

```sql
SELECT
id,
name,
etag,
githubProfile,
location,
stages,
systemData,
tags,
templates,
terraformProfile,
type
FROM azure_extras.devhub.iac_profiles
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

Creates or updates a IacProfile. Creates or updates a IacProfile.

```sql
INSERT INTO azure_extras.devhub.iac_profiles (
tags,
location,
properties,
resource_group_name,
iac_profile_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ iac_profile_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
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
- name: iac_profiles
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the iac_profiles resource.
    - name: iac_profile_name
      value: "{{ iac_profile_name }}"
      description: Required parameter for the iac_profiles resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the iac_profiles resource.
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
        Properties of a IacProfile.
      value:
        githubProfile:
          repositoryName: "{{ repositoryName }}"
          repositoryMainBranch: "{{ repositoryMainBranch }}"
          repositoryOwner: "{{ repositoryOwner }}"
          authStatus: "{{ authStatus }}"
          pullNumber: {{ pullNumber }}
          prStatus: "{{ prStatus }}"
          branchName: "{{ branchName }}"
        terraformProfile:
          storageAccountSubscription: "{{ storageAccountSubscription }}"
          storageAccountResourceGroup: "{{ storageAccountResourceGroup }}"
          storageAccountName: "{{ storageAccountName }}"
          storageContainerName: "{{ storageContainerName }}"
        stages:
          - stageName: "{{ stageName }}"
            dependencies: "{{ dependencies }}"
            gitEnvironment: "{{ gitEnvironment }}"
        templates:
          - templateName: "{{ templateName }}"
            sourceResourceId: "{{ sourceResourceId }}"
            instanceStage: "{{ instanceStage }}"
            instanceName: "{{ instanceName }}"
            templateDetails: "{{ templateDetails }}"
            quickStartTemplateType: "{{ quickStartTemplateType }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_tags"
    values={[
        { label: 'update_tags', value: 'update_tags' }
    ]}
>
<TabItem value="update_tags">

Updates tags on a IacProfile. Updates tags on a IacProfile.

```sql
UPDATE azure_extras.devhub.iac_profiles
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND iac_profile_name = '{{ iac_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
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

Creates or updates a IacProfile. Creates or updates a IacProfile.

```sql
REPLACE azure_extras.devhub.iac_profiles
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND iac_profile_name = '{{ iac_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
etag,
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

Deletes a IacProfile. Deletes a IacProfile.

```sql
DELETE FROM azure_extras.devhub.iac_profiles
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND iac_profile_name = '{{ iac_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="export"
    values={[
        { label: 'export', value: 'export' },
        { label: 'scale', value: 'scale' },
        { label: 'sync', value: 'sync' }
    ]}
>
<TabItem value="export">

Export a template. Export a template.

```sql
EXEC azure_extras.devhub.iac_profiles.export 
@resource_group_name='{{ resource_group_name }}' --required, 
@iac_profile_name='{{ iac_profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"templateName": "{{ templateName }}", 
"resourceGroupIds": "{{ resourceGroupIds }}", 
"siteId": "{{ siteId }}", 
"instanceName": "{{ instanceName }}", 
"instanceStage": "{{ instanceStage }}"
}'
;
```
</TabItem>
<TabItem value="scale">

Scale by template. Scale by template.

```sql
EXEC azure_extras.devhub.iac_profiles.scale 
@resource_group_name='{{ resource_group_name }}' --required, 
@iac_profile_name='{{ iac_profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"templateName": "{{ templateName }}", 
"scaleRequirement": "{{ scaleRequirement }}"
}'
;
```
</TabItem>
<TabItem value="sync">

Sync template. Sync template.

```sql
EXEC azure_extras.devhub.iac_profiles.sync 
@resource_group_name='{{ resource_group_name }}' --required, 
@iac_profile_name='{{ iac_profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
