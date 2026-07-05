--- 
title: data_collection_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rules
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

Creates, updates, deletes, gets or lists a <code>data_collection_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_collection_rules" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.data_collection_rules" /></td></tr>
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
    <td><CopyableCode code="agentSettings" /></td>
    <td><code>object</code></td>
    <td>Agent settings used to modify agent behavior on a given host.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionEndpointId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection endpoint that this rule can be used with.</td>
</tr>
<tr>
    <td><CopyableCode code="dataFlows" /></td>
    <td><code>array</code></td>
    <td>The specification of data flows.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSources" /></td>
    <td><code>object</code></td>
    <td>The specification of data sources. This property is optional and can be omitted if the rule is meant to be used via direct calls to the provisioned endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the data collection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="destinations" /></td>
    <td><code>object</code></td>
    <td>The specification of destinations.</td>
</tr>
<tr>
    <td><CopyableCode code="directDataSources" /></td>
    <td><code>object</code></td>
    <td>The specification of direct data sources. This property is optional and can be omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>Defines the ingestion endpoints to send data to via this rule.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableId" /></td>
    <td><code>string</code></td>
    <td>The immutable ID of this data collection rule. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="ingestionQuotas" /></td>
    <td><code>object</code></td>
    <td>The specification for ingestion limits.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="references" /></td>
    <td><code>object</code></td>
    <td>Defines all the references that may be used in other sections of the DCR.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="streamDeclarations" /></td>
    <td><code>object</code></td>
    <td>Declaration of custom streams used in this rule.</td>
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
    <td><CopyableCode code="agentSettings" /></td>
    <td><code>object</code></td>
    <td>Agent settings used to modify agent behavior on a given host.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionEndpointId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection endpoint that this rule can be used with.</td>
</tr>
<tr>
    <td><CopyableCode code="dataFlows" /></td>
    <td><code>array</code></td>
    <td>The specification of data flows.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSources" /></td>
    <td><code>object</code></td>
    <td>The specification of data sources. This property is optional and can be omitted if the rule is meant to be used via direct calls to the provisioned endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the data collection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="destinations" /></td>
    <td><code>object</code></td>
    <td>The specification of destinations.</td>
</tr>
<tr>
    <td><CopyableCode code="directDataSources" /></td>
    <td><code>object</code></td>
    <td>The specification of direct data sources. This property is optional and can be omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>Defines the ingestion endpoints to send data to via this rule.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableId" /></td>
    <td><code>string</code></td>
    <td>The immutable ID of this data collection rule. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="ingestionQuotas" /></td>
    <td><code>object</code></td>
    <td>The specification for ingestion limits.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="references" /></td>
    <td><code>object</code></td>
    <td>Defines all the references that may be used in other sections of the DCR.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="streamDeclarations" /></td>
    <td><code>object</code></td>
    <td>Declaration of custom streams used in this rule.</td>
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
    <td><CopyableCode code="agentSettings" /></td>
    <td><code>object</code></td>
    <td>Agent settings used to modify agent behavior on a given host.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionEndpointId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection endpoint that this rule can be used with.</td>
</tr>
<tr>
    <td><CopyableCode code="dataFlows" /></td>
    <td><code>array</code></td>
    <td>The specification of data flows.</td>
</tr>
<tr>
    <td><CopyableCode code="dataSources" /></td>
    <td><code>object</code></td>
    <td>The specification of data sources. This property is optional and can be omitted if the rule is meant to be used via direct calls to the provisioned endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the data collection rule.</td>
</tr>
<tr>
    <td><CopyableCode code="destinations" /></td>
    <td><code>object</code></td>
    <td>The specification of destinations.</td>
</tr>
<tr>
    <td><CopyableCode code="directDataSources" /></td>
    <td><code>object</code></td>
    <td>The specification of direct data sources. This property is optional and can be omitted.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>object</code></td>
    <td>Defines the ingestion endpoints to send data to via this rule.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Managed service identity of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="immutableId" /></td>
    <td><code>string</code></td>
    <td>The immutable ID of this data collection rule. This property is READ-ONLY.</td>
