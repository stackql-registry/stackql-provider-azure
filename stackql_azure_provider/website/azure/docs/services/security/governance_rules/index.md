--- 
title: governance_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - governance_rules
  - security
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

Creates, updates, deletes, gets or lists a <code>governance_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="governance_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.governance_rules" /></td></tr>
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
    <td><CopyableCode code="conditionSets" /></td>
    <td><code>array</code></td>
    <td>The governance rule conditionSets - see examples. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the governance rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the governance rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="excludedScopes" /></td>
    <td><code>array</code></td>
    <td>Excluded scopes, filter out the descendants of the scope (on management scopes).</td>
</tr>
<tr>
    <td><CopyableCode code="governanceEmailNotification" /></td>
    <td><code>object</code></td>
    <td>The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners.</td>
</tr>
<tr>
    <td><CopyableCode code="includeMemberScopes" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether the rule is management scope rule (master connector as a single scope or management scope).</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether the rule is active/inactive.</td>
</tr>
<tr>
    <td><CopyableCode code="isGracePeriod" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether there is a grace period on the governance rule.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The governance rule metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerSource" /></td>
    <td><code>object</code></td>
    <td>The owner source for the governance rule - e.g. Manually by `user@contoso.com `_ - see example. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remediationTimeframe" /></td>
    <td><code>string</code></td>
    <td>Governance rule remediation timeframe - this is the time that will affect on the grace-period duration e.g. 7.00:00:00 - means 7 days.</td>
</tr>
<tr>
    <td><CopyableCode code="rulePriority" /></td>
    <td><code>integer</code></td>
    <td>The governance rule priority, priority to the lower number. Rules with the same priority on the same scope will not be allowed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleType" /></td>
    <td><code>string</code></td>
    <td>The rule type of the governance rule, defines the source of the rule e.g. Integrated. Required. Known values are: "Integrated" and "ServiceNow". (Integrated, ServiceNow)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceType" /></td>
    <td><code>string</code></td>
    <td>The governance rule source, what the rule affects, e.g. Assessments. Required. "Assessments" (Assessments)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId (GUID).</td>
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
    <td><CopyableCode code="conditionSets" /></td>
    <td><code>array</code></td>
    <td>The governance rule conditionSets - see examples. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the governance rule.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the governance rule. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="excludedScopes" /></td>
    <td><code>array</code></td>
    <td>Excluded scopes, filter out the descendants of the scope (on management scopes).</td>
</tr>
<tr>
    <td><CopyableCode code="governanceEmailNotification" /></td>
    <td><code>object</code></td>
    <td>The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners.</td>
</tr>
<tr>
    <td><CopyableCode code="includeMemberScopes" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether the rule is management scope rule (master connector as a single scope or management scope).</td>
</tr>
<tr>
    <td><CopyableCode code="isDisabled" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether the rule is active/inactive.</td>
</tr>
<tr>
    <td><CopyableCode code="isGracePeriod" /></td>
    <td><code>boolean</code></td>
    <td>Defines whether there is a grace period on the governance rule.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The governance rule metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="ownerSource" /></td>
    <td><code>object</code></td>
    <td>The owner source for the governance rule - e.g. Manually by `user@contoso.com `_ - see example. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="remediationTimeframe" /></td>
    <td><code>string</code></td>
    <td>Governance rule remediation timeframe - this is the time that will affect on the grace-period duration e.g. 7.00:00:00 - means 7 days.</td>
</tr>
<tr>
    <td><CopyableCode code="rulePriority" /></td>
    <td><code>integer</code></td>
    <td>The governance rule priority, priority to the lower number. Rules with the same priority on the same scope will not be allowed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleType" /></td>
    <td><code>string</code></td>
    <td>The rule type of the governance rule, defines the source of the rule e.g. Integrated. Required. Known values are: "Integrated" and "ServiceNow". (Integrated, ServiceNow)</td>
</tr>
<tr>
    <td><CopyableCode code="sourceResourceType" /></td>
    <td><code>string</code></td>
    <td>The governance rule source, what the rule affects, e.g. Assessments. Required. "Assessments" (Assessments)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId (GUID).</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Get a specific governance rule for the requested scope by ruleId.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get a list of all relevant governance rules over a scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Creates or updates a governance rule over a given scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Creates or updates a governance rule over a given scope.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Delete a Governance rule over a given scope.</td>
