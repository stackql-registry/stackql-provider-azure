--- 
title: group_quota_location_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quota_location_settings
  - quota
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

Creates, updates, deletes, gets or lists a <code>group_quota_location_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="group_quota_location_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quota_location_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
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
    <td><CopyableCode code="enforcedGroupName" /></td>
    <td><code>string</code></td>
    <td>The name of the group that is enforced.</td>
</tr>
<tr>
    <td><CopyableCode code="enforcementEnabled" /></td>
    <td><code>string</code></td>
    <td>Is the GroupQuota Enforcement enabled for the Azure region. Known values are: "Enabled", "Disabled", and "NotAvailable". (Enabled, Disabled, NotAvailable)</td>
</tr>
<tr>
    <td><CopyableCode code="faultCode" /></td>
    <td><code>string</code></td>
    <td>Details of the failure.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Request status. Known values are: "Accepted", "Created", "Invalid", "Succeeded", "Escalated", "Failed", "InProgress", and "Canceled". (Accepted, Created, Invalid, Succeeded, Escalated, Failed, InProgress, Canceled)</td>
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
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-group_quota_name"><code>group_quota_name</code></a>, <a href="#parameter-resource_provider_name"><code>resource_provider_name</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Gets the GroupQuotas enforcement settings for the ResourceProvider/location. The locations, where GroupQuota enforcement is not enabled will return Not Found.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-group_quota_name"><code>group_quota_name</code></a>, <a href="#parameter-resource_provider_name"><code>resource_provider_name</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Enables the GroupQuotas enforcement for the resource provider and the location specified. The resource provider will start using the group quotas as the overall quota for the subscriptions included in the GroupQuota. The subscriptions cannot request quota at subscription level since it is now part of an enforced group. The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource - provider/location/resource. Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To disable GroupQuota Enforcement - 1. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions (Check the example - GroupQuotaSubscriptions_Delete). 2. Then delete the GroupQuota (Check the example - GroupQuotas_Delete).</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-group_quota_name"><code>group_quota_name</code></a>, <a href="#parameter-resource_provider_name"><code>resource_provider_name</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Enables the GroupQuotas enforcement for the resource provider and the location specified. The resource provider will start using the group quotas as the overall quota for the subscriptions included in the GroupQuota. The subscriptions cannot request quota at subscription level since it is now part of an enforced group. The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource - provider/location/resource. Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To disable GroupQuota Enforcement - 1. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions (Check the example - GroupQuotaSubscriptions_Delete). 2. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete).</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-management_group_id"><code>management_group_id</code></a>, <a href="#parameter-group_quota_name"><code>group_quota_name</code></a>, <a href="#parameter-resource_provider_name"><code>resource_provider_name</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Enables the GroupQuotas enforcement for the resource provider and the location specified. The resource provider will start using the group quotas as the overall quota for the subscriptions included in the GroupQuota. The subscriptions cannot request quota at subscription level since it is now part of an enforced group. The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource - provider/location/resource. Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To disable GroupQuota Enforcement - 1. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions (Check the example - GroupQuotaSubscriptions_Delete). 2. Then delete the GroupQuota (Check the example - GroupQuotas_Delete).</td>
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
<tr id="parameter-group_quota_name">
    <td><CopyableCode code="group_quota_name" /></td>
    <td><code>string</code></td>
    <td>The GroupQuota name. The name should be unique for the provided context tenantId/MgId. Required.</td>
</tr>
<tr id="parameter-location">
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure region. Required.</td>
</tr>
<tr id="parameter-management_group_id">
    <td><CopyableCode code="management_group_id" /></td>
    <td><code>string</code></td>
    <td>The management group ID. Required.</td>
</tr>
<tr id="parameter-resource_provider_name">
    <td><CopyableCode code="resource_provider_name" /></td>
    <td><code>string</code></td>
    <td>The resource provider name, such as - Microsoft.Compute. Currently only Microsoft.Compute resource provider supports this API. Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get">

Gets the GroupQuotas enforcement settings for the ResourceProvider/location. The locations, where GroupQuota enforcement is not enabled will return Not Found.

