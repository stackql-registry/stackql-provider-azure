--- 
title: custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domains
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

Creates, updates, deletes, gets or lists a <code>custom_domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="custom_domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.custom_domains" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_endpoint', value: 'list_by_endpoint' }
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
    <td><CopyableCode code="customHttpsParameters" /></td>
    <td><code>object</code></td>
    <td>Certificate parameters for securing custom HTTPS.</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsProvisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the custom domain. Known values are: "Enabling", "Enabled", "Disabling", "Disabled", and "Failed". (Enabling, Enabled, Disabling, Disabled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsProvisioningSubstate" /></td>
    <td><code>string</code></td>
    <td>Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. Known values are: "SubmittingDomainControlValidationRequest", "PendingDomainControlValidationREquestApproval", "DomainControlValidationRequestApproved", "DomainControlValidationRequestRejected", "DomainControlValidationRequestTimedOut", "IssuingCertificate", "DeployingCertificate", "CertificateDeployed", "DeletingCertificate", and "CertificateDeleted". (SubmittingDomainControlValidationRequest, PendingDomainControlValidationREquestApproval, DomainControlValidationRequestApproved, DomainControlValidationRequestRejected, DomainControlValidationRequestTimedOut, IssuingCertificate, DeployingCertificate, CertificateDeployed, DeletingCertificate, CertificateDeleted)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the custom domain. Must be a domain name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of Custom Https of the custom domain. Known values are: "Enabling", "Enabled", "Disabling", "Disabled", and "Failed". (Enabling, Enabled, Disabling, Disabled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the custom domain. Known values are: "Creating", "Active", and "Deleting". (Creating, Active, Deleting)</td>
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
    <td><CopyableCode code="validationData" /></td>
    <td><code>string</code></td>
    <td>Special validation or data may be required when delivering CDN to some regions due to local compliance reasons. E.g. ICP license number of a custom domain is required to deliver content in China.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_endpoint">

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
    <td><CopyableCode code="customHttpsParameters" /></td>
    <td><code>object</code></td>
    <td>Certificate parameters for securing custom HTTPS.</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsProvisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of the custom domain. Known values are: "Enabling", "Enabled", "Disabling", "Disabled", and "Failed". (Enabling, Enabled, Disabling, Disabled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsProvisioningSubstate" /></td>
    <td><code>string</code></td>
    <td>Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. Known values are: "SubmittingDomainControlValidationRequest", "PendingDomainControlValidationREquestApproval", "DomainControlValidationRequestApproved", "DomainControlValidationRequestRejected", "DomainControlValidationRequestTimedOut", "IssuingCertificate", "DeployingCertificate", "CertificateDeployed", "DeletingCertificate", and "CertificateDeleted". (SubmittingDomainControlValidationRequest, PendingDomainControlValidationREquestApproval, DomainControlValidationRequestApproved, DomainControlValidationRequestRejected, DomainControlValidationRequestTimedOut, IssuingCertificate, DeployingCertificate, CertificateDeployed, DeletingCertificate, CertificateDeleted)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the custom domain. Must be a domain name. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of Custom Https of the custom domain. Known values are: "Enabling", "Enabled", "Disabling", "Disabled", and "Failed". (Enabling, Enabled, Disabling, Disabled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the custom domain. Known values are: "Creating", "Active", and "Deleting". (Creating, Active, Deleting)</td>
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
    <td><CopyableCode code="validationData" /></td>
    <td><code>string</code></td>
    <td>Special validation or data may be required when delivering CDN to some regions due to local compliance reasons. E.g. ICP license number of a custom domain is required to deliver content in China.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets an existing custom domain within an endpoint.</td>
</tr>
<tr>
    <td><a href="#list_by_endpoint"><CopyableCode code="list_by_endpoint" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the existing custom domains within an endpoint.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates a new custom domain within an endpoint.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes an existing custom domain within an endpoint.</td>
</tr>
<tr>
    <td><a href="#disable_custom_https"><CopyableCode code="disable_custom_https" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disable https delivery of the custom domain.</td>
</tr>
<tr>
    <td><a href="#enable_custom_https"><CopyableCode code="enable_custom_https" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-profile_name"><code>profile_name</code></a>, <a href="#parameter-endpoint_name"><code>endpoint_name</code></a>, <a href="#parameter-custom_domain_name"><code>custom_domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-certificateSource"><code>certificateSource</code></a>, <a href="#parameter-protocolType"><code>protocolType</code></a></td>
    <td></td>
    <td>Enable https delivery of the custom domain.</td>
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
    <td>Name of the custom domain within an endpoint. Required.</td>
</tr>
<tr id="parameter-endpoint_name">
    <td><CopyableCode code="endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of the endpoint under the profile which is unique globally. Required.</td>
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
        { label: 'list_by_endpoint', value: 'list_by_endpoint' }
    ]}
>
<TabItem value="get">

Gets an existing custom domain within an endpoint.

```sql
SELECT
id,
name,
customHttpsParameters,
customHttpsProvisioningState,
customHttpsProvisioningSubstate,
hostName,
provisioningState,
resourceState,
systemData,
type,
validationData
FROM azure.cdn.custom_domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
AND custom_domain_name = '{{ custom_domain_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_endpoint">

Lists all of the existing custom domains within an endpoint.

```sql
SELECT
id,
name,
customHttpsParameters,
customHttpsProvisioningState,
customHttpsProvisioningSubstate,
hostName,
provisioningState,
resourceState,
systemData,
type,
validationData
FROM azure.cdn.custom_domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND profile_name = '{{ profile_name }}' -- required
AND endpoint_name = '{{ endpoint_name }}' -- required
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

Creates a new custom domain within an endpoint.

```sql
INSERT INTO azure.cdn.custom_domains (
properties,
resource_group_name,
profile_name,
endpoint_name,
custom_domain_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ profile_name }}',
'{{ endpoint_name }}',
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
- name: custom_domains
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the custom_domains resource.
    - name: profile_name
      value: "{{ profile_name }}"
      description: Required parameter for the custom_domains resource.
    - name: endpoint_name
      value: "{{ endpoint_name }}"
      description: Required parameter for the custom_domains resource.
    - name: custom_domain_name
      value: "{{ custom_domain_name }}"
      description: Required parameter for the custom_domains resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the custom_domains resource.
    - name: properties
      description: |
        The JSON object that contains the properties of the custom domain to create.
      value:
        hostName: "{{ hostName }}"
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

Deletes an existing custom domain within an endpoint.

```sql
DELETE FROM azure.cdn.custom_domains
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND profile_name = '{{ profile_name }}' --required
AND endpoint_name = '{{ endpoint_name }}' --required
AND custom_domain_name = '{{ custom_domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="disable_custom_https"
    values={[
        { label: 'disable_custom_https', value: 'disable_custom_https' },
        { label: 'enable_custom_https', value: 'enable_custom_https' }
    ]}
>
<TabItem value="disable_custom_https">

Disable https delivery of the custom domain.

```sql
EXEC azure.cdn.custom_domains.disable_custom_https 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@custom_domain_name='{{ custom_domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="enable_custom_https">

Enable https delivery of the custom domain.

```sql
EXEC azure.cdn.custom_domains.enable_custom_https 
@resource_group_name='{{ resource_group_name }}' --required, 
@profile_name='{{ profile_name }}' --required, 
@endpoint_name='{{ endpoint_name }}' --required, 
@custom_domain_name='{{ custom_domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"certificateSource": "{{ certificateSource }}", 
"protocolType": "{{ protocolType }}", 
"minimumTlsVersion": "{{ minimumTlsVersion }}"
}'
;
```
</TabItem>
</Tabs>
