--- 
title: gallery_in_vm_access_control_profile_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_in_vm_access_control_profile_versions
  - compute
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

Creates, updates, deletes, gets or lists a <code>gallery_in_vm_access_control_profile_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="gallery_in_vm_access_control_profile_versions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.gallery_in_vm_access_control_profile_versions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_gallery_in_vm_access_control_profile', value: 'list_by_gallery_in_vm_access_control_profile' }
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
    <td><CopyableCode code="defaultAccess" /></td>
    <td><code>string</code></td>
    <td>This property allows you to specify if the requests will be allowed to access the host endpoints. Possible values are: 'Allow', 'Deny'. Required. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="excludeFromLatest" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, Virtual Machines deployed from the latest version of the Resource Profile won't use this Profile version.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>This property allows you to specify whether the access control rules are in Audit mode, in Enforce mode or Disabled. Possible values are: 'Audit', 'Enforce' or 'Disabled'. Required. Known values are: "Audit", "Enforce", and "Disabled". (Audit, Enforce, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating". (Creating, Updating, Failed, Succeeded, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="publishedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp for when the Resource Profile Version is published.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationStatus" /></td>
    <td><code>object</code></td>
    <td>This is the replication status of the gallery image version.</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>object</code></td>
    <td>This is the Access Control Rules specification for an inVMAccessControlProfile version.</td>
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
    <td><CopyableCode code="targetLocations" /></td>
    <td><code>array</code></td>
    <td>The target regions where the Resource Profile version is going to be replicated to. This property is updatable.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_gallery_in_vm_access_control_profile">

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
    <td><CopyableCode code="defaultAccess" /></td>
    <td><code>string</code></td>
    <td>This property allows you to specify if the requests will be allowed to access the host endpoints. Possible values are: 'Allow', 'Deny'. Required. Known values are: "Allow" and "Deny". (Allow, Deny)</td>
</tr>
<tr>
    <td><CopyableCode code="excludeFromLatest" /></td>
    <td><code>boolean</code></td>
    <td>If set to true, Virtual Machines deployed from the latest version of the Resource Profile won't use this Profile version.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="mode" /></td>
    <td><code>string</code></td>
    <td>This property allows you to specify whether the access control rules are in Audit mode, in Enforce mode or Disabled. Possible values are: 'Audit', 'Enforce' or 'Disabled'. Required. Known values are: "Audit", "Enforce", and "Disabled". (Audit, Enforce, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. Known values are: "Creating", "Updating", "Failed", "Succeeded", "Deleting", and "Migrating". (Creating, Updating, Failed, Succeeded, Deleting, Migrating)</td>
</tr>
<tr>
    <td><CopyableCode code="publishedDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The timestamp for when the Resource Profile Version is published.</td>
</tr>
<tr>
    <td><CopyableCode code="replicationStatus" /></td>
    <td><code>object</code></td>
    <td>This is the replication status of the gallery image version.</td>
</tr>
<tr>
    <td><CopyableCode code="rules" /></td>
    <td><code>object</code></td>
    <td>This is the Access Control Rules specification for an inVMAccessControlProfile version.</td>
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
    <td><CopyableCode code="targetLocations" /></td>
    <td><code>array</code></td>
    <td>The target regions where the Resource Profile version is going to be replicated to. This property is updatable.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-in_vm_access_control_profile_name"><code>in_vm_access_control_profile_name</code></a>, <a href="#parameter-in_vm_access_control_profile_version_name"><code>in_vm_access_control_profile_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves information about a gallery inVMAccessControlProfile version.</td>
</tr>
<tr>
    <td><a href="#list_by_gallery_in_vm_access_control_profile"><CopyableCode code="list_by_gallery_in_vm_access_control_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-in_vm_access_control_profile_name"><code>in_vm_access_control_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List gallery inVMAccessControlProfile versions in a gallery inVMAccessControlProfile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-in_vm_access_control_profile_name"><code>in_vm_access_control_profile_name</code></a>, <a href="#parameter-in_vm_access_control_profile_version_name"><code>in_vm_access_control_profile_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a gallery inVMAccessControlProfile version.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-in_vm_access_control_profile_name"><code>in_vm_access_control_profile_name</code></a>, <a href="#parameter-in_vm_access_control_profile_version_name"><code>in_vm_access_control_profile_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a gallery inVMAccessControlProfile version.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-in_vm_access_control_profile_name"><code>in_vm_access_control_profile_name</code></a>, <a href="#parameter-in_vm_access_control_profile_version_name"><code>in_vm_access_control_profile_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Create or update a gallery inVMAccessControlProfile version.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-gallery_name"><code>gallery_name</code></a>, <a href="#parameter-in_vm_access_control_profile_name"><code>in_vm_access_control_profile_name</code></a>, <a href="#parameter-in_vm_access_control_profile_version_name"><code>in_vm_access_control_profile_version_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a gallery inVMAccessControlProfile version.</td>
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
<tr id="parameter-gallery_name">
    <td><CopyableCode code="gallery_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Shared Image Gallery. Required.</td>
</tr>
<tr id="parameter-in_vm_access_control_profile_name">
    <td><CopyableCode code="in_vm_access_control_profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the gallery inVMAccessControlProfile to be retrieved. Required.</td>
</tr>
<tr id="parameter-in_vm_access_control_profile_version_name">
    <td><CopyableCode code="in_vm_access_control_profile_version_name" /></td>
    <td><code>string</code></td>
    <td>The name of the gallery inVMAccessControlProfile version to be retrieved. Required.</td>
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
        { label: 'list_by_gallery_in_vm_access_control_profile', value: 'list_by_gallery_in_vm_access_control_profile' }
    ]}
