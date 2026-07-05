--- 
title: security_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_settings
  - azurestackhci
  - azure_stack
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_stack resources using SQL
custom_edit_url: null
image: /img/stackql-azure_stack-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>security_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="security_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azurestackhci.security_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_clusters', value: 'list_by_clusters' }
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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="securedCoreComplianceAssignment" /></td>
    <td><code>string</code></td>
    <td>Secured Core Compliance Assignment. Known values are: "Audit" and "ApplyAndAutoCorrect". (Audit, ApplyAndAutoCorrect)</td>
</tr>
<tr>
    <td><CopyableCode code="securityComplianceStatus" /></td>
    <td><code>object</code></td>
    <td>Security Compliance Status.</td>
</tr>
<tr>
    <td><CopyableCode code="smbEncryptionForIntraClusterTrafficComplianceAssignment" /></td>
    <td><code>string</code></td>
    <td>SMB encryption for intra-cluster traffic Compliance Assignment. Known values are: "Audit" and "ApplyAndAutoCorrect". (Audit, ApplyAndAutoCorrect)</td>
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
    <td><CopyableCode code="wdacComplianceAssignment" /></td>
    <td><code>string</code></td>
    <td>WDAC Compliance Assignment. Known values are: "Audit" and "ApplyAndAutoCorrect". (Audit, ApplyAndAutoCorrect)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_clusters">

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
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The status of the last operation. Known values are: "NotSpecified", "Error", "Succeeded", "Failed", "Canceled", "Connected", "Disconnected", "Deleted", "Creating", "Updating", "Deleting", "Moving", "PartiallySucceeded", "PartiallyConnected", "InProgress", "Accepted", "Provisioning", and "DisableInProgress". (NotSpecified, Error, Succeeded, Failed, Canceled, Connected, Disconnected, Deleted, Creating, Updating, Deleting, Moving, PartiallySucceeded, PartiallyConnected, InProgress, Accepted, Provisioning, DisableInProgress)</td>
</tr>
<tr>
    <td><CopyableCode code="securedCoreComplianceAssignment" /></td>
    <td><code>string</code></td>
    <td>Secured Core Compliance Assignment. Known values are: "Audit" and "ApplyAndAutoCorrect". (Audit, ApplyAndAutoCorrect)</td>
</tr>
<tr>
    <td><CopyableCode code="securityComplianceStatus" /></td>
    <td><code>object</code></td>
    <td>Security Compliance Status.</td>
</tr>
<tr>
    <td><CopyableCode code="smbEncryptionForIntraClusterTrafficComplianceAssignment" /></td>
    <td><code>string</code></td>
    <td>SMB encryption for intra-cluster traffic Compliance Assignment. Known values are: "Audit" and "ApplyAndAutoCorrect". (Audit, ApplyAndAutoCorrect)</td>
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
    <td><CopyableCode code="wdacComplianceAssignment" /></td>
    <td><code>string</code></td>
    <td>WDAC Compliance Assignment. Known values are: "Audit" and "ApplyAndAutoCorrect". (Audit, ApplyAndAutoCorrect)</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-security_settings_name"><code>security_settings_name</code></a></td>
    <td></td>
    <td>Get a SecuritySetting.</td>
</tr>
<tr>
    <td><a href="#list_by_clusters"><CopyableCode code="list_by_clusters" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List SecuritySetting resources by Clusters.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-security_settings_name"><code>security_settings_name</code></a></td>
    <td></td>
    <td>Create a security setting.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-security_settings_name"><code>security_settings_name</code></a></td>
    <td></td>
    <td>Create a security setting.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-cluster_name"><code>cluster_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-security_settings_name"><code>security_settings_name</code></a></td>
    <td></td>
    <td>Delete a SecuritySetting.</td>
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
    <td>The name of the cluster. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-security_settings_name">
    <td><CopyableCode code="security_settings_name" /></td>
    <td><code>string</code></td>
    <td>Name of security setting. Default value is "default".</td>
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
        { label: 'list_by_clusters', value: 'list_by_clusters' }
    ]}
>
<TabItem value="get">

Get a SecuritySetting.

```sql
SELECT
id,
name,
provisioningState,
securedCoreComplianceAssignment,
securityComplianceStatus,
smbEncryptionForIntraClusterTrafficComplianceAssignment,
systemData,
type,
wdacComplianceAssignment
FROM azure_stack.azurestackhci.security_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND cluster_name = '{{ cluster_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND security_settings_name = '{{ security_settings_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_clusters">

List SecuritySetting resources by Clusters.

```sql
SELECT
id,
name,
provisioningState,
securedCoreComplianceAssignment,
securityComplianceStatus,
smbEncryptionForIntraClusterTrafficComplianceAssignment,
systemData,
type,
wdacComplianceAssignment
FROM azure_stack.azurestackhci.security_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
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

Create a security setting.

```sql
INSERT INTO azure_stack.azurestackhci.security_settings (
properties,
resource_group_name,
cluster_name,
subscription_id,
security_settings_name
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ cluster_name }}',
'{{ subscription_id }}',
'{{ security_settings_name }}'
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
- name: security_settings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the security_settings resource.
    - name: cluster_name
      value: "{{ cluster_name }}"
      description: Required parameter for the security_settings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the security_settings resource.
    - name: security_settings_name
      value: "{{ security_settings_name }}"
      description: Required parameter for the security_settings resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        securedCoreComplianceAssignment: "{{ securedCoreComplianceAssignment }}"
        wdacComplianceAssignment: "{{ wdacComplianceAssignment }}"
        smbEncryptionForIntraClusterTrafficComplianceAssignment: "{{ smbEncryptionForIntraClusterTrafficComplianceAssignment }}"
        securityComplianceStatus:
          securedCoreCompliance: "{{ securedCoreCompliance }}"
          wdacCompliance: "{{ wdacCompliance }}"
          dataAtRestEncrypted: "{{ dataAtRestEncrypted }}"
          dataInTransitProtected: "{{ dataInTransitProtected }}"
          lastUpdated: "{{ lastUpdated }}"
        provisioningState: "{{ provisioningState }}"
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

Create a security setting.

```sql
REPLACE azure_stack.azurestackhci.security_settings
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND security_settings_name = '{{ security_settings_name }}' --required
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

Delete a SecuritySetting.

```sql
DELETE FROM azure_stack.azurestackhci.security_settings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND cluster_name = '{{ cluster_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND security_settings_name = '{{ security_settings_name }}' --required
;
```
</TabItem>
</Tabs>
