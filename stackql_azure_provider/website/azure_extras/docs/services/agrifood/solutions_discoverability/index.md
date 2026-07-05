--- 
title: solutions_discoverability
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions_discoverability
  - agrifood
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>solutions_discoverability</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="solutions_discoverability" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood.solutions_discoverability" /></td></tr>
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
    <td><CopyableCode code="accessFBApplicationId" /></td>
    <td><code>string</code></td>
    <td>Application id of the multi tenant application to be used by partner to access FarmBeats data.</td>
</tr>
<tr>
    <td><CopyableCode code="accessFBApplicationName" /></td>
    <td><code>string</code></td>
    <td>Application name of the multi tenant application to be used by partner to access FarmBeatsData.</td>
</tr>
<tr>
    <td><CopyableCode code="dataAccessScopes" /></td>
    <td><code>array</code></td>
    <td>Gets scope of the FarmBeats data access that's required for processing solution request to partner. Example: For gdd they might need weatherScope and satelliteScope.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluatedOutputsDictionary" /></td>
    <td><code>object</code></td>
    <td>Gets example name: insight sample response Dictionary to capture all variations of computed results ingested by partner.</td>
</tr>
<tr>
    <td><CopyableCode code="inputParametersValidationScopes" /></td>
    <td><code>array</code></td>
    <td>Gets scope of the FarmBeats related parameters that need to be validated in apiInputParameters. Example: For if 'FarmHierarchy' is the input scope for 'WeatherScope' data access For working with WeatherScope we need FarmHierarchy info implies 'farmerId', 'resourceId', 'resourceType' in request body.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceOfferDetails" /></td>
    <td><code>object</code></td>
    <td>:vartype marketplace_offer_details: ~azure.mgmt.agrifood.models.MarketplaceOfferDetails</td>
</tr>
<tr>
    <td><CopyableCode code="openApiSpecsDictionary" /></td>
    <td><code>object</code></td>
    <td>Gets apiVersion: Swagger Document Dictionary to capture all api versions of swagger exposed by partner to farmbeats.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerId" /></td>
    <td><code>string</code></td>
    <td>Solution Partner Id.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTenantId" /></td>
    <td><code>string</code></td>
    <td>Solution Partner Tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="roleId" /></td>
    <td><code>string</code></td>
    <td>Role Id of the SaaS multi tenant application to access relevant fb data.</td>
</tr>
<tr>
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>Role Name of the SaaS multi tenant application to access relevant fb data.</td>
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
    <td><CopyableCode code="accessFBApplicationId" /></td>
    <td><code>string</code></td>
    <td>Application id of the multi tenant application to be used by partner to access FarmBeats data.</td>
</tr>
<tr>
    <td><CopyableCode code="accessFBApplicationName" /></td>
    <td><code>string</code></td>
    <td>Application name of the multi tenant application to be used by partner to access FarmBeatsData.</td>
</tr>
<tr>
    <td><CopyableCode code="dataAccessScopes" /></td>
    <td><code>array</code></td>
    <td>Gets scope of the FarmBeats data access that's required for processing solution request to partner. Example: For gdd they might need weatherScope and satelliteScope.</td>
</tr>
<tr>
    <td><CopyableCode code="evaluatedOutputsDictionary" /></td>
    <td><code>object</code></td>
    <td>Gets example name: insight sample response Dictionary to capture all variations of computed results ingested by partner.</td>
</tr>
<tr>
    <td><CopyableCode code="inputParametersValidationScopes" /></td>
    <td><code>array</code></td>
    <td>Gets scope of the FarmBeats related parameters that need to be validated in apiInputParameters. Example: For if 'FarmHierarchy' is the input scope for 'WeatherScope' data access For working with WeatherScope we need FarmHierarchy info implies 'farmerId', 'resourceId', 'resourceType' in request body.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplaceOfferDetails" /></td>
    <td><code>object</code></td>
    <td>:vartype marketplace_offer_details: ~azure.mgmt.agrifood.models.MarketplaceOfferDetails</td>
</tr>
<tr>
    <td><CopyableCode code="openApiSpecsDictionary" /></td>
    <td><code>object</code></td>
    <td>Gets apiVersion: Swagger Document Dictionary to capture all api versions of swagger exposed by partner to farmbeats.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerId" /></td>
    <td><code>string</code></td>
    <td>Solution Partner Id.</td>
</tr>
<tr>
    <td><CopyableCode code="partnerTenantId" /></td>
    <td><code>string</code></td>
    <td>Solution Partner Tenant Id.</td>
</tr>
<tr>
    <td><CopyableCode code="roleId" /></td>
    <td><code>string</code></td>
    <td>Role Id of the SaaS multi tenant application to access relevant fb data.</td>
</tr>
<tr>
    <td><CopyableCode code="roleName" /></td>
    <td><code>string</code></td>
    <td>Role Name of the SaaS multi tenant application to access relevant fb data.</td>
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
    <td><a href="#parameter-farm_beats_solution_id"><code>farm_beats_solution_id</code></a></td>
    <td></td>
    <td>Get farmBeats solution by id.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$maxPageSize"><code>$maxPageSize</code></a></td>
    <td>Get list of farmBeats solutions.</td>
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
<tr id="parameter-farm_beats_solution_id">
    <td><CopyableCode code="farm_beats_solution_id" /></td>
    <td><code>string</code></td>
    <td>farmBeatsSolutionId to be queried. Required.</td>
</tr>
<tr id="parameter-$maxPageSize">
    <td><CopyableCode code="$maxPageSize" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of items needed (inclusive). Minimum = 10, Maximum = 1000, Default value = 50. Default value is 50.</td>
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

Get farmBeats solution by id.

```sql
SELECT
id,
name,
accessFBApplicationId,
accessFBApplicationName,
dataAccessScopes,
evaluatedOutputsDictionary,
inputParametersValidationScopes,
marketplaceOfferDetails,
openApiSpecsDictionary,
partnerId,
partnerTenantId,
roleId,
roleName,
systemData,
type
FROM azure_extras.agrifood.solutions_discoverability
WHERE farm_beats_solution_id = '{{ farm_beats_solution_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get list of farmBeats solutions.

```sql
SELECT
id,
name,
accessFBApplicationId,
accessFBApplicationName,
dataAccessScopes,
evaluatedOutputsDictionary,
inputParametersValidationScopes,
marketplaceOfferDetails,
openApiSpecsDictionary,
partnerId,
partnerTenantId,
roleId,
roleName,
systemData,
type
FROM azure_extras.agrifood.solutions_discoverability
WHERE $maxPageSize = '{{ $maxPageSize }}'
;
```
</TabItem>
</Tabs>
