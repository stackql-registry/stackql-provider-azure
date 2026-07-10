--- 
title: analyze_from_image_datas
hide_title: false
hide_table_of_contents: false
keywords:
  - analyze_from_image_datas
  - ai_vision_imageanalysis
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

Creates, updates, deletes, gets or lists an <code>analyze_from_image_datas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="analyze_from_image_datas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_vision_imageanalysis.analyze_from_image_datas" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#analyze_from_image_data"><CopyableCode code="analyze_from_image_data" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-features"><code>features</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-language"><code>language</code></a>, <a href="#parameter-gender-neutral-caption"><code>gender-neutral-caption</code></a>, <a href="#parameter-smartcrops-aspect-ratios"><code>smartcrops-aspect-ratios</code></a>, <a href="#parameter-model-version"><code>model-version</code></a></td>
    <td>Performs a single Image Analysis operation.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme), e.g. myaccount.table.cosmos.azure.com:443 - value of the client `endpoint` parameter. (default: )</td>
</tr>
<tr id="parameter-features">
    <td><CopyableCode code="features" /></td>
    <td><code>array</code></td>
    <td>A list of visual features to analyze. Seven visual features are supported: Caption, DenseCaptions, Read (OCR), Tags, Objects, SmartCrops, and People. At least one visual feature must be specified. Required.</td>
</tr>
<tr id="parameter-gender-neutral-caption">
    <td><CopyableCode code="gender-neutral-caption" /></td>
    <td><code>boolean</code></td>
    <td>Boolean flag for enabling gender-neutral captioning for Caption and Dense Captions features. By default captions may contain gender terms (for example: 'man', 'woman', or 'boy', 'girl'). If you set this to "true", those will be replaced with gender-neutral terms (for example: 'person' or 'child'). Default value is None.</td>
</tr>
<tr id="parameter-language">
    <td><CopyableCode code="language" /></td>
    <td><code>string</code></td>
    <td>The desired language for result generation (a two-letter language code). If this option is not specified, the default value 'en' is used (English). See https://aka.ms/cv-languages for a list of supported languages. Default value is None.</td>
</tr>
<tr id="parameter-model-version">
    <td><CopyableCode code="model-version" /></td>
    <td><code>string</code></td>
    <td>The version of cloud AI-model used for analysis. The format is the following: 'latest' (default value) or 'YYYY-MM-DD' or 'YYYY-MM-DD-preview', where 'YYYY', 'MM', 'DD' are the year, month and day associated with the model. This is not commonly set, as the default always gives the latest AI model with recent improvements. If however you would like to make sure analysis results do not change over time, set this value to a specific model version. Default value is None.</td>
</tr>
<tr id="parameter-smartcrops-aspect-ratios">
    <td><CopyableCode code="smartcrops-aspect-ratios" /></td>
    <td><code>array</code></td>
    <td>A list of aspect ratios to use for smart cropping. Aspect ratios are calculated by dividing the target crop width in pixels by the height in pixels. Supported values are between 0.75 and 1.8 (inclusive). If this parameter is not specified, the service will return one crop region with an aspect ratio it sees fit between 0.5 and 2.0 (inclusive). Default value is None.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="analyze_from_image_data"
    values={[
        { label: 'analyze_from_image_data', value: 'analyze_from_image_data' }
    ]}
>
<TabItem value="analyze_from_image_data">

Performs a single Image Analysis operation.

```sql
EXEC azure.ai_vision_imageanalysis.analyze_from_image_datas.analyze_from_image_data 
@features='{{ features }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@language='{{ language }}', 
@gender-neutral-caption={{ gender-neutral-caption }}, 
@smartcrops-aspect-ratios='{{ smartcrops-aspect-ratios }}', 
@model-version='{{ model-version }}'
;
```
</TabItem>
</Tabs>
