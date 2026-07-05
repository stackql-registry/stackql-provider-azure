--- 
title: managed_database_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_security_alert_policies
  - sql
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

Creates, updates, deletes, gets or lists a <code>managed_database_security_alert_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="managed_database_security_alert_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_security_alert_policies" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_database', value: 'list_by_database' }
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
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the UTC creation time of the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledAlerts" /></td>
    <td><code>array</code></td>
    <td>Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action, Brute_Force.</td>
</tr>
<tr>
    <td><CopyableCode code="emailAccountAdmins" /></td>
    <td><code>boolean</code></td>
    <td>Specifies that the alert is sent to the account administrators.</td>
</tr>
<tr>
    <td><CopyableCode code="emailAddresses" /></td>
    <td><code>array</code></td>
    <td>Specifies an array of e-mail addresses to which the alert is sent.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionDays" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days to keep in the Threat Detection audit logs.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database. Required. Known values are: "New", "Enabled", and "Disabled". (New, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountAccessKey" /></td>
    <td><code>string</code></td>
    <td>Specifies the identifier key of the Threat Detection audit storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoint" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage endpoint (e.g. `https://MyAccount.blob.core.windows.net `_). This blob storage will hold all Threat Detection audit logs.</td>
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
<TabItem value="list_by_database">

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
    <td><CopyableCode code="creationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Specifies the UTC creation time of the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="disabledAlerts" /></td>
    <td><code>array</code></td>
    <td>Specifies an array of alerts that are disabled. Allowed values are: Sql_Injection, Sql_Injection_Vulnerability, Access_Anomaly, Data_Exfiltration, Unsafe_Action, Brute_Force.</td>
</tr>
<tr>
    <td><CopyableCode code="emailAccountAdmins" /></td>
    <td><code>boolean</code></td>
    <td>Specifies that the alert is sent to the account administrators.</td>
</tr>
<tr>
    <td><CopyableCode code="emailAddresses" /></td>
    <td><code>array</code></td>
    <td>Specifies an array of e-mail addresses to which the alert is sent.</td>
</tr>
<tr>
    <td><CopyableCode code="retentionDays" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days to keep in the Threat Detection audit logs.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database. Required. Known values are: "New", "Enabled", and "Disabled". (New, Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="storageAccountAccessKey" /></td>
    <td><code>string</code></td>
    <td>Specifies the identifier key of the Threat Detection audit storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="storageEndpoint" /></td>
    <td><code>string</code></td>
    <td>Specifies the blob storage endpoint (e.g. `https://MyAccount.blob.core.windows.net `_). This blob storage will hold all Threat Detection audit logs.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-security_alert_policy_name"><code>security_alert_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a managed database's security alert policy.</td>
</tr>
<tr>
    <td><a href="#list_by_database"><CopyableCode code="list_by_database" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of managed database's security alert policies.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-security_alert_policy_name"><code>security_alert_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a database's security alert policy.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-managed_instance_name"><code>managed_instance_name</code></a>, <a href="#parameter-database_name"><code>database_name</code></a>, <a href="#parameter-security_alert_policy_name"><code>security_alert_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a database's security alert policy.</td>
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
<tr id="parameter-database_name">
    <td><CopyableCode code="database_name" /></td>
    <td><code>string</code></td>
    <td>The name of the database. Required.</td>
</tr>
<tr id="parameter-managed_instance_name">
    <td><CopyableCode code="managed_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the managed instance. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-security_alert_policy_name">
    <td><CopyableCode code="security_alert_policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the security alert policy. "Default" Required.</td>
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
        { label: 'get', value: 'get' },
        { label: 'list_by_database', value: 'list_by_database' }
    ]}
>
<TabItem value="get">

Gets a managed database's security alert policy.

```sql
SELECT
id,
name,
creationTime,
disabledAlerts,
emailAccountAdmins,
emailAddresses,
retentionDays,
state,
storageAccountAccessKey,
storageEndpoint,
systemData,
type
FROM azure.sql.managed_database_security_alert_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
AND security_alert_policy_name = '{{ security_alert_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_database">

Gets a list of managed database's security alert policies.

```sql
SELECT
id,
name,
creationTime,
disabledAlerts,
emailAccountAdmins,
emailAddresses,
retentionDays,
state,
storageAccountAccessKey,
storageEndpoint,
systemData,
type
FROM azure.sql.managed_database_security_alert_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND managed_instance_name = '{{ managed_instance_name }}' -- required
AND database_name = '{{ database_name }}' -- required
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

Creates or updates a database's security alert policy.

```sql
INSERT INTO azure.sql.managed_database_security_alert_policies (
properties,
resource_group_name,
managed_instance_name,
database_name,
security_alert_policy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ managed_instance_name }}',
'{{ database_name }}',
'{{ security_alert_policy_name }}',
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
- name: managed_database_security_alert_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the managed_database_security_alert_policies resource.
    - name: managed_instance_name
      value: "{{ managed_instance_name }}"
      description: Required parameter for the managed_database_security_alert_policies resource.
    - name: database_name
      value: "{{ database_name }}"
      description: Required parameter for the managed_database_security_alert_policies resource.
    - name: security_alert_policy_name
      value: "{{ security_alert_policy_name }}"
      description: Required parameter for the managed_database_security_alert_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the managed_database_security_alert_policies resource.
    - name: properties
      description: |
        Resource properties.
      value:
        state: "{{ state }}"
        disabledAlerts:
          - "{{ disabledAlerts }}"
        emailAddresses:
          - "{{ emailAddresses }}"
        emailAccountAdmins: {{ emailAccountAdmins }}
        storageEndpoint: "{{ storageEndpoint }}"
        storageAccountAccessKey: "{{ storageAccountAccessKey }}"
        retentionDays: {{ retentionDays }}
        creationTime: "{{ creationTime }}"
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

Creates or updates a database's security alert policy.

```sql
REPLACE azure.sql.managed_database_security_alert_policies
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND managed_instance_name = '{{ managed_instance_name }}' --required
AND database_name = '{{ database_name }}' --required
AND security_alert_policy_name = '{{ security_alert_policy_name }}' --required
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
