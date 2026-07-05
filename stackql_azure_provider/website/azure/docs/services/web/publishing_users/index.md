--- 
title: publishing_users
hide_title: false
hide_table_of_contents: false
keywords:
  - publishing_users
  - web
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

Creates, updates, deletes, gets or lists a <code>publishing_users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="publishing_users" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.publishing_users" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_publishing_user"
    values={[
        { label: 'get_publishing_user', value: 'get_publishing_user' }
    ]}
>
<TabItem value="get_publishing_user">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="publishingPassword" /></td>
    <td><code>string</code></td>
    <td>Password used for publishing.</td>
</tr>
<tr>
    <td><CopyableCode code="publishingPasswordHash" /></td>
    <td><code>string</code></td>
    <td>Password hash used for publishing.</td>
</tr>
<tr>
    <td><CopyableCode code="publishingPasswordHashSalt" /></td>
    <td><code>string</code></td>
    <td>Password hash salt used for publishing.</td>
</tr>
<tr>
    <td><CopyableCode code="publishingUserName" /></td>
    <td><code>string</code></td>
    <td>Username used for publishing. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="scmUri" /></td>
    <td><code>string</code></td>
    <td>Url of SCM site.</td>
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
    <td><a href="#get_publishing_user"><CopyableCode code="get_publishing_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Gets publishing user. Description for Gets publishing user.</td>
</tr>
<tr>
    <td><a href="#update_publishing_user"><CopyableCode code="update_publishing_user" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td></td>
    <td></td>
    <td>Updates publishing user. Description for Updates publishing user.</td>
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
    defaultValue="get_publishing_user"
    values={[
        { label: 'get_publishing_user', value: 'get_publishing_user' }
    ]}
>
<TabItem value="get_publishing_user">

Gets publishing user. Description for Gets publishing user.

```sql
SELECT
id,
name,
kind,
publishingPassword,
publishingPasswordHash,
publishingPasswordHashSalt,
publishingUserName,
scmUri,
systemData,
type
FROM azure.web.publishing_users
;
```
</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_publishing_user"
    values={[
        { label: 'update_publishing_user', value: 'update_publishing_user' }
    ]}
>
<TabItem value="update_publishing_user">

Updates publishing user. Description for Updates publishing user.

```sql
UPDATE azure.web.publishing_users
SET 
properties = '{{ properties }}',
kind = '{{ kind }}'
RETURNING
id,
name,
kind,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
