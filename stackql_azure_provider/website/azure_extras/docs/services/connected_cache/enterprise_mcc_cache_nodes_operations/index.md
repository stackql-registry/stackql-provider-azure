--- 
title: enterprise_mcc_cache_nodes_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprise_mcc_cache_nodes_operations
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

Creates, updates, deletes, gets or lists an <code>enterprise_mcc_cache_nodes_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="enterprise_mcc_cache_nodes_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_enterprise_mcc_customer_resource', value: 'list_by_enterprise_mcc_customer_resource' }
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
    <td><CopyableCode code="additionalCacheNodeProperties" /></td>
    <td><code>object</code></td>
    <td>Mcc cache node resource additional properties.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheNode" /></td>
    <td><code>object</code></td>
    <td>Mcc cache node resource (cache node entity).</td>
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
<TabItem value="list_by_enterprise_mcc_customer_resource">

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
    <td><CopyableCode code="additionalCacheNodeProperties" /></td>
    <td><code>object</code></td>
    <td>Mcc cache node resource additional properties.</td>
</tr>
<tr>
    <td><CopyableCode code="cacheNode" /></td>
    <td><code>object</code></td>
    <td>Mcc cache node resource (cache node entity).</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api gets ispCacheNode resource information.</td>
</tr>
<tr>
    <td><a href="#list_by_enterprise_mcc_customer_resource"><CopyableCode code="list_by_enterprise_mcc_customer_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api retrieves information about all ispCacheNode resources under the given subscription and resource group.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>This api creates an ispCacheNode with the specified create parameters.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api updates an existing ispCacheNode resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>This api creates an ispCacheNode with the specified create parameters.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api deletes an existing ispCacheNode resource.</td>
</tr>
<tr>
    <td><a href="#get_cache_node_install_details"><CopyableCode code="get_cache_node_install_details" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api gets secrets of the ispCacheNode resource install details.</td>
</tr>
<tr>
    <td><a href="#get_cache_node_auto_update_history"><CopyableCode code="get_cache_node_auto_update_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api gets ispCacheNode resource auto update histrory information.</td>
</tr>
<tr>
    <td><a href="#get_cache_node_mcc_issue_details_history"><CopyableCode code="get_cache_node_mcc_issue_details_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api gets ispCacheNode resource issues details histrory information.</td>
</tr>
<tr>
    <td><a href="#get_cache_node_tls_certificate_history"><CopyableCode code="get_cache_node_tls_certificate_history" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-customer_resource_name"><code>customer_resource_name</code></a>, <a href="#parameter-cache_node_resource_name"><code>cache_node_resource_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>This api gets ispCacheNode resource tls certificate histrory information.</td>
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
<tr id="parameter-cache_node_resource_name">
    <td><CopyableCode code="cache_node_resource_name" /></td>
    <td><code>string</code></td>
    <td>Name of the ConnectedCache resource. Required.</td>
</tr>
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
        { label: 'list_by_enterprise_mcc_customer_resource', value: 'list_by_enterprise_mcc_customer_resource' }
    ]}
>
<TabItem value="get">

This api gets ispCacheNode resource information.

```sql
SELECT
id,
name,
additionalCacheNodeProperties,
cacheNode,
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
FROM azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND customer_resource_name = '{{ customer_resource_name }}' -- required
AND cache_node_resource_name = '{{ cache_node_resource_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_enterprise_mcc_customer_resource">

This api retrieves information about all ispCacheNode resources under the given subscription and resource group.

```sql
SELECT
id,
name,
additionalCacheNodeProperties,
cacheNode,
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
FROM azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND customer_resource_name = '{{ customer_resource_name }}' -- required
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

This api creates an ispCacheNode with the specified create parameters.