```sql
SELECT
id,
name,
enforcedGroupName,
enforcementEnabled,
faultCode,
provisioningState,
systemData,
type
FROM azure.quota.group_quota_location_settings
WHERE management_group_id = '{{ management_group_id }}' -- required
AND group_quota_name = '{{ group_quota_name }}' -- required
AND resource_provider_name = '{{ resource_provider_name }}' -- required
AND location = '{{ location }}' -- required
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

Enables the GroupQuotas enforcement for the resource provider and the location specified. The resource provider will start using the group quotas as the overall quota for the subscriptions included in the GroupQuota. The subscriptions cannot request quota at subscription level since it is now part of an enforced group. The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource - provider/location/resource. Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To disable GroupQuota Enforcement - 1. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions (Check the example - GroupQuotaSubscriptions_Delete). 2. Then delete the GroupQuota (Check the example - GroupQuotas_Delete).

```sql
INSERT INTO azure.quota.group_quota_location_settings (
properties,
management_group_id,
group_quota_name,
resource_provider_name,
location
)
SELECT 
'{{ properties }}',
'{{ management_group_id }}',
'{{ group_quota_name }}',
'{{ resource_provider_name }}',
'{{ location }}'
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
- name: group_quota_location_settings
  props:
    - name: management_group_id
      value: "{{ management_group_id }}"
      description: Required parameter for the group_quota_location_settings resource.
    - name: group_quota_name
      value: "{{ group_quota_name }}"
      description: Required parameter for the group_quota_location_settings resource.
    - name: resource_provider_name
      value: "{{ resource_provider_name }}"
      description: Required parameter for the group_quota_location_settings resource.
    - name: location
      value: "{{ location }}"
      description: Required parameter for the group_quota_location_settings resource.
    - name: properties
      description: |
        :vartype properties: ~azure.mgmt.quota.models.GroupQuotasEnforcementStatusProperties
      value:
        enforcementEnabled: "{{ enforcementEnabled }}"
        enforcedGroupName: "{{ enforcedGroupName }}"
        provisioningState: "{{ provisioningState }}"
        faultCode: "{{ faultCode }}"
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

Enables the GroupQuotas enforcement for the resource provider and the location specified. The resource provider will start using the group quotas as the overall quota for the subscriptions included in the GroupQuota. The subscriptions cannot request quota at subscription level since it is now part of an enforced group. The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource - provider/location/resource. Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To disable GroupQuota Enforcement - 1. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions (Check the example - GroupQuotaSubscriptions_Delete). 2. Ten delete the GroupQuota (Check the example - GroupQuotas_Delete).

```sql
UPDATE azure.quota.group_quota_location_settings
SET 
properties = '{{ properties }}'
WHERE 
management_group_id = '{{ management_group_id }}' --required
AND group_quota_name = '{{ group_quota_name }}' --required
AND resource_provider_name = '{{ resource_provider_name }}' --required
AND location = '{{ location }}' --required
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

Enables the GroupQuotas enforcement for the resource provider and the location specified. The resource provider will start using the group quotas as the overall quota for the subscriptions included in the GroupQuota. The subscriptions cannot request quota at subscription level since it is now part of an enforced group. The subscriptions share the GroupQuotaLimits assigned to the GroupQuota. If the GroupQuotaLimits is used, then submit a groupQuotaLimit request for the specific resource - provider/location/resource. Once the GroupQuota Enforcement is enabled then, it cannot be deleted or reverted back. To disable GroupQuota Enforcement - 1. Remove all the subscriptions from the groupQuota using the delete API for Subscriptions (Check the example - GroupQuotaSubscriptions_Delete). 2. Then delete the GroupQuota (Check the example - GroupQuotas_Delete).

```sql
REPLACE azure.quota.group_quota_location_settings
SET 
properties = '{{ properties }}'
WHERE 
management_group_id = '{{ management_group_id }}' --required
AND group_quota_name = '{{ group_quota_name }}' --required
AND resource_provider_name = '{{ resource_provider_name }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
</Tabs>
