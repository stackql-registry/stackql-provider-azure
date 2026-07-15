--- 
title: github_issues
hide_title: false
hide_table_of_contents: false
keywords:
  - github_issues
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

Creates, updates, deletes, gets or lists a <code>github_issues</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="github_issues" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.github_issues" /></td></tr>
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
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-security_connector_name"><code>security_connector_name</code></a>, <a href="#parameter-owner_name"><code>owner_name</code></a>, <a href="#parameter-repo_name"><code>repo_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a GitHub issue for the specified repository and assessment. Creates a GitHub issue for the specified repository and assessment.</td>
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
<tr id="parameter-owner_name">
    <td><CopyableCode code="owner_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-repo_name">
    <td><CopyableCode code="repo_name" /></td>
    <td><code>string</code></td>
    <td>Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-security_connector_name">
    <td><CopyableCode code="security_connector_name" /></td>
    <td><code>string</code></td>
    <td>The security connector name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Creates a GitHub issue for the specified repository and assessment. Creates a GitHub issue for the specified repository and assessment.

```sql
INSERT INTO azure.security.github_issues (
securityAssessmentResourceId,
resource_group_name,
security_connector_name,
owner_name,
repo_name,
subscription_id
)
SELECT 
'{{ securityAssessmentResourceId }}',
'{{ resource_group_name }}',
'{{ security_connector_name }}',
'{{ owner_name }}',
'{{ repo_name }}',
'{{ subscription_id }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: github_issues
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the github_issues resource.
    - name: security_connector_name
      value: "{{ security_connector_name }}"
      description: Required parameter for the github_issues resource.
    - name: owner_name
      value: "{{ owner_name }}"
      description: Required parameter for the github_issues resource.
    - name: repo_name
      value: "{{ repo_name }}"
      description: Required parameter for the github_issues resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the github_issues resource.
    - name: securityAssessmentResourceId
      value: "{{ securityAssessmentResourceId }}"
      description: |
        The security assessment resource id that the issue will be opened based on.
`}</CodeBlock>

</TabItem>
</Tabs>