>
<TabItem value="get">

Retrieves information about a gallery inVMAccessControlProfile version.

```sql
SELECT
id,
name,
defaultAccess,
excludeFromLatest,
location,
mode,
provisioningState,
publishedDate,
replicationStatus,
rules,
systemData,
tags,
targetLocations,
type
FROM azure.compute.gallery_in_vm_access_control_profile_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
AND in_vm_access_control_profile_name = '{{ in_vm_access_control_profile_name }}' -- required
AND in_vm_access_control_profile_version_name = '{{ in_vm_access_control_profile_version_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_gallery_in_vm_access_control_profile">

List gallery inVMAccessControlProfile versions in a gallery inVMAccessControlProfile.

```sql
SELECT
id,
name,
defaultAccess,
excludeFromLatest,
location,
mode,
provisioningState,
publishedDate,
replicationStatus,
rules,
systemData,
tags,
targetLocations,
type
FROM azure.compute.gallery_in_vm_access_control_profile_versions
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND gallery_name = '{{ gallery_name }}' -- required
AND in_vm_access_control_profile_name = '{{ in_vm_access_control_profile_name }}' -- required
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

Create or update a gallery inVMAccessControlProfile version.

```sql
INSERT INTO azure.compute.gallery_in_vm_access_control_profile_versions (
tags,
location,
properties,
resource_group_name,
gallery_name,
in_vm_access_control_profile_name,
in_vm_access_control_profile_version_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ gallery_name }}',
'{{ in_vm_access_control_profile_name }}',
'{{ in_vm_access_control_profile_version_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
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
- name: gallery_in_vm_access_control_profile_versions
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the gallery_in_vm_access_control_profile_versions resource.
    - name: gallery_name
      value: "{{ gallery_name }}"
      description: Required parameter for the gallery_in_vm_access_control_profile_versions resource.
    - name: in_vm_access_control_profile_name
      value: "{{ in_vm_access_control_profile_name }}"
      description: Required parameter for the gallery_in_vm_access_control_profile_versions resource.
    - name: in_vm_access_control_profile_version_name
      value: "{{ in_vm_access_control_profile_version_name }}"
      description: Required parameter for the gallery_in_vm_access_control_profile_versions resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the gallery_in_vm_access_control_profile_versions resource.
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
        Describes the properties of an inVMAccessControlProfile version.
      value:
        targetLocations:
          - name: "{{ name }}"
            regionalReplicaCount: {{ regionalReplicaCount }}
            storageAccountType: "{{ storageAccountType }}"
            encryption:
              osDiskImage:
                diskEncryptionSetId: "{{ diskEncryptionSetId }}"
                securityProfile:
                  confidentialVMEncryptionType: "{{ confidentialVMEncryptionType }}"
                  secureVMDiskEncryptionSetId: "{{ secureVMDiskEncryptionSetId }}"
              dataDiskImages:
                - diskEncryptionSetId: "{{ diskEncryptionSetId }}"
                  lun: {{ lun }}
            excludeFromLatest: {{ excludeFromLatest }}
            additionalReplicaSets: "{{ additionalReplicaSets }}"
        excludeFromLatest: {{ excludeFromLatest }}
        publishedDate: "{{ publishedDate }}"
        provisioningState: "{{ provisioningState }}"
        replicationStatus:
          aggregatedState: "{{ aggregatedState }}"
          summary:
            - region: "{{ region }}"
              state: "{{ state }}"
              details: "{{ details }}"
              progress: {{ progress }}
        mode: "{{ mode }}"
        defaultAccess: "{{ defaultAccess }}"
        rules:
          privileges:
            - name: "{{ name }}"
              path: "{{ path }}"
              queryParameters: "{{ queryParameters }}"
          roles:
            - name: "{{ name }}"
              privileges: "{{ privileges }}"
          identities:
            - name: "{{ name }}"
              userName: "{{ userName }}"
              groupName: "{{ groupName }}"
              exePath: "{{ exePath }}"
              processName: "{{ processName }}"
          roleAssignments:
            - role: "{{ role }}"
              identities: "{{ identities }}"
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

Update a gallery inVMAccessControlProfile version.

```sql
UPDATE azure.compute.gallery_in_vm_access_control_profile_versions
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND gallery_name = '{{ gallery_name }}' --required
AND in_vm_access_control_profile_name = '{{ in_vm_access_control_profile_name }}' --required
AND in_vm_access_control_profile_version_name = '{{ in_vm_access_control_profile_version_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Create or update a gallery inVMAccessControlProfile version.

```sql
REPLACE azure.compute.gallery_in_vm_access_control_profile_versions
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND gallery_name = '{{ gallery_name }}' --required
AND in_vm_access_control_profile_name = '{{ in_vm_access_control_profile_name }}' --required
AND in_vm_access_control_profile_version_name = '{{ in_vm_access_control_profile_version_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
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

Delete a gallery inVMAccessControlProfile version.

```sql
DELETE FROM azure.compute.gallery_in_vm_access_control_profile_versions
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND gallery_name = '{{ gallery_name }}' --required
AND in_vm_access_control_profile_name = '{{ in_vm_access_control_profile_name }}' --required
AND in_vm_access_control_profile_version_name = '{{ in_vm_access_control_profile_version_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
