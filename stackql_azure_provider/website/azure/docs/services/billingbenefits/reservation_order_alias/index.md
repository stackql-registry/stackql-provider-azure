--- 
title: reservation_order_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - reservation_order_alias
  - billingbenefits
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

Creates, updates, deletes, gets or lists a <code>reservation_order_alias</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="reservation_order_alias" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billingbenefits.reservation_order_alias" /></td></tr>
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
    <td><CopyableCode code="appliedScopeProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to applied scope type. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="appliedScopeType" /></td>
    <td><code>string</code></td>
    <td>Type of the Applied Scope. Known values are: "Single", "Shared", and "ManagementGroup". (Single, Shared, ManagementGroup)</td>
</tr>
<tr>
    <td><CopyableCode code="billingPlan" /></td>
    <td><code>string</code></td>
    <td>Represents the billing plan in ISO 8601 format. Required only for monthly billing plans. "P1M" (P1M)</td>
</tr>
<tr>
    <td><CopyableCode code="billingScopeId" /></td>
    <td><code>string</code></td>
    <td>Subscription that will be charged for purchasing the benefit.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure Region where the reserved resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state. Known values are: "Creating", "PendingBilling", "ConfirmedBilling", "Created", "Succeeded", "Cancelled", "Expired", and "Failed". (Creating, PendingBilling, ConfirmedBilling, Created, Succeeded, Cancelled, Expired, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="quantity" /></td>
    <td><code>integer</code></td>
    <td>Total Quantity of the SKUs purchased in the Reservation.</td>
</tr>
<tr>
    <td><CopyableCode code="renew" /></td>
    <td><code>boolean</code></td>
    <td>Setting this to true will automatically purchase a new benefit on the expiration date time.</td>
</tr>
<tr>
    <td><CopyableCode code="reservationOrderId" /></td>
    <td><code>string</code></td>
    <td>Identifier of the reservation order created.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceProperties" /></td>
    <td><code>object</code></td>
    <td>Properties specific to each reserved resource type. Not required if not applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="reservedResourceType" /></td>
    <td><code>string</code></td>
    <td>The type of the resource that is being reserved. Known values are: "VirtualMachines", "SqlDatabases", "SuseLinux", "CosmosDb", "RedHat", "SqlDataWarehouse", "VMwareCloudSimple", "RedHatOsa", "Databricks", "AppService", "ManagedDisk", "BlockBlob", "RedisCache", "AzureDataExplorer", "MySql", "MariaDb", "PostgreSql", "DedicatedHost", "SapHana", "SqlAzureHybridBenefit", "AVS", "DataFactory", "NetAppStorage", "AzureFiles", "SqlEdge", and "VirtualMachineSoftware". (VirtualMachines, SqlDatabases, SuseLinux, CosmosDb, RedHat, SqlDataWarehouse, VMwareCloudSimple, RedHatOsa, Databricks, AppService, ManagedDisk, BlockBlob, RedisCache, AzureDataExplorer, MySql, MariaDb, PostgreSql, DedicatedHost, SapHana, SqlAzureHybridBenefit, AVS, DataFactory, NetAppStorage, AzureFiles, SqlEdge, VirtualMachineSoftware)</td>
</tr>
<tr>
    <td><CopyableCode code="reviewDateTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>This is the date-time when the Reservation needs to be reviewed.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>Reservation order SKU. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="term" /></td>
    <td><code>string</code></td>
    <td>Represent benefit term in ISO 8601 format. Known values are: "P1M", "P1Y", "P3Y", and "P5Y". (P1M, P1Y, P3Y, P5Y)</td>
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
    <td><a href="#parameter-reservation_order_alias_name"><code>reservation_order_alias_name</code></a></td>
    <td></td>
    <td>Get a reservation order alias.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-reservation_order_alias_name"><code>reservation_order_alias_name</code></a>, <a href="#parameter-sku"><code>sku</code></a></td>
    <td></td>
    <td>Create a reservation order alias.</td>
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
<tr id="parameter-reservation_order_alias_name">
    <td><CopyableCode code="reservation_order_alias_name" /></td>
    <td><code>string</code></td>
    <td>Name of the reservation order alias. Required.</td>
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

Get a reservation order alias.

```sql
SELECT
id,
name,
appliedScopeProperties,
appliedScopeType,
billingPlan,
billingScopeId,
displayName,
location,
provisioningState,
quantity,
renew,
reservationOrderId,
reservedResourceProperties,
reservedResourceType,
reviewDateTime,
sku,
systemData,
term,
type
FROM azure.billingbenefits.reservation_order_alias
WHERE reservation_order_alias_name = '{{ reservation_order_alias_name }}' -- required
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

Create a reservation order alias.

```sql
INSERT INTO azure.billingbenefits.reservation_order_alias (
sku,
location,
properties,
reservation_order_alias_name
)
SELECT 
'{{ sku }}' /* required */,
'{{ location }}',
'{{ properties }}',
'{{ reservation_order_alias_name }}'
RETURNING
id,
name,
location,
properties,
sku,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: reservation_order_alias
  props:
    - name: reservation_order_alias_name
      value: "{{ reservation_order_alias_name }}"
      description: Required parameter for the reservation_order_alias resource.
    - name: sku
      description: |
        Reservation order SKU. Required.
      value:
        name: "{{ name }}"
    - name: location
      value: "{{ location }}"
      description: |
        The Azure Region where the reservation benefits are applied to.
    - name: properties
      description: |
        Reservation order alias request properties.
      value:
        displayName: "{{ displayName }}"
        billingScopeId: "{{ billingScopeId }}"
        term: "{{ term }}"
        billingPlan: "{{ billingPlan }}"
        appliedScopeType: "{{ appliedScopeType }}"
        appliedScopeProperties:
          tenantId: "{{ tenantId }}"
          managementGroupId: "{{ managementGroupId }}"
          subscriptionId: "{{ subscriptionId }}"
          resourceGroupId: "{{ resourceGroupId }}"
          displayName: "{{ displayName }}"
        quantity: {{ quantity }}
        renew: {{ renew }}
        reservedResourceType: "{{ reservedResourceType }}"
        reviewDateTime: "{{ reviewDateTime }}"
        reservedResourceProperties:
          instanceFlexibility: "{{ instanceFlexibility }}"
`}</CodeBlock>

</TabItem>
</Tabs>
