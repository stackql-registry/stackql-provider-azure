--- 
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - cdn
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.policies" /></td></tr>
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
    <td><CopyableCode code="customRules" /></td>
    <td><code>object</code></td>
    <td>Describes custom rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointLinks" /></td>
    <td><code>array</code></td>
    <td>Describes Azure CDN endpoints associated with this Web Application Firewall policy.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets a unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing additional properties for Web Application Firewall policy.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedRules" /></td>
    <td><code>object</code></td>
    <td>Describes managed rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policySettings" /></td>
    <td><code>object</code></td>
    <td>Describes policySettings for policy.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the WebApplicationFirewallPolicy. Known values are: "Creating", "Succeeded", and "Failed". (Creating, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="rateLimitRules" /></td>
    <td><code>object</code></td>
    <td>Describes rate limit rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the policy. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", and "Deleting". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The pricing tier (defines a CDN provider, feature list and rate) of the CdnWebApplicationFirewallPolicy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><CopyableCode code="customRules" /></td>
    <td><code>object</code></td>
    <td>Describes custom rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="endpointLinks" /></td>
    <td><code>array</code></td>
    <td>Describes Azure CDN endpoints associated with this Web Application Firewall policy.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Gets a unique read-only string that changes whenever the resource is updated.</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing additional properties for Web Application Firewall policy.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedRules" /></td>
    <td><code>object</code></td>
    <td>Describes managed rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="policySettings" /></td>
    <td><code>object</code></td>
    <td>Describes policySettings for policy.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the WebApplicationFirewallPolicy. Known values are: "Creating", "Succeeded", and "Failed". (Creating, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="rateLimitRules" /></td>
    <td><code>object</code></td>
    <td>Describes rate limit rules inside the policy.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the policy. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", and "Deleting". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The pricing tier (defines a CDN provider, feature list and rate) of the CdnWebApplicationFirewallPolicy. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieve protection policy with specified name within a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the protection policies within a resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update policy with specified rule set name within a resource group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update an existing CdnWebApplicationFirewallPolicy with the specified policy name under the specified subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create or update policy with specified rule set name within a resource group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-policy_name"><code>policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes Policy.</td>
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
<tr id="parameter-policy_name">
    <td><CopyableCode code="policy_name" /></td>
    <td><code>string</code></td>
    <td>The name of the CdnWebApplicationFirewallPolicy. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
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

Retrieve protection policy with specified name within a resource group.

```sql
SELECT
id,
name,
customRules,
endpointLinks,
etag,
extendedProperties,
location,
managedRules,
policySettings,
provisioningState,
rateLimitRules,
resourceState,
sku,
systemData,
tags,
type
FROM azure.cdn.policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND policy_name = '{{ policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists all of the protection policies within a resource group.

```sql
SELECT
id,
name,
customRules,
endpointLinks,
etag,
extendedProperties,
location,
managedRules,
policySettings,
provisioningState,
rateLimitRules,
resourceState,
sku,
systemData,
tags,
type
FROM azure.cdn.policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create or update policy with specified rule set name within a resource group.

```sql
INSERT INTO azure.cdn.policies (
tags,
location,
properties,
etag,
sku,
resource_group_name,
policy_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ etag }}',
'{{ sku }}' /* required */,
'{{ resource_group_name }}',
'{{ policy_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
location,
properties,
sku,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the policies resource.
    - name: policy_name
      value: "{{ policy_name }}"
      description: Required parameter for the policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the policies resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives. Required.
    - name: properties
      description: |
        Properties of the web application firewall policy.
      value:
        policySettings:
          enabledState: "{{ enabledState }}"
          mode: "{{ mode }}"
          defaultRedirectUrl: "{{ defaultRedirectUrl }}"
          defaultCustomBlockResponseStatusCode: "{{ defaultCustomBlockResponseStatusCode }}"
          defaultCustomBlockResponseBody: "{{ defaultCustomBlockResponseBody }}"
        rateLimitRules:
          rules:
            - name: "{{ name }}"
              enabledState: "{{ enabledState }}"
              priority: {{ priority }}
              matchConditions: "{{ matchConditions }}"
              action: "{{ action }}"
              rateLimitThreshold: {{ rateLimitThreshold }}
              rateLimitDurationInMinutes: {{ rateLimitDurationInMinutes }}
        customRules:
          rules:
            - name: "{{ name }}"
              enabledState: "{{ enabledState }}"
              priority: {{ priority }}
              matchConditions: "{{ matchConditions }}"
              action: "{{ action }}"
        managedRules:
          managedRuleSets:
            - ruleSetType: "{{ ruleSetType }}"
              ruleSetVersion: "{{ ruleSetVersion }}"
              anomalyScore: {{ anomalyScore }}
              ruleGroupOverrides: "{{ ruleGroupOverrides }}"
        endpointLinks:
          - id: "{{ id }}"
        extendedProperties: "{{ extendedProperties }}"
        provisioningState: "{{ provisioningState }}"
        resourceState: "{{ resourceState }}"
    - name: etag
      value: "{{ etag }}"
      description: |
        Gets a unique read-only string that changes whenever the resource is updated.
    - name: sku
      description: |
        The pricing tier (defines a CDN provider, feature list and rate) of the CdnWebApplicationFirewallPolicy. Required.
      value:
        name: "{{ name }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update"
    values={[
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update">

Update an existing CdnWebApplicationFirewallPolicy with the specified policy name under the specified subscription and resource group.

```sql
UPDATE azure.cdn.policies
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND policy_name = '{{ policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
systemData,
tags,
type;
```
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

Create or update policy with specified rule set name within a resource group.

```sql
REPLACE azure.cdn.policies
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
etag = '{{ etag }}',
sku = '{{ sku }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND policy_name = '{{ policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND sku = '{{ sku }}' --required
RETURNING
id,
name,
etag,
location,
properties,
sku,
systemData,
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

Deletes Policy.

```sql
DELETE FROM azure.cdn.policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND policy_name = '{{ policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
