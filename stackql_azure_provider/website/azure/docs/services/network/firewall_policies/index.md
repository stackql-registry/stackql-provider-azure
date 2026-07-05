--- 
title: firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policies
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

Creates, updates, deletes, gets or lists a <code>firewall_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="firewall_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="basePolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="childPolicies" /></td>
    <td><code>array</code></td>
    <td>List of references to Child Firewall Policies.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>DNS Proxy Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="explicitProxy" /></td>
    <td><code>object</code></td>
    <td>Explicit Proxy Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="firewalls" /></td>
    <td><code>array</code></td>
    <td>List of references to Azure Firewalls that this Firewall Policy is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the firewall policy.</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code>object</code></td>
    <td>Insights on Firewall Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="intrusionDetection" /></td>
    <td><code>object</code></td>
    <td>The configuration for Intrusion detection.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the firewall policy resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleCollectionGroups" /></td>
    <td><code>array</code></td>
    <td>List of references to FirewallPolicyRuleCollectionGroups.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>A read-only string that represents the size of the FirewallPolicyPropertiesFormat in MB. (ex 0.5MB).</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Firewall Policy SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="snat" /></td>
    <td><code>object</code></td>
    <td>The private IP addresses/IP ranges to which traffic will not be SNAT.</td>
</tr>
<tr>
    <td><CopyableCode code="sql" /></td>
    <td><code>object</code></td>
    <td>SQL Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelMode" /></td>
    <td><code>string</code></td>
    <td>The operation mode for Threat Intelligence. Known values are: "Alert", "Deny", and "Off". (Alert, Deny, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelWhitelist" /></td>
    <td><code>object</code></td>
    <td>ThreatIntel Whitelist for Firewall Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="transportSecurity" /></td>
    <td><code>object</code></td>
    <td>TLS Configuration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="basePolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="childPolicies" /></td>
    <td><code>array</code></td>
    <td>List of references to Child Firewall Policies.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>DNS Proxy Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="explicitProxy" /></td>
    <td><code>object</code></td>
    <td>Explicit Proxy Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="firewalls" /></td>
    <td><code>array</code></td>
    <td>List of references to Azure Firewalls that this Firewall Policy is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the firewall policy.</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code>object</code></td>
    <td>Insights on Firewall Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="intrusionDetection" /></td>
    <td><code>object</code></td>
    <td>The configuration for Intrusion detection.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the firewall policy resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleCollectionGroups" /></td>
    <td><code>array</code></td>
    <td>List of references to FirewallPolicyRuleCollectionGroups.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>A read-only string that represents the size of the FirewallPolicyPropertiesFormat in MB. (ex 0.5MB).</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Firewall Policy SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="snat" /></td>
    <td><code>object</code></td>
    <td>The private IP addresses/IP ranges to which traffic will not be SNAT.</td>
</tr>
<tr>
    <td><CopyableCode code="sql" /></td>
    <td><code>object</code></td>
    <td>SQL Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelMode" /></td>
    <td><code>string</code></td>
    <td>The operation mode for Threat Intelligence. Known values are: "Alert", "Deny", and "Off". (Alert, Deny, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelWhitelist" /></td>
    <td><code>object</code></td>
    <td>ThreatIntel Whitelist for Firewall Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="transportSecurity" /></td>
    <td><code>object</code></td>
    <td>TLS Configuration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="basePolicy" /></td>
    <td><code>object</code></td>
    <td>Reference to another subresource.</td>
</tr>
<tr>
    <td><CopyableCode code="childPolicies" /></td>
    <td><code>array</code></td>
    <td>List of references to Child Firewall Policies.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>DNS Proxy Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>A unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="explicitProxy" /></td>
    <td><code>object</code></td>
    <td>Explicit Proxy Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="firewalls" /></td>
    <td><code>array</code></td>
    <td>List of references to Azure Firewalls that this Firewall Policy is associated with.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The identity of the firewall policy.</td>
</tr>
<tr>
    <td><CopyableCode code="insights" /></td>
    <td><code>object</code></td>
    <td>Insights on Firewall Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="intrusionDetection" /></td>
    <td><code>object</code></td>
    <td>The configuration for Intrusion detection.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the firewall policy resource. Known values are: "Failed", "Succeeded", "Canceled", "Creating", "Updating", and "Deleting". (Failed, Succeeded, Canceled, Creating, Updating, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="ruleCollectionGroups" /></td>
    <td><code>array</code></td>
    <td>List of references to FirewallPolicyRuleCollectionGroups.</td>
</tr>
<tr>
    <td><CopyableCode code="size" /></td>
    <td><code>string</code></td>
    <td>A read-only string that represents the size of the FirewallPolicyPropertiesFormat in MB. (ex 0.5MB).</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The Firewall Policy SKU.</td>
</tr>
<tr>
    <td><CopyableCode code="snat" /></td>
    <td><code>object</code></td>
    <td>The private IP addresses/IP ranges to which traffic will not be SNAT.</td>
</tr>
<tr>
    <td><CopyableCode code="sql" /></td>
    <td><code>object</code></td>
    <td>SQL Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelMode" /></td>
    <td><code>string</code></td>
    <td>The operation mode for Threat Intelligence. Known values are: "Alert", "Deny", and "Off". (Alert, Deny, Off)</td>
</tr>
<tr>
    <td><CopyableCode code="threatIntelWhitelist" /></td>
    <td><code>object</code></td>
    <td>ThreatIntel Whitelist for Firewall Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="transportSecurity" /></td>
    <td><code>object</code></td>
    <td>TLS Configuration definition.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets the specified Firewall Policy.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Firewall Policies in a resource group.</td>
</tr>
<tr>
    <td><a href="#list_all"><CopyableCode code="list_all" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all the Firewall Policies in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified Firewall Policy.</td>
</tr>
<tr>
    <td><a href="#update_tags"><CopyableCode code="update_tags" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates tags of a Azure Firewall Policy resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates the specified Firewall Policy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the specified Firewall Policy.</td>
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
<tr id="parameter-firewall_policy_name">
    <td><CopyableCode code="firewall_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Firewall Policy. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Expands referenced resources. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'list_all', value: 'list_all' }
    ]}
>
<TabItem value="get">

Gets the specified Firewall Policy.

```sql
SELECT
id,
name,
basePolicy,
childPolicies,
dnsSettings,
etag,
explicitProxy,
firewalls,
identity,
insights,
intrusionDetection,
location,
provisioningState,
ruleCollectionGroups,
size,
sku,
snat,
sql,
tags,
threatIntelMode,
threatIntelWhitelist,
transportSecurity,
type
FROM azure.network.firewall_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND firewall_policy_name = '{{ firewall_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Lists all Firewall Policies in a resource group.

```sql
SELECT
id,
name,
basePolicy,
childPolicies,
dnsSettings,
etag,
explicitProxy,
firewalls,
identity,
insights,
intrusionDetection,
location,
provisioningState,
ruleCollectionGroups,
size,
sku,
snat,
sql,
tags,
threatIntelMode,
threatIntelWhitelist,
transportSecurity,
type
FROM azure.network.firewall_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all">

Gets all the Firewall Policies in a subscription.

```sql
SELECT
id,
name,
basePolicy,
childPolicies,
dnsSettings,
etag,
explicitProxy,
firewalls,
identity,
insights,
intrusionDetection,
location,
provisioningState,
ruleCollectionGroups,
size,
sku,
snat,
sql,
tags,
threatIntelMode,
threatIntelWhitelist,
transportSecurity,
type
FROM azure.network.firewall_policies
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

Creates or updates the specified Firewall Policy.

```sql
INSERT INTO azure.network.firewall_policies (
id,
location,
tags,
properties,
identity,
resource_group_name,
firewall_policy_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ firewall_policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: firewall_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the firewall_policies resource.
    - name: firewall_policy_name
      value: "{{ firewall_policy_name }}"
      description: Required parameter for the firewall_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the firewall_policies resource.
    - name: id
      value: "{{ id }}"
      description: |
        Resource ID.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: properties
      description: |
        Properties of the firewall policy.
      value:
        size: "{{ size }}"
        ruleCollectionGroups:
          - id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
        basePolicy:
          id: "{{ id }}"
        firewalls:
          - id: "{{ id }}"
        childPolicies:
          - id: "{{ id }}"
        threatIntelMode: "{{ threatIntelMode }}"
        threatIntelWhitelist:
          ipAddresses:
            - "{{ ipAddresses }}"
          fqdns:
            - "{{ fqdns }}"
        insights:
          isEnabled: {{ isEnabled }}
          retentionDays: {{ retentionDays }}
          logAnalyticsResources:
            workspaces:
              - region: "{{ region }}"
                workspaceId:
                  id: "{{ id }}"
            defaultWorkspaceId:
              id: "{{ id }}"
        snat:
          privateRanges:
            - "{{ privateRanges }}"
          autoLearnPrivateRanges: "{{ autoLearnPrivateRanges }}"
        sql:
          allowSqlRedirect: {{ allowSqlRedirect }}
        dnsSettings:
          servers:
            - "{{ servers }}"
          enableProxy: {{ enableProxy }}
          requireProxyForNetworkRules: {{ requireProxyForNetworkRules }}
        explicitProxy:
          enableExplicitProxy: {{ enableExplicitProxy }}
          httpPort: {{ httpPort }}
          httpsPort: {{ httpsPort }}
          enablePacFile: {{ enablePacFile }}
          pacFilePort: {{ pacFilePort }}
          pacFile: "{{ pacFile }}"
        intrusionDetection:
          mode: "{{ mode }}"
          profile: "{{ profile }}"
          configuration:
            signatureOverrides:
              - id: "{{ id }}"
                mode: "{{ mode }}"
            bypassTrafficSettings:
              - name: "{{ name }}"
                description: "{{ description }}"
                protocol: "{{ protocol }}"
                sourceAddresses: "{{ sourceAddresses }}"
                destinationAddresses: "{{ destinationAddresses }}"
                destinationPorts: "{{ destinationPorts }}"
                sourceIpGroups: "{{ sourceIpGroups }}"
                destinationIpGroups: "{{ destinationIpGroups }}"
            privateRanges:
              - "{{ privateRanges }}"
        transportSecurity:
          certificateAuthority:
            keyVaultSecretId: "{{ keyVaultSecretId }}"
            name: "{{ name }}"
        sku:
          tier: "{{ tier }}"
    - name: identity
      description: |
        The identity of the firewall policy.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Updates tags of a Azure Firewall Policy resource.

```sql
UPDATE azure.network.firewall_policies
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND firewall_policy_name = '{{ firewall_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
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

Creates or updates the specified Firewall Policy.

```sql
REPLACE azure.network.firewall_policies
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND firewall_policy_name = '{{ firewall_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
location,
properties,
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

Deletes the specified Firewall Policy.

```sql
DELETE FROM azure.network.firewall_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND firewall_policy_name = '{{ firewall_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
