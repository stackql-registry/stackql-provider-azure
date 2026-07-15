--- 
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - traffic_manager
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="profiles" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.profiles" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'check_traffic_manager_relative_dns_name_availability', value: 'check_traffic_manager_relative_dns_name_availability' }
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/trafficManagerProfiles/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedEndpointRecordTypes" /></td>
    <td><code>array</code></td>
    <td>The list of allowed endpoint record types.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfig" /></td>
    <td><code>object</code></td>
    <td>The DNS settings of the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>The list of endpoints in the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure Region where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="maxReturn" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of endpoints to be returned for MultiValue routing type.</td>
</tr>
<tr>
    <td><CopyableCode code="monitorConfig" /></td>
    <td><code>object</code></td>
    <td>The endpoint monitoring settings of the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="profileStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the Traffic Manager profile. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="recordType" /></td>
    <td><code>string</code></td>
    <td>When record type is set, a traffic manager profile will allow only endpoints that match this type. Known values are: "A", "AAAA", and "CNAME". (A, AAAA, CNAME)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRoutingMethod" /></td>
    <td><code>string</code></td>
    <td>The traffic routing method of the Traffic Manager profile. Known values are: "Performance", "Priority", "Weighted", "Geographic", "MultiValue", and "Subnet". (Performance, Priority, Weighted, Geographic, MultiValue, Subnet)</td>
</tr>
<tr>
    <td><CopyableCode code="trafficViewEnrollmentStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Traffic View is 'Enabled' or 'Disabled' for the Traffic Manager profile. Null, indicates 'Disabled'. Enabling this feature will increase the cost of the Traffic Manage profile. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.</td>
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/trafficManagerProfiles/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedEndpointRecordTypes" /></td>
    <td><code>array</code></td>
    <td>The list of allowed endpoint record types.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfig" /></td>
    <td><code>object</code></td>
    <td>The DNS settings of the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>The list of endpoints in the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure Region where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="maxReturn" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of endpoints to be returned for MultiValue routing type.</td>
</tr>
<tr>
    <td><CopyableCode code="monitorConfig" /></td>
    <td><code>object</code></td>
    <td>The endpoint monitoring settings of the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="profileStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the Traffic Manager profile. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="recordType" /></td>
    <td><code>string</code></td>
    <td>When record type is set, a traffic manager profile will allow only endpoints that match this type. Known values are: "A", "AAAA", and "CNAME". (A, AAAA, CNAME)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRoutingMethod" /></td>
    <td><code>string</code></td>
    <td>The traffic routing method of the Traffic Manager profile. Known values are: "Performance", "Priority", "Weighted", "Geographic", "MultiValue", and "Subnet". (Performance, Priority, Weighted, Geographic, MultiValue, Subnet)</td>
</tr>
<tr>
    <td><CopyableCode code="trafficViewEnrollmentStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Traffic View is 'Enabled' or 'Disabled' for the Traffic Manager profile. Null, indicates 'Disabled'. Enabling this feature will increase the cost of the Traffic Manage profile. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.</td>
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
    <td>Fully qualified resource Id for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.Network/trafficManagerProfiles/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="allowedEndpointRecordTypes" /></td>
    <td><code>array</code></td>
    <td>The list of allowed endpoint record types.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsConfig" /></td>
    <td><code>object</code></td>
    <td>The DNS settings of the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="endpoints" /></td>
    <td><code>array</code></td>
    <td>The list of endpoints in the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The Azure Region where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="maxReturn" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of endpoints to be returned for MultiValue routing type.</td>
</tr>
<tr>
    <td><CopyableCode code="monitorConfig" /></td>
    <td><code>object</code></td>
    <td>The endpoint monitoring settings of the Traffic Manager profile.</td>
</tr>
<tr>
    <td><CopyableCode code="profileStatus" /></td>
    <td><code>string</code></td>
    <td>The status of the Traffic Manager profile. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="recordType" /></td>
    <td><code>string</code></td>
    <td>When record type is set, a traffic manager profile will allow only endpoints that match this type. Known values are: "A", "AAAA", and "CNAME". (A, AAAA, CNAME)</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="trafficRoutingMethod" /></td>
    <td><code>string</code></td>
    <td>The traffic routing method of the Traffic Manager profile. Known values are: "Performance", "Priority", "Weighted", "Geographic", "MultiValue", and "Subnet". (Performance, Priority, Weighted, Geographic, MultiValue, Subnet)</td>
</tr>
<tr>
    <td><CopyableCode code="trafficViewEnrollmentStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether Traffic View is 'Enabled' or 'Disabled' for the Traffic Manager profile. Null, indicates 'Disabled'. Enabling this feature will increase the cost of the Traffic Manage profile. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="check_traffic_manager_relative_dns_name_availability">

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
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The relative name.</td>
</tr>
<tr>
    <td><CopyableCode code="message" /></td>
    <td><code>string</code></td>
    <td>Descriptive message that explains why the name is not available, when applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="nameAvailable" /></td>
    <td><code>boolean</code></td>
    <td>Describes whether the relative name is available or not.</td>
</tr>
<tr>
    <td><CopyableCode code="reason" /></td>
    <td><code>string</code></td>
    <td>The reason why the name is not available, when applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Traffic Manager profile resource type.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Traffic Manager profile.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Traffic Manager profiles within a resource group.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all Traffic Manager profiles within a subscription.</td>
</tr>
<tr>
    <td><a href="#check_traffic_manager_relative_dns_name_availability"><CopyableCode code="check_traffic_manager_relative_dns_name_availability" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td></td>
    <td>Checks the availability of a Traffic Manager Relative DNS name.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Traffic Manager profile.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a Traffic Manager profile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a Traffic Manager profile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a Traffic Manager profile.</td>
