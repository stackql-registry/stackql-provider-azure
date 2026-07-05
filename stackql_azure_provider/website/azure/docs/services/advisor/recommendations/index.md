--- 
title: recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendations
  - advisor
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

Creates, updates, deletes, gets or lists a <code>recommendations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="recommendations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.advisor.recommendations" /></td></tr>
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
    <td>The resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The list of recommended actions to implement recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the recommendation. Known values are: "HighAvailability", "Security", "Performance", "Cost", and "OperationalExcellence".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The detailed description of recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="exposedMetadataProperties" /></td>
    <td><code>object</code></td>
    <td>The recommendation metadata properties exposed to customer to provide additional information.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Extended properties.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>string</code></td>
    <td>The business impact of the recommendation. Known values are: "High", "Medium", and "Low".</td>
</tr>
<tr>
    <td><CopyableCode code="impactedField" /></td>
    <td><code>string</code></td>
    <td>The resource type identified by Advisor.</td>
</tr>
<tr>
    <td><CopyableCode code="impactedValue" /></td>
    <td><code>string</code></td>
    <td>The resource identified by Advisor.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The label of recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The most recent time that Advisor checked the validity of the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="learnMoreLink" /></td>
    <td><code>string</code></td>
    <td>The link to learn more about recommendation and generation logic.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The recommendation metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="potentialBenefits" /></td>
    <td><code>string</code></td>
    <td>The potential benefit of implementing recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationTypeId" /></td>
    <td><code>string</code></td>
    <td>The recommendation-type GUID.</td>
</tr>
<tr>
    <td><CopyableCode code="remediation" /></td>
    <td><code>object</code></td>
    <td>The automated way to apply recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMetadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of resource that was assessed.</td>
</tr>
<tr>
    <td><CopyableCode code="shortDescription" /></td>
    <td><code>object</code></td>
    <td>A summary of the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="suppressionIds" /></td>
    <td><code>array</code></td>
    <td>The list of snoozed and dismissed rules for the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td>The resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="actions" /></td>
    <td><code>array</code></td>
    <td>The list of recommended actions to implement recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="category" /></td>
    <td><code>string</code></td>
    <td>The category of the recommendation. Known values are: "HighAvailability", "Security", "Performance", "Cost", and "OperationalExcellence".</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The detailed description of recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="exposedMetadataProperties" /></td>
    <td><code>object</code></td>
    <td>The recommendation metadata properties exposed to customer to provide additional information.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Extended properties.</td>
</tr>
<tr>
    <td><CopyableCode code="impact" /></td>
    <td><code>string</code></td>
    <td>The business impact of the recommendation. Known values are: "High", "Medium", and "Low".</td>
</tr>
<tr>
    <td><CopyableCode code="impactedField" /></td>
    <td><code>string</code></td>
    <td>The resource type identified by Advisor.</td>
</tr>
<tr>
    <td><CopyableCode code="impactedValue" /></td>
    <td><code>string</code></td>
    <td>The resource identified by Advisor.</td>
</tr>
<tr>
    <td><CopyableCode code="label" /></td>
    <td><code>string</code></td>
    <td>The label of recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdated" /></td>
    <td><code>string (date-time)</code></td>
    <td>The most recent time that Advisor checked the validity of the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="learnMoreLink" /></td>
    <td><code>string</code></td>
    <td>The link to learn more about recommendation and generation logic.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The recommendation metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="potentialBenefits" /></td>
    <td><code>string</code></td>
    <td>The potential benefit of implementing recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="recommendationTypeId" /></td>
    <td><code>string</code></td>
    <td>The recommendation-type GUID.</td>
</tr>
<tr>
    <td><CopyableCode code="remediation" /></td>
    <td><code>object</code></td>
    <td>The automated way to apply recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceMetadata" /></td>
    <td><code>object</code></td>
    <td>Metadata of resource that was assessed.</td>
</tr>
<tr>
    <td><CopyableCode code="shortDescription" /></td>
    <td><code>object</code></td>
    <td>A summary of the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="suppressionIds" /></td>
    <td><code>array</code></td>
    <td>The list of snoozed and dismissed rules for the recommendation.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-recommendation_id"><code>recommendation_id</code></a></td>
    <td></td>
    <td>Obtains details of a cached recommendation.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$skipToken"><code>$skipToken</code></a></td>
    <td>Obtains cached recommendations for a subscription. The recommendations are generated or computed by invoking generateRecommendations.</td>
</tr>
<tr>
    <td><a href="#get_generate_status"><CopyableCode code="get_generate_status" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves the status of the recommendation computation or generation process. Invoke this API after calling the generation recommendation. The URI of this API is returned in the Location field of the response header.</td>
</tr>
<tr>
    <td><a href="#generate"><CopyableCode code="generate" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Initiates the recommendation generation or computation process for a subscription. This operation is asynchronous. The generated recommendations are stored in a cache in the Advisor service.</td>
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
    <td>The operation ID, which can be found from the Location field in the generate recommendation response header. Required.</td>
</tr>
<tr id="parameter-recommendation_id">
    <td><CopyableCode code="recommendation_id" /></td>
    <td><code>string</code></td>
    <td>The recommendation ID. Required.</td>
</tr>
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply to the recommendations.\ Filter can be applied to properties ['ResourceId', 'ResourceGroup', 'RecommendationTypeGuid', '\ `Category <#category>`_\ '] with operators ['eq', 'and', 'or'].\ Example:\ - $filter=Category eq 'Cost' and ResourceGroup eq 'MyResourceGroup'. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>The page-continuation token to use with a paged version of this API. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of recommendations per page if a paged version of this API is being used. Default value is None.</td>
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

Obtains details of a cached recommendation.

```sql
SELECT
id,
name,
actions,
category,
description,
exposedMetadataProperties,
extendedProperties,
impact,
impactedField,
impactedValue,
label,
lastUpdated,
learnMoreLink,
metadata,
potentialBenefits,
recommendationTypeId,
remediation,
resourceMetadata,
shortDescription,
suppressionIds,
type
FROM azure.advisor.recommendations
WHERE resource_uri = '{{ resource_uri }}' -- required
AND recommendation_id = '{{ recommendation_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Obtains cached recommendations for a subscription. The recommendations are generated or computed by invoking generateRecommendations.

```sql
SELECT
id,
name,
actions,
category,
description,
exposedMetadataProperties,
extendedProperties,
impact,
impactedField,
impactedValue,
label,
lastUpdated,
learnMoreLink,
metadata,
potentialBenefits,
recommendationTypeId,
remediation,
resourceMetadata,
shortDescription,
suppressionIds,
type
FROM azure.advisor.recommendations
WHERE subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $skipToken = '{{ $skipToken }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_generate_status"
    values={[
        { label: 'get_generate_status', value: 'get_generate_status' },
        { label: 'generate', value: 'generate' }
    ]}
>
<TabItem value="get_generate_status">

Retrieves the status of the recommendation computation or generation process. Invoke this API after calling the generation recommendation. The URI of this API is returned in the Location field of the response header.

```sql
EXEC azure.advisor.recommendations.get_generate_status 
@operation_id='{{ operation_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="generate">

Initiates the recommendation generation or computation process for a subscription. This operation is asynchronous. The generated recommendations are stored in a cache in the Advisor service.

```sql
EXEC azure.advisor.recommendations.generate 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
