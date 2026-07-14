--- 
title: server_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - server_instances
  - migration_discovery_sap
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

Creates, updates, deletes, gets or lists a <code>server_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="server_instances" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.migration_discovery_sap.server_instances" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sap_instance', value: 'list_by_sap_instance' }
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
    <td><CopyableCode code="configurationData" /></td>
    <td><code>object</code></td>
    <td>Configuration data for this server instance.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the errors related to SAP Instance resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceSid" /></td>
    <td><code>string</code></td>
    <td>This is the Instance SID for ASCS/AP/DB instance. An SAP system with HANA database for example could have a different SID for database Instance than that of ASCS instance.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystem" /></td>
    <td><code>string</code></td>
    <td>This is Operating System on which the host server is running. Known values are: "IBMAIX", "RedHat", "SUSE", "Solaris", "Unix", and "WindowsServer".</td>
</tr>
<tr>
    <td><CopyableCode code="performanceData" /></td>
    <td><code>object</code></td>
    <td>Configuration data for this server instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Failed", "Creating", "Canceled", "Accepted", "Deleting", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="sapInstanceType" /></td>
    <td><code>string</code></td>
    <td>Defines the type SAP instance on this server instance. Known values are: "ASCS", "DB", "APP", "SCS", and "WEBDISP".</td>
</tr>
<tr>
    <td><CopyableCode code="sapProduct" /></td>
    <td><code>string</code></td>
    <td>This is the SAP Application Component; e.g. SAP S/4HANA 2022, SAP ERP ENHANCE PACKAGE.</td>
</tr>
<tr>
    <td><CopyableCode code="sapProductVersion" /></td>
    <td><code>string</code></td>
    <td>Provide the product version of the SAP product.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>This is the Virtual Machine Name of the SAP system. Add all the virtual machines attached to an SAP system which you wish to migrate to Azure. Keeping this not equal to ID as for single tier all InstanceTypes would be on same server, leading to multiple resources with same servername.</td>
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
<TabItem value="list_by_sap_instance">

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
    <td><CopyableCode code="configurationData" /></td>
    <td><code>object</code></td>
    <td>Configuration data for this server instance.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>object</code></td>
    <td>Defines the errors related to SAP Instance resource.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceSid" /></td>
    <td><code>string</code></td>
    <td>This is the Instance SID for ASCS/AP/DB instance. An SAP system with HANA database for example could have a different SID for database Instance than that of ASCS instance.</td>
</tr>
<tr>
    <td><CopyableCode code="operatingSystem" /></td>
    <td><code>string</code></td>
    <td>This is Operating System on which the host server is running. Known values are: "IBMAIX", "RedHat", "SUSE", "Solaris", "Unix", and "WindowsServer".</td>
</tr>
<tr>
    <td><CopyableCode code="performanceData" /></td>
    <td><code>object</code></td>
    <td>Configuration data for this server instance.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Defines the provisioning states. Known values are: "Succeeded", "Updating", "Failed", "Creating", "Canceled", "Accepted", "Deleting", and "Unknown".</td>
</tr>
<tr>
    <td><CopyableCode code="sapInstanceType" /></td>
    <td><code>string</code></td>
    <td>Defines the type SAP instance on this server instance. Known values are: "ASCS", "DB", "APP", "SCS", and "WEBDISP".</td>
</tr>
<tr>
    <td><CopyableCode code="sapProduct" /></td>
    <td><code>string</code></td>
    <td>This is the SAP Application Component; e.g. SAP S/4HANA 2022, SAP ERP ENHANCE PACKAGE.</td>
</tr>
<tr>
    <td><CopyableCode code="sapProductVersion" /></td>
    <td><code>string</code></td>
    <td>Provide the product version of the SAP product.</td>
</tr>
<tr>
    <td><CopyableCode code="serverName" /></td>
    <td><code>string</code></td>
    <td>This is the Virtual Machine Name of the SAP system. Add all the virtual machines attached to an SAP system which you wish to migrate to Azure. Keeping this not equal to ID as for single tier all InstanceTypes would be on same server, leading to multiple resources with same servername.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-server_instance_name"><code>server_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the Server Instance resource.</td>
