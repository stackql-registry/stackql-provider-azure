--- 
title: virtual_machine_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_run_commands
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_run_commands</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="virtual_machine_run_commands" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_run_commands" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_virtual_machine"
    values={[
        { label: 'get_by_virtual_machine', value: 'get_by_virtual_machine' },
        { label: 'get', value: 'get' },
        { label: 'list_by_virtual_machine', value: 'list_by_virtual_machine' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_virtual_machine">

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
    <td><CopyableCode code="asyncExecution" /></td>
    <td><code>boolean</code></td>
    <td>Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.</td>
</tr>
<tr>
    <td><CopyableCode code="errorBlobManagedIdentity" /></td>
    <td><code>object</code></td>
    <td>User-assigned managed identity that has access to errorBlobUri storage blob. Use an empty object in case of system-assigned identity. Make sure managed identity has been given access to blob's container with 'Storage Blob Data Contributor' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer `https://aka.ms/ManagedIdentity `_ and `https://aka.ms/RunCommandManaged `_.</td>
</tr>
<tr>
    <td><CopyableCode code="errorBlobUri" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure storage blob where script error stream will be uploaded. Use a SAS URI with read, append, create, write access OR use managed identity to provide the VM access to the blob. Refer errorBlobManagedIdentity parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine run command instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="outputBlobManagedIdentity" /></td>
    <td><code>object</code></td>
    <td>User-assigned managed identity that has access to outputBlobUri storage blob. Use an empty object in case of system-assigned identity. Make sure managed identity has been given access to blob's container with 'Storage Blob Data Contributor' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer `https://aka.ms/ManagedIdentity `_ and `https://aka.ms/RunCommandManaged `_.</td>
</tr>
<tr>
    <td><CopyableCode code="outputBlobUri" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure storage blob where script output stream will be uploaded. Use a SAS URI with read, append, create, write access OR use managed identity to provide the VM access to the blob. Refer outputBlobManagedIdentity parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>The parameters used by the script.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedParameters" /></td>
    <td><code>array</code></td>
    <td>The parameters used by the script.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. If treatFailureAsDeploymentFailure set to true, any failure in the script will fail the deployment and ProvisioningState will be marked as Failed. If treatFailureAsDeploymentFailure set to false, ProvisioningState would only reflect whether the run command was run or not by the extensions platform, it would not indicate whether script failed in case of script failures. See instance view of run command in case of script failures to see executionMessage, output, error: `https://aka.ms/runcommandmanaged#get-execution-status-and-results `_.</td>
</tr>
<tr>
    <td><CopyableCode code="runAsPassword" /></td>
    <td><code>string</code></td>
    <td>Specifies the user account password on the VM when executing the run command.</td>
</tr>
<tr>
    <td><CopyableCode code="runAsUser" /></td>
    <td><code>string</code></td>
    <td>Specifies the user account on the VM when executing the run command.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The source of the run command script.</td>
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
    <td><CopyableCode code="timeoutInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The timeout in seconds to execute the run command.</td>
</tr>
<tr>
    <td><CopyableCode code="treatFailureAsDeploymentFailure" /></td>
    <td><code>boolean</code></td>
    <td>Optional. If set to true, any failure in the script will fail the deployment and ProvisioningState will be marked as Failed. If set to false, ProvisioningState would only reflect whether the run command was run or not by the extensions platform, it would not indicate whether script failed in case of script failures. See instance view of run command in case of script failures to see executionMessage, output, error: `https://aka.ms/runcommandmanaged#get-execution-status-and-results `_.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>The VM run command id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="$schema" /></td>
    <td><code>string</code></td>
    <td>The VM run command schema. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The VM run command description. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The VM run command label. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The Operating System type. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>The parameters used by the script.</td>
</tr>
<tr>
    <td><CopyableCode code="script" /></td>
    <td><code>array</code></td>
    <td>The script to be executed. Required.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_virtual_machine">

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
    <td><CopyableCode code="asyncExecution" /></td>
    <td><code>boolean</code></td>
    <td>Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.</td>
</tr>
<tr>
    <td><CopyableCode code="errorBlobManagedIdentity" /></td>
    <td><code>object</code></td>
    <td>User-assigned managed identity that has access to errorBlobUri storage blob. Use an empty object in case of system-assigned identity. Make sure managed identity has been given access to blob's container with 'Storage Blob Data Contributor' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer `https://aka.ms/ManagedIdentity `_ and `https://aka.ms/RunCommandManaged `_.</td>
</tr>
<tr>
    <td><CopyableCode code="errorBlobUri" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure storage blob where script error stream will be uploaded. Use a SAS URI with read, append, create, write access OR use managed identity to provide the VM access to the blob. Refer errorBlobManagedIdentity parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceView" /></td>
    <td><code>object</code></td>
    <td>The virtual machine run command instance view.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="outputBlobManagedIdentity" /></td>
    <td><code>object</code></td>
    <td>User-assigned managed identity that has access to outputBlobUri storage blob. Use an empty object in case of system-assigned identity. Make sure managed identity has been given access to blob's container with 'Storage Blob Data Contributor' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer `https://aka.ms/ManagedIdentity `_ and `https://aka.ms/RunCommandManaged `_.</td>
</tr>
<tr>
    <td><CopyableCode code="outputBlobUri" /></td>
    <td><code>string</code></td>
    <td>Specifies the Azure storage blob where script output stream will be uploaded. Use a SAS URI with read, append, create, write access OR use managed identity to provide the VM access to the blob. Refer outputBlobManagedIdentity parameter.</td>
</tr>
<tr>
    <td><CopyableCode code="parameters" /></td>
    <td><code>array</code></td>
    <td>The parameters used by the script.</td>
</tr>
<tr>
    <td><CopyableCode code="protectedParameters" /></td>
    <td><code>array</code></td>
    <td>The parameters used by the script.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state, which only appears in the response. If treatFailureAsDeploymentFailure set to true, any failure in the script will fail the deployment and ProvisioningState will be marked as Failed. If treatFailureAsDeploymentFailure set to false, ProvisioningState would only reflect whether the run command was run or not by the extensions platform, it would not indicate whether script failed in case of script failures. See instance view of run command in case of script failures to see executionMessage, output, error: `https://aka.ms/runcommandmanaged#get-execution-status-and-results `_.</td>
</tr>
<tr>
    <td><CopyableCode code="runAsPassword" /></td>
    <td><code>string</code></td>
    <td>Specifies the user account password on the VM when executing the run command.</td>
</tr>
<tr>
    <td><CopyableCode code="runAsUser" /></td>
    <td><code>string</code></td>
    <td>Specifies the user account on the VM when executing the run command.</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>The source of the run command script.</td>
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
    <td><CopyableCode code="timeoutInSeconds" /></td>
    <td><code>integer</code></td>
    <td>The timeout in seconds to execute the run command.</td>
</tr>
<tr>
    <td><CopyableCode code="treatFailureAsDeploymentFailure" /></td>
    <td><code>boolean</code></td>
    <td>Optional. If set to true, any failure in the script will fail the deployment and ProvisioningState will be marked as Failed. If set to false, ProvisioningState would only reflect whether the run command was run or not by the extensions platform, it would not indicate whether script failed in case of script failures. See instance view of run command in case of script failures to see executionMessage, output, error: `https://aka.ms/runcommandmanaged#get-execution-status-and-results `_.</td>
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
    <td>The VM run command id. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="$schema" /></td>
    <td><code>string</code></td>
    <td>The VM run command schema. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The VM run command description. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The VM run command label. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The Operating System type. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
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
    <td><a href="#get_by_virtual_machine"><CopyableCode code="get_by_virtual_machine" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-run_command_name"><code>run_command_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to get the run command.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-command_id"><code>command_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets specific run command for a subscription in a location.</td>
</tr>
<tr>
    <td><a href="#list_by_virtual_machine"><CopyableCode code="list_by_virtual_machine" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>The operation to get all run commands of a Virtual Machine.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all available run commands for a subscription in a location.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-run_command_name"><code>run_command_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update the run command.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-run_command_name"><code>run_command_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to update the run command.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-run_command_name"><code>run_command_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>The operation to create or update the run command.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-vm_name"><code>vm_name</code></a>, <a href="#parameter-run_command_name"><code>run_command_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>The operation to delete the run command.</td>
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
<tr id="parameter-command_id">
    <td><CopyableCode code="command_id" /></td>
    <td><code>string</code></td>
    <td>Specifies a commandId of predefined built-in script. Command IDs available for Linux are listed at `https://aka.ms/RunCommandManagedLinux#available-commands `_, Windows at `https://aka.ms/RunCommandManagedWindows#available-commands `_. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-run_command_name">
    <td><CopyableCode code="run_command_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VirtualMachineRunCommand. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-vm_name">
    <td><CopyableCode code="vm_name" /></td>
    <td><code>string</code></td>
    <td>The name of the VirtualMachine. Required.</td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The expand expression to apply on the operation. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_by_virtual_machine"
    values={[
        { label: 'get_by_virtual_machine', value: 'get_by_virtual_machine' },
        { label: 'get', value: 'get' },
        { label: 'list_by_virtual_machine', value: 'list_by_virtual_machine' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_by_virtual_machine">

The operation to get the run command.

```sql
SELECT
id,
name,
asyncExecution,
errorBlobManagedIdentity,
errorBlobUri,
instanceView,
location,
outputBlobManagedIdentity,
outputBlobUri,
parameters,
protectedParameters,
provisioningState,
runAsPassword,
runAsUser,
source,
systemData,
tags,
timeoutInSeconds,
treatFailureAsDeploymentFailure,
type
FROM azure.compute.virtual_machine_run_commands
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND run_command_name = '{{ run_command_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="get">

Gets specific run command for a subscription in a location.

```sql
SELECT
id,
$schema,
description,
label,
osType,
parameters,
script
FROM azure.compute.virtual_machine_run_commands
WHERE location = '{{ location }}' -- required
AND command_id = '{{ command_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_virtual_machine">

The operation to get all run commands of a Virtual Machine.

```sql
SELECT
id,
name,
asyncExecution,
errorBlobManagedIdentity,
errorBlobUri,
instanceView,
location,
outputBlobManagedIdentity,
outputBlobUri,
parameters,
protectedParameters,
provisioningState,
runAsPassword,
runAsUser,
source,
systemData,
tags,
timeoutInSeconds,
treatFailureAsDeploymentFailure,
type
FROM azure.compute.virtual_machine_run_commands
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND vm_name = '{{ vm_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Lists all available run commands for a subscription in a location.

```sql
SELECT
id,
$schema,
description,
label,
osType
FROM azure.compute.virtual_machine_run_commands
WHERE location = '{{ location }}' -- required
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

The operation to create or update the run command.

```sql
INSERT INTO azure.compute.virtual_machine_run_commands (
tags,
location,
properties,
resource_group_name,
vm_name,
run_command_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ vm_name }}',
'{{ run_command_name }}',
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
- name: virtual_machine_run_commands
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the virtual_machine_run_commands resource.
    - name: vm_name
      value: "{{ vm_name }}"
      description: Required parameter for the virtual_machine_run_commands resource.
    - name: run_command_name
      value: "{{ run_command_name }}"
      description: Required parameter for the virtual_machine_run_commands resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the virtual_machine_run_commands resource.
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
        Describes the properties of a Virtual Machine run command.
      value:
        source:
          script: "{{ script }}"
          scriptUri: "{{ scriptUri }}"
          commandId: "{{ commandId }}"
          scriptUriManagedIdentity:
            clientId: "{{ clientId }}"
            objectId: "{{ objectId }}"
          scriptShell: "{{ scriptShell }}"
          galleryScriptReferenceId: "{{ galleryScriptReferenceId }}"
        parameters:
          - name: "{{ name }}"
            value: "{{ value }}"
        protectedParameters:
          - name: "{{ name }}"
            value: "{{ value }}"
        asyncExecution: {{ asyncExecution }}
        runAsUser: "{{ runAsUser }}"
        runAsPassword: "{{ runAsPassword }}"
        timeoutInSeconds: {{ timeoutInSeconds }}
        outputBlobUri: "{{ outputBlobUri }}"
        errorBlobUri: "{{ errorBlobUri }}"
        outputBlobManagedIdentity:
          clientId: "{{ clientId }}"
          objectId: "{{ objectId }}"
        errorBlobManagedIdentity:
          clientId: "{{ clientId }}"
          objectId: "{{ objectId }}"
        provisioningState: "{{ provisioningState }}"
        instanceView:
          executionState: "{{ executionState }}"
          executionMessage: "{{ executionMessage }}"
          exitCode: {{ exitCode }}
          output: "{{ output }}"
          error: "{{ error }}"
          startTime: "{{ startTime }}"
          endTime: "{{ endTime }}"
          statuses:
            - code: "{{ code }}"
              level: "{{ level }}"
              displayStatus: "{{ displayStatus }}"
              message: "{{ message }}"
              time: "{{ time }}"
        treatFailureAsDeploymentFailure: {{ treatFailureAsDeploymentFailure }}
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

The operation to update the run command.

```sql
UPDATE azure.compute.virtual_machine_run_commands
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND run_command_name = '{{ run_command_name }}' --required
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

The operation to create or update the run command.

```sql
REPLACE azure.compute.virtual_machine_run_commands
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND run_command_name = '{{ run_command_name }}' --required
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

The operation to delete the run command.

```sql
DELETE FROM azure.compute.virtual_machine_run_commands
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND vm_name = '{{ vm_name }}' --required
AND run_command_name = '{{ run_command_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
