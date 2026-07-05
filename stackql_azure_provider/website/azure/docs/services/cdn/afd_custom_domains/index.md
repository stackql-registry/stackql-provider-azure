--- 
title: afd_custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_custom_domains
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

Creates, updates, deletes, gets or lists an <code>afd_custom_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="afd_custom_domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_custom_domains" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_profile', value: 'list_by_profile' }
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
    <td><CopyableCode code="azureDnsZone" /></td>
    <td><code>object</code></td>
    <td>Resource reference to the Azure DNS zone.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="domainValidationState" /></td>
    <td><code>string</code></td>
    <td>Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. DCV stands for DomainControlValidation. Known values are: "Unknown", "Submitting", "Pending", "Rejected", "TimedOut", "PendingRevalidation", "Approved", "RefreshingValidationToken", and "InternalError". (Unknown, Submitting, Pending, Rejected, TimedOut, PendingRevalidation, Approved, RefreshingValidationToken, InternalError)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing migration properties for domains.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the domain. Must be a domain name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="preValidatedCustomDomainResourceId" /></td>
    <td><code>object</code></td>
    <td>Resource reference to the Azure resource where custom domain ownership was prevalidated.</td>
</tr>
<tr>
    <td><CopyableCode code="profileName" /></td>
    <td><code>string</code></td>
    <td>The name of the profile which holds the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tlsSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration specifying how to enable HTTPS for the domain - using AzureFrontDoor managed certificate or user's own certificate. If not specified, enabling ssl uses AzureFrontDoor managed certificate by default.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationProperties" /></td>
    <td><code>object</code></td>
    <td>Values the customer needs to validate domain ownership.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_profile">

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
    <td><CopyableCode code="azureDnsZone" /></td>
    <td><code>object</code></td>
    <td>Resource reference to the Azure DNS zone.</td>
</tr>
<tr>
    <td><CopyableCode code="deploymentStatus" /></td>
    <td><code>string</code></td>
    <td>Known values are: "NotStarted", "InProgress", "Succeeded", and "Failed". (NotStarted, InProgress, Succeeded, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="domainValidationState" /></td>
    <td><code>string</code></td>
    <td>Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. DCV stands for DomainControlValidation. Known values are: "Unknown", "Submitting", "Pending", "Rejected", "TimedOut", "PendingRevalidation", "Approved", "RefreshingValidationToken", and "InternalError". (Unknown, Submitting, Pending, Rejected, TimedOut, PendingRevalidation, Approved, RefreshingValidationToken, InternalError)</td>
</tr>
<tr>
    <td><CopyableCode code="extendedProperties" /></td>
    <td><code>object</code></td>
    <td>Key-Value pair representing migration properties for domains.</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the domain. Must be a domain name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="preValidatedCustomDomainResourceId" /></td>
    <td><code>object</code></td>
    <td>Resource reference to the Azure resource where custom domain ownership was prevalidated.</td>
</tr>
<tr>
    <td><CopyableCode code="profileName" /></td>
    <td><code>string</code></td>
    <td>The name of the profile which holds the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status. Known values are: "Succeeded", "Failed", "Updating", "Deleting", and "Creating". (Succeeded, Failed, Updating, Deleting, Creating)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tlsSettings" /></td>
    <td><code>object</code></td>
    <td>The configuration specifying how to enable HTTPS for the domain - using AzureFrontDoor managed certificate or user's own certificate. If not specified, enabling ssl uses AzureFrontDoor managed certificate by default.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="validationProperties" /></td>
    <td><code>object</code></td>
    <td>Values the customer needs to validate domain ownership.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile.</td>
</tr>
<tr>
    <td><a href="#list_by_profile"><CopyableCode code="list_by_profile" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists existing AzureFrontDoor domains.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new domain within the specified profile.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates an existing domain within a profile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile.</td>
</tr>
<tr>
    <td><a href="#refresh_validation_token"><CopyableCode code="refresh_validation_token" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates the domain validation token.</td>
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
<tr id="parameter-custom_domain_name">
    <td><CopyableCode code="custom_domain_name" /></td>
    <td><code>string</code></td>
    <td>Name of the domain under the profile which is unique globally. Required.</td>
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
        { label: 'list_by_profile', value: 'list_by_profile' }
    ]}
>
<TabItem value="get">

Gets an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile.

```sql
SELECT
id,
name,
azureDnsZone,
deploymentStatus,
domainValidationState,
extendedProperties,
hostName,
preValidatedCustomDomainResourceId,
profileName,
provisioningState,
systemData,
tlsSettings,
type,
validationProperties
FROM azure.cdn.afd_custom_domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND custom_domain_name = '{{ custom_domain_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_profile">

Lists existing AzureFrontDoor domains.

```sql
SELECT
id,
name,
azureDnsZone,
deploymentStatus,
domainValidationState,
extendedProperties,
hostName,
preValidatedCustomDomainResourceId,
profileName,
provisioningState,
systemData,
tlsSettings,
type,
validationProperties
FROM azure.cdn.afd_custom_domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
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

Creates a new domain within the specified profile.

```sql
INSERT INTO azure.cdn.afd_custom_domains (
properties,
resource_group_name,
profile_name,
custom_domain_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ custom_domain_name }}',
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
- name: afd_custom_domains
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the afd_custom_domains resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the afd_custom_domains resource.
    - name: custom_domain_name
      value: "{{ custom_domain_name }}"
      description: Required parameter for the afd_custom_domains resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the afd_custom_domains resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the domain to create.
      value:
        profileName: "{{ profileName }}"
        tlsSettings:
          certificateType: "{{ certificateType }}"
          cipherSuiteSetType: "{{ cipherSuiteSetType }}"
          minimumTlsVersion: "{{ minimumTlsVersion }}"
          customizedCipherSuiteSet:
            cipherSuiteSetForTls12:
              - "{{ cipherSuiteSetForTls12 }}"
            cipherSuiteSetForTls13:
              - "{{ cipherSuiteSetForTls13 }}"
          secret:
            id: "{{ id }}"
        azureDnsZone:
          id: "{{ id }}"
        preValidatedCustomDomainResourceId:
          id: "{{ id }}"
        provisioningState: "{{ provisioningState }}"
        deploymentStatus: "{{ deploymentStatus }}"
        domainValidationState: "{{ domainValidationState }}"
        hostName: "{{ hostName }}"
        extendedProperties: "{{ extendedProperties }}"
        validationProperties:
          validationToken: "{{ validationToken }}"
          expirationDate: "{{ expirationDate }}"
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

Updates an existing domain within a profile.

```sql
UPDATE azure.cdn.afd_custom_domains
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND custom_domain_name = '{{ custom_domain_name }}' --required
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

Deletes an existing AzureFrontDoor domain with the specified domain name under the specified subscription, resource group and profile.

```sql
DELETE FROM azure.cdn.afd_custom_domains
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND custom_domain_name = '{{ custom_domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="refresh_validation_token"
    values={[
        { label: 'refresh_validation_token', value: 'refresh_validation_token' }
    ]}
>
<TabItem value="refresh_validation_token">

Updates the domain validation token.

```sql
EXEC azure.cdn.afd_custom_domains.refresh_validation_token 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@custom_domain_name='{{ custom_domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