</tr>
<tr>
    <td><CopyableCode code="ingestionQuotas" /></td>
    <td><code>object</code></td>
    <td>The specification for ingestion limits.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>The kind of the resource. Known values are: "Linux" and "Windows". (Linux, Windows)</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>Metadata about the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Creating", "Updating", "Deleting", "Succeeded", "Canceled", and "Failed". (Creating, Updating, Deleting, Succeeded, Canceled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="references" /></td>
    <td><code>object</code></td>
    <td>Defines all the references that may be used in other sections of the DCR.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>object</code></td>
    <td>The SKU of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="streamDeclarations" /></td>
    <td><code>object</code></td>
    <td>Declaration of custom streams used in this rule.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_rule_name"><code>data_collection_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Returns the specified data collection rule. Returns the specified data collection rule.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all data collection rules in the specified resource group. Lists all data collection rules in the specified resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all data collection rules in the specified subscription. Lists all data collection rules in the specified subscription.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_rule_name"><code>data_collection_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a data collection rule. Creates or updates a data collection rule.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_rule_name"><code>data_collection_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates part of a data collection rule. Updates part of a data collection rule.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_rule_name"><code>data_collection_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-deleteAssociations"><code>deleteAssociations</code></a></td>
    <td>Deletes a data collection rule. Deletes a data collection rule.</td>
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
<tr id="parameter-data_collection_rule_name">
    <td><CopyableCode code="data_collection_rule_name" /></td>
    <td><code>string</code></td>
    <td>The name of the data collection rule. The name is case insensitive. Required.</td>
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
<tr id="parameter-deleteAssociations">
    <td><CopyableCode code="deleteAssociations" /></td>
    <td><code>boolean</code></td>
    <td>If set to 'true' then all associations of this data collection rule will also be deleted. Default value is None.</td>
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

Returns the specified data collection rule. Returns the specified data collection rule.

```sql
SELECT
id,
name,
agentSettings,
dataCollectionEndpointId,
dataFlows,
dataSources,
description,
destinations,
directDataSources,
endpoints,
etag,
identity,
immutableId,
ingestionQuotas,
kind,
location,
metadata,
provisioningState,
references,
sku,
streamDeclarations,
systemData,
tags,
type
FROM azure.monitor.data_collection_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_collection_rule_name = '{{ data_collection_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all data collection rules in the specified resource group. Lists all data collection rules in the specified resource group.

```sql
SELECT
id,
name,
agentSettings,
dataCollectionEndpointId,
dataFlows,
dataSources,
description,
destinations,
directDataSources,
endpoints,
etag,
identity,
immutableId,
ingestionQuotas,
kind,
location,
metadata,
provisioningState,
references,
sku,
streamDeclarations,
systemData,
tags,
type
FROM azure.monitor.data_collection_rules
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all data collection rules in the specified subscription. Lists all data collection rules in the specified subscription.