</tr>
<tr>
    <td><a href="#list_by_sap_instance"><CopyableCode code="list_by_sap_instance" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists the Server Instance resources for the given SAP Instance resource.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-server_instance_name"><code>server_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates the Server Instance resource. ;This will be used by service only. PUT operation on this resource by end user will return a Bad Request error.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-server_instance_name"><code>server_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the Server Instance resource. This operation on a resource by end user will return a Bad Request error.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sap_discovery_site_name"><code>sap_discovery_site_name</code></a>, <a href="#parameter-sap_instance_name"><code>sap_instance_name</code></a>, <a href="#parameter-server_instance_name"><code>server_instance_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes the Server Instance resource. ;This will be used by service only. Delete operation on this resource by end user will return a Bad Request error. You can delete the parent resource, which is the SAP Migration discovery site resource, using the delete operation on it.</td>
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
<tr id="parameter-server_instance_name">
    <td><CopyableCode code="server_instance_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Server instance resource for SAP Migration. Required.</td>
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
        { label: 'list_by_sap_instance', value: 'list_by_sap_instance' }
    ]}
>
<TabItem value="get">

Gets the Server Instance resource.

```sql
SELECT
id,
name,
configurationData,
errors,
instanceSid,
operatingSystem,
performanceData,
provisioningState,
sapInstanceType,
sapProduct,
sapProductVersion,
serverName,
systemData,
type
FROM azure_extras.migration_discovery_sap.server_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_discovery_site_name = '{{ sap_discovery_site_name }}' -- required
AND sap_instance_name = '{{ sap_instance_name }}' -- required
AND server_instance_name = '{{ server_instance_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_sap_instance">

Lists the Server Instance resources for the given SAP Instance resource.

```sql
SELECT
id,
name,
configurationData,
errors,
instanceSid,
operatingSystem,
performanceData,
provisioningState,
sapInstanceType,
sapProduct,
sapProductVersion,
serverName,
systemData,
type
FROM azure_extras.migration_discovery_sap.server_instances
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sap_discovery_site_name = '{{ sap_discovery_site_name }}' -- required
AND sap_instance_name = '{{ sap_instance_name }}' -- required
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

Creates the Server Instance resource. ;This will be used by service only. PUT operation on this resource by end user will return a Bad Request error.

```sql
INSERT INTO azure_extras.migration_discovery_sap.server_instances (
properties,
resource_group_name,
sap_discovery_site_name,
sap_instance_name,
server_instance_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sap_discovery_site_name }}',
'{{ sap_instance_name }}',
'{{ server_instance_name }}',
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
- name: server_instances
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the server_instances resource.
    - name: sap_discovery_site_name
      value: "{{ sap_discovery_site_name }}"
      description: Required parameter for the server_instances resource.
    - name: sap_instance_name
      value: "{{ sap_instance_name }}"
      description: Required parameter for the server_instances resource.
    - name: server_instance_name
      value: "{{ server_instance_name }}"
      description: Required parameter for the server_instances resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the server_instances resource.
    - name: properties
      description: |
        The resource-specific properties for this resource.
      value:
        serverName: "{{ serverName }}"
        sapInstanceType: "{{ sapInstanceType }}"
        instanceSid: "{{ instanceSid }}"
        sapProduct: "{{ sapProduct }}"
        sapProductVersion: "{{ sapProductVersion }}"
        operatingSystem: "{{ operatingSystem }}"
        configurationData:
          saps: {{ saps }}
          cpu: {{ cpu }}
          cpuType: "{{ cpuType }}"
          cpuInMhz: {{ cpuInMhz }}
          ram: {{ ram }}
          hardwareManufacturer: "{{ hardwareManufacturer }}"
          model: "{{ model }}"
          totalDiskSizeGB: {{ totalDiskSizeGB }}
          totalDiskIops: {{ totalDiskIops }}
          databaseType: "{{ databaseType }}"
          targetHanaRamSizeGB: {{ targetHanaRamSizeGB }}
        performanceData:
          dataSource: "{{ dataSource }}"
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

Updates the Server Instance resource. This operation on a resource by end user will return a Bad Request error.

```sql
UPDATE azure_extras.migration_discovery_sap.server_instances
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sap_discovery_site_name = '{{ sap_discovery_site_name }}' --required
AND sap_instance_name = '{{ sap_instance_name }}' --required
AND server_instance_name = '{{ server_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
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

Deletes the Server Instance resource. ;This will be used by service only. Delete operation on this resource by end user will return a Bad Request error. You can delete the parent resource, which is the SAP Migration discovery site resource, using the delete operation on it.

```sql
DELETE FROM azure_extras.migration_discovery_sap.server_instances
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sap_discovery_site_name = '{{ sap_discovery_site_name }}' --required
AND sap_instance_name = '{{ sap_instance_name }}' --required
AND server_instance_name = '{{ server_instance_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
