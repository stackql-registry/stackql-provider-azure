--- 
title: data_masking_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_rules
  - synapse
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

Creates, updates, deletes, gets or lists a <code>data_masking_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_masking_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.data_masking_rules" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sql_pool', value: 'list_by_sql_pool' }
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
    <td><CopyableCode code="aliasName" /></td>
    <td><code>string</code></td>
    <td>The alias name. This is a legacy parameter and is no longer used.</td>
</tr>
<tr>
    <td><CopyableCode code="columnName" /></td>
    <td><code>string</code></td>
    <td>The column name on which the data masking rule is applied.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of Data Masking Rule. Metadata, used for Azure portal.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the data masking rule.</td>
</tr>
<tr>
    <td><CopyableCode code="maskingFunction" /></td>
    <td><code>string</code></td>
    <td>The masking function that is used for the data masking rule. Known values are: "Default", "CCN", "Email", "Number", "SSN", and "Text".</td>
</tr>
<tr>
    <td><CopyableCode code="numberFrom" /></td>
    <td><code>string</code></td>
    <td>The numberFrom property of the masking rule. Required if maskingFunction is set to Number, otherwise this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="numberTo" /></td>
    <td><code>string</code></td>
    <td>The numberTo property of the data masking rule. Required if maskingFunction is set to Number, otherwise this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixSize" /></td>
    <td><code>string</code></td>
    <td>If maskingFunction is set to Text, the number of characters to show unmasked in the beginning of the string. Otherwise, this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="replacementString" /></td>
    <td><code>string</code></td>
    <td>If maskingFunction is set to Text, the character to use for masking the unexposed part of the string. Otherwise, this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleState" /></td>
    <td><code>string</code></td>
    <td>The rule state. Used to delete a rule. To delete an existing rule, specify the schemaName, tableName, columnName, maskingFunction, and specify ruleState as disabled. However, if the rule doesn't already exist, the rule will be created with ruleState set to enabled, regardless of the provided value of ruleState. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="schemaName" /></td>
    <td><code>string</code></td>
    <td>The schema name on which the data masking rule is applied.</td>
</tr>
<tr>
    <td><CopyableCode code="suffixSize" /></td>
    <td><code>string</code></td>
    <td>If maskingFunction is set to Text, the number of characters to show unmasked at the end of the string. Otherwise, this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="tableName" /></td>
    <td><code>string</code></td>
    <td>The table name on which the data masking rule is applied.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_sql_pool">

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
    <td><CopyableCode code="aliasName" /></td>
    <td><code>string</code></td>
    <td>The alias name. This is a legacy parameter and is no longer used.</td>
</tr>
<tr>
    <td><CopyableCode code="columnName" /></td>
    <td><code>string</code></td>
    <td>The column name on which the data masking rule is applied.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of Data Masking Rule. Metadata, used for Azure portal.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the data masking rule.</td>
</tr>
<tr>
    <td><CopyableCode code="maskingFunction" /></td>
    <td><code>string</code></td>
    <td>The masking function that is used for the data masking rule. Known values are: "Default", "CCN", "Email", "Number", "SSN", and "Text".</td>
</tr>
<tr>
    <td><CopyableCode code="numberFrom" /></td>
    <td><code>string</code></td>
    <td>The numberFrom property of the masking rule. Required if maskingFunction is set to Number, otherwise this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="numberTo" /></td>
    <td><code>string</code></td>
    <td>The numberTo property of the data masking rule. Required if maskingFunction is set to Number, otherwise this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="prefixSize" /></td>
    <td><code>string</code></td>
    <td>If maskingFunction is set to Text, the number of characters to show unmasked in the beginning of the string. Otherwise, this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="replacementString" /></td>
    <td><code>string</code></td>
    <td>If maskingFunction is set to Text, the character to use for masking the unexposed part of the string. Otherwise, this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="ruleState" /></td>
    <td><code>string</code></td>
    <td>The rule state. Used to delete a rule. To delete an existing rule, specify the schemaName, tableName, columnName, maskingFunction, and specify ruleState as disabled. However, if the rule doesn't already exist, the rule will be created with ruleState set to enabled, regardless of the provided value of ruleState. Known values are: "Disabled" and "Enabled".</td>
