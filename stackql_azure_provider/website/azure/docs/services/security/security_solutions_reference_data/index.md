--- 
title: security_solutions_reference_data
hide_title: false
hide_table_of_contents: false
keywords:
  - security_solutions_reference_data
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

Creates, updates, deletes, gets or lists a <code>security_solutions_reference_data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="security_solutions_reference_data" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.security_solutions_reference_data" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_home_region"
    values={[
        { label: 'list_by_home_region', value: 'list_by_home_region' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_by_home_region">

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
    <td><CopyableCode code="alertVendorName" /></td>
    <td><code>string</code></td>
    <td>The security solutions' vendor name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where the resource is stored.</td>
</tr>
<tr>
    <td><CopyableCode code="packageInfoUrl" /></td>
    <td><code>string</code></td>
    <td>The security solutions' package info url. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The security solutions' product name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The security solutions' publisher. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDisplayName" /></td>
    <td><code>string</code></td>
    <td>The security solutions' publisher display name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="securityFamily" /></td>
    <td><code>string</code></td>
    <td>The security family of the security solution. Required. Known values are: "Waf", "Ngfw", "SaasWaf", and "Va". (Waf, Ngfw, SaasWaf, Va)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="template" /></td>
    <td><code>string</code></td>
    <td>The security solutions' template. Required.</td>
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
    <td><CopyableCode code="alertVendorName" /></td>
    <td><code>string</code></td>
    <td>The security solutions' vendor name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Location where the resource is stored.</td>
</tr>
<tr>
    <td><CopyableCode code="packageInfoUrl" /></td>
    <td><code>string</code></td>
    <td>The security solutions' package info url. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="productName" /></td>
    <td><code>string</code></td>
    <td>The security solutions' product name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="publisher" /></td>
    <td><code>string</code></td>
    <td>The security solutions' publisher. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherDisplayName" /></td>
    <td><code>string</code></td>
    <td>The security solutions' publisher display name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="securityFamily" /></td>
    <td><code>string</code></td>
    <td>The security family of the security solution. Required. Known values are: "Waf", "Ngfw", "SaasWaf", and "Va". (Waf, Ngfw, SaasWaf, Va)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="template" /></td>
    <td><code>string</code></td>
    <td>The security solutions' template. Required.</td>
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
    <td><a href="#list_by_home_region"><CopyableCode code="list_by_home_region" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-asc_location"><code>asc_location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets list of all supported Security Solutions for subscription and location.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a list of all supported Security Solutions for the subscription.</td>
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
<tr id="parameter-asc_location">
    <td><CopyableCode code="asc_location" /></td>
    <td><code>string</code></td>
    <td>The location where ASC stores the data of the subscription. can be retrieved from Get locations. Required.</td>
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
    defaultValue="list_by_home_region"
    values={[
        { label: 'list_by_home_region', value: 'list_by_home_region' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list_by_home_region">

Gets list of all supported Security Solutions for subscription and location.

```sql
SELECT
id,
name,
alertVendorName,
location,
packageInfoUrl,
productName,
publisher,
publisherDisplayName,
securityFamily,
systemData,
template,
type
FROM azure.security.security_solutions_reference_data
WHERE asc_location = '{{ asc_location }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of all supported Security Solutions for the subscription.

```sql
SELECT
id,
name,
alertVendorName,
location,
packageInfoUrl,
productName,
publisher,
publisherDisplayName,
securityFamily,
systemData,
template,
type
FROM azure.security.security_solutions_reference_data
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
