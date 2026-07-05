--- 
title: classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - classifiers
  - ai_documentintelligence
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

Creates, updates, deletes, gets or lists a <code>classifiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="classifiers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ai_documentintelligence.classifiers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_classifier"
    values={[
        { label: 'get_classifier', value: 'get_classifier' },
        { label: 'list_classifiers', value: 'list_classifiers' }
    ]}
>
<TabItem value="get_classifier">

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
    <td><CopyableCode code="apiVersion" /></td>
    <td><code>string</code></td>
    <td>API version used to create this document classifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="baseClassifierId" /></td>
    <td><code>string</code></td>
    <td>Base classifierId on top of which the classifier was trained.</td>
</tr>
<tr>
    <td><CopyableCode code="classifierId" /></td>
    <td><code>string</code></td>
    <td>Unique document classifier name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document classifier was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Document classifier description.</td>
</tr>
<tr>
    <td><CopyableCode code="docTypes" /></td>
    <td><code>object</code></td>
    <td>List of document types to classify against. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document classifier will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document model was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>List of warnings encountered while building the classifier.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_classifiers">

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
    <td><CopyableCode code="apiVersion" /></td>
    <td><code>string</code></td>
    <td>API version used to create this document classifier. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="baseClassifierId" /></td>
    <td><code>string</code></td>
    <td>Base classifierId on top of which the classifier was trained.</td>
</tr>
<tr>
    <td><CopyableCode code="classifierId" /></td>
    <td><code>string</code></td>
    <td>Unique document classifier name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document classifier was created. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Document classifier description.</td>
</tr>
<tr>
    <td><CopyableCode code="docTypes" /></td>
    <td><code>object</code></td>
    <td>List of document types to classify against. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document classifier will expire.</td>
</tr>
<tr>
    <td><CopyableCode code="modifiedDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time (UTC) when the document model was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="warnings" /></td>
    <td><code>array</code></td>
    <td>List of warnings encountered while building the classifier.</td>
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
    <td><a href="#get_classifier"><CopyableCode code="get_classifier" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-classifier_id"><code>classifier_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Gets detailed document classifier information.</td>
</tr>
<tr>
    <td><a href="#list_classifiers"><CopyableCode code="list_classifiers" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>List all document classifiers.</td>
</tr>
<tr>
    <td><a href="#delete_classifier"><CopyableCode code="delete_classifier" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-classifier_id"><code>classifier_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Deletes document classifier.</td>
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
<tr id="parameter-classifier_id">
    <td><CopyableCode code="classifier_id" /></td>
    <td><code>string</code></td>
    <td>Unique document classifier name. Required.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint, e.g. value of the client `endpoint` parameter. (default: )</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_classifier"
    values={[
        { label: 'get_classifier', value: 'get_classifier' },
        { label: 'list_classifiers', value: 'list_classifiers' }
    ]}
>
<TabItem value="get_classifier">

Gets detailed document classifier information.

```sql
SELECT
apiVersion,
baseClassifierId,
classifierId,
createdDateTime,
description,
docTypes,
expirationDateTime,
modifiedDateTime,
warnings
FROM azure.ai_documentintelligence.classifiers
WHERE classifier_id = '{{ classifier_id }}' -- required
AND endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
<TabItem value="list_classifiers">

List all document classifiers.

```sql
SELECT
apiVersion,
baseClassifierId,
classifierId,
createdDateTime,
description,
docTypes,
expirationDateTime,
modifiedDateTime,
warnings
FROM azure.ai_documentintelligence.classifiers
WHERE endpoint = '{{ endpoint }}' -- required
;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_classifier"
    values={[
        { label: 'delete_classifier', value: 'delete_classifier' }
    ]}
>
<TabItem value="delete_classifier">

Deletes document classifier.

```sql
DELETE FROM azure.ai_documentintelligence.classifiers
WHERE classifier_id = '{{ classifier_id }}' --required
AND endpoint = '{{ endpoint }}' --required
;
```
</TabItem>
</Tabs>
