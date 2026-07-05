--- 
title: generate_preview_artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - generate_preview_artifacts
  - devhub
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

Creates, updates, deletes, gets or lists a <code>generate_preview_artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="generate_preview_artifacts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.devhub.generate_preview_artifacts" /></td></tr>
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
    <td><a href="#generate_preview_artifacts"><CopyableCode code="generate_preview_artifacts" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-location"><code>location</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate preview dockerfile and manifests. Generate preview dockerfile and manifests.</td>
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
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="generate_preview_artifacts"
    values={[
        { label: 'generate_preview_artifacts', value: 'generate_preview_artifacts' }
    ]}
>
<TabItem value="generate_preview_artifacts">

Generate preview dockerfile and manifests. Generate preview dockerfile and manifests.

```sql
EXEC azure_extras.devhub.generate_preview_artifacts.generate_preview_artifacts 
@location='{{ location }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"generationLanguage": "{{ generationLanguage }}", 
"languageVersion": "{{ languageVersion }}", 
"builderVersion": "{{ builderVersion }}", 
"port": "{{ port }}", 
"appName": "{{ appName }}", 
"dockerfileOutputDirectory": "{{ dockerfileOutputDirectory }}", 
"manifestOutputDirectory": "{{ manifestOutputDirectory }}", 
"dockerfileGenerationMode": "{{ dockerfileGenerationMode }}", 
"manifestGenerationMode": "{{ manifestGenerationMode }}", 
"manifestType": "{{ manifestType }}", 
"imageName": "{{ imageName }}", 
"namespace": "{{ namespace }}", 
"imageTag": "{{ imageTag }}"
}'
;
```
</TabItem>
</Tabs>
