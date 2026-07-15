--- 
title: tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - tenants
  - resource
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

Creates, updates, deletes, gets or lists a <code>tenants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="tenants" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.tenants" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
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
    <td>The fully qualified ID of the tenant. For example, /tenants/8d65815f-a5b6-402f-9298-045155da7d74.</td>
</tr>
<tr>
    <td><CopyableCode code="country" /></td>
    <td><code>string</code></td>
    <td>Country/region name of the address for the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="countryCode" /></td>
    <td><code>string</code></td>
    <td>Country/region abbreviation for the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultDomain" /></td>
    <td><code>string</code></td>
    <td>The default domain for the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The display name of the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="domains" /></td>
    <td><code>array</code></td>
    <td>The list of domains for the tenant.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantBrandingLogoUrl" /></td>
    <td><code>string</code></td>
    <td>The tenant's branding logo URL. Only available for 'Home' tenant category.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantCategory" /></td>
    <td><code>string</code></td>
    <td>Category of the tenant. Known values are: "Home", "ProjectedBy", and "ManagedBy". (Home, ProjectedBy, ManagedBy)</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant ID. For example, 8d65815f-a5b6-402f-9298-045155da7d74.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantType" /></td>
    <td><code>string</code></td>
    <td>The tenant type. Only available for 'Home' tenant category.</td>
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
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets the tenants for your account.</td>
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
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="list">

Gets the tenants for your account.

```sql
SELECT
id,
country,
countryCode,
defaultDomain,
displayName,
domains,
tenantBrandingLogoUrl,
tenantCategory,
tenantId,
tenantType
FROM azure.resource.tenants
;
```
</TabItem>
</Tabs>
