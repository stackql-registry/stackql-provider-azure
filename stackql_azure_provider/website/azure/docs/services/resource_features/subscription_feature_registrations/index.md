--- 
title: subscription_feature_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - subscription_feature_registrations
  - resource_features
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

Creates, updates, deletes, gets or lists a <code>subscription_feature_registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="subscription_feature_registrations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_features.subscription_feature_registrations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_all_by_subscription', value: 'list_all_by_subscription' }
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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="approvalType" /></td>
    <td><code>string</code></td>
    <td>The feature approval type. Known values are: "NotSpecified", "ApprovalRequired", and "AutoApproval".</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationProfile" /></td>
    <td><code>object</code></td>
    <td>Authorization Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The feature description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The featureDisplayName.</td>
</tr>
<tr>
    <td><CopyableCode code="documentationLink" /></td>
    <td><code>string</code></td>
    <td>The feature documentation link.</td>
</tr>
<tr>
    <td><CopyableCode code="featureName" /></td>
    <td><code>string</code></td>
    <td>The featureName.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs for meta data.</td>
</tr>
<tr>
    <td><CopyableCode code="providerNamespace" /></td>
    <td><code>string</code></td>
    <td>The providerNamespace.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The feature registration date.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The feature release date.</td>
</tr>
<tr>
    <td><CopyableCode code="shouldFeatureDisplayInPortal" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether feature should be displayed in Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state. Known values are: "NotSpecified", "NotRegistered", "Pending", "Registering", "Registered", "Unregistering", and "Unregistered".</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The subscriptionId.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_subscription">

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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="approvalType" /></td>
    <td><code>string</code></td>
    <td>The feature approval type. Known values are: "NotSpecified", "ApprovalRequired", and "AutoApproval".</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationProfile" /></td>
    <td><code>object</code></td>
    <td>Authorization Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The feature description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The featureDisplayName.</td>
</tr>
<tr>
    <td><CopyableCode code="documentationLink" /></td>
    <td><code>string</code></td>
    <td>The feature documentation link.</td>
</tr>
<tr>
    <td><CopyableCode code="featureName" /></td>
    <td><code>string</code></td>
    <td>The featureName.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs for meta data.</td>
</tr>
<tr>
    <td><CopyableCode code="providerNamespace" /></td>
    <td><code>string</code></td>
    <td>The providerNamespace.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The feature registration date.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The feature release date.</td>
</tr>
<tr>
    <td><CopyableCode code="shouldFeatureDisplayInPortal" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether feature should be displayed in Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state. Known values are: "NotSpecified", "NotRegistered", "Pending", "Registering", "Registered", "Unregistering", and "Unregistered".</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The subscriptionId.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_all_by_subscription">

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
    <td>Azure resource Id.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Azure resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="approvalType" /></td>
    <td><code>string</code></td>
    <td>The feature approval type. Known values are: "NotSpecified", "ApprovalRequired", and "AutoApproval".</td>
</tr>
<tr>
    <td><CopyableCode code="authorizationProfile" /></td>
    <td><code>object</code></td>
    <td>Authorization Profile.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The feature description.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>The featureDisplayName.</td>
</tr>
<tr>
    <td><CopyableCode code="documentationLink" /></td>
    <td><code>string</code></td>
    <td>The feature documentation link.</td>
</tr>
<tr>
    <td><CopyableCode code="featureName" /></td>
    <td><code>string</code></td>
    <td>The featureName.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Key-value pairs for meta data.</td>
</tr>
<tr>
    <td><CopyableCode code="providerNamespace" /></td>
    <td><code>string</code></td>
    <td>The providerNamespace.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The feature registration date.</td>
</tr>
<tr>
    <td><CopyableCode code="releaseDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The feature release date.</td>
</tr>
<tr>
    <td><CopyableCode code="shouldFeatureDisplayInPortal" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether feature should be displayed in Portal.</td>
</tr>
<tr>
    <td><CopyableCode code="state" /></td>
    <td><code>string</code></td>
    <td>The state. Known values are: "NotSpecified", "NotRegistered", "Pending", "Registering", "Registered", "Unregistering", and "Unregistered".</td>
</tr>
<tr>
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>The subscriptionId.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>The tenantId.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Azure resource type.</td>
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
    <td><a href="#parameter-provider_namespace"><code>provider_namespace</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns a feature registration.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-provider_namespace"><code>provider_namespace</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns subscription feature registrations for given subscription and provider namespace.</td>
