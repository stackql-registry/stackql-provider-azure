--- 
title: post_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - post_rules
  - paloaltonetworksngfw
  - azure_isv
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_isv resources using SQL
custom_edit_url: null
image: /img/stackql-azure_isv-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>post_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="post_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworksngfw.post_rules" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>rule action. Known values are: "Allow", "DenySilent", "DenyResetServer", and "DenyResetBoth".</td>
</tr>
<tr>
    <td><CopyableCode code="applications" /></td>
    <td><code>array</code></td>
    <td>array of rule applications.</td>
</tr>
<tr>
    <td><CopyableCode code="auditComment" /></td>
    <td><code>string</code></td>
    <td>rule comment.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>object</code></td>
    <td>rule category.</td>
</tr>
<tr>
    <td><CopyableCode code="decryptionRuleType" /></td>
    <td><code>string</code></td>
    <td>enable or disable decryption. Known values are: "SSLOutboundInspection", "SSLInboundInspection", and "None".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>rule description.</td>
</tr>
<tr>
    <td><CopyableCode code="destination" /></td>
    <td><code>object</code></td>
    <td>destination address.</td>
</tr>
<tr>
    <td><CopyableCode code="enableLogging" /></td>
    <td><code>string</code></td>
    <td>enable or disable logging. Known values are: "DISABLED" and "ENABLED".</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag info.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundInspectionCertificate" /></td>
    <td><code>string</code></td>
    <td>inbound Inspection Certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="negateDestination" /></td>
    <td><code>string</code></td>
    <td>cidr should not be 'any'. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="negateSource" /></td>
    <td><code>string</code></td>
    <td>cidr should not be 'any'. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>:vartype priority: int</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>any, application-default, TCP:number, UDP:number.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolPortList" /></td>
    <td><code>array</code></td>
    <td>prot port list.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="ruleName" /></td>
    <td><code>string</code></td>
    <td>rule name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleState" /></td>
    <td><code>string</code></td>
    <td>state of this rule. Known values are: "DISABLED" and "ENABLED".</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>source address.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>tag for rule.</td>
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
    <td><CopyableCode code="actionType" /></td>
    <td><code>string</code></td>
    <td>rule action. Known values are: "Allow", "DenySilent", "DenyResetServer", and "DenyResetBoth".</td>
</tr>
<tr>
    <td><CopyableCode code="applications" /></td>
    <td><code>array</code></td>
    <td>array of rule applications.</td>
</tr>
<tr>
    <td><CopyableCode code="auditComment" /></td>
    <td><code>string</code></td>
    <td>rule comment.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>object</code></td>
    <td>rule category.</td>
</tr>
<tr>
    <td><CopyableCode code="decryptionRuleType" /></td>
    <td><code>string</code></td>
    <td>enable or disable decryption. Known values are: "SSLOutboundInspection", "SSLInboundInspection", and "None".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>rule description.</td>
</tr>
<tr>
    <td><CopyableCode code="destination" /></td>
    <td><code>object</code></td>
    <td>destination address.</td>
</tr>
<tr>
    <td><CopyableCode code="enableLogging" /></td>
    <td><code>string</code></td>
    <td>enable or disable logging. Known values are: "DISABLED" and "ENABLED".</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>etag info.</td>
</tr>
<tr>
    <td><CopyableCode code="inboundInspectionCertificate" /></td>
    <td><code>string</code></td>
    <td>inbound Inspection Certificate.</td>
</tr>
<tr>
    <td><CopyableCode code="negateDestination" /></td>
    <td><code>string</code></td>
    <td>cidr should not be 'any'. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="negateSource" /></td>
    <td><code>string</code></td>
    <td>cidr should not be 'any'. Known values are: "TRUE" and "FALSE".</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>:vartype priority: int</td>
</tr>
<tr>
    <td><CopyableCode code="protocol" /></td>
    <td><code>string</code></td>
    <td>any, application-default, TCP:number, UDP:number.</td>
</tr>
<tr>
    <td><CopyableCode code="protocolPortList" /></td>
    <td><code>array</code></td>
    <td>prot port list.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the resource. Known values are: "Accepted", "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", and "NotSpecified".</td>
</tr>
<tr>
    <td><CopyableCode code="ruleName" /></td>
    <td><code>string</code></td>
    <td>rule name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleState" /></td>
    <td><code>string</code></td>
    <td>state of this rule. Known values are: "DISABLED" and "ENABLED".</td>
</tr>
<tr>
    <td><CopyableCode code="source" /></td>
    <td><code>object</code></td>
    <td>source address.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>array</code></td>
    <td>tag for rule.</td>
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
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-priority"><code>priority</code></a></td>
    <td></td>
    <td>Get a PostRulesResource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a></td>
    <td></td>
    <td>List PostRulesResource resources by Tenant.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-priority"><code>priority</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a PostRulesResource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-priority"><code>priority</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a PostRulesResource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-priority"><code>priority</code></a></td>
    <td></td>
    <td>Delete a PostRulesResource.</td>
</tr>
<tr>
    <td><a href="#get_counters"><CopyableCode code="get_counters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-priority"><code>priority</code></a></td>
    <td><a href="#parameter-firewallName"><code>firewallName</code></a></td>
    <td>Get counters.</td>
</tr>
<tr>
    <td><a href="#refresh_counters"><CopyableCode code="refresh_counters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-priority"><code>priority</code></a></td>
    <td><a href="#parameter-firewallName"><code>firewallName</code></a></td>
    <td>Refresh counters.</td>
