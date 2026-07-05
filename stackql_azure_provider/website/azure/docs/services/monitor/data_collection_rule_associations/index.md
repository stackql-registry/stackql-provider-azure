--- 
title: data_collection_rule_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rule_associations
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

Creates, updates, deletes, gets or lists a <code>data_collection_rule_associations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_collection_rule_associations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.data_collection_rule_associations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_by_data_collection_endpoint"
    values={[
        { label: 'list_by_data_collection_endpoint', value: 'list_by_data_collection_endpoint' },
        { label: 'list_by_rule', value: 'list_by_rule' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource', value: 'list_by_resource' }
    ]}
>
<TabItem value="list_by_data_collection_endpoint">

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
    <td><CopyableCode code="dataCollectionEndpointId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection endpoint that is to be associated.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionRuleId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection rule that is to be associated.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the association.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
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
<TabItem value="list_by_rule">

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
    <td><CopyableCode code="dataCollectionEndpointId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection endpoint that is to be associated.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionRuleId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection rule that is to be associated.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the association.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
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
    <td><CopyableCode code="dataCollectionEndpointId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection endpoint that is to be associated.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionRuleId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection rule that is to be associated.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the association.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
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
<TabItem value="list_by_resource">

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
    <td><CopyableCode code="dataCollectionEndpointId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection endpoint that is to be associated.</td>
</tr>
<tr>
    <td><CopyableCode code="dataCollectionRuleId" /></td>
    <td><code>string</code></td>
    <td>The resource ID of the data collection rule that is to be associated.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the association.</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource entity tag (ETag).</td>
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
    <td><a href="#list_by_data_collection_endpoint"><CopyableCode code="list_by_data_collection_endpoint" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_endpoint_name"><code>data_collection_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists associations for the specified data collection endpoint. Lists associations for the specified data collection endpoint.</td>
</tr>
<tr>
    <td><a href="#list_by_rule"><CopyableCode code="list_by_rule" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_collection_rule_name"><code>data_collection_rule_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a></td>
    <td>Lists associations for the specified data collection rule. Lists associations for the specified data collection rule.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-association_name"><code>association_name</code></a></td>
    <td></td>
    <td>Returns the specified association. Returns the specified association.</td>
</tr>
<tr>
    <td><a href="#list_by_resource"><CopyableCode code="list_by_resource" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a></td>
    <td></td>
    <td>Lists associations for the specified resource. Lists associations for the specified resource.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-association_name"><code>association_name</code></a></td>
    <td></td>
    <td>Creates or updates an association. Creates or updates an association.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_uri"><code>resource_uri</code></a>, <a href="#parameter-association_name"><code>association_name</code></a></td>
    <td></td>
    <td>Deletes an association. Deletes an association.</td>
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
<tr id="parameter-association_name">
    <td><CopyableCode code="association_name" /></td>
    <td><code>string</code></td>
    <td>The name of the association. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-data_collection_endpoint_name">
    <td><CopyableCode code="data_collection_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>The name of the data collection endpoint. The name is case insensitive. Required.</td>
</tr>
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
<tr id="parameter-resource_uri">
    <td><CopyableCode code="resource_uri" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>(Optional) The continuation token for paginated responses. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>(Optional) The max number of items to return per page. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_by_data_collection_endpoint"
    values={[
        { label: 'list_by_data_collection_endpoint', value: 'list_by_data_collection_endpoint' },
        { label: 'list_by_rule', value: 'list_by_rule' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource', value: 'list_by_resource' }
    ]}
>
<TabItem value="list_by_data_collection_endpoint">

Lists associations for the specified data collection endpoint. Lists associations for the specified data collection endpoint.

```sql
SELECT
id,
name,
dataCollectionEndpointId,
dataCollectionRuleId,
description,
etag,
metadata,
provisioningState,
systemData,
type
FROM azure.monitor.data_collection_rule_associations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_collection_endpoint_name = '{{ data_collection_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_rule">

Lists associations for the specified data collection rule. Lists associations for the specified data collection rule.

```sql
SELECT
id,
name,
dataCollectionEndpointId,
dataCollectionRuleId,
description,
etag,
metadata,
provisioningState,
systemData,
type
FROM azure.monitor.data_collection_rule_associations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_collection_rule_name = '{{ data_collection_rule_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get">

Returns the specified association. Returns the specified association.

```sql
SELECT
id,
name,
dataCollectionEndpointId,
dataCollectionRuleId,
description,
etag,
metadata,
provisioningState,
systemData,
type
FROM azure.monitor.data_collection_rule_associations
WHERE resource_uri = '{{ resource_uri }}' -- required
AND association_name = '{{ association_name }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource">

Lists associations for the specified resource. Lists associations for the specified resource.

```sql
SELECT
id,
name,
dataCollectionEndpointId,
dataCollectionRuleId,
description,
etag,
metadata,
provisioningState,
systemData,
type
FROM azure.monitor.data_collection_rule_associations
WHERE resource_uri = '{{ resource_uri }}' -- required
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

Creates or updates an association. Creates or updates an association.

```sql
INSERT INTO azure.monitor.data_collection_rule_associations (
properties,
resource_uri,
association_name
)
SELECT 
'{{ properties }}',
'{{ resource_uri }}',
'{{ association_name }}'
RETURNING
id,
name,
etag,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: data_collection_rule_associations
  props:
    - name: resource_uri
      value: "{{ resource_uri }}"
      description: Required parameter for the data_collection_rule_associations resource.
    - name: association_name
      value: "{{ association_name }}"
      description: Required parameter for the data_collection_rule_associations resource.
    - name: properties
      description: |
        :vartype properties: ~azure.mgmt.monitor.models.DataCollectionRuleAssociationProxyOnlyResourceProperties
      value:
        description: "{{ description }}"
        dataCollectionRuleId: "{{ dataCollectionRuleId }}"
        dataCollectionEndpointId: "{{ dataCollectionEndpointId }}"
        provisioningState: "{{ provisioningState }}"
        metadata:
          provisionedBy: "{{ provisionedBy }}"
          provisionedByResourceId: "{{ provisionedByResourceId }}"
          provisionedByImmutableId: "{{ provisionedByImmutableId }}"
`}</CodeBlock>

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

Deletes an association. Deletes an association.

```sql
DELETE FROM azure.monitor.data_collection_rule_associations
WHERE resource_uri = '{{ resource_uri }}' --required
AND association_name = '{{ association_name }}' --required
;
```
</TabItem>
</Tabs>