```sql
INSERT INTO azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations (
tags,
location,
properties,
resource_group_name,
customer_resource_name,
cache_node_resource_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ customer_resource_name }}',
'{{ cache_node_resource_name }}',
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
- name: enterprise_mcc_cache_nodes_operations
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the enterprise_mcc_cache_nodes_operations resource.
    - name: customer_resource_name
      value: "{{ customer_resource_name }}"
      description: Required parameter for the enterprise_mcc_cache_nodes_operations resource.
    - name: cache_node_resource_name
      value: "{{ cache_node_resource_name }}"
      description: Required parameter for the enterprise_mcc_cache_nodes_operations resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the enterprise_mcc_cache_nodes_operations resource.
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
        cacheNode:
          fullyQualifiedResourceId: "{{ fullyQualifiedResourceId }}"
          customerId: "{{ customerId }}"
          customerName: "{{ customerName }}"
          ipAddress: "{{ ipAddress }}"
          customerIndex: "{{ customerIndex }}"
          cacheNodeId: "{{ cacheNodeId }}"
          cacheNodeName: "{{ cacheNodeName }}"
          customerAsn: {{ customerAsn }}
          isEnabled: {{ isEnabled }}
          maxAllowableEgressInMbps: {{ maxAllowableEgressInMbps }}
          maxAllowableProbability: {{ maxAllowableProbability }}
          xCid: "{{ xCid }}"
          isEnterpriseManaged: {{ isEnterpriseManaged }}
          createAsyncOperationId: "{{ createAsyncOperationId }}"
          deleteAsyncOperationId: "{{ deleteAsyncOperationId }}"
          clientTenantId: "{{ clientTenantId }}"
          category: "{{ category }}"
          releaseVersion: {{ releaseVersion }}
          lastSyncWithAzureTimestamp: "{{ lastSyncWithAzureTimestamp }}"
          lastUpdatedTimestamp: "{{ lastUpdatedTimestamp }}"
          synchWithAzureAttemptsCount: {{ synchWithAzureAttemptsCount }}
          containerConfigurations: "{{ containerConfigurations }}"
          cidrCsv:
            - "{{ cidrCsv }}"
          cidrCsvLastUpdateTime: "{{ cidrCsvLastUpdateTime }}"
          bgpCidrCsvLastUpdateTime: "{{ bgpCidrCsvLastUpdateTime }}"
          bgpLastReportedTime: "{{ bgpLastReportedTime }}"
          bgpReviewStateText: "{{ bgpReviewStateText }}"
          bgpReviewState: "{{ bgpReviewState }}"
          bgpReviewFeedback: "{{ bgpReviewFeedback }}"
          bgpNumberOfTimesUpdated: {{ bgpNumberOfTimesUpdated }}
          bgpNumberOfRecords: {{ bgpNumberOfRecords }}
          bgpCidrBlocksCount: {{ bgpCidrBlocksCount }}
          bgpAddressSpace: {{ bgpAddressSpace }}
          shouldMigrate: {{ shouldMigrate }}
          bgpFileBytesTruncated: {{ bgpFileBytesTruncated }}
          cidrSelectionType: {{ cidrSelectionType }}
          isFrozen: {{ isFrozen }}
          reviewState: {{ reviewState }}
          reviewStateText: "{{ reviewStateText }}"
          reviewFeedback: "{{ reviewFeedback }}"
          configurationState: "{{ configurationState }}"
          configurationStateText: "{{ configurationStateText }}"
          addressSpace: {{ addressSpace }}
          workerConnections: {{ workerConnections }}
          workerConnectionsLastUpdatedDateTime: "{{ workerConnectionsLastUpdatedDateTime }}"
          containerResyncTrigger: {{ containerResyncTrigger }}
          imageUri: "{{ imageUri }}"
          fullyQualifiedDomainName: "{{ fullyQualifiedDomainName }}"
          autoUpdateRingType: "{{ autoUpdateRingType }}"
          autoUpdateRequestedWeek: {{ autoUpdateRequestedWeek }}
          autoUpdateRequestedDay: {{ autoUpdateRequestedDay }}
          autoUpdateRequestedTime: "{{ autoUpdateRequestedTime }}"
        additionalCacheNodeProperties:
          cacheNodePropertiesDetailsIssuesList:
            - "{{ cacheNodePropertiesDetailsIssuesList }}"
          issuesList:
            - "{{ issuesList }}"
          issuesCount: {{ issuesCount }}
          currentTlsCertificate:
            actionRequired: "{{ actionRequired }}"
            certificateFileName: "{{ certificateFileName }}"
            thumbprint: "{{ thumbprint }}"
            expiryDate: "{{ expiryDate }}"
            notBeforeDate: "{{ notBeforeDate }}"
            subject: "{{ subject }}"
            subjectAltName: "{{ subjectAltName }}"
          lastAutoUpdateInfo:
            imageUriBeforeUpdate: "{{ imageUriBeforeUpdate }}"
            imageUriTargeted: "{{ imageUriTargeted }}"
            imageUriTerminal: "{{ imageUriTerminal }}"
            autoUpdateRingType: {{ autoUpdateRingType }}
            movedToTerminalStateDateTime: "{{ movedToTerminalStateDateTime }}"
            ruleRequestedWeek: {{ ruleRequestedWeek }}
            ruleRequestedDay: {{ ruleRequestedDay }}
            createdDateTimeUtc: "{{ createdDateTimeUtc }}"
            updatedRegistryDateTimeUtc: "{{ updatedRegistryDateTimeUtc }}"
            planChangeLogText: "{{ planChangeLogText }}"
            autoUpdateLastAppliedStatus: {{ autoUpdateLastAppliedStatus }}
            autoUpdateLastAppliedStatusText: "{{ autoUpdateLastAppliedStatusText }}"
            autoUpdateLastAppliedStatusDetailedText: "{{ autoUpdateLastAppliedStatusDetailedText }}"
            planId: {{ planId }}
            timeToGoLiveDateTime: "{{ timeToGoLiveDateTime }}"
            ruleRequestedMinute: "{{ ruleRequestedMinute }}"
            ruleRequestedHour: "{{ ruleRequestedHour }}"
          aggregatedStatusDetails: "{{ aggregatedStatusDetails }}"
          aggregatedStatusText: "{{ aggregatedStatusText }}"
          aggregatedStatusCode: {{ aggregatedStatusCode }}
          productVersion: "{{ productVersion }}"
          isProvisioned: {{ isProvisioned }}
          cacheNodeStateDetailedText: "{{ cacheNodeStateDetailedText }}"
          cacheNodeStateShortText: "{{ cacheNodeStateShortText }}"
          cacheNodeState: {{ cacheNodeState }}
          driveConfiguration:
            - physicalPath: "{{ physicalPath }}"
              sizeInGb: {{ sizeInGb }}
              cacheNumber: {{ cacheNumber }}
              nginxMapping: "{{ nginxMapping }}"
          bgpConfiguration:
            asnToIpAddressMapping: "{{ asnToIpAddressMapping }}"
          proxyUrlConfiguration:
            proxyUrl: "{{ proxyUrl }}"
          isProxyRequired: "{{ isProxyRequired }}"
          osType: "{{ osType }}"
          autoUpdateVersion: "{{ autoUpdateVersion }}"
          updateInfoDetails: "{{ updateInfoDetails }}"
          updateRequestedDateTime: "{{ updateRequestedDateTime }}"
          autoUpdateNextAvailableVersion: "{{ autoUpdateNextAvailableVersion }}"
          autoUpdateNextAvailableDateTime: "{{ autoUpdateNextAvailableDateTime }}"
          autoUpdateAppliedVersion: "{{ autoUpdateAppliedVersion }}"
          autoUpdateLastAppliedDetails: "{{ autoUpdateLastAppliedDetails }}"
          autoUpdateLastAppliedState: "{{ autoUpdateLastAppliedState }}"
          autoUpdateLastAppliedDateTime: "{{ autoUpdateLastAppliedDateTime }}"
          autoUpdateLastTriggeredDateTime: "{{ autoUpdateLastTriggeredDateTime }}"
          creationMethod: {{ creationMethod }}
          tlsStatus: "{{ tlsStatus }}"
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

This api updates an existing ispCacheNode resource.

```sql
UPDATE azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND customer_resource_name = '{{ customer_resource_name }}' --required
AND cache_node_resource_name = '{{ cache_node_resource_name }}' --required
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

