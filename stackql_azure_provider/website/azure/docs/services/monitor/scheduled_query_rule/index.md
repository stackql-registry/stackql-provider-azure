--- 
title: scheduled_query_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_query_rule
  - monitor
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

Creates, updates, deletes, gets or lists a <code>scheduled_query_rule</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="scheduled_query_rule" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.scheduled_query_rule" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_nsp"
    values={[
        { label: 'get_nsp', value: 'get_nsp' },
        { label: 'list_nsp', value: 'list_nsp' }
    ]}
>
<TabItem value="get_nsp">

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
    <td>:vartype profile: ~azure.mgmt.monitor.models.NetworkSecurityProfile</td>
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
    <td>:vartype resource_association: ~azure.mgmt.monitor.models.ResourceAssociation</td>
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
<TabItem value="list_nsp">

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
    <td>:vartype profile: ~azure.mgmt.monitor.models.NetworkSecurityProfile</td>
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
    <td>:vartype resource_association: ~azure.mgmt.monitor.models.ResourceAssociation</td>
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
    <td><a href="#get_nsp"><CopyableCode code="get_nsp" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-network_security_perimeter_configuration_name"><code>network_security_perimeter_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a network security perimeter configuration.</td>
</tr>
<tr>
    <td><a href="#list_nsp"><CopyableCode code="list_nsp" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of NSP configurations for specified scheduled query rule.</td>
</tr>
<tr>
    <td><a href="#reconcile_nsp"><CopyableCode code="reconcile_nsp" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-rule_name"><code>rule_name</code></a>, <a href="#parameter-network_security_perimeter_configuration_name"><code>network_security_perimeter_configuration_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reconcile network security perimeter configuration for ScheduledQueryRule resource.</td>
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
<tr id="parameter-rule_name">
    <td><CopyableCode code="rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the rule. Required.</td>
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
    defaultValue="get_nsp"
    values={[
        { label: 'get_nsp', value: 'get_nsp' },
        { label: 'list_nsp', value: 'list_nsp' }
    ]}
>
<TabItem value="get_nsp">

Gets a network security perimeter configuration.

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
FROM azure.monitor.scheduled_query_rule
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND network_security_perimeter_configuration_name = '{{ network_security_perimeter_configuration_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_nsp">

Gets a list of NSP configurations for specified scheduled query rule.

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
FROM azure.monitor.scheduled_query_rule
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND rule_name = '{{ rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reconcile_nsp"
    values={[
        { label: 'reconcile_nsp', value: 'reconcile_nsp' }
    ]}
>
<TabItem value="reconcile_nsp">

Reconcile network security perimeter configuration for ScheduledQueryRule resource.

```sql
EXEC azure.monitor.scheduled_query_rule.reconcile_nsp 
@resource_group_name='{{ resource_group_name }}' --required, 
@rule_name='{{ rule_name }}' --required, 
@network_security_perimeter_configuration_name='{{ network_security_perimeter_configuration_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