</tr>
<tr>
    <td><a href="#reset_counters"><CopyableCode code="reset_counters" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-global_rulestack_name"><code>global_rulestack_name</code></a>, <a href="#parameter-priority"><code>priority</code></a></td>
    <td><a href="#parameter-firewallName"><code>firewallName</code></a></td>
    <td>Reset counters.</td>
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
<tr id="parameter-global_rulestack_name">
    <td><CopyableCode code="global_rulestack_name" /></td>
    <td><code>string</code></td>
    <td>GlobalRulestack resource name. Required.</td>
</tr>
<tr id="parameter-priority">
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>Post Rule priority. Required.</td>
</tr>
<tr id="parameter-firewallName">
    <td><CopyableCode code="firewallName" /></td>
    <td><code>string</code></td>
    <td>Default value is None.</td>
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

Get a PostRulesResource.

```sql
SELECT
id,
name,
actionType,
applications,
auditComment,
category,
decryptionRuleType,
description,
destination,
enableLogging,
etag,
inboundInspectionCertificate,
negateDestination,
negateSource,
priority,
protocol,
protocolPortList,
provisioningState,
ruleName,
ruleState,
source,
systemData,
tags,
type
FROM azure_isv.paloaltonetworksngfw.post_rules
WHERE global_rulestack_name = '{{ global_rulestack_name }}' -- required
AND priority = '{{ priority }}' -- required
;
```
</TabItem>
<TabItem value="list">

List PostRulesResource resources by Tenant.

```sql
SELECT
id,
name,
actionType,
applications,
auditComment,
category,
decryptionRuleType,
description,
destination,
enableLogging,
etag,
inboundInspectionCertificate,
negateDestination,
negateSource,
priority,
protocol,
protocolPortList,
provisioningState,
ruleName,
ruleState,
source,
systemData,
tags,
type
FROM azure_isv.paloaltonetworksngfw.post_rules
WHERE global_rulestack_name = '{{ global_rulestack_name }}' -- required
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

Create a PostRulesResource.

```sql
INSERT INTO azure_isv.paloaltonetworksngfw.post_rules (
properties,
global_rulestack_name,
priority
)
SELECT 
'{{ properties }}' /* required */,
'{{ global_rulestack_name }}',
'{{ priority }}'
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
- name: post_rules
  props:
    - name: global_rulestack_name
      value: "{{ global_rulestack_name }}"
      description: Required parameter for the post_rules resource.
    - name: priority
      value: "{{ priority }}"
      description: Required parameter for the post_rules resource.
    - name: properties
      value:
        etag: "{{ etag }}"
        ruleName: "{{ ruleName }}"
        description: "{{ description }}"
        ruleState: "{{ ruleState }}"
        source:
          cidrs:
            - "{{ cidrs }}"
          countries:
            - "{{ countries }}"
          feeds:
            - "{{ feeds }}"
          prefixLists:
            - "{{ prefixLists }}"
        negateSource: "{{ negateSource }}"
        destination:
          cidrs:
            - "{{ cidrs }}"
          countries:
            - "{{ countries }}"
          feeds:
            - "{{ feeds }}"
          prefixLists:
            - "{{ prefixLists }}"
          fqdnLists:
            - "{{ fqdnLists }}"
        negateDestination: "{{ negateDestination }}"
        applications:
          - "{{ applications }}"
        category:
          urlCustom:
            - "{{ urlCustom }}"
          feeds:
            - "{{ feeds }}"
        protocol: "{{ protocol }}"
        protocolPortList:
          - "{{ protocolPortList }}"
        inboundInspectionCertificate: "{{ inboundInspectionCertificate }}"
        auditComment: "{{ auditComment }}"
        actionType: "{{ actionType }}"
        enableLogging: "{{ enableLogging }}"
        decryptionRuleType: "{{ decryptionRuleType }}"
        tags:
          - key: "{{ key }}"
            value: "{{ value }}"
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

Create a PostRulesResource.

```sql
REPLACE azure_isv.paloaltonetworksngfw.post_rules
SET 
properties = '{{ properties }}'
WHERE 
global_rulestack_name = '{{ global_rulestack_name }}' --required
AND priority = '{{ priority }}' --required
AND properties = '{{ properties }}' --required
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

Delete a PostRulesResource.

```sql
DELETE FROM azure_isv.paloaltonetworksngfw.post_rules
WHERE global_rulestack_name = '{{ global_rulestack_name }}' --required
AND priority = '{{ priority }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_counters"
    values={[
        { label: 'get_counters', value: 'get_counters' },
        { label: 'refresh_counters', value: 'refresh_counters' },
        { label: 'reset_counters', value: 'reset_counters' }
    ]}
>
<TabItem value="get_counters">

Get counters.

```sql
EXEC azure_isv.paloaltonetworksngfw.post_rules.get_counters 
@global_rulestack_name='{{ global_rulestack_name }}' --required, 
@priority='{{ priority }}' --required, 
@firewallName='{{ firewallName }}'
;
```
</TabItem>
<TabItem value="refresh_counters">

Refresh counters.

```sql
EXEC azure_isv.paloaltonetworksngfw.post_rules.refresh_counters 
@global_rulestack_name='{{ global_rulestack_name }}' --required, 
@priority='{{ priority }}' --required, 
@firewallName='{{ firewallName }}'
;
```
</TabItem>
<TabItem value="reset_counters">

Reset counters.

```sql
EXEC azure_isv.paloaltonetworksngfw.post_rules.reset_counters 
@global_rulestack_name='{{ global_rulestack_name }}' --required, 
@priority='{{ priority }}' --required, 
@firewallName='{{ firewallName }}'
;
```
</TabItem>
</Tabs>
