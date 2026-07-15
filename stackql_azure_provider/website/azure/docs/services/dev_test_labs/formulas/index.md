--- 
title: formulas
hide_title: false
hide_table_of_contents: false
keywords:
  - formulas
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>formulas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="formulas" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.formulas" /></td></tr>
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
    <td>The identifier of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="author" /></td>
    <td><code>string</code></td>
    <td>The author of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="formulaContent" /></td>
    <td><code>object</code></td>
    <td>The content of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The OS type of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueIdentifier" /></td>
    <td><code>string</code></td>
    <td>The unique immutable identifier of a resource (Guid).</td>
</tr>
<tr>
    <td><CopyableCode code="vm" /></td>
    <td><code>object</code></td>
    <td>Information about a VM from which a formula is to be created.</td>
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
    <td>The identifier of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="author" /></td>
    <td><code>string</code></td>
    <td>The author of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="creationDate" /></td>
    <td><code>string (date-time)</code></td>
    <td>The creation date of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>The description of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="formulaContent" /></td>
    <td><code>object</code></td>
    <td>The content of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The location of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The OS type of the formula.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The provisioning status of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>The tags of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="uniqueIdentifier" /></td>
    <td><code>string</code></td>
    <td>The unique immutable identifier of a resource (Guid).</td>
</tr>
<tr>
    <td><CopyableCode code="vm" /></td>
    <td><code>object</code></td>
    <td>Information about a VM from which a formula is to be created.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Get formula.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List formulas in a given lab.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or replace an existing formula. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Allows modifying tags of formulas. All other properties will be ignored.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or replace an existing formula. This operation can take a while to complete.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-lab_name"><code>lab_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete formula.</td>
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
<tr id="parameter-lab_name">
    <td><CopyableCode code="lab_name" /></td>
    <td><code>string</code></td>
    <td>The name of the lab. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the formula. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>Specify the $expand query. Example: 'properties($select=description)'. Default value is None.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply to the operation. Example: '$filter=contains(name,'myName'). Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>The ordering expression for the results, using OData notation. Example: '$orderby=name desc'. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The maximum number of resources to return from the operation. Example: '$top=10'. Default value is None.</td>
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

Get formula.

```sql
SELECT
id,
name,
author,
creationDate,
description,
formulaContent,
location,
osType,
provisioningState,
tags,
type,
uniqueIdentifier,
vm
FROM azure.dev_test_labs.formulas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list">

List formulas in a given lab.

```sql
SELECT
id,
name,
author,
creationDate,
description,
formulaContent,
location,
osType,
provisioningState,
tags,
type,
uniqueIdentifier,
vm
FROM azure.dev_test_labs.formulas
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND lab_name = '{{ lab_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
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

Create or replace an existing formula. This operation can take a while to complete.

```sql
INSERT INTO azure.dev_test_labs.formulas (
location,
tags,
properties,
resource_group_name,
lab_name,
name,
subscription_id
)
SELECT 
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ lab_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
tags,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: formulas
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the formulas resource.
    - name: lab_name
      value: "{{ lab_name }}"
      description: Required parameter for the formulas resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the formulas resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the formulas resource.
    - name: location
      value: "{{ location }}"
      description: |
        The location of the resource.
    - name: tags
      value: "{{ tags }}"
      description: |
        The tags of the resource.
    - name: properties
      value:
        description: "{{ description }}"
        osType: "{{ osType }}"
        formulaContent:
          name: "{{ name }}"
          location: "{{ location }}"
          tags: "{{ tags }}"
          properties:
            bulkCreationParameters:
              instanceCount: {{ instanceCount }}
            notes: "{{ notes }}"
            ownerObjectId: "{{ ownerObjectId }}"
            ownerUserPrincipalName: "{{ ownerUserPrincipalName }}"
            createdDate: "{{ createdDate }}"
            customImageId: "{{ customImageId }}"
            size: "{{ size }}"
            userName: "{{ userName }}"
            password: "{{ password }}"
            sshKey: "{{ sshKey }}"
            isAuthenticationWithSshKey: {{ isAuthenticationWithSshKey }}
            labSubnetName: "{{ labSubnetName }}"
            labVirtualNetworkId: "{{ labVirtualNetworkId }}"
            disallowPublicIpAddress: {{ disallowPublicIpAddress }}
            artifacts:
              - artifactId: "{{ artifactId }}"
                artifactTitle: "{{ artifactTitle }}"
                parameters: "{{ parameters }}"
                status: "{{ status }}"
                deploymentStatusMessage: "{{ deploymentStatusMessage }}"
                vmExtensionStatusMessage: "{{ vmExtensionStatusMessage }}"
                installTime: "{{ installTime }}"
            galleryImageReference:
              offer: "{{ offer }}"
              publisher: "{{ publisher }}"
              sku: "{{ sku }}"
              osType: "{{ osType }}"
              version: "{{ version }}"
            planId: "{{ planId }}"
            networkInterface:
              virtualNetworkId: "{{ virtualNetworkId }}"
              subnetId: "{{ subnetId }}"
              publicIpAddressId: "{{ publicIpAddressId }}"
              publicIpAddress: "{{ publicIpAddress }}"
              privateIpAddress: "{{ privateIpAddress }}"
              dnsName: "{{ dnsName }}"
              rdpAuthority: "{{ rdpAuthority }}"
              sshAuthority: "{{ sshAuthority }}"
              sharedPublicIpAddressConfiguration:
                inboundNatRules: "{{ inboundNatRules }}"
            expirationDate: "{{ expirationDate }}"
            allowClaim: {{ allowClaim }}
            storageType: "{{ storageType }}"
            environmentId: "{{ environmentId }}"
            dataDiskParameters:
              - attachNewDataDiskOptions:
                  diskSizeGiB: {{ diskSizeGiB }}
                  diskName: "{{ diskName }}"
                  diskType: "{{ diskType }}"
                existingLabDiskId: "{{ existingLabDiskId }}"
                hostCaching: "{{ hostCaching }}"
            scheduleParameters:
              - name: "{{ name }}"
                location: "{{ location }}"
                tags: "{{ tags }}"
                properties:
                  status: "{{ status }}"
                  taskType: "{{ taskType }}"
                  weeklyRecurrence: "{{ weeklyRecurrence }}"
                  dailyRecurrence: "{{ dailyRecurrence }}"
                  hourlyRecurrence: "{{ hourlyRecurrence }}"
                  timeZoneId: "{{ timeZoneId }}"
                  notificationSettings: "{{ notificationSettings }}"
                  targetResourceId: "{{ targetResourceId }}"
        vm:
          labVmId: "{{ labVmId }}"
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

Allows modifying tags of formulas. All other properties will be ignored.

```sql
UPDATE azure.dev_test_labs.formulas
SET 
-- No updatable properties
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Create or replace an existing formula. This operation can take a while to complete.

```sql
REPLACE azure.dev_test_labs.formulas
SET 
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
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

Delete formula.

```sql
DELETE FROM azure.dev_test_labs.formulas
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND lab_name = '{{ lab_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
