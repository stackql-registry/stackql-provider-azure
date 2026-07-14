--- 
title: disaster_recovery_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - disaster_recovery_configs
  - service_bus
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

Creates, updates, deletes, gets or lists a <code>disaster_recovery_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="disaster_recovery_configs" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_bus.disaster_recovery_configs" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_keys">

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
    <td><CopyableCode code="aliasPrimaryConnectionString" /></td>
    <td><code>string</code></td>
    <td>Primary connection string of the alias if GEO DR is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="aliasSecondaryConnectionString" /></td>
    <td><code>string</code></td>
    <td>Secondary connection string of the alias if GEO DR is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="keyName" /></td>
    <td><code>string</code></td>
    <td>A string that describes the authorization rule.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryConnectionString" /></td>
    <td><code>string</code></td>
    <td>Primary connection string of the created namespace authorization rule.</td>
</tr>
<tr>
    <td><CopyableCode code="primaryKey" /></td>
    <td><code>string</code></td>
    <td>A base64-encoded 256-bit primary key for signing and validating the SAS token.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryConnectionString" /></td>
    <td><code>string</code></td>
    <td>Secondary connection string of the created namespace authorization rule.</td>
</tr>
<tr>
    <td><CopyableCode code="secondaryKey" /></td>
    <td><code>string</code></td>
    <td>A base64-encoded 256-bit primary key for signing and validating the SAS token.</td>
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
    <td><CopyableCode code="alternateName" /></td>
    <td><code>string</code></td>
    <td>Primary/Secondary eventhub namespace name, which is part of GEO DR pairing.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerNamespace" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing.</td>
</tr>
<tr>
    <td><CopyableCode code="pendingReplicationOperationsCount" /></td>
    <td><code>integer</code></td>
    <td>Number of entities pending to be replicated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Alias(Disaster Recovery configuration) - possible values 'Accepted' or 'Succeeded' or 'Failed'. Known values are: "Accepted", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>role of namespace in GEO DR - possible values 'Primary' or 'PrimaryNotReplicating' or 'Secondary'. Known values are: "Primary", "PrimaryNotReplicating", and "Secondary".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_name_availability">

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
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>The detailed info regarding the reason associated with the namespace.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Value indicating namespace is availability, true if the namespace is available; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason for unavailability of a namespace. Known values are: "None", "InvalidName", "SubscriptionIsDisabled", "NameInUse", "NameInLockdown", and "TooManyNamespaceInCurrentSubscription".</td>
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
    <td><CopyableCode code="alternateName" /></td>
    <td><code>string</code></td>
    <td>Primary/Secondary eventhub namespace name, which is part of GEO DR pairing.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerNamespace" /></td>
    <td><code>string</code></td>
    <td>ARM Id of the Primary/Secondary eventhub namespace name, which is part of GEO DR pairing.</td>
</tr>
<tr>
    <td><CopyableCode code="pendingReplicationOperationsCount" /></td>
    <td><code>integer</code></td>
    <td>Number of entities pending to be replicated.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the Alias(Disaster Recovery configuration) - possible values 'Accepted' or 'Succeeded' or 'Failed'. Known values are: "Accepted", "Succeeded", and "Failed".</td>
</tr>
<tr>
    <td><CopyableCode code="role" /></td>
    <td><code>string</code></td>
    <td>role of namespace in GEO DR - possible values 'Primary' or 'PrimaryNotReplicating' or 'Secondary'. Known values are: "Primary", "PrimaryNotReplicating", and "Secondary".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs".</td>
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
    <td><a href="#list_keys"><CopyableCode code="list_keys" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the primary and secondary connection strings for the namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639398.aspx</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves Alias(Disaster Recovery configuration) for primary or secondary namespace.</td>
</tr>
<tr>
    <td><a href="#check_name_availability"><CopyableCode code="check_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check the give namespace name availability.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all Alias(Disaster Recovery configurations).</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a new Alias(Disaster Recovery configuration).</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a new Alias(Disaster Recovery configuration).</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Alias(Disaster Recovery configuration).</td>
</tr>
<tr>
    <td><a href="#list_authorization_rules"><CopyableCode code="list_authorization_rules" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the authorization rules for a namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639376.aspx</td>
</tr>
<tr>
    <td><a href="#get_authorization_rule"><CopyableCode code="get_authorization_rule" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-authorization_rule_name"><code>authorization_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an authorization rule for a namespace by rule name. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639392.aspx</td>
</tr>
<tr>
    <td><a href="#break_pairing"><CopyableCode code="break_pairing" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This operation disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces.</td>
