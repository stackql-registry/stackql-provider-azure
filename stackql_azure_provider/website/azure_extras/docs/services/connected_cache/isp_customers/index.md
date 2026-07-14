--- 
title: isp_customers
hide_title: false
hide_table_of_contents: false
keywords:
  - isp_customers
  - connected_cache
  - azure_extras
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage azure_extras resources using SQL
custom_edit_url: null
image: /img/stackql-azure_extras-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import CodeBlock from '@theme/CodeBlock';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists an <code>isp_customers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="isp_customers" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.connected_cache.isp_customers" /></td></tr>
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
    <td><CopyableCode code="additionalCustomerProperties" /></td>
    <td><code>object</code></td>
    <td>Mcc customer resource additional properties.</td>
</tr>
<tr>
    <td><CopyableCode code="customer" /></td>
    <td><code>object</code></td>
    <td>Mcc customer resource (customer entity).</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Mcc response error details.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Unknown", "Accepted", "Upgrading", and "Deleting". (Succeeded, Failed, Canceled, Unknown, Accepted, Upgrading, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>HTTP error status code.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Mcc response status code.</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Mcc response status details for retrieving response inner details.</td>
</tr>
<tr>
    <td><CopyableCode code="statusText" /></td>
    <td><code>string</code></td>
    <td>Mcc response status text as string for retrieving status details.</td>
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
    <td><CopyableCode code="additionalCustomerProperties" /></td>
    <td><code>object</code></td>
    <td>Mcc customer resource additional properties.</td>
</tr>
<tr>
    <td><CopyableCode code="customer" /></td>
    <td><code>object</code></td>
    <td>Mcc customer resource (customer entity).</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Mcc response error details.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Unknown", "Accepted", "Upgrading", and "Deleting". (Succeeded, Failed, Canceled, Unknown, Accepted, Upgrading, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>HTTP error status code.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Mcc response status code.</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Mcc response status details for retrieving response inner details.</td>
</tr>
<tr>
    <td><CopyableCode code="statusText" /></td>
    <td><code>string</code></td>
    <td>Mcc response status text as string for retrieving status details.</td>
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
    <td><CopyableCode code="additionalCustomerProperties" /></td>
    <td><code>object</code></td>
    <td>Mcc customer resource additional properties.</td>
