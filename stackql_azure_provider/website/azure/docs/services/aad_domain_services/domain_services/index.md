--- 
title: domain_services
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_services
  - aad_domain_services
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

Creates, updates, deletes, gets or lists a <code>domain_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="domain_services" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aad_domain_services.domain_services" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

HTTP 200 (OK) if the operation was successful.

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
    <td>Resource Id</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Domain service properties</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_resource_group">

HTTP 200 (OK) if the operation was successful.

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
    <td>Resource Id</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Domain service properties</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list">

HTTP 200 (OK) if the operation was successful.

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
    <td>Resource Id</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name</td>
</tr>
<tr>
    <td><CopyableCode code="etag" /></td>
    <td><code>string</code></td>
    <td>Resource etag</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location</td>
</tr>
<tr>
    <td><CopyableCode code="properties" /></td>
    <td><code>object</code></td>
    <td>Domain service properties</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system meta data relating to this resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type</td>
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
    <td><a href="#parameter-subscriptionId"><code>subscriptionId</code></a>, <a href="#parameter-resourceGroupName"><code>resourceGroupName</code></a>, <a href="#parameter-domainServiceName"><code>domainServiceName</code></a></td>
    <td></td>
    <td>The Get Domain Service operation retrieves a json representation of the Domain Service.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscriptionId"><code>subscriptionId</code></a>, <a href="#parameter-resourceGroupName"><code>resourceGroupName</code></a></td>
    <td></td>
    <td>The List Domain Services in Resource Group operation lists all the domain services available under the given resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscriptionId"><code>subscriptionId</code></a></td>
    <td></td>
    <td>The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription).</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-subscriptionId"><code>subscriptionId</code></a>, <a href="#parameter-resourceGroupName"><code>resourceGroupName</code></a>, <a href="#parameter-domainServiceName"><code>domainServiceName</code></a></td>
    <td></td>
    <td>The Create Domain Service operation creates a new domain service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-subscriptionId"><code>subscriptionId</code></a>, <a href="#parameter-resourceGroupName"><code>resourceGroupName</code></a>, <a href="#parameter-domainServiceName"><code>domainServiceName</code></a></td>
    <td></td>
    <td>The Update Domain Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-subscriptionId"><code>subscriptionId</code></a>, <a href="#parameter-resourceGroupName"><code>resourceGroupName</code></a>, <a href="#parameter-domainServiceName"><code>domainServiceName</code></a></td>
    <td></td>
    <td>The Delete Domain Service operation deletes an existing Domain Service.</td>
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
<tr id="parameter-domainServiceName">
    <td><CopyableCode code="domainServiceName" /></td>
    <td><code>string</code></td>
    <td>The name of the domain service.</td>
</tr>
<tr id="parameter-resourceGroupName">
    <td><CopyableCode code="resourceGroupName" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group within the user's subscription. The name is case insensitive.</td>
</tr>
<tr id="parameter-subscriptionId">
    <td><CopyableCode code="subscriptionId" /></td>
    <td><code>string</code></td>
    <td>Gets subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

The Get Domain Service operation retrieves a json representation of the Domain Service.

```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.aad_domain_services.domain_services
WHERE subscriptionId = '{{ subscriptionId }}' -- required
AND resourceGroupName = '{{ resourceGroupName }}' -- required
AND domainServiceName = '{{ domainServiceName }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

The List Domain Services in Resource Group operation lists all the domain services available under the given resource group.

```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.aad_domain_services.domain_services
WHERE subscriptionId = '{{ subscriptionId }}' -- required
AND resourceGroupName = '{{ resourceGroupName }}' -- required
;
```
</TabItem>
<TabItem value="list">

The List Domain Services in Subscription operation lists all the domain services available under the given subscription (and across all resource groups within that subscription).

```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.aad_domain_services.domain_services
WHERE subscriptionId = '{{ subscriptionId }}' -- required
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

The Create Domain Service operation creates a new domain service with the specified parameters. If the specific service already exists, then any patchable properties will be updated and any immutable properties will remain unchanged.

