--- 
title: afd_origins
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_origins
  - cdn
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

Creates, updates, deletes, gets or lists an <code>afd_origins</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="afd_origins" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_origins" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_origin_group', value: 'list_by_origin_group' }
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
    <td><CopyableCode code="azureOrigin" /></td>
    <td><code>object</code></td>
    <td>Resource reference to the Azure origin resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="enforceCertificateNameCheck" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable certificate name check at origin level.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="httpPort" /></td>
    <td><code>integer</code></td>
    <td>The value of the HTTP port. Must be between 1 and 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsPort" /></td>
    <td><code>integer</code></td>
    <td>The value of the HTTPS port. Must be between 1 and 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="originGroupName" /></td>
    <td><code>string</code></td>
    <td>The name of the origin group which contains this origin.</td>
</tr>
<tr>
    <td><CopyableCode code="originHostHeader" /></td>
    <td><code>string</code></td>
    <td>The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure Front Door origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResource" /></td>
    <td><code>object</code></td>
    <td>The properties of the private link resource for private origin.</td>
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
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>Weight of the origin in given origin group for load balancing. Must be between 1 and 1000.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_origin_group">

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
    <td><CopyableCode code="azureOrigin" /></td>
    <td><code>object</code></td>
    <td>Resource reference to the Azure origin resource.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="enabledState" /></td>
    <td><code>string</code></td>
    <td>Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="enforceCertificateNameCheck" /></td>
    <td><code>boolean</code></td>
    <td>Whether to enable certificate name check at origin level.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="httpPort" /></td>
    <td><code>integer</code></td>
    <td>The value of the HTTP port. Must be between 1 and 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsPort" /></td>
    <td><code>integer</code></td>
    <td>The value of the HTTPS port. Must be between 1 and 65535.</td>
</tr>
<tr>
    <td><CopyableCode code="originGroupName" /></td>
    <td><code>string</code></td>
    <td>The name of the origin group which contains this origin.</td>
</tr>
<tr>
    <td><CopyableCode code="originHostHeader" /></td>
    <td><code>string</code></td>
    <td>The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure Front Door origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>integer</code></td>
    <td>Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="sharedPrivateLinkResource" /></td>
    <td><code>object</code></td>
    <td>The properties of the private link resource for private origin.</td>
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
<tr>
    <td><CopyableCode code="weight" /></td>
    <td><code>integer</code></td>
    <td>Weight of the origin in given origin group for load balancing. Must be between 1 and 1000.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing origin within an origin group.</td>
</tr>
<tr>
    <td><a href="#list_by_origin_group"><CopyableCode code="list_by_origin_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the existing origins within an origin group.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new origin within the specified origin group.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing origin within an origin group.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-origin_group_name"><code>origin_group_name</code></a>, <a href="#parameter-origin_name"><code>origin_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing origin within an origin group.</td>
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
<tr id="parameter-origin_group_name">
    <td><CopyableCode code="origin_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the origin group which is unique within the endpoint. Required.</td>
</tr>
<tr id="parameter-origin_name">
    <td><CopyableCode code="origin_name" /></td>
    <td><code>string</code></td>
    <td>Name of the origin which is unique within the profile. Required.</td>
</tr>
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group. Required.</td>
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
        { label: 'list_by_origin_group', value: 'list_by_origin_group' }
    ]}
>
<TabItem value="get">

Gets an existing origin within an origin group.

```sql
SELECT
id,
name,
azureOrigin,
deploymentStatus,
enabledState,
enforceCertificateNameCheck,
hostName,
httpPort,
httpsPort,
originGroupName,
originHostHeader,
priority,
provisioningState,
sharedPrivateLinkResource,
systemData,
type,
weight
FROM azure.cdn.afd_origins
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND origin_group_name = '{{ origin_group_name }}' -- required
AND origin_name = '{{ origin_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_origin_group">

Lists all of the existing origins within an origin group.

```sql
SELECT
id,
name,
azureOrigin,
deploymentStatus,
enabledState,
enforceCertificateNameCheck,
hostName,
httpPort,
httpsPort,
originGroupName,
originHostHeader,
priority,
provisioningState,
sharedPrivateLinkResource,
systemData,
type,
weight
FROM azure.cdn.afd_origins
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND origin_group_name = '{{ origin_group_name }}' -- required
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

Creates a new origin within the specified origin group.

```sql
INSERT INTO azure.cdn.afd_origins (
properties,
resource_group_name,
profile_name,
origin_group_name,
origin_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ origin_group_name }}',
'{{ origin_name }}',
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
- name: afd_origins
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the afd_origins resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the afd_origins resource.
    - name: origin_group_name
      value: "{{ origin_group_name }}"
      description: Required parameter for the afd_origins resource.
    - name: origin_name
      value: "{{ origin_name }}"
      description: Required parameter for the afd_origins resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the afd_origins resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the origin.
      value:
        originGroupName: "{{ originGroupName }}"
        azureOrigin:
          id: "{{ id }}"
        hostName: "{{ hostName }}"
        httpPort: {{ httpPort }}
        httpsPort: {{ httpsPort }}
        originHostHeader: "{{ originHostHeader }}"
        priority: {{ priority }}
        weight: {{ weight }}
        sharedPrivateLinkResource:
          privateLink:
            id: "{{ id }}"
          privateLinkLocation: "{{ privateLinkLocation }}"
          groupId: "{{ groupId }}"
          requestMessage: "{{ requestMessage }}"
          status: "{{ status }}"
        enabledState: "{{ enabledState }}"
        enforceCertificateNameCheck: {{ enforceCertificateNameCheck }}
        provisioningState: "{{ provisioningState }}"
        deploymentStatus: "{{ deploymentStatus }}"
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

Updates an existing origin within an origin group.

```sql
UPDATE azure.cdn.afd_origins
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND origin_group_name = '{{ origin_group_name }}' --required
AND origin_name = '{{ origin_name }}' --required
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

Deletes an existing origin within an origin group.

```sql
DELETE FROM azure.cdn.afd_origins
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND origin_group_name = '{{ origin_group_name }}' --required
AND origin_name = '{{ origin_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
