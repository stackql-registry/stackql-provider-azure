--- 
title: alert_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_definitions
  - authorization
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

Creates, updates, deletes, gets or lists an <code>alert_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="alert_definitions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alert_definitions" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_for_scope', value: 'list_for_scope' }
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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The alert description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The alert display name.</td>
</tr>
<tr>
    <td><CopyableCode code="howToPrevent" /></td>
    <td><code>string</code></td>
    <td>The ways to prevent the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="isConfigurable" /></td>
    <td><code>boolean</code></td>
    <td>True if the alert configuration can be configured; false, otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="isRemediatable" /></td>
    <td><code>boolean</code></td>
    <td>True if the alert can be remediated; false, otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="mitigationSteps" /></td>
    <td><code>string</code></td>
    <td>The methods to mitigate the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The alert scope.</td>
</tr>
<tr>
    <td><CopyableCode code="securityImpact" /></td>
    <td><code>string</code></td>
    <td>Security impact of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="severityLevel" /></td>
    <td><code>string</code></td>
    <td>Severity level of the alert. Known values are: "Low", "Medium", and "High". (Low, Medium, High)</td>
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
<TabItem value="list_for_scope">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The alert description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The alert display name.</td>
</tr>
<tr>
    <td><CopyableCode code="howToPrevent" /></td>
    <td><code>string</code></td>
    <td>The ways to prevent the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="isConfigurable" /></td>
    <td><code>boolean</code></td>
    <td>True if the alert configuration can be configured; false, otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="isRemediatable" /></td>
    <td><code>boolean</code></td>
    <td>True if the alert can be remediated; false, otherwise.</td>
</tr>
<tr>
    <td><CopyableCode code="mitigationSteps" /></td>
    <td><code>string</code></td>
    <td>The methods to mitigate the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The alert scope.</td>
</tr>
<tr>
    <td><CopyableCode code="securityImpact" /></td>
    <td><code>string</code></td>
    <td>Security impact of the alert.</td>
</tr>
<tr>
    <td><CopyableCode code="severityLevel" /></td>
    <td><code>string</code></td>
    <td>Severity level of the alert. Known values are: "Low", "Medium", and "High". (Low, Medium, High)</td>
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
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-alert_definition_id"><code>alert_definition_id</code></a></td>
    <td></td>
    <td>Get the specified alert definition.</td>
</tr>
<tr>
    <td><a href="#list_for_scope"><CopyableCode code="list_for_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Gets alert definitions for a resource scope.</td>
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
<tr id="parameter-alert_definition_id">
    <td><CopyableCode code="alert_definition_id" /></td>
    <td><code>string</code></td>
    <td>The name of the alert definition to get. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_for_scope', value: 'list_for_scope' }
    ]}
>
<TabItem value="get">

Get the specified alert definition.

```sql
SELECT
id,
name,
description,
displayName,
howToPrevent,
isConfigurable,
isRemediatable,
mitigationSteps,
scope,
securityImpact,
severityLevel,
systemData,
type
FROM azure.authorization.alert_definitions
WHERE scope = '{{ scope }}' -- required
AND alert_definition_id = '{{ alert_definition_id }}' -- required
;
```
</TabItem>
<TabItem value="list_for_scope">

Gets alert definitions for a resource scope.

```sql
SELECT
id,
name,
description,
displayName,
howToPrevent,
isConfigurable,
isRemediatable,
mitigationSteps,
scope,
securityImpact,
severityLevel,
systemData,
type
FROM azure.authorization.alert_definitions
WHERE scope = '{{ scope }}' -- required
;
```
</TabItem>
</Tabs>
