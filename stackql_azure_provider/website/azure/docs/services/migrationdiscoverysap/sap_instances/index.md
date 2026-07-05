--- 
title: sap_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_instances
  - migrationdiscoverysap
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

Creates, updates, deletes, gets or lists a <code>sap_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sap_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrationdiscoverysap.sap_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sap_discovery_site', value: 'list_by_sap_discovery_site' }
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
    <td><CopyableCode code="application" /></td>
    <td><code>string</code></td>
    <td>Enter a business function/department identifier to group multiple SIDs.</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>The Environment; PRD, QA, DEV, etc to which SAP system belongs to. Select from the list of available dropdown values. Known values are: "Production", "PreProduction", "Test", "QualityAssurance", "Development", "Sandbox", "DisasterRecovery", and "Training".</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the errors related to SAP Instance resource.</td>
</tr>
<tr>
    <td><CopyableCode code="landscapeSid" /></td>
    <td><code>string</code></td>
    <td>This is the SID of the production system in a landscape. An SAP system could itself be a production SID or a part of a landscape with a different Production SID. This field can be used to relate non-prod SIDs, other components, SID (WEBDISP) to the prod SID. Enter the value of Production SID.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Failed", "Creating", "Canceled", "Accepted", "Deleting", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSid" /></td>
    <td><code>string</code></td>
    <td>This is the SID of SAP System. Keeping this not equal to ID as different landscapes can have repeated System SID IDs.</td>
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
<TabItem value="list_by_sap_discovery_site">

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
    <td><CopyableCode code="application" /></td>
    <td><code>string</code></td>
    <td>Enter a business function/department identifier to group multiple SIDs.</td>
</tr>
<tr>
    <td><CopyableCode code="environment" /></td>
    <td><code>string</code></td>
    <td>The Environment; PRD, QA, DEV, etc to which SAP system belongs to. Select from the list of available dropdown values. Known values are: "Production", "PreProduction", "Test", "QualityAssurance", "Development", "Sandbox", "DisasterRecovery", and "Training".</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the errors related to SAP Instance resource.</td>
</tr>
<tr>
    <td><CopyableCode code="landscapeSid" /></td>
    <td><code>string</code></td>
    <td>This is the SID of the production system in a landscape. An SAP system could itself be a production SID or a part of a landscape with a different Production SID. This field can be used to relate non-prod SIDs, other components, SID (WEBDISP) to the prod SID. Enter the value of Production SID.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Failed", "Creating", "Canceled", "Accepted", "Deleting", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="systemSid" /></td>
    <td><code>string</code></td>
    <td>This is the SID of SAP System. Keeping this not equal to ID as different landscapes can have repeated System SID IDs.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the SAP Instance resource.</td>
</tr>
<tr>
    <td><a href="#list_by_sap_discovery_site"><CopyableCode code="list_by_sap_discovery_site" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the SAP Instance resources for the given SAP Migration discovery site resource.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates the SAP Instance resource. This will be used by service only. PUT operation on this resource by end user will return a Bad Request error.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the SAP Instance resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the SAP Instance resource. This will be used by service only. Delete operation on this resource by end user will return a Bad Request error. You can delete the parent resource, which is the SAP Migration discovery site resource, using the delete operation on it.</td>
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
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-sap_discovery_site_name">
    <td><CopyableCode code="sap_discovery_site_name" /></td>
    <td><code>string</code></td>
    <td>The name of the discovery site resource for SAP Migration. Required.</td>
</tr>
<tr id="parameter-sap_instance_name">
    <td><CopyableCode code="sap_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of SAP Instance resource for SAP Migration. Required.</td>
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
        { label: 'list_by_sap_discovery_site', value: 'list_by_sap_discovery_site' }
    ]}
>
<TabItem value="get">

Gets the SAP Instance resource.

```sql
SELECT
id,
name,
application,
environment,
errors,
landscapeSid,
location,
provisioningState,
systemData,
systemSid,
tags,
type
FROM azure.migrationdiscoverysap.sap_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_discovery_site_name = '{{ sap_discovery_site_name }}' -- required
AND sap_instance_name = '{{ sap_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sap_discovery_site">

Lists the SAP Instance resources for the given SAP Migration discovery site resource.

```sql
SELECT
id,
name,
application,
environment,
errors,
landscapeSid,
location,
provisioningState,
systemData,
systemSid,
tags,
type
FROM azure.migrationdiscoverysap.sap_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_discovery_site_name = '{{ sap_discovery_site_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Creates the SAP Instance resource. This will be used by service only. PUT operation on this resource by end user will return a Bad Request error.

```sql
INSERT INTO azure.migrationdiscoverysap.sap_instances (
tags,
location,
properties,
resource_group_name,
sap_discovery_site_name,
sap_instance_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sap_discovery_site_name }}',
'{{ sap_instance_name }}',
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
- name: sap_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sap_instances resource.
    - name: sap_discovery_site_name
      value: "{{ sap_discovery_site_name }}"
      description: Required parameter for the sap_instances resource.
    - name: sap_instance_name
      value: "{{ sap_instance_name }}"
      description: Required parameter for the sap_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sap_instances resource.
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
        systemSid: "{{ systemSid }}"
        environment: "{{ environment }}"
        landscapeSid: "{{ landscapeSid }}"
        application: "{{ application }}"
        provisioningState: "{{ provisioningState }}"
        errors:
          properties:
            code: "{{ code }}"
            message: "{{ message }}"
            recommendation: "{{ recommendation }}"
            details:
              - code: "{{ code }}"
                message: "{{ message }}"
                recommendation: "{{ recommendation }}"
                details: "{{ details }}"
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

Updates the SAP Instance resource.

```sql
UPDATE azure.migrationdiscoverysap.sap_instances
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sap_discovery_site_name = '{{ sap_discovery_site_name }}' --required
AND sap_instance_name = '{{ sap_instance_name }}' --required
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


## `DELETE` examples

<Tabs
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Deletes the SAP Instance resource. This will be used by service only. Delete operation on this resource by end user will return a Bad Request error. You can delete the parent resource, which is the SAP Migration discovery site resource, using the delete operation on it.

```sql
DELETE FROM azure.migrationdiscoverysap.sap_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sap_discovery_site_name = '{{ sap_discovery_site_name }}' --required
AND sap_instance_name = '{{ sap_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