```sql
INSERT INTO azure.aad_domain_services.domain_services (
data__properties,
data__location,
data__tags,
data__etag,
subscriptionId,
resourceGroupName,
domainServiceName
)
SELECT 
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ etag }}',
'{{ subscriptionId }}',
'{{ resourceGroupName }}',
'{{ domainServiceName }}'
RETURNING
id,
name,
etag,
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
- name: domain_services
  props:
    - name: subscriptionId
      value: "{{ subscriptionId }}"
      description: Required parameter for the domain_services resource.
    - name: resourceGroupName
      value: "{{ resourceGroupName }}"
      description: Required parameter for the domain_services resource.
    - name: domainServiceName
      value: "{{ domainServiceName }}"
      description: Required parameter for the domain_services resource.
    - name: properties
      description: |
        Domain service properties
      value:
        version: {{ version }}
        tenantId: "{{ tenantId }}"
        domainName: "{{ domainName }}"
        deploymentId: "{{ deploymentId }}"
        syncOwner: "{{ syncOwner }}"
        syncApplicationId: "{{ syncApplicationId }}"
        replicaSets:
          - replicaSetId: "{{ replicaSetId }}"
            location: "{{ location }}"
            vnetSiteId: "{{ vnetSiteId }}"
            subnetId: "{{ subnetId }}"
            domainControllerIpAddress: "{{ domainControllerIpAddress }}"
            externalAccessIpAddress: "{{ externalAccessIpAddress }}"
            serviceStatus: "{{ serviceStatus }}"
            healthLastEvaluated: "{{ healthLastEvaluated }}"
            healthMonitors: "{{ healthMonitors }}"
            healthAlerts: "{{ healthAlerts }}"
        ldapsSettings:
          ldaps: "{{ ldaps }}"
          pfxCertificate: "{{ pfxCertificate }}"
          pfxCertificatePassword: "{{ pfxCertificatePassword }}"
          publicCertificate: "{{ publicCertificate }}"
          certificateThumbprint: "{{ certificateThumbprint }}"
          certificateNotAfter: "{{ certificateNotAfter }}"
          externalAccess: "{{ externalAccess }}"
        resourceForestSettings:
          settings:
            - trustedDomainFqdn: "{{ trustedDomainFqdn }}"
              trustDirection: "{{ trustDirection }}"
              friendlyName: "{{ friendlyName }}"
              remoteDnsIps: "{{ remoteDnsIps }}"
              trustPassword: "{{ trustPassword }}"
          resourceForest: "{{ resourceForest }}"
        domainSecuritySettings:
          ntlmV1: "{{ ntlmV1 }}"
          tlsV1: "{{ tlsV1 }}"
          syncNtlmPasswords: "{{ syncNtlmPasswords }}"
          syncKerberosPasswords: "{{ syncKerberosPasswords }}"
          syncOnPremPasswords: "{{ syncOnPremPasswords }}"
          kerberosRc4Encryption: "{{ kerberosRc4Encryption }}"
          kerberosArmoring: "{{ kerberosArmoring }}"
          ldapSigning: "{{ ldapSigning }}"
          channelBinding: "{{ channelBinding }}"
        domainConfigurationType: "{{ domainConfigurationType }}"
        sku: "{{ sku }}"
        filteredSync: "{{ filteredSync }}"
        syncScope: "{{ syncScope }}"
        notificationSettings:
          notifyGlobalAdmins: "{{ notifyGlobalAdmins }}"
          notifyDcAdmins: "{{ notifyDcAdmins }}"
          additionalRecipients:
            - "{{ additionalRecipients }}"
        migrationProperties:
          oldSubnetId: "{{ oldSubnetId }}"
          oldVnetSiteId: "{{ oldVnetSiteId }}"
          migrationProgress:
            completionPercentage: {{ completionPercentage }}
            progressMessage: "{{ progressMessage }}"
        provisioningState: "{{ provisioningState }}"
        configDiagnostics:
          lastExecuted: "{{ lastExecuted }}"
          validatorResults:
            - validatorId: "{{ validatorId }}"
              replicaSetSubnetDisplayName: "{{ replicaSetSubnetDisplayName }}"
              status: "{{ status }}"
              issues: "{{ issues }}"
    - name: location
      value: "{{ location }}"
      description: |
        Resource location
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags
    - name: etag
      value: "{{ etag }}"
      description: |
        Resource etag
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

The Update Domain Service operation can be used to update the existing deployment. The update call only supports the properties listed in the PATCH body.

```sql
UPDATE azure.aad_domain_services.domain_services
SET 
data__properties = '{{ properties }}',
data__location = '{{ location }}',
data__tags = '{{ tags }}',
data__etag = '{{ etag }}'
WHERE 
subscriptionId = '{{ subscriptionId }}' --required
AND resourceGroupName = '{{ resourceGroupName }}' --required
AND domainServiceName = '{{ domainServiceName }}' --required
RETURNING
id,
name,
etag,
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

The Delete Domain Service operation deletes an existing Domain Service.

```sql
DELETE FROM azure.aad_domain_services.domain_services
WHERE subscriptionId = '{{ subscriptionId }}' --required
AND resourceGroupName = '{{ resourceGroupName }}' --required
AND domainServiceName = '{{ domainServiceName }}' --required
;
```
</TabItem>
</Tabs>