</tr>
<tr>
    <td><a href="#execute"><CopyableCode code="execute" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a></td>
    <td></td>
    <td>Execute a governance rule.</td>
</tr>
<tr>
    <td><a href="#operation_results"><CopyableCode code="operation_results" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-rule_id"><code>rule_id</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Get governance rules long run operation result for the requested scope by ruleId and operationId.</td>
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
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The governance rule long running operation unique key. Required.</td>
</tr>
<tr id="parameter-rule_id">
    <td><CopyableCode code="rule_id" /></td>
    <td><code>string</code></td>
    <td>The governance rule key. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The scope of the governance rule. Required.</td>
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

Get a specific governance rule for the requested scope by ruleId.

```sql
SELECT
id,
name,
conditionSets,
description,
displayName,
excludedScopes,
governanceEmailNotification,
includeMemberScopes,
isDisabled,
isGracePeriod,
metadata,
ownerSource,
remediationTimeframe,
rulePriority,
ruleType,
sourceResourceType,
systemData,
tenantId,
type
FROM azure.security.governance_rules
WHERE scope = '{{ scope }}' -- required
AND rule_id = '{{ rule_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of all relevant governance rules over a scope.

```sql
SELECT
id,
name,
conditionSets,
description,
displayName,
excludedScopes,
governanceEmailNotification,
includeMemberScopes,
isDisabled,
isGracePeriod,
metadata,
ownerSource,
remediationTimeframe,
rulePriority,
ruleType,
sourceResourceType,
systemData,
tenantId,
type
FROM azure.security.governance_rules
WHERE scope = '{{ scope }}' -- required
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

Creates or updates a governance rule over a given scope.

```sql
INSERT INTO azure.security.governance_rules (
properties,
scope,
rule_id
)
SELECT 
'{{ properties }}',
'{{ scope }}',
'{{ rule_id }}'
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
- name: governance_rules
  props:
    - name: scope
      value: "{{ scope }}"
      description: Required parameter for the governance_rules resource.
    - name: rule_id
      value: "{{ rule_id }}"
      description: Required parameter for the governance_rules resource.
    - name: properties
      description: |
        Properties of a governance rule.
      value:
        tenantId: "{{ tenantId }}"
        displayName: "{{ displayName }}"
        description: "{{ description }}"
        remediationTimeframe: "{{ remediationTimeframe }}"
        isGracePeriod: {{ isGracePeriod }}
        rulePriority: {{ rulePriority }}
        isDisabled: {{ isDisabled }}
        ruleType: "{{ ruleType }}"
        sourceResourceType: "{{ sourceResourceType }}"
        excludedScopes:
          - "{{ excludedScopes }}"
        conditionSets: "{{ conditionSets }}"
        includeMemberScopes: {{ includeMemberScopes }}
        ownerSource:
          type: "{{ type }}"
          value: "{{ value }}"
        governanceEmailNotification:
          disableManagerEmailNotification: {{ disableManagerEmailNotification }}
          disableOwnerEmailNotification: {{ disableOwnerEmailNotification }}
        metadata:
          createdBy: "{{ createdBy }}"
          createdOn: "{{ createdOn }}"
          updatedBy: "{{ updatedBy }}"
          updatedOn: "{{ updatedOn }}"
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

Creates or updates a governance rule over a given scope.

```sql
REPLACE azure.security.governance_rules
SET 
properties = '{{ properties }}'
WHERE 
scope = '{{ scope }}' --required
AND rule_id = '{{ rule_id }}' --required
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

Delete a Governance rule over a given scope.

```sql
DELETE FROM azure.security.governance_rules
WHERE scope = '{{ scope }}' --required
AND rule_id = '{{ rule_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="execute"
    values={[
        { label: 'execute', value: 'execute' },
        { label: 'operation_results', value: 'operation_results' }
    ]}
>
<TabItem value="execute">

Execute a governance rule.

```sql
EXEC azure.security.governance_rules.execute 
@scope='{{ scope }}' --required, 
@rule_id='{{ rule_id }}' --required 
@@json=
'{
"override": {{ override }}
}'
;
```
</TabItem>
<TabItem value="operation_results">

Get governance rules long run operation result for the requested scope by ruleId and operationId.

```sql
EXEC azure.security.governance_rules.operation_results 
@scope='{{ scope }}' --required, 
@rule_id='{{ rule_id }}' --required, 
@operation_id='{{ operation_id }}' --required
;
```
</TabItem>
</Tabs>