</tr>
<tr>
    <td><CopyableCode code="schemaName" /></td>
    <td><code>string</code></td>
    <td>The schema name on which the data masking rule is applied.</td>
</tr>
<tr>
    <td><CopyableCode code="suffixSize" /></td>
    <td><code>string</code></td>
    <td>If maskingFunction is set to Text, the number of characters to show unmasked at the end of the string. Otherwise, this parameter will be ignored.</td>
</tr>
<tr>
    <td><CopyableCode code="tableName" /></td>
    <td><code>string</code></td>
    <td>The table name on which the data masking rule is applied.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-data_masking_rule_name"><code>data_masking_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the specific Sql pool data masking rule.</td>
</tr>
<tr>
    <td><a href="#list_by_sql_pool"><CopyableCode code="list_by_sql_pool" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of Sql pool data masking rules.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-data_masking_rule_name"><code>data_masking_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Sql pool data masking rule.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-sql_pool_name"><code>sql_pool_name</code></a>, <a href="#parameter-data_masking_rule_name"><code>data_masking_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a Sql pool data masking rule.</td>
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
<tr id="parameter-data_masking_rule_name">
    <td><CopyableCode code="data_masking_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the data masking rule. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sql_pool_name">
    <td><CopyableCode code="sql_pool_name" /></td>
    <td><code>string</code></td>
    <td>SQL pool name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the workspace. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sql_pool', value: 'list_by_sql_pool' }
    ]}
>
<TabItem value="get">

Gets the specific Sql pool data masking rule.

```sql
SELECT
id,
name,
aliasName,
columnName,
kind,
location,
maskingFunction,
numberFrom,
numberTo,
prefixSize,
replacementString,
ruleState,
schemaName,
suffixSize,
tableName,
type
FROM azure.synapse.data_masking_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
AND data_masking_rule_name = '{{ data_masking_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sql_pool">

Gets a list of Sql pool data masking rules.

```sql
SELECT
id,
name,
aliasName,
columnName,
kind,
location,
maskingFunction,
numberFrom,
numberTo,
prefixSize,
replacementString,
ruleState,
schemaName,
suffixSize,
tableName,
type
FROM azure.synapse.data_masking_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND sql_pool_name = '{{ sql_pool_name }}' -- required
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

Creates or updates a Sql pool data masking rule.

```sql
INSERT INTO azure.synapse.data_masking_rules (
properties,
resource_group_name,
workspace_name,
sql_pool_name,
data_masking_rule_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ sql_pool_name }}',
'{{ data_masking_rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
location,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: data_masking_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_masking_rules resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the data_masking_rules resource.
    - name: sql_pool_name
      value: "{{ sql_pool_name }}"
      description: Required parameter for the data_masking_rules resource.
    - name: data_masking_rule_name
      value: "{{ data_masking_rule_name }}"
      description: Required parameter for the data_masking_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the data_masking_rules resource.
    - name: properties
      value:
        aliasName: "{{ aliasName }}"
        ruleState: "{{ ruleState }}"
        schemaName: "{{ schemaName }}"
        tableName: "{{ tableName }}"
        columnName: "{{ columnName }}"
        maskingFunction: "{{ maskingFunction }}"
        numberFrom: "{{ numberFrom }}"
        numberTo: "{{ numberTo }}"
        prefixSize: "{{ prefixSize }}"
        suffixSize: "{{ suffixSize }}"
        replacementString: "{{ replacementString }}"
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

Creates or updates a Sql pool data masking rule.

```sql
REPLACE azure.synapse.data_masking_rules
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND sql_pool_name = '{{ sql_pool_name }}' --required
AND data_masking_rule_name = '{{ data_masking_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
location,
properties,
type;
```
</TabItem>
</Tabs>
