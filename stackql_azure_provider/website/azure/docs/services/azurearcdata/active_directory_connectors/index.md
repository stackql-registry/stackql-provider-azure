--- 
title: active_directory_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - active_directory_connectors
  - azurearcdata
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

Creates, updates, deletes, gets or lists an <code>active_directory_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="active_directory_connectors" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azurearcdata.active_directory_connectors" /></td></tr>
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
    <td><CopyableCode code="domainServiceAccountLoginInformation" /></td>
    <td><code>object</code></td>
    <td>Username and password for domain service account authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Active Directory connector resource.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><code>object</code></td>
    <td>null. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>null.</td>
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
    <td><CopyableCode code="domainServiceAccountLoginInformation" /></td>
    <td><code>object</code></td>
    <td>Username and password for domain service account authentication.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning state of the Active Directory connector resource.</td>
</tr>
<tr>
    <td><CopyableCode code="spec" /></td>
    <td><code>object</code></td>
    <td>null. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>null.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_controller_name"><code>data_controller_name</code></a>, <a href="#parameter-active_directory_connector_name"><code>active_directory_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Retrieves an Active Directory connector resource.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_controller_name"><code>data_controller_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List the active directory connectors associated with the given data controller. List the active directory connectors associated with the given data controller.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_controller_name"><code>data_controller_name</code></a>, <a href="#parameter-active_directory_connector_name"><code>active_directory_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Creates or replaces an Active Directory connector resource.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-data_controller_name"><code>data_controller_name</code></a>, <a href="#parameter-active_directory_connector_name"><code>active_directory_connector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an Active Directory connector resource.</td>
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
<tr id="parameter-active_directory_connector_name">
    <td><CopyableCode code="active_directory_connector_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Active Directory connector instance. Required.</td>
</tr>
<tr id="parameter-data_controller_name">
    <td><CopyableCode code="data_controller_name" /></td>
    <td><code>string</code></td>
    <td>The name of the data controller. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Azure resource group. Required.</td>
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
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Retrieves an Active Directory connector resource.

```sql
SELECT
id,
name,
domainServiceAccountLoginInformation,
provisioningState,
spec,
status,
systemData,
type
FROM azure.azurearcdata.active_directory_connectors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_controller_name = '{{ data_controller_name }}' -- required
AND active_directory_connector_name = '{{ active_directory_connector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List the active directory connectors associated with the given data controller. List the active directory connectors associated with the given data controller.

```sql
SELECT
id,
name,
domainServiceAccountLoginInformation,
provisioningState,
spec,
status,
systemData,
type
FROM azure.azurearcdata.active_directory_connectors
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND data_controller_name = '{{ data_controller_name }}' -- required
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

Creates or replaces an Active Directory connector resource.

```sql
INSERT INTO azure.azurearcdata.active_directory_connectors (
properties,
resource_group_name,
data_controller_name,
active_directory_connector_name,
subscription_id
)
SELECT 
'{{ properties }}' /* required */,
'{{ resource_group_name }}',
'{{ data_controller_name }}',
'{{ active_directory_connector_name }}',
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
- name: active_directory_connectors
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the active_directory_connectors resource.
    - name: data_controller_name
      value: "{{ data_controller_name }}"
      description: Required parameter for the active_directory_connectors resource.
    - name: active_directory_connector_name
      value: "{{ active_directory_connector_name }}"
      description: Required parameter for the active_directory_connectors resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the active_directory_connectors resource.
    - name: properties
      description: |
        null. Required.
      value:
        domainServiceAccountLoginInformation:
          username: "{{ username }}"
          password: "{{ password }}"
        provisioningState: "{{ provisioningState }}"
        spec:
          activeDirectory:
            realm: "{{ realm }}"
            netbiosDomainName: "{{ netbiosDomainName }}"
            serviceAccountProvisioning: "{{ serviceAccountProvisioning }}"
            ouDistinguishedName: "{{ ouDistinguishedName }}"
            domainControllers:
              primaryDomainController:
                hostname: "{{ hostname }}"
              secondaryDomainControllers:
                - hostname: "{{ hostname }}"
          dns:
            domainName: "{{ domainName }}"
            nameserverIPAddresses:
              - "{{ nameserverIPAddresses }}"
            replicas: {{ replicas }}
            preferK8sDnsForPtrLookups: {{ preferK8sDnsForPtrLookups }}
        status:
          : "{{  }}"
          lastUpdateTime: "{{ lastUpdateTime }}"
          observedGeneration: {{ observedGeneration }}
          state: "{{ state }}"
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

Deletes an Active Directory connector resource.

```sql
DELETE FROM azure.azurearcdata.active_directory_connectors
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND data_controller_name = '{{ data_controller_name }}' --required
AND active_directory_connector_name = '{{ active_directory_connector_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
