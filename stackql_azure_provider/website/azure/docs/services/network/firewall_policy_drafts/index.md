--- 
title: firewall_policy_drafts
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_drafts
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_drafts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="firewall_policy_drafts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_drafts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="dnsSettings" /></td>
    <td><code>object</code></td>
    <td>DNS Proxy Settings definition.</td>
</tr>
<tr>
    <td><CopyableCode code="explicitProxy" /></td>
    <td><code>object</code></td>
    <td>Explicit Proxy Settings definition.</td>
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
    <td></td>
    <td>Get a draft Firewall Policy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a draft Firewall Policy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a draft Firewall Policy.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-firewall_policy_name"><code>firewall_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a draft policy.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Get a draft Firewall Policy.

```sql
SELECT
id,
name,
basePolicy,
dnsSettings,
explicitProxy,
insights,
intrusionDetection,
location,
snat,
sql,
tags,
threatIntelMode,
threatIntelWhitelist,
type
FROM azure.network.firewall_policy_drafts
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND firewall_policy_name = '{{ firewall_policy_name }}' -- required
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

Create or update a draft Firewall Policy.

```sql
INSERT INTO azure.network.firewall_policy_drafts (
id,
location,
tags,
properties,
resource_group_name,
firewall_policy_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ firewall_policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: firewall_policy_drafts
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the firewall_policy_drafts resource.
    - name: firewall_policy_name
      value: "{{ firewall_policy_name }}"
      description: Required parameter for the firewall_policy_drafts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the firewall_policy_drafts resource.
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
        basePolicy:
          id: "{{ id }}"
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

Create or update a draft Firewall Policy.

```sql
REPLACE azure.network.firewall_policy_drafts
SET 
id = '{{ id }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND firewall_policy_name = '{{ firewall_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
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

Delete a draft policy.

```sql
DELETE FROM azure.network.firewall_policy_drafts
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND firewall_policy_name = '{{ firewall_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
