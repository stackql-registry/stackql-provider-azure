--- 
title: integration_account_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_agreements
  - logic
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

Creates, updates, deletes, gets or lists an <code>integration_account_agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="integration_account_agreements" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic.integration_account_agreements" /></td></tr>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="agreementType" /></td>
    <td><code>string</code></td>
    <td>The agreement type. Required. Known values are: "NotSpecified", "AS2", "X12", and "Edifact".</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>The agreement content. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The created time.</td>
</tr>
<tr>
    <td><CopyableCode code="guestIdentity" /></td>
    <td><code>object</code></td>
    <td>The business identity of the guest partner. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="guestPartner" /></td>
    <td><code>string</code></td>
    <td>The integration account partner that is set as guest partner for this agreement. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hostIdentity" /></td>
    <td><code>object</code></td>
    <td>The business identity of the host partner. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hostPartner" /></td>
    <td><code>string</code></td>
    <td>The integration account partner that is set as host partner for this agreement. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the resource type.</td>
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
    <td>The resource id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Gets the resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="agreementType" /></td>
    <td><code>string</code></td>
    <td>The agreement type. Required. Known values are: "NotSpecified", "AS2", "X12", and "Edifact".</td>
</tr>
<tr>
    <td><CopyableCode code="changedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The changed time.</td>
</tr>
<tr>
    <td><CopyableCode code="content" /></td>
    <td><code>object</code></td>
    <td>The agreement content. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The created time.</td>
</tr>
<tr>
    <td><CopyableCode code="guestIdentity" /></td>
    <td><code>object</code></td>
    <td>The business identity of the guest partner. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="guestPartner" /></td>
    <td><code>string</code></td>
    <td>The integration account partner that is set as guest partner for this agreement. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hostIdentity" /></td>
    <td><code>object</code></td>
    <td>The business identity of the host partner. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="hostPartner" /></td>
    <td><code>string</code></td>
    <td>The integration account partner that is set as host partner for this agreement. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The resource location.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>The metadata.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Gets the resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-agreement_name"><code>agreement_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an integration account agreement.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$filter"><code>$filter</code></a></td>
    <td>Gets a list of integration account agreements.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-agreement_name"><code>agreement_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an integration account agreement.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-agreement_name"><code>agreement_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an integration account agreement.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-agreement_name"><code>agreement_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an integration account agreement.</td>
</tr>
<tr>
    <td><a href="#list_content_callback_url"><CopyableCode code="list_content_callback_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-integration_account_name"><code>integration_account_name</code></a>, <a href="#parameter-agreement_name"><code>agreement_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the content callback url.</td>
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
<tr id="parameter-agreement_name">
    <td><CopyableCode code="agreement_name" /></td>
    <td><code>string</code></td>
    <td>The integration account agreement name. Required.</td>
</tr>
<tr id="parameter-integration_account_name">
    <td><CopyableCode code="integration_account_name" /></td>
    <td><code>string</code></td>
    <td>The integration account name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The resource group name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Options for filters include: AgreementType. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of items to be included in the result. Default value is None.</td>
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

Gets an integration account agreement.

```sql
SELECT
id,
name,
agreementType,
changedTime,
content,
createdTime,
guestIdentity,
guestPartner,
hostIdentity,
hostPartner,
location,
metadata,
tags,
type
FROM azure.logic.integration_account_agreements
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND integration_account_name = '{{ integration_account_name }}' -- required
AND agreement_name = '{{ agreement_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets a list of integration account agreements.

```sql
SELECT
id,
name,
agreementType,
changedTime,
content,
createdTime,
guestIdentity,
guestPartner,
hostIdentity,
hostPartner,
location,
metadata,
tags,
type
FROM azure.logic.integration_account_agreements
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND integration_account_name = '{{ integration_account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
AND $filter = '{{ $filter }}'
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

Creates or updates an integration account agreement.