This api creates an ispCacheNode with the specified create parameters.

```sql
REPLACE azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND customer_resource_name = '{{ customer_resource_name }}' --required
AND cache_node_resource_name = '{{ cache_node_resource_name }}' --required
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

This api deletes an existing ispCacheNode resource.

```sql
DELETE FROM azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND customer_resource_name = '{{ customer_resource_name }}' --required
AND cache_node_resource_name = '{{ cache_node_resource_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_cache_node_install_details"
    values={[
        { label: 'get_cache_node_install_details', value: 'get_cache_node_install_details' },
        { label: 'get_cache_node_auto_update_history', value: 'get_cache_node_auto_update_history' },
        { label: 'get_cache_node_mcc_issue_details_history', value: 'get_cache_node_mcc_issue_details_history' },
        { label: 'get_cache_node_tls_certificate_history', value: 'get_cache_node_tls_certificate_history' }
    ]}
>
<TabItem value="get_cache_node_install_details">

This api gets secrets of the ispCacheNode resource install details.

```sql
EXEC azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations.get_cache_node_install_details 
@resource_group_name='{{ resource_group_name }}' --required, 
@customer_resource_name='{{ customer_resource_name }}' --required, 
@cache_node_resource_name='{{ cache_node_resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_cache_node_auto_update_history">

This api gets ispCacheNode resource auto update histrory information.

```sql
EXEC azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations.get_cache_node_auto_update_history 
@resource_group_name='{{ resource_group_name }}' --required, 
@customer_resource_name='{{ customer_resource_name }}' --required, 
@cache_node_resource_name='{{ cache_node_resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_cache_node_mcc_issue_details_history">

This api gets ispCacheNode resource issues details histrory information.

```sql
EXEC azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations.get_cache_node_mcc_issue_details_history 
@resource_group_name='{{ resource_group_name }}' --required, 
@customer_resource_name='{{ customer_resource_name }}' --required, 
@cache_node_resource_name='{{ cache_node_resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_cache_node_tls_certificate_history">

This api gets ispCacheNode resource tls certificate histrory information.

```sql
EXEC azure_extras.connected_cache.enterprise_mcc_cache_nodes_operations.get_cache_node_tls_certificate_history 
@resource_group_name='{{ resource_group_name }}' --required, 
@customer_resource_name='{{ customer_resource_name }}' --required, 
@cache_node_resource_name='{{ cache_node_resource_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