</tr>
<tr>
    <td><a href="#fail_over"><CopyableCode code="fail_over" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-namespace_name"><code>namespace_name</code></a>, <a href="#parameter-alias"><code>alias</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace.</td>
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
<tr id="parameter-alias">
    <td><CopyableCode code="alias" /></td>
    <td><code>string</code></td>
    <td>The Disaster Recovery configuration name. Required.</td>
</tr>
<tr id="parameter-authorization_rule_name">
    <td><CopyableCode code="authorization_rule_name" /></td>
    <td><code>string</code></td>
    <td>The authorization rule name. Required.</td>
</tr>
<tr id="parameter-namespace_name">
    <td><CopyableCode code="namespace_name" /></td>
    <td><code>string</code></td>
    <td>The namespace name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Resource group within the Azure subscription. Required.</td>
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
    defaultValue="list_keys"
    values={[
        { label: 'list_keys', value: 'list_keys' },
        { label: 'get', value: 'get' },
        { label: 'check_name_availability', value: 'check_name_availability' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_keys">

Gets the primary and secondary connection strings for the namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639398.aspx

```sql
SELECT
aliasPrimaryConnectionString,
aliasSecondaryConnectionString,
keyName,
primaryConnectionString,
primaryKey,
secondaryConnectionString,
secondaryKey
FROM azure.service_bus.disaster_recovery_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND alias = '{{ alias }}' -- required
AND authorization_rule_name = '{{ authorization_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Retrieves Alias(Disaster Recovery configuration) for primary or secondary namespace.

```sql
SELECT
id,
name,
alternateName,
location,
partnerNamespace,
pendingReplicationOperationsCount,
provisioningState,
role,
systemData,
type
FROM azure.service_bus.disaster_recovery_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND alias = '{{ alias }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_name_availability">

Check the give namespace name availability.

```sql
SELECT
message,
nameAvailable,
reason
FROM azure.service_bus.disaster_recovery_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all Alias(Disaster Recovery configurations).

```sql
SELECT
id,
name,
alternateName,
location,
partnerNamespace,
pendingReplicationOperationsCount,
provisioningState,
role,
systemData,
type
FROM azure.service_bus.disaster_recovery_configs
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND namespace_name = '{{ namespace_name }}' -- required
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

Creates or updates a new Alias(Disaster Recovery configuration).

```sql
INSERT INTO azure.service_bus.disaster_recovery_configs (
properties,
resource_group_name,
namespace_name,
alias,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ namespace_name }}',
'{{ alias }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: disaster_recovery_configs
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the disaster_recovery_configs resource.
    - name: namespace_name
      value: "{{ namespace_name }}"
      description: Required parameter for the disaster_recovery_configs resource.
    - name: alias
      value: "{{ alias }}"
      description: Required parameter for the disaster_recovery_configs resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the disaster_recovery_configs resource.
    - name: properties
      value:
        partnerNamespace: "{{ partnerNamespace }}"
        alternateName: "{{ alternateName }}"
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

Creates or updates a new Alias(Disaster Recovery configuration).

```sql
REPLACE azure.service_bus.disaster_recovery_configs
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND alias = '{{ alias }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
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

Deletes an Alias(Disaster Recovery configuration).

```sql
DELETE FROM azure.service_bus.disaster_recovery_configs
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND namespace_name = '{{ namespace_name }}' --required
AND alias = '{{ alias }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_authorization_rules"
    values={[
        { label: 'list_authorization_rules', value: 'list_authorization_rules' },
        { label: 'get_authorization_rule', value: 'get_authorization_rule' },
        { label: 'break_pairing', value: 'break_pairing' },
        { label: 'fail_over', value: 'fail_over' }
    ]}
>
<TabItem value="list_authorization_rules">

Gets the authorization rules for a namespace. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639376.aspx

```sql
EXEC azure.service_bus.disaster_recovery_configs.list_authorization_rules 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@alias='{{ alias }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_authorization_rule">

Gets an authorization rule for a namespace by rule name. .. seealso:: - https://msdn.microsoft.com/en-us/library/azure/mt639392.aspx

```sql
EXEC azure.service_bus.disaster_recovery_configs.get_authorization_rule 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@alias='{{ alias }}' --required, 
@authorization_rule_name='{{ authorization_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="break_pairing">

This operation disables the Disaster Recovery and stops replicating changes from primary to secondary namespaces.

```sql
EXEC azure.service_bus.disaster_recovery_configs.break_pairing 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@alias='{{ alias }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="fail_over">

Invokes GEO DR failover and reconfigure the alias to point to the secondary namespace.

```sql
EXEC azure.service_bus.disaster_recovery_configs.fail_over 
@resource_group_name='{{ resource_group_name }}' --required, 
@namespace_name='{{ namespace_name }}' --required, 
@alias='{{ alias }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"properties": "{{ properties }}"
}'
;
```
</TabItem>
</Tabs>