```sql
INSERT INTO azure.logic.integration_account_agreements (
location,
tags,
properties,
resource_group_name,
integration_account_name,
agreement_name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ integration_account_name }}',
'{{ agreement_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: integration_account_agreements
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the integration_account_agreements resource.
    - name: integration_account_name
      value: "{{ integration_account_name }}"
      description: Required parameter for the integration_account_agreements resource.
    - name: agreement_name
      value: "{{ agreement_name }}"
      description: Required parameter for the integration_account_agreements resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the integration_account_agreements resource.
    - name: location
      value: "{{ location }}"
      description: |
        The resource location.
    - name: tags
      value: "{{ tags }}"
      description: |
        The resource tags.
    - name: properties
      value:
        metadata: "{{ metadata }}"
        agreementType: "{{ agreementType }}"
        hostPartner: "{{ hostPartner }}"
        guestPartner: "{{ guestPartner }}"
        hostIdentity:
          qualifier: "{{ qualifier }}"
          value: "{{ value }}"
        guestIdentity:
          qualifier: "{{ qualifier }}"
          value: "{{ value }}"
        content:
          aS2:
            receiveAgreement:
              senderBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              receiverBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              protocolSettings:
                messageConnectionSettings: "{{ messageConnectionSettings }}"
                acknowledgementConnectionSettings: "{{ acknowledgementConnectionSettings }}"
                mdnSettings: "{{ mdnSettings }}"
                securitySettings: "{{ securitySettings }}"
                validationSettings: "{{ validationSettings }}"
                envelopeSettings: "{{ envelopeSettings }}"
                errorSettings: "{{ errorSettings }}"
            sendAgreement:
              senderBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              receiverBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              protocolSettings:
                messageConnectionSettings: "{{ messageConnectionSettings }}"
                acknowledgementConnectionSettings: "{{ acknowledgementConnectionSettings }}"
                mdnSettings: "{{ mdnSettings }}"
                securitySettings: "{{ securitySettings }}"
                validationSettings: "{{ validationSettings }}"
                envelopeSettings: "{{ envelopeSettings }}"
                errorSettings: "{{ errorSettings }}"
          x12:
            receiveAgreement:
              senderBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              receiverBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              protocolSettings:
                validationSettings: "{{ validationSettings }}"
                framingSettings: "{{ framingSettings }}"
                envelopeSettings: "{{ envelopeSettings }}"
                acknowledgementSettings: "{{ acknowledgementSettings }}"
                messageFilter: "{{ messageFilter }}"
                securitySettings: "{{ securitySettings }}"
                processingSettings: "{{ processingSettings }}"
                envelopeOverrides: "{{ envelopeOverrides }}"
                validationOverrides: "{{ validationOverrides }}"
                messageFilterList: "{{ messageFilterList }}"
                schemaReferences: "{{ schemaReferences }}"
                x12DelimiterOverrides: "{{ x12DelimiterOverrides }}"
            sendAgreement:
              senderBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              receiverBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              protocolSettings:
                validationSettings: "{{ validationSettings }}"
                framingSettings: "{{ framingSettings }}"
                envelopeSettings: "{{ envelopeSettings }}"
                acknowledgementSettings: "{{ acknowledgementSettings }}"
                messageFilter: "{{ messageFilter }}"
                securitySettings: "{{ securitySettings }}"
                processingSettings: "{{ processingSettings }}"
                envelopeOverrides: "{{ envelopeOverrides }}"
                validationOverrides: "{{ validationOverrides }}"
                messageFilterList: "{{ messageFilterList }}"
                schemaReferences: "{{ schemaReferences }}"
                x12DelimiterOverrides: "{{ x12DelimiterOverrides }}"
          edifact:
            receiveAgreement:
              senderBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              receiverBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              protocolSettings:
                validationSettings: "{{ validationSettings }}"
                framingSettings: "{{ framingSettings }}"
                envelopeSettings: "{{ envelopeSettings }}"
                acknowledgementSettings: "{{ acknowledgementSettings }}"
                messageFilter: "{{ messageFilter }}"
                processingSettings: "{{ processingSettings }}"
                envelopeOverrides: "{{ envelopeOverrides }}"
                messageFilterList: "{{ messageFilterList }}"
                schemaReferences: "{{ schemaReferences }}"
                validationOverrides: "{{ validationOverrides }}"
                edifactDelimiterOverrides: "{{ edifactDelimiterOverrides }}"
            sendAgreement:
              senderBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              receiverBusinessIdentity:
                qualifier: "{{ qualifier }}"
                value: "{{ value }}"
              protocolSettings:
                validationSettings: "{{ validationSettings }}"
                framingSettings: "{{ framingSettings }}"
                envelopeSettings: "{{ envelopeSettings }}"
                acknowledgementSettings: "{{ acknowledgementSettings }}"
                messageFilter: "{{ messageFilter }}"
                processingSettings: "{{ processingSettings }}"
                envelopeOverrides: "{{ envelopeOverrides }}"
                messageFilterList: "{{ messageFilterList }}"
                schemaReferences: "{{ schemaReferences }}"
                validationOverrides: "{{ validationOverrides }}"
                edifactDelimiterOverrides: "{{ edifactDelimiterOverrides }}"
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

Creates or updates an integration account agreement.

```sql
REPLACE azure.logic.integration_account_agreements
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND integration_account_name = '{{ integration_account_name }}' --required
AND agreement_name = '{{ agreement_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
location,
properties,
tags,
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

Deletes an integration account agreement.

```sql
DELETE FROM azure.logic.integration_account_agreements
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND integration_account_name = '{{ integration_account_name }}' --required
AND agreement_name = '{{ agreement_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_content_callback_url"
    values={[
        { label: 'list_content_callback_url', value: 'list_content_callback_url' }
    ]}
>
<TabItem value="list_content_callback_url">

Get the content callback url.

```sql
EXEC azure.logic.integration_account_agreements.list_content_callback_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@integration_account_name='{{ integration_account_name }}' --required, 
@agreement_name='{{ agreement_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"notAfter": "{{ notAfter }}", 
"keyType": "{{ keyType }}"
}'
;
```
</TabItem>
</Tabs>
