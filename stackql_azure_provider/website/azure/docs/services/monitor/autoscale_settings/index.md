--- 
title: autoscale_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - autoscale_settings
  - monitor
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

Creates, updates, deletes, gets or lists an <code>autoscale_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="autoscale_settings" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.autoscale_settings" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is 'false'.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>array</code></td>
    <td>the collection of notifications.</td>
</tr>
<tr>
    <td><CopyableCode code="predictiveAutoscalePolicy" /></td>
    <td><code>object</code></td>
    <td>the predictive autoscale policy mode.</td>
</tr>
<tr>
    <td><CopyableCode code="profiles" /></td>
    <td><code>array</code></td>
    <td>the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified. Required.</td>
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
    <td><CopyableCode code="targetResourceLocation" /></td>
    <td><code>string</code></td>
    <td>the location of the resource that the autoscale setting should be added to.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceUri" /></td>
    <td><code>string</code></td>
    <td>the resource identifier of the resource that the autoscale setting should be added to.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

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
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is 'false'.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>array</code></td>
    <td>the collection of notifications.</td>
</tr>
<tr>
    <td><CopyableCode code="predictiveAutoscalePolicy" /></td>
    <td><code>object</code></td>
    <td>the predictive autoscale policy mode.</td>
</tr>
<tr>
    <td><CopyableCode code="profiles" /></td>
    <td><code>array</code></td>
    <td>the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified. Required.</td>
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
    <td><CopyableCode code="targetResourceLocation" /></td>
    <td><code>string</code></td>
    <td>the location of the resource that the autoscale setting should be added to.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceUri" /></td>
    <td><code>string</code></td>
    <td>the resource identifier of the resource that the autoscale setting should be added to.</td>
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
    <td><CopyableCode code="enabled" /></td>
    <td><code>boolean</code></td>
    <td>the enabled flag. Specifies whether automatic scaling is enabled for the resource. The default value is 'false'.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="notifications" /></td>
    <td><code>array</code></td>
    <td>the collection of notifications.</td>
</tr>
<tr>
    <td><CopyableCode code="predictiveAutoscalePolicy" /></td>
    <td><code>object</code></td>
    <td>the predictive autoscale policy mode.</td>
</tr>
<tr>
    <td><CopyableCode code="profiles" /></td>
    <td><code>array</code></td>
    <td>the collection of automatic scaling profiles that specify different scaling parameters for different time periods. A maximum of 20 profiles can be specified. Required.</td>
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
    <td><CopyableCode code="targetResourceLocation" /></td>
    <td><code>string</code></td>
    <td>the location of the resource that the autoscale setting should be added to.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceUri" /></td>
    <td><code>string</code></td>
    <td>the resource identifier of the resource that the autoscale setting should be added to.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autoscale_setting_name"><code>autoscale_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an autoscale setting.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the autoscale settings for a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the autoscale settings for a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autoscale_setting_name"><code>autoscale_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an autoscale setting.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autoscale_setting_name"><code>autoscale_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autoscale_setting_name"><code>autoscale_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or updates an autoscale setting.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-autoscale_setting_name"><code>autoscale_setting_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes and autoscale setting.</td>
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
<tr id="parameter-autoscale_setting_name">
    <td><CopyableCode code="autoscale_setting_name" /></td>
    <td><code>string</code></td>
    <td>The autoscale setting name. Required.</td>
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
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Gets an autoscale setting.

```sql
SELECT
id,
name,
enabled,
location,
notifications,
predictiveAutoscalePolicy,
profiles,
systemData,
tags,
targetResourceLocation,
targetResourceUri,
type
FROM azure.monitor.autoscale_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND autoscale_setting_name = '{{ autoscale_setting_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists the autoscale settings for a resource group.

```sql
SELECT
id,
name,
enabled,
location,
notifications,
predictiveAutoscalePolicy,
profiles,
systemData,
tags,
targetResourceLocation,
targetResourceUri,
type
FROM azure.monitor.autoscale_settings
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists the autoscale settings for a subscription.

```sql
SELECT
id,
name,
enabled,
location,
notifications,
predictiveAutoscalePolicy,
profiles,
systemData,
tags,
targetResourceLocation,
targetResourceUri,
type
FROM azure.monitor.autoscale_settings
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

Creates or updates an autoscale setting.

```sql
INSERT INTO azure.monitor.autoscale_settings (
tags,
location,
properties,
resource_group_name,
autoscale_setting_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ autoscale_setting_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: autoscale_settings
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the autoscale_settings resource.
    - name: autoscale_setting_name
      value: "{{ autoscale_setting_name }}"
      description: Required parameter for the autoscale_settings resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the autoscale_settings resource.
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
        The autoscale setting of the resource. Required.
      value:
        profiles:
          - name: "{{ name }}"
            capacity:
              minimum: "{{ minimum }}"
              maximum: "{{ maximum }}"
              default: "{{ default }}"
            rules: "{{ rules }}"
            fixedDate:
              timeZone: "{{ timeZone }}"
              start: "{{ start }}"
              end: "{{ end }}"
            recurrence:
              frequency: "{{ frequency }}"
              schedule:
                timeZone: "{{ timeZone }}"
                days:
                  - "{{ days }}"
                hours:
                  - {{ hours }}
                minutes:
                  - {{ minutes }}
        notifications:
          - operation: "{{ operation }}"
            email:
              sendToSubscriptionAdministrator: {{ sendToSubscriptionAdministrator }}
              sendToSubscriptionCoAdministrators: {{ sendToSubscriptionCoAdministrators }}
              customEmails:
                - "{{ customEmails }}"
            webhooks: "{{ webhooks }}"
        enabled: {{ enabled }}
        predictiveAutoscalePolicy:
          scaleMode: "{{ scaleMode }}"
          scaleLookAheadTime: "{{ scaleLookAheadTime }}"
        name: "{{ name }}"
        targetResourceUri: "{{ targetResourceUri }}"
        targetResourceLocation: "{{ targetResourceLocation }}"
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

Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method.

```sql
UPDATE azure.monitor.autoscale_settings
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND autoscale_setting_name = '{{ autoscale_setting_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Creates or updates an autoscale setting.

```sql
REPLACE azure.monitor.autoscale_settings
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND autoscale_setting_name = '{{ autoscale_setting_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
AND properties = '{{ properties }}' --required
RETURNING
id,
name,
location,
properties,
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

Deletes and autoscale setting.

```sql
DELETE FROM azure.monitor.autoscale_settings
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND autoscale_setting_name = '{{ autoscale_setting_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
