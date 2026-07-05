--- 
title: network_security_perimeter_access_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_access_rules
  - network
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

Creates, updates, deletes, gets or lists a <code>network_security_perimeter_access_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="network_security_perimeter_access_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.network_security_perimeter_access_rules" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefixes" /></td>
    <td><code>array</code></td>
    <td>Inbound address prefixes (IPv4/IPv6).</td>
</tr>
<tr>
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Direction that specifies whether the access rules is inbound/outbound. Known values are: "Inbound" and "Outbound". (Inbound, Outbound)</td>
</tr>
<tr>
    <td><CopyableCode code="emailAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound rules in email address format. This access rule type is currently unavailable for use.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainNames" /></td>
    <td><code>array</code></td>
    <td>Outbound rules in fully qualified domain name format.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityPerimeters" /></td>
    <td><code>array</code></td>
    <td>Rule specified by the perimeter id.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumbers" /></td>
    <td><code>array</code></td>
    <td>Outbound rules in phone number format. This access rule type is currently unavailable for use.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the scope assignment resource. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", and "Failed". (Succeeded, Creating, Updating, Deleting, Accepted, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTags" /></td>
    <td><code>array</code></td>
    <td>Inbound rules of type service tag. This access rule type is currently unavailable for use.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptions" /></td>
    <td><code>array</code></td>
    <td>List of subscription ids.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addressPrefixes" /></td>
    <td><code>array</code></td>
    <td>Inbound address prefixes (IPv4/IPv6).</td>
</tr>
<tr>
    <td><CopyableCode code="direction" /></td>
    <td><code>string</code></td>
    <td>Direction that specifies whether the access rules is inbound/outbound. Known values are: "Inbound" and "Outbound". (Inbound, Outbound)</td>
</tr>
<tr>
    <td><CopyableCode code="emailAddresses" /></td>
    <td><code>array</code></td>
    <td>Outbound rules in email address format. This access rule type is currently unavailable for use.</td>
</tr>
<tr>
    <td><CopyableCode code="fullyQualifiedDomainNames" /></td>
    <td><code>array</code></td>
    <td>Outbound rules in fully qualified domain name format.</td>
</tr>
<tr>
    <td><CopyableCode code="networkSecurityPerimeters" /></td>
    <td><code>array</code></td>
    <td>Rule specified by the perimeter id.</td>
</tr>
<tr>
    <td><CopyableCode code="phoneNumbers" /></td>
    <td><code>array</code></td>
    <td>Outbound rules in phone number format. This access rule type is currently unavailable for use.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the scope assignment resource. Known values are: "Succeeded", "Creating", "Updating", "Deleting", "Accepted", and "Failed". (Succeeded, Creating, Updating, Deleting, Accepted, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="serviceTags" /></td>
    <td><code>array</code></td>
    <td>Inbound rules of type service tag. This access rule type is currently unavailable for use.</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptions" /></td>
    <td><code>array</code></td>
    <td>List of subscription ids.</td>
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
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-access_rule_name"><code>access_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specified NSP access rule by name.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Lists the NSP access rules in the specified NSP profile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-access_rule_name"><code>access_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a network access rule.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-access_rule_name"><code>access_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a network access rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-access_rule_name"><code>access_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an NSP access rule.</td>
</tr>
<tr>
    <td><a href="#reconcile"><CopyableCode code="reconcile" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-network_security_perimeter_name"><code>network_security_perimeter_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-access_rule_name"><code>access_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Reconcile NSP access rules.</td>
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
<tr id="parameter-access_rule_name">
    <td><CopyableCode code="access_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NSP access rule. Required.</td>
</tr>
<tr id="parameter-network_security_perimeter_name">
    <td><CopyableCode code="network_security_perimeter_name" /></td>
    <td><code>string</code></td>
    <td>The name of the network security perimeter. Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the NSP profile. Required.</td>
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
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>SkipToken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>An optional query parameter which specifies the maximum number of records to be returned by the server. Default value is None.</td>
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

Gets the specified NSP access rule by name.

```sql
SELECT
id,
name,
addressPrefixes,
direction,
emailAddresses,
fullyQualifiedDomainNames,
networkSecurityPerimeters,
phoneNumbers,
provisioningState,
serviceTags,
subscriptions,
systemData,
type
FROM azure.network.network_security_perimeter_access_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND access_rule_name = '{{ access_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the NSP access rules in the specified NSP profile.

```sql
SELECT
id,
name,
addressPrefixes,
direction,
emailAddresses,
fullyQualifiedDomainNames,
networkSecurityPerimeters,
phoneNumbers,
provisioningState,
serviceTags,
subscriptions,
systemData,
type
FROM azure.network.network_security_perimeter_access_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
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

Creates or updates a network access rule.

```sql
INSERT INTO azure.network.network_security_perimeter_access_rules (
properties,
resource_group_name,
network_security_perimeter_name,
profile_name,
access_rule_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ network_security_perimeter_name }}',
'{{ profile_name }}',
'{{ access_rule_name }}',
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
- name: network_security_perimeter_access_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the network_security_perimeter_access_rules resource.
    - name: network_security_perimeter_name
      value: "{{ network_security_perimeter_name }}"
      description: Required parameter for the network_security_perimeter_access_rules resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the network_security_perimeter_access_rules resource.
    - name: access_rule_name
      value: "{{ access_rule_name }}"
      description: Required parameter for the network_security_perimeter_access_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the network_security_perimeter_access_rules resource.
    - name: properties
      description: |
        Properties of the NSP access rule.
      value:
        provisioningState: "{{ provisioningState }}"
        direction: "{{ direction }}"
        addressPrefixes:
          - "{{ addressPrefixes }}"
        fullyQualifiedDomainNames:
          - "{{ fullyQualifiedDomainNames }}"
        subscriptions:
          - id: "{{ id }}"
        networkSecurityPerimeters:
          - id: "{{ id }}"
            perimeterGuid: "{{ perimeterGuid }}"
            location: "{{ location }}"
        emailAddresses:
          - "{{ emailAddresses }}"
        phoneNumbers:
          - "{{ phoneNumbers }}"
        serviceTags:
          - "{{ serviceTags }}"
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

Creates or updates a network access rule.

```sql
REPLACE azure.network.network_security_perimeter_access_rules
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND access_rule_name = '{{ access_rule_name }}' --required
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

Deletes an NSP access rule.

```sql
DELETE FROM azure.network.network_security_perimeter_access_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND network_security_perimeter_name = '{{ network_security_perimeter_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND access_rule_name = '{{ access_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="reconcile"
    values={[
        { label: 'reconcile', value: 'reconcile' }
    ]}
>
<TabItem value="reconcile">

Reconcile NSP access rules.

```sql
EXEC azure.network.network_security_perimeter_access_rules.reconcile 
@resource_group_name='{{ resource_group_name }}' --required, 
@network_security_perimeter_name='{{ network_security_perimeter_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@access_rule_name='{{ access_rule_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
