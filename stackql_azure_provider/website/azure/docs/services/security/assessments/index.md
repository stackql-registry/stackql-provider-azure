--- 
title: assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments
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

Creates, updates, deletes, gets or lists an <code>assessments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="assessments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.assessments" /></td></tr>
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
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data regarding the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>object</code></td>
    <td>Links relevant to the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Describes properties of an assessment metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="partnersData" /></td>
    <td><code>object</code></td>
    <td>Data regarding 3rd party partner integration.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDetails" /></td>
    <td><code>object</code></td>
    <td>Details of the resource that was assessed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="risk" /></td>
    <td><code>object</code></td>
    <td>External model of risk result.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The result of the assessment. Required.</td>
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
    <td><CopyableCode code="additionalData" /></td>
    <td><code>object</code></td>
    <td>Additional data regarding the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>User friendly display name of the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="links" /></td>
    <td><code>object</code></td>
    <td>Links relevant to the assessment.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Describes properties of an assessment metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="partnersData" /></td>
    <td><code>object</code></td>
    <td>Data regarding 3rd party partner integration.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceDetails" /></td>
    <td><code>object</code></td>
    <td>Details of the resource that was assessed. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="risk" /></td>
    <td><code>object</code></td>
    <td>External model of risk result.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>The result of the assessment. Required.</td>
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
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get a security assessment on your scanned resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a></td>
    <td></td>
    <td>Get security assessments on all your scanned resources inside a scope.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a></td>
    <td></td>
    <td>Create a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a></td>
    <td></td>
    <td>Create a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-assessment_name"><code>assessment_name</code></a></td>
    <td></td>
    <td>Delete a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result.</td>
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
<tr id="parameter-assessment_name">
    <td><CopyableCode code="assessment_name" /></td>
    <td><code>string</code></td>
    <td>The Assessment Key - Unique key for the assessment type. Required.</td>
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
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>OData expand. Optional. Known values are: "links" and "metadata". Default value is None.</td>
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

Get a security assessment on your scanned resource.

```sql
SELECT
id,
name,
additionalData,
displayName,
links,
metadata,
partnersData,
resourceDetails,
risk,
status,
systemData,
type
FROM azure.security.assessments
WHERE resource_id = '{{ resource_id }}' -- required
AND assessment_name = '{{ assessment_name }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

Get security assessments on all your scanned resources inside a scope.

```sql
SELECT
id,
name,
additionalData,
displayName,
links,
metadata,
partnersData,
resourceDetails,
risk,
status,
systemData,
type
FROM azure.security.assessments
WHERE scope = '{{ scope }}' -- required
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

Create a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result.

```sql
INSERT INTO azure.security.assessments (
properties,
resource_id,
assessment_name
)
SELECT 
'{{ properties }}',
'{{ resource_id }}',
'{{ assessment_name }}'
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
- name: assessments
  props:
    - name: resource_id
      value: "{{ resource_id }}"
      description: Required parameter for the assessments resource.
    - name: assessment_name
      value: "{{ assessment_name }}"
      description: Required parameter for the assessments resource.
    - name: properties
      description: |
        Describes properties of an assessment.
      value:
        risk:
          riskFactors:
            - "{{ riskFactors }}"
          level: "{{ level }}"
          attackPathsReferences:
            - "{{ attackPathsReferences }}"
          paths:
            - id: "{{ id }}"
              nodes: "{{ nodes }}"
              edges: "{{ edges }}"
          isContextualRisk: {{ isContextualRisk }}
        resourceDetails:
          source: "{{ source }}"
        displayName: "{{ displayName }}"
        additionalData: "{{ additionalData }}"
        links:
          azurePortalUri: "{{ azurePortalUri }}"
        metadata:
          displayName: "{{ displayName }}"
          policyDefinitionId: "{{ policyDefinitionId }}"
          description: "{{ description }}"
          remediationDescription: "{{ remediationDescription }}"
          categories:
            - "{{ categories }}"
          severity: "{{ severity }}"
          userImpact: "{{ userImpact }}"
          implementationEffort: "{{ implementationEffort }}"
          threats:
            - "{{ threats }}"
          preview: {{ preview }}
          assessmentType: "{{ assessmentType }}"
          partnerData:
            partnerName: "{{ partnerName }}"
            productName: "{{ productName }}"
            secret: "{{ secret }}"
        partnersData:
          partnerName: "{{ partnerName }}"
          secret: "{{ secret }}"
        status:
          code: "{{ code }}"
          cause: "{{ cause }}"
          description: "{{ description }}"
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

Create a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result.

```sql
REPLACE azure.security.assessments
SET 
properties = '{{ properties }}'
WHERE 
resource_id = '{{ resource_id }}' --required
AND assessment_name = '{{ assessment_name }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete a security assessment on your resource. An assessment metadata that describes this assessment must be predefined with the same name before inserting the assessment result.

```sql
DELETE FROM azure.security.assessments
WHERE resource_id = '{{ resource_id }}' --required
AND assessment_name = '{{ assessment_name }}' --required
;
```
</TabItem>
</Tabs>