</tr>
<tr>
    <td><a href="#check_traffic_manager_name_availability_v2"><CopyableCode code="check_traffic_manager_name_availability_v2" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Checks the availability of a Traffic Manager Relative DNS name.</td>
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
<tr id="parameter-profile_name">
    <td><CopyableCode code="profile_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Traffic Manager profile. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' },
        { label: 'check_traffic_manager_relative_dns_name_availability', value: 'check_traffic_manager_relative_dns_name_availability' }
    ]}
>
<TabItem value="get">

Gets a Traffic Manager profile.

```sql
SELECT
id,
name,
allowedEndpointRecordTypes,
dnsConfig,
endpoints,
location,
maxReturn,
monitorConfig,
profileStatus,
recordType,
tags,
trafficRoutingMethod,
trafficViewEnrollmentStatus,
type
FROM azure.traffic_manager.profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Lists all Traffic Manager profiles within a resource group.

```sql
SELECT
id,
name,
allowedEndpointRecordTypes,
dnsConfig,
endpoints,
location,
maxReturn,
monitorConfig,
profileStatus,
recordType,
tags,
trafficRoutingMethod,
trafficViewEnrollmentStatus,
type
FROM azure.traffic_manager.profiles
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

Lists all Traffic Manager profiles within a subscription.

```sql
SELECT
id,
name,
allowedEndpointRecordTypes,
dnsConfig,
endpoints,
location,
maxReturn,
monitorConfig,
profileStatus,
recordType,
tags,
trafficRoutingMethod,
trafficViewEnrollmentStatus,
type
FROM azure.traffic_manager.profiles
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="check_traffic_manager_relative_dns_name_availability">

Checks the availability of a Traffic Manager Relative DNS name.

```sql
SELECT
name,
message,
nameAvailable,
reason,
type
FROM azure.traffic_manager.profiles
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

Create or update a Traffic Manager profile.

```sql
INSERT INTO azure.traffic_manager.profiles (
id,
name,
type,
tags,
location,
properties,
resource_group_name,
profile_name,
subscription_id
)
SELECT 
'{{ id }}',
'{{ name }}',
'{{ type }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
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
- name: profiles
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the profiles resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the profiles resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the profiles resource.
    - name: id
      value: "{{ id }}"
      description: |
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}.
    - name: name
      value: "{{ name }}"
      description: |
        The name of the resource.
    - name: type
      value: "{{ type }}"
      description: |
        The type of the resource. Ex- Microsoft.Network/trafficManagerProfiles.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The Azure Region where the resource lives.
    - name: properties
      description: |
        The properties of the Traffic Manager profile.
      value:
        profileStatus: "{{ profileStatus }}"
        trafficRoutingMethod: "{{ trafficRoutingMethod }}"
        dnsConfig:
          relativeName: "{{ relativeName }}"
          fqdn: "{{ fqdn }}"
          ttl: {{ ttl }}
        monitorConfig:
          profileMonitorStatus: "{{ profileMonitorStatus }}"
          protocol: "{{ protocol }}"
          port: {{ port }}
          path: "{{ path }}"
          intervalInSeconds: {{ intervalInSeconds }}
          timeoutInSeconds: {{ timeoutInSeconds }}
          toleratedNumberOfFailures: {{ toleratedNumberOfFailures }}
          customHeaders:
            - name: "{{ name }}"
              value: "{{ value }}"
          expectedStatusCodeRanges:
            - min: {{ min }}
              max: {{ max }}
        endpoints:
          - id: "{{ id }}"
            name: "{{ name }}"
            type: "{{ type }}"
            properties:
              targetResourceId: "{{ targetResourceId }}"
              target: "{{ target }}"
              endpointStatus: "{{ endpointStatus }}"
              weight: {{ weight }}
              priority: {{ priority }}
              endpointLocation: "{{ endpointLocation }}"
              endpointMonitorStatus: "{{ endpointMonitorStatus }}"
              minChildEndpoints: {{ minChildEndpoints }}
              minChildEndpointsIPv4: {{ minChildEndpointsIPv4 }}
              minChildEndpointsIPv6: {{ minChildEndpointsIPv6 }}
              geoMapping:
                - "{{ geoMapping }}"
              subnets:
                - first: "{{ first }}"
                  last: "{{ last }}"
                  scope: {{ scope }}
              customHeaders:
                - name: "{{ name }}"
                  value: "{{ value }}"
              alwaysServe: "{{ alwaysServe }}"
        trafficViewEnrollmentStatus: "{{ trafficViewEnrollmentStatus }}"
        allowedEndpointRecordTypes:
          - "{{ allowedEndpointRecordTypes }}"
        maxReturn: {{ maxReturn }}
        recordType: "{{ recordType }}"
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

Update a Traffic Manager profile.

```sql
UPDATE azure.traffic_manager.profiles
SET 
id = '{{ id }}',
name = '{{ name }}',
type = '{{ type }}',
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
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

Create or update a Traffic Manager profile.

```sql
REPLACE azure.traffic_manager.profiles
SET 
id = '{{ id }}',
name = '{{ name }}',
type = '{{ type }}',
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
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

Deletes a Traffic Manager profile.

```sql
DELETE FROM azure.traffic_manager.profiles
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="check_traffic_manager_name_availability_v2"
    values={[
        { label: 'check_traffic_manager_name_availability_v2', value: 'check_traffic_manager_name_availability_v2' }
    ]}
>
<TabItem value="check_traffic_manager_name_availability_v2">

Checks the availability of a Traffic Manager Relative DNS name.

```sql
EXEC azure.traffic_manager.profiles.check_traffic_manager_name_availability_v2 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}", 
"type": "{{ type }}"
}'
;
```
</TabItem>
</Tabs>