</tr>
<tr>
    <td><CopyableCode code="customer" /></td>
    <td><code>object</code></td>
    <td>Mcc customer resource (customer entity).</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Mcc response error details.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioned state of the resource. Known values are: "Succeeded", "Failed", "Canceled", "Unknown", "Accepted", "Upgrading", and "Deleting". (Succeeded, Failed, Canceled, Unknown, Accepted, Upgrading, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>HTTP error status code.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Mcc response status code.</td>
</tr>
<tr>
    <td><CopyableCode code="statusDetails" /></td>
    <td><code>string</code></td>
    <td>Mcc response status details for retrieving response inner details.</td>
</tr>
<tr>
    <td><CopyableCode code="statusText" /></td>
    <td><code>string</code></td>
    <td>Mcc response status text as string for retrieving status details.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the ispCustomer resource information using this get call.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api gets the information about all ispCustomer resources under the given subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api gets information about all ispCustomer resources under the given subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>This api creates an ispCustomer with the specified create parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api updates an existing ispCustomer resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>This api creates an ispCustomer with the specified create parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api deletes an existing ispCustomer resource.</td>
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
<tr id="parameter-customer_resource_name">
    <td><CopyableCode code="customer_resource_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Customer resource. Required.</td>
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

Gets the ispCustomer resource information using this get call.

```sql
SELECT
id,
name,
additionalCustomerProperties,
customer,
error,
location,
provisioningState,
status,
statusCode,
statusDetails,
statusText,
systemData,
tags,
type
FROM azure_extras.connected_cache.isp_customers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND customer_resource_name = '{{ customer_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

This api gets the information about all ispCustomer resources under the given subscription and resource group.

```sql
SELECT
id,
name,
additionalCustomerProperties,
customer,
error,
location,
provisioningState,
status,
statusCode,
statusDetails,
statusText,
systemData,
tags,
type
FROM azure_extras.connected_cache.isp_customers
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

This api gets information about all ispCustomer resources under the given subscription.

```sql
SELECT
id,
name,
additionalCustomerProperties,
customer,
error,
location,
provisioningState,
status,
statusCode,
statusDetails,
statusText,
systemData,
tags,
type
FROM azure_extras.connected_cache.isp_customers
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

This api creates an ispCustomer with the specified create parameters.

```sql
INSERT INTO azure_extras.connected_cache.isp_customers (
tags,
location,
properties,
resource_group_name,
customer_resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ customer_resource_name }}',
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
- name: isp_customers
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the isp_customers resource.
    - name: customer_resource_name
      value: "{{ customer_resource_name }}"
      description: Required parameter for the isp_customers resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the isp_customers resource.
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
        The resource-specific properties for this resource.
      value:
        provisioningState: "{{ provisioningState }}"
        customer:
          fullyQualifiedResourceId: "{{ fullyQualifiedResourceId }}"
          customerId: "{{ customerId }}"
          customerName: "{{ customerName }}"
          contactEmail: "{{ contactEmail }}"
          contactPhone: "{{ contactPhone }}"
          contactName: "{{ contactName }}"
          isEntitled: {{ isEntitled }}
          releaseVersion: {{ releaseVersion }}
          createAsyncOperationId: "{{ createAsyncOperationId }}"
          deleteAsyncOperationId: "{{ deleteAsyncOperationId }}"
          clientTenantId: "{{ clientTenantId }}"
          synchWithAzureAttemptsCount: {{ synchWithAzureAttemptsCount }}
          lastSyncWithAzureTimestamp: "{{ lastSyncWithAzureTimestamp }}"
          isEnterpriseManaged: {{ isEnterpriseManaged }}
          shouldMigrate: {{ shouldMigrate }}
          resendSignupCode: {{ resendSignupCode }}
          verifySignupCode: {{ verifySignupCode }}
          verifySignupPhrase: "{{ verifySignupPhrase }}"
        additionalCustomerProperties:
          customerPropertiesOverviewCacheEfficiency: {{ customerPropertiesOverviewCacheEfficiency }}
          customerPropertiesOverviewAverageEgressMbps: {{ customerPropertiesOverviewAverageEgressMbps }}
          customerPropertiesOverviewAverageMissMbps: {{ customerPropertiesOverviewAverageMissMbps }}
          customerPropertiesOverviewEgressMbpsMax: {{ customerPropertiesOverviewEgressMbpsMax }}
          customerPropertiesOverviewEgressMbpsMaxDateTime: "{{ customerPropertiesOverviewEgressMbpsMaxDateTime }}"
          customerPropertiesOverviewMissMbpsMax: {{ customerPropertiesOverviewMissMbpsMax }}
          customerPropertiesOverviewMissMbpsMaxDateTime: "{{ customerPropertiesOverviewMissMbpsMaxDateTime }}"
          customerPropertiesOverviewCacheNodesHealthyCount: {{ customerPropertiesOverviewCacheNodesHealthyCount }}
          customerPropertiesOverviewCacheNodesUnhealthyCount: {{ customerPropertiesOverviewCacheNodesUnhealthyCount }}
          signupStatus: {{ signupStatus }}
          signupStatusCode: {{ signupStatusCode }}
          signupStatusText: "{{ signupStatusText }}"
          signupPhaseStatusCode: {{ signupPhaseStatusCode }}
          signupPhaseStatusText: "{{ signupPhaseStatusText }}"
          peeringDbLastUpdateDate: "{{ peeringDbLastUpdateDate }}"
          customerOrgName: "{{ customerOrgName }}"
          customerEmail: "{{ customerEmail }}"
          customerTransitAsn: "{{ customerTransitAsn }}"
          customerTransitState: "{{ customerTransitState }}"
          customerAsn: "{{ customerAsn }}"
          customerAsnEstimatedEgressPeekGbps: {{ customerAsnEstimatedEgressPeekGbps }}
          customerEntitlementSkuId: "{{ customerEntitlementSkuId }}"
          customerEntitlementSkuGuid: "{{ customerEntitlementSkuGuid }}"
          customerEntitlementSkuName: "{{ customerEntitlementSkuName }}"
          customerEntitlementExpiration: "{{ customerEntitlementExpiration }}"
          optionalProperty1: "{{ optionalProperty1 }}"
          optionalProperty2: "{{ optionalProperty2 }}"
          optionalProperty3: "{{ optionalProperty3 }}"
          optionalProperty4: "{{ optionalProperty4 }}"
          optionalProperty5: "{{ optionalProperty5 }}"
        statusCode: "{{ statusCode }}"
        statusText: "{{ statusText }}"
        statusDetails: "{{ statusDetails }}"
        status: "{{ status }}"
        error:
          code: "{{ code }}"
          message: "{{ message }}"
          target: "{{ target }}"
          details:
            - code: "{{ code }}"
              message: "{{ message }}"
              target: "{{ target }}"
              details: "{{ details }}"
              additionalInfo: "{{ additionalInfo }}"
          additionalInfo:
            - type: "{{ type }}"
              info: "{{ info }}"
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

This api updates an existing ispCustomer resource.

```sql
UPDATE azure_extras.connected_cache.isp_customers
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND customer_resource_name = '{{ customer_resource_name }}' --required
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

This api creates an ispCustomer with the specified create parameters.

```sql
REPLACE azure_extras.connected_cache.isp_customers
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND customer_resource_name = '{{ customer_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
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

This api deletes an existing ispCustomer resource.

```sql
DELETE FROM azure_extras.connected_cache.isp_customers
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND customer_resource_name = '{{ customer_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
