--- 
title: health_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - health_reports
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

Creates, updates, deletes, gets or lists a <code>health_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="health_reports" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.health_reports" /></td></tr>
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
    <td><CopyableCode code="affectedDefendersPlans" /></td>
    <td><code>array</code></td>
    <td>The affected defenders plans by unhealthy report.</td>
</tr>
<tr>
    <td><CopyableCode code="affectedDefendersSubPlans" /></td>
    <td><code>array</code></td>
    <td>The affected defenders sub plans by unhealthy report.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentDetails" /></td>
    <td><code>object</code></td>
    <td>The environment details of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="healthDataClassification" /></td>
    <td><code>object</code></td>
    <td>The classification of the health report.</td>
</tr>
<tr>
    <td><CopyableCode code="issues" /></td>
    <td><code>array</code></td>
    <td>A collection of the issues in the report.</td>
</tr>
<tr>
    <td><CopyableCode code="reportAdditionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data for the given health report, this field can include more details on the resource and the health scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDetails" /></td>
    <td><code>object</code></td>
    <td>The resource details of the health report.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status of the health report.</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="affectedDefendersPlans" /></td>
    <td><code>array</code></td>
    <td>The affected defenders plans by unhealthy report.</td>
</tr>
<tr>
    <td><CopyableCode code="affectedDefendersSubPlans" /></td>
    <td><code>array</code></td>
    <td>The affected defenders sub plans by unhealthy report.</td>
</tr>
<tr>
    <td><CopyableCode code="environmentDetails" /></td>
    <td><code>object</code></td>
    <td>The environment details of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="healthDataClassification" /></td>
    <td><code>object</code></td>
    <td>The classification of the health report.</td>
</tr>
<tr>
    <td><CopyableCode code="issues" /></td>
    <td><code>array</code></td>
    <td>A collection of the issues in the report.</td>
</tr>
<tr>
    <td><CopyableCode code="reportAdditionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data for the given health report, this field can include more details on the resource and the health scenario.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDetails" /></td>
    <td><code>object</code></td>
    <td>The resource details of the health report.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The status of the health report.</td>
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
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-health_report_name"><code>health_report_name</code></a></td>
    <td></td>
    <td>Get health report of resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get a list of all health reports inside a scope. Valid scopes are: subscription (format: 'subscriptions/&#123;subscriptionId&#125;'), or security connector (format: 'subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Security/securityConnectors/&#123;securityConnectorName&#125;)'.</td>
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
<tr id="parameter-health_report_name">
    <td><CopyableCode code="health_report_name" /></td>
    <td><code>string</code></td>
    <td>The health report key. Required.</td>
</tr>
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get health report of resource.

```sql
SELECT
id,
name,
affectedDefendersPlans,
affectedDefendersSubPlans,
environmentDetails,
healthDataClassification,
issues,
reportAdditionalData,
resourceDetails,
status,
systemData,
type
FROM azure.security.health_reports
WHERE resource_id = '{{ resource_id }}' -- required
AND health_report_name = '{{ health_report_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get a list of all health reports inside a scope. Valid scopes are: subscription (format: 'subscriptions/&#123;subscriptionId&#125;'), or security connector (format: 'subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Security/securityConnectors/&#123;securityConnectorName&#125;)'.

```sql
SELECT
id,
name,
affectedDefendersPlans,
affectedDefendersSubPlans,
environmentDetails,
healthDataClassification,
issues,
reportAdditionalData,
resourceDetails,
status,
systemData,
type
FROM azure.security.health_reports
WHERE scope = '{{ scope }}' -- required
;
```
</TabItem>
</Tabs>
