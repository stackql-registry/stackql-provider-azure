--- 
title: data_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connectors
  - securityinsight
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

Creates, updates, deletes, gets or lists a <code>data_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="data_connectors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.securityinsight.data_connectors" /></td></tr>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. Known values are: "AzureActiveDirectory", "AzureSecurityCenter", "MicrosoftCloudAppSecurity", "ThreatIntelligence", "ThreatIntelligenceTaxii", "Office365", "OfficeATP", "OfficeIRM", "Office365Project", "MicrosoftPurviewInformationProtection", "OfficePowerBI", "AmazonWebServicesCloudTrail", "AmazonWebServicesS3", "AzureAdvancedThreatProtection", "MicrosoftDefenderAdvancedThreatProtection", "Dynamics365", "MicrosoftThreatProtection", "MicrosoftThreatIntelligence", "PremiumMicrosoftDefenderForThreatIntelligence", "GenericUI", "APIPolling", "IOT", "GCP", "RestApiPoller", and "PurviewAudit".</td>
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
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Etag of the azure resource.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. Known values are: "AzureActiveDirectory", "AzureSecurityCenter", "MicrosoftCloudAppSecurity", "ThreatIntelligence", "ThreatIntelligenceTaxii", "Office365", "OfficeATP", "OfficeIRM", "Office365Project", "MicrosoftPurviewInformationProtection", "OfficePowerBI", "AmazonWebServicesCloudTrail", "AmazonWebServicesS3", "AzureAdvancedThreatProtection", "MicrosoftDefenderAdvancedThreatProtection", "Dynamics365", "MicrosoftThreatProtection", "MicrosoftThreatIntelligence", "PremiumMicrosoftDefenderForThreatIntelligence", "GenericUI", "APIPolling", "IOT", "GCP", "RestApiPoller", and "PurviewAudit".</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_connector_id"><code>data_connector_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a data connector.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all data connectors.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_connector_id"><code>data_connector_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates or updates the data connector.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_connector_id"><code>data_connector_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-kind"><code>kind</code></a></td>
    <td></td>
    <td>Creates or updates the data connector.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_connector_id"><code>data_connector_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete the data connector.</td>
</tr>
<tr>
    <td><a href="#connect"><CopyableCode code="connect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_connector_id"><code>data_connector_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Connects a data connector.</td>
</tr>
<tr>
    <td><a href="#disconnect"><CopyableCode code="disconnect" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-workspace_name"><code>workspace_name</code></a>, <a href="#parameter-data_connector_id"><code>data_connector_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disconnect a data connector.</td>
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
<tr id="parameter-data_connector_id">
    <td><CopyableCode code="data_connector_id" /></td>
    <td><code>string</code></td>
    <td>Connector ID. Required.</td>
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
<tr id="parameter-workspace_name">
    <td><CopyableCode code="workspace_name" /></td>
    <td><code>string</code></td>
    <td>The name of the monitor workspace. Required.</td>
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

Gets a data connector.

```sql
SELECT
id,
name,
etag,
kind,
systemData,
type
FROM azure.securityinsight.data_connectors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
AND data_connector_id = '{{ data_connector_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all data connectors.

```sql
SELECT
id,
name,
etag,
kind,
systemData,
type
FROM azure.securityinsight.data_connectors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND workspace_name = '{{ workspace_name }}' -- required
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

Creates or updates the data connector.

```sql
INSERT INTO azure.securityinsight.data_connectors (
kind,
etag,
resource_group_name,
workspace_name,
data_connector_id,
subscription_id
)
SELECT 
'{{ kind }}' /* required */,
'{{ etag }}',
'{{ resource_group_name }}',
'{{ workspace_name }}',
'{{ data_connector_id }}',
'{{ subscription_id }}'
RETURNING
id,
name,
etag,
kind,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: data_connectors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the data_connectors resource.
    - name: workspace_name
      value: "{{ workspace_name }}"
      description: Required parameter for the data_connectors resource.
    - name: data_connector_id
      value: "{{ data_connector_id }}"
      description: Required parameter for the data_connectors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the data_connectors resource.
    - name: kind
      value: "{{ kind }}"
      description: |
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type. If supported, the resource provider must validate and persist this value. Required. Known values are: "AzureActiveDirectory", "AzureSecurityCenter", "MicrosoftCloudAppSecurity", "ThreatIntelligence", "ThreatIntelligenceTaxii", "Office365", "OfficeATP", "OfficeIRM", "Office365Project", "MicrosoftPurviewInformationProtection", "OfficePowerBI", "AmazonWebServicesCloudTrail", "AmazonWebServicesS3", "AzureAdvancedThreatProtection", "MicrosoftDefenderAdvancedThreatProtection", "Dynamics365", "MicrosoftThreatProtection", "MicrosoftThreatIntelligence", "PremiumMicrosoftDefenderForThreatIntelligence", "GenericUI", "APIPolling", "IOT", "GCP", "RestApiPoller", and "PurviewAudit".
    - name: etag
      value: "{{ etag }}"
      description: |
        Etag of the azure resource.
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

Creates or updates the data connector.

```sql
REPLACE azure.securityinsight.data_connectors
SET 
kind = '{{ kind }}',
etag = '{{ etag }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND data_connector_id = '{{ data_connector_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND kind = '{{ kind }}' --required
RETURNING
id,
name,
etag,
kind,
systemData,
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

Delete the data connector.

```sql
DELETE FROM azure.securityinsight.data_connectors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND workspace_name = '{{ workspace_name }}' --required
AND data_connector_id = '{{ data_connector_id }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="connect"
    values={[
        { label: 'connect', value: 'connect' },
        { label: 'disconnect', value: 'disconnect' }
    ]}
>
<TabItem value="connect">

Connects a data connector.

```sql
EXEC azure.securityinsight.data_connectors.connect 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@data_connector_id='{{ data_connector_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"kind": "{{ kind }}", 
"apiKey": "{{ apiKey }}", 
"dataCollectionEndpoint": "{{ dataCollectionEndpoint }}", 
"dataCollectionRuleImmutableId": "{{ dataCollectionRuleImmutableId }}", 
"outputStream": "{{ outputStream }}", 
"clientSecret": "{{ clientSecret }}", 
"clientId": "{{ clientId }}", 
"authorizationCode": "{{ authorizationCode }}", 
"userName": "{{ userName }}", 
"password": "{{ password }}", 
"requestConfigUserInputValues": "{{ requestConfigUserInputValues }}"
}'
;
```
</TabItem>
<TabItem value="disconnect">

Disconnect a data connector.

```sql
EXEC azure.securityinsight.data_connectors.disconnect 
@resource_group_name='{{ resource_group_name }}' --required, 
@workspace_name='{{ workspace_name }}' --required, 
@data_connector_id='{{ data_connector_id }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