</tr>
<tr>
    <td><a href="#list_all_by_subscription"><CopyableCode code="list_all_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns subscription feature registrations for given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-provider_namespace"><code>provider_namespace</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a feature registration.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-provider_namespace"><code>provider_namespace</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a feature registration.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-provider_namespace"><code>provider_namespace</code></a>, <a href="#parameter-feature_name"><code>feature_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a feature registration.</td>
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
<tr id="parameter-feature_name">
    <td><CopyableCode code="feature_name" /></td>
    <td><code>string</code></td>
    <td>The feature name. Required.</td>
</tr>
<tr id="parameter-provider_namespace">
    <td><CopyableCode code="provider_namespace" /></td>
    <td><code>string</code></td>
    <td>The provider namespace. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'list_all_by_subscription', value: 'list_all_by_subscription' }
    ]}
>
<TabItem value="get">

Returns a feature registration.

```sql
SELECT
id,
name,
approvalType,
authorizationProfile,
description,
displayName,
documentationLink,
featureName,
metadata,
providerNamespace,
registrationDate,
releaseDate,
shouldFeatureDisplayInPortal,
state,
subscriptionId,
tenantId,
type
FROM azure.resource_features.subscription_feature_registrations
WHERE provider_namespace = '{{ provider_namespace }}' -- required
AND feature_name = '{{ feature_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Returns subscription feature registrations for given subscription and provider namespace.

```sql
SELECT
id,
name,
approvalType,
authorizationProfile,
description,
displayName,
documentationLink,
featureName,
metadata,
providerNamespace,
registrationDate,
releaseDate,
shouldFeatureDisplayInPortal,
state,
subscriptionId,
tenantId,
type
FROM azure.resource_features.subscription_feature_registrations
WHERE provider_namespace = '{{ provider_namespace }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_all_by_subscription">

Returns subscription feature registrations for given subscription.

```sql
SELECT
id,
name,
approvalType,
authorizationProfile,
description,
displayName,
documentationLink,
featureName,
metadata,
providerNamespace,
registrationDate,
releaseDate,
shouldFeatureDisplayInPortal,
state,
subscriptionId,
tenantId,
type
FROM azure.resource_features.subscription_feature_registrations
WHERE subscription_id = '{{ subscription_id }}' -- required
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

Create or update a feature registration.

```sql
INSERT INTO azure.resource_features.subscription_feature_registrations (
properties,
provider_namespace,
feature_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ provider_namespace }}',
'{{ feature_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
properties,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: subscription_feature_registrations
  props:
    - name: provider_namespace
      value: "{{ provider_namespace }}"
      description: Required parameter for the subscription_feature_registrations resource.
    - name: feature_name
      value: "{{ feature_name }}"
      description: Required parameter for the subscription_feature_registrations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the subscription_feature_registrations resource.
    - name: properties
      description: |
        :vartype properties: ~azure.mgmt.resource.features.models.SubscriptionFeatureRegistrationProperties
      value:
        tenantId: "{{ tenantId }}"
        subscriptionId: "{{ subscriptionId }}"
        featureName: "{{ featureName }}"
        displayName: "{{ displayName }}"
        providerNamespace: "{{ providerNamespace }}"
        state: "{{ state }}"
        authorizationProfile:
          requestedTime: "{{ requestedTime }}"
          requester: "{{ requester }}"
          requesterObjectId: "{{ requesterObjectId }}"
          approvedTime: "{{ approvedTime }}"
          approver: "{{ approver }}"
        metadata: "{{ metadata }}"
        releaseDate: "{{ releaseDate }}"
        registrationDate: "{{ registrationDate }}"
        documentationLink: "{{ documentationLink }}"
        approvalType: "{{ approvalType }}"
        shouldFeatureDisplayInPortal: {{ shouldFeatureDisplayInPortal }}
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

Create or update a feature registration.

```sql
REPLACE azure.resource_features.subscription_feature_registrations
SET 
properties = '{{ properties }}'
WHERE 
provider_namespace = '{{ provider_namespace }}' --required
AND feature_name = '{{ feature_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
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

Deletes a feature registration.

```sql
DELETE FROM azure.resource_features.subscription_feature_registrations
WHERE provider_namespace = '{{ provider_namespace }}' --required
AND feature_name = '{{ feature_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
