--- 
title: network_security_perimeter
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter
  - batch
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeter</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_security_perimeter" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.network_security_perimeter" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_configuration"
    values={[
        { label: 'get_configuration', value: 'get_configuration' },
        { label: 'list_configurations', value: 'list_configurations' }
    ]}
>
<TabItem value="get_configuration">

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
    <td><CopyableCode code="networkSecurityPerimeter" /></td>
    <td><code>object</code></td>
    <td>Information about a network security perimeter (NSP).</td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td>:vartype profile: ~azure.mgmt.batch.models.NetworkSecurityProfile</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>List of provisioning issues, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", "Failed", and "Canceled". (Succeeded, Creating, Updating, Deleting, Accepted, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAssociation" /></td>
    <td><code>object</code></td>
    <td>:vartype resource_association: ~azure.mgmt.batch.models.ResourceAssociation</td>
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
</tbody>
</table>
</TabItem>
<TabItem value="list_configurations">

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
    <td><CopyableCode code="networkSecurityPerimeter" /></td>
    <td><code>object</code></td>
    <td>Information about a network security perimeter (NSP).</td>
</tr>
<tr>
    <td><CopyableCode code="profile" /></td>
    <td><code>object</code></td>
    <td>:vartype profile: ~azure.mgmt.batch.models.NetworkSecurityProfile</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningIssues" /></td>
    <td><code>array</code></td>
    <td>List of provisioning issues, if any.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", "Failed", and "Canceled". (Succeeded, Creating, Updating, Deleting, Accepted, Failed, Canceled)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceAssociation" /></td>
    <td><code>object</code></td>
    <td>:vartype resource_association: ~azure.mgmt.batch.models.ResourceAssociation</td>
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
    <td><a href="#get_configuration"><CopyableCode code="get_configuration" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-network_security_perimeter_configuration_name"><code>network_security_perimeter_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets information about the specified NSP configuration.</td>
</tr>
<tr>
    <td><a href="#list_configurations"><CopyableCode code="list_configurations" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the NSP configurations in the specified account.</td>
</tr>
<tr>
    <td><a href="#reconcile_configuration"><CopyableCode code="reconcile_configuration" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-network_security_perimeter_configuration_name"><code>network_security_perimeter_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reconciles the specified NSP configuration.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>A name for the Batch account which must be unique within the region. Batch account names must be between 3 and 24 characters in length and must use only numbers and lowercase letters. This name is used as part of the DNS name that is used to access the Batch service in the region in which the account is created. For example: `http://accountname.region.batch.azure.com/ `_. Required.</td>
</tr>
<tr id="parameter-network_security_perimeter_configuration_name">
    <td><CopyableCode code="network_security_perimeter_configuration_name" /></td>
    <td><code>string</code></td>
    <td>The name for a network security perimeter configuration. Required.</td>
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
    defaultValue="get_configuration"
    values={[
        { label: 'get_configuration', value: 'get_configuration' },
        { label: 'list_configurations', value: 'list_configurations' }
    ]}
>
<TabItem value="get_configuration">

Gets information about the specified NSP configuration.

```sql
SELECT
id,
name,
networkSecurityPerimeter,
profile,
provisioningIssues,
provisioningState,
resourceAssociation,
systemData,
type
FROM azure.batch.network_security_perimeter
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND network_security_perimeter_configuration_name = '{{ network_security_perimeter_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_configurations">

Lists all of the NSP configurations in the specified account.

```sql
SELECT
id,
name,
networkSecurityPerimeter,
profile,
provisioningIssues,
provisioningState,
resourceAssociation,
systemData,
type
FROM azure.batch.network_security_perimeter
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reconcile_configuration"
    values={[
        { label: 'reconcile_configuration', value: 'reconcile_configuration' }
    ]}
>
<TabItem value="reconcile_configuration">

Reconciles the specified NSP configuration.

```sql
EXEC azure.batch.network_security_perimeter.reconcile_configuration 
@resource_group_name='{{ resource_group_name }}' --required, 
@account_name='{{ account_name }}' --required, 
@network_security_perimeter_configuration_name='{{ network_security_perimeter_configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