```sql
SELECT
id,
name,
agentSettings,
dataCollectionEndpointId,
dataFlows,
dataSources,
description,
destinations,
directDataSources,
endpoints,
etag,
identity,
immutableId,
ingestionQuotas,
kind,
location,
metadata,
provisioningState,
references,
sku,
streamDeclarations,
systemData,
tags,
type
FROM azure.monitor.data_collection_rules
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

Creates or updates a data collection rule. Creates or updates a data collection rule.

```sql
INSERT INTO azure.monitor.data_collection_rules (
tags,
location,
properties,
kind,
sku,
identity,
resource_group_name,
data_collection_rule_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ sku }}',
'{{ identity }}',
'{{ resource_group_name }}',
'{{ data_collection_rule_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
identity,
kind,
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
- name: data_collection_rules
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_collection_rules resource.
    - name: data_collection_rule_name
      value: "{{ data_collection_rule_name }}"
      description: Required parameter for the data_collection_rules resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the data_collection_rules resource.
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
        :vartype properties: ~azure.mgmt.monitor.models.DataCollectionRuleResourceProperties
      value:
        description: "{{ description }}"
        immutableId: "{{ immutableId }}"
        dataCollectionEndpointId: "{{ dataCollectionEndpointId }}"
        metadata:
          provisionedBy: "{{ provisionedBy }}"
          provisionedByResourceId: "{{ provisionedByResourceId }}"
          provisionedByImmutableId: "{{ provisionedByImmutableId }}"
        endpoints:
          logsIngestion: "{{ logsIngestion }}"
          metricsIngestion: "{{ metricsIngestion }}"
        references:
          enrichmentData:
            storageBlobs:
              - resourceId: "{{ resourceId }}"
                blobUrl: "{{ blobUrl }}"
                lookupType: "{{ lookupType }}"
                name: "{{ name }}"
          applicationInsights:
            - resourceId: "{{ resourceId }}"
              name: "{{ name }}"
        agentSettings:
          logs:
            - name: "{{ name }}"
              value: "{{ value }}"
        streamDeclarations: "{{ streamDeclarations }}"
        dataSources:
          performanceCounters:
            - streams: "{{ streams }}"
              samplingFrequencyInSeconds: {{ samplingFrequencyInSeconds }}
              counterSpecifiers: "{{ counterSpecifiers }}"
              transformKql: "{{ transformKql }}"
              name: "{{ name }}"
          performanceCountersOTel:
            - streams: "{{ streams }}"
              samplingFrequencyInSeconds: {{ samplingFrequencyInSeconds }}
              counterSpecifiers: "{{ counterSpecifiers }}"
              name: "{{ name }}"
          windowsEventLogs:
            - streams: "{{ streams }}"
              xPathQueries: "{{ xPathQueries }}"
              transformKql: "{{ transformKql }}"
              name: "{{ name }}"
          syslog:
            - streams: "{{ streams }}"
              facilityNames: "{{ facilityNames }}"
              logLevels: "{{ logLevels }}"
              transformKql: "{{ transformKql }}"
              name: "{{ name }}"
          extensions:
            - streams: "{{ streams }}"
              extensionName: "{{ extensionName }}"
              extensionSettings: "{{ extensionSettings }}"
              inputDataSources: "{{ inputDataSources }}"
              name: "{{ name }}"
          logFiles:
            - streams: "{{ streams }}"
              filePatterns: "{{ filePatterns }}"
              format: "{{ format }}"
              settings:
                text:
                  recordStartTimestampFormat: "{{ recordStartTimestampFormat }}"
              transformKql: "{{ transformKql }}"
              name: "{{ name }}"
          iisLogs:
            - streams: "{{ streams }}"
              logDirectories: "{{ logDirectories }}"
              transformKql: "{{ transformKql }}"
              name: "{{ name }}"
          windowsFirewallLogs:
            - streams: "{{ streams }}"
              profileFilter: "{{ profileFilter }}"
              name: "{{ name }}"
          prometheusForwarder:
            - streams: "{{ streams }}"
              labelIncludeFilter: "{{ labelIncludeFilter }}"
              customVMScrapeConfig: "{{ customVMScrapeConfig }}"
              name: "{{ name }}"
          platformTelemetry:
            - streams: "{{ streams }}"
              name: "{{ name }}"
          dataImports:
            eventHub:
              name: "{{ name }}"
              consumerGroup: "{{ consumerGroup }}"
              stream: "{{ stream }}"
          otelLogs:
            - streams: "{{ streams }}"
              resourceAttributeRouting:
                attributeName: "{{ attributeName }}"
                attributeValue: "{{ attributeValue }}"
              enrichWithResourceAttributes: "{{ enrichWithResourceAttributes }}"
              enrichWithReference: "{{ enrichWithReference }}"
              replaceResourceIdWithReference: {{ replaceResourceIdWithReference }}
              name: "{{ name }}"
          otelTraces:
            - streams: "{{ streams }}"
              resourceAttributeRouting:
                attributeName: "{{ attributeName }}"
                attributeValue: "{{ attributeValue }}"
              enrichWithResourceAttributes: "{{ enrichWithResourceAttributes }}"
              enrichWithReference: "{{ enrichWithReference }}"
              replaceResourceIdWithReference: {{ replaceResourceIdWithReference }}
              name: "{{ name }}"
          otelMetrics:
            - streams: "{{ streams }}"
              resourceAttributeRouting:
                attributeName: "{{ attributeName }}"
                attributeValue: "{{ attributeValue }}"
              enrichWithResourceAttributes: "{{ enrichWithResourceAttributes }}"
              enrichWithReference: "{{ enrichWithReference }}"
              name: "{{ name }}"
          etwProviders:
            - streams: "{{ streams }}"
              provider: "{{ provider }}"
              providerType: "{{ providerType }}"
              logLevel: "{{ logLevel }}"
              eventIds: "{{ eventIds }}"
              keyword: "{{ keyword }}"
              name: "{{ name }}"
        directDataSources:
          otelMetrics:
            - streams: "{{ streams }}"
              enrichWithResourceAttributes: "{{ enrichWithResourceAttributes }}"
              enrichWithReference: "{{ enrichWithReference }}"
              name: "{{ name }}"
          otelLogs:
            - streams: "{{ streams }}"
              enrichWithResourceAttributes: "{{ enrichWithResourceAttributes }}"
              enrichWithReference: "{{ enrichWithReference }}"
              replaceResourceIdWithReference: {{ replaceResourceIdWithReference }}
              name: "{{ name }}"
          otelTraces:
            - streams: "{{ streams }}"
              enrichWithResourceAttributes: "{{ enrichWithResourceAttributes }}"
              enrichWithReference: "{{ enrichWithReference }}"
              replaceResourceIdWithReference: {{ replaceResourceIdWithReference }}
              name: "{{ name }}"
        destinations:
          logAnalytics:
            - workspaceResourceId: "{{ workspaceResourceId }}"
              workspaceId: "{{ workspaceId }}"
              name: "{{ name }}"
          monitoringAccounts:
            - accountResourceId: "{{ accountResourceId }}"
              accountId: "{{ accountId }}"
              name: "{{ name }}"
          azureMonitorMetrics:
            name: "{{ name }}"
          eventHubs:
            - eventHubResourceId: "{{ eventHubResourceId }}"
              name: "{{ name }}"
          eventHubsDirect:
            - eventHubResourceId: "{{ eventHubResourceId }}"
              name: "{{ name }}"
          storageBlobsDirect:
            - containerName: "{{ containerName }}"
              storageAccountResourceId: "{{ storageAccountResourceId }}"
              name: "{{ name }}"
          storageTablesDirect:
            - tableName: "{{ tableName }}"
              storageAccountResourceId: "{{ storageAccountResourceId }}"
              name: "{{ name }}"
          storageAccounts:
            - containerName: "{{ containerName }}"
              storageAccountResourceId: "{{ storageAccountResourceId }}"
              name: "{{ name }}"
          microsoftFabric:
            - tenantId: "{{ tenantId }}"
              artifactId: "{{ artifactId }}"
              databaseName: "{{ databaseName }}"
              ingestionUri: "{{ ingestionUri }}"
              name: "{{ name }}"
          azureDataExplorer:
            - resourceId: "{{ resourceId }}"
              databaseName: "{{ databaseName }}"
              ingestionUri: "{{ ingestionUri }}"
              name: "{{ name }}"
        dataFlows:
          - streams: "{{ streams }}"
            destinations: "{{ destinations }}"
            transformKql: "{{ transformKql }}"
            outputStream: "{{ outputStream }}"
            builtInTransform: "{{ builtInTransform }}"
            captureOverflow: {{ captureOverflow }}
        ingestionQuotas:
          logs:
            maxSizePerMinuteInGB: "{{ maxSizePerMinuteInGB }}"
            maxRequestsPerMinute: "{{ maxRequestsPerMinute }}"
        provisioningState: "{{ provisioningState }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        The kind of the resource. Known values are: "Linux" and "Windows".
      valid_values: ['Linux', 'Windows']
    - name: sku
      description: |
        The SKU of the resource.
      value:
        name: "{{ name }}"
        tier: "{{ tier }}"
        size: "{{ size }}"
        family: "{{ family }}"
        capacity: {{ capacity }}
    - name: identity
      description: |
        Managed service identity of the resource.
      value:
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        type: "{{ type }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
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

Updates part of a data collection rule. Updates part of a data collection rule.

```sql
UPDATE azure.monitor.data_collection_rules
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND data_collection_rule_name = '{{ data_collection_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
etag,
identity,
kind,
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

Deletes a data collection rule. Deletes a data collection rule.

```sql
DELETE FROM azure.monitor.data_collection_rules
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND data_collection_rule_name = '{{ data_collection_rule_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND deleteAssociations = '{{ deleteAssociations }}'
;
```
</TabItem>
</Tabs>
