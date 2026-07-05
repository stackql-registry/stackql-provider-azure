--- 
title: security_contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - security_contacts
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

Creates, updates, deletes, gets or lists a <code>security_contacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="security_contacts" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.security_contacts" /></td></tr>
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
    <td><CopyableCode code="emails" /></td>
    <td><code>string</code></td>
    <td>List of email addresses which will get notifications from Microsoft Defender for Cloud by the configurations defined in this security contact.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the security contact is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationsByRole" /></td>
    <td><code>object</code></td>
    <td>Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationsSources" /></td>
    <td><code>array</code></td>
    <td>A collection of sources types which evaluate the email notification.</td>
</tr>
<tr>
    <td><CopyableCode code="phone" /></td>
    <td><code>string</code></td>
    <td>The security contact's phone number.</td>
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
    <td><CopyableCode code="emails" /></td>
    <td><code>string</code></td>
    <td>List of email addresses which will get notifications from Microsoft Defender for Cloud by the configurations defined in this security contact.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the security contact is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationsByRole" /></td>
    <td><code>object</code></td>
    <td>Defines whether to send email notifications from Microsoft Defender for Cloud to persons with specific RBAC roles on the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="notificationsSources" /></td>
    <td><code>array</code></td>
    <td>A collection of sources types which evaluate the email notification.</td>
</tr>
<tr>
    <td><CopyableCode code="phone" /></td>
    <td><code>string</code></td>
    <td>The security contact's phone number.</td>
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
    <td><a href="#parameter-security_contact_name"><code>security_contact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Default Security contact configurations for the subscription.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List all security contact configurations for the subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-security_contact_name"><code>security_contact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create security contact configurations for the subscription.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-security_contact_name"><code>security_contact_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete security contact configurations for the subscription.</td>
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
<tr id="parameter-security_contact_name">
    <td><CopyableCode code="security_contact_name" /></td>
    <td><code>string</code></td>
    <td>Name of the security contact object. "default" Required.</td>
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
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get Default Security contact configurations for the subscription.

```sql
SELECT
id,
name,
emails,
isEnabled,
notificationsByRole,
notificationsSources,
phone,
systemData,
type
FROM azure.security.security_contacts
WHERE security_contact_name = '{{ security_contact_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List all security contact configurations for the subscription.

```sql
SELECT
id,
name,
emails,
isEnabled,
notificationsByRole,
notificationsSources,
phone,
systemData,
type
FROM azure.security.security_contacts
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create security contact configurations for the subscription.

```sql
INSERT INTO azure.security.security_contacts (
properties,
security_contact_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ security_contact_name }}',
'{{ subscription_id }}'
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
- name: security_contacts
  props:
    - name: security_contact_name
      value: "{{ security_contact_name }}"
      description: Required parameter for the security_contacts resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the security_contacts resource.
    - name: properties
      description: |
        Security contact data.
      value:
        emails: "{{ emails }}"
        phone: "{{ phone }}"
        isEnabled: {{ isEnabled }}
        notificationsSources:
          - sourceType: "{{ sourceType }}"
        notificationsByRole:
          state: "{{ state }}"
          roles:
            - "{{ roles }}"
`}</CodeBlock>

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

Delete security contact configurations for the subscription.

```sql
DELETE FROM azure.security.security_contacts
WHERE security_contact_name = '{{ security_contact_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
