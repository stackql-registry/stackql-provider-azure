--- 
title: quota_tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - quota_tiers
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>quota_tiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="quota_tiers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.quota_tiers" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="assignmentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date on which the current tier was assigned to the subscription (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="currentTierName" /></td>
    <td><code>string</code></td>
    <td>Name of the current quota tier for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tierUpgradeEligibilityInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the quota tier upgrade eligibility for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="tierUpgradePolicy" /></td>
    <td><code>string</code></td>
    <td>Gets the tier upgrade policy for the subscription. Known values are: "OnceUpgradeIsAvailable" and "NoAutoUpgrade". (OnceUpgradeIsAvailable, NoAutoUpgrade)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="assignmentDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date on which the current tier was assigned to the subscription (UTC).</td>
</tr>
<tr>
    <td><CopyableCode code="currentTierName" /></td>
    <td><code>string</code></td>
    <td>Name of the current quota tier for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tierUpgradeEligibilityInfo" /></td>
    <td><code>object</code></td>
    <td>Information about the quota tier upgrade eligibility for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="tierUpgradePolicy" /></td>
    <td><code>string</code></td>
    <td>Gets the tier upgrade policy for the subscription. Known values are: "OnceUpgradeIsAvailable" and "NoAutoUpgrade". (OnceUpgradeIsAvailable, NoAutoUpgrade)</td>
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
    <td><a href="#parameter-default_name"><code>default_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Quota Tier for a subscription. Gets the Quota Tier information for the given subscription. QuotaTiers is a subscription wide resource type. It holds current tier information.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns all the resources of a particular type belonging to a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-default_name"><code>default_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Quota Tier resource for a subscription. Update the Quota Tier information for the given subscription. QuotaTiers is a subscription wide resource type. It holds current tier information.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-default_name"><code>default_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Quota Tier resource for a subscription. The only properties that can be updated are "tierUpgradePolicy". Update the Quota Tier information for the given subscription. QuotaTiers is a subscription wide resource type. It holds current tier information.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-default_name"><code>default_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Quota Tier resource for a subscription. Update the Quota Tier information for the given subscription. QuotaTiers is a subscription wide resource type. It holds current tier information.</td>
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
<tr id="parameter-default_name">
    <td><CopyableCode code="default_name" /></td>
    <td><code>string</code></td>
    <td>Default parameter. Leave the value as default. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets the Quota Tier for a subscription. Gets the Quota Tier information for the given subscription. QuotaTiers is a subscription wide resource type. It holds current tier information.

```sql
SELECT
id,
name,
assignmentDate,
currentTierName,
systemData,
tierUpgradeEligibilityInfo,
tierUpgradePolicy,
type
FROM azure.cognitive_services.quota_tiers
WHERE default_name = '{{ default_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Returns all the resources of a particular type belonging to a subscription.

```sql
SELECT
id,
name,
assignmentDate,
currentTierName,
systemData,
tierUpgradeEligibilityInfo,
tierUpgradePolicy,
type
FROM azure.cognitive_services.quota_tiers
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

Updates the Quota Tier resource for a subscription. Update the Quota Tier information for the given subscription. QuotaTiers is a subscription wide resource type. It holds current tier information.

```sql
INSERT INTO azure.cognitive_services.quota_tiers (
properties,
default_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ default_name }}',
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
- name: quota_tiers
  props:
    - name: default_name
      value: "{{ default_name }}"
      description: Required parameter for the quota_tiers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the quota_tiers resource.
    - name: properties
      description: |
        Properties of quota tier resource.
      value:
        currentTierName: "{{ currentTierName }}"
        tierUpgradePolicy: "{{ tierUpgradePolicy }}"
        assignmentDate: "{{ assignmentDate }}"
        tierUpgradeEligibilityInfo:
          nextTierName: "{{ nextTierName }}"
          upgradeAvailabilityStatus: "{{ upgradeAvailabilityStatus }}"
          upgradeApplicableDate: "{{ upgradeApplicableDate }}"
          upgradeUnavailabilityReason: "{{ upgradeUnavailabilityReason }}"
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

Updates the Quota Tier resource for a subscription. The only properties that can be updated are "tierUpgradePolicy". Update the Quota Tier information for the given subscription. QuotaTiers is a subscription wide resource type. It holds current tier information.

```sql
UPDATE azure.cognitive_services.quota_tiers
SET 
properties = '{{ properties }}'
WHERE 
default_name = '{{ default_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
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

Updates the Quota Tier resource for a subscription. Update the Quota Tier information for the given subscription. QuotaTiers is a subscription wide resource type. It holds current tier information.

```sql
REPLACE azure.cognitive_services.quota_tiers
SET 
properties = '{{ properties }}'
WHERE 
default_name = '{{ default_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
