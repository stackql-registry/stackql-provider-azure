--- 
title: frontend_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - frontend_endpoints
  - frontdoor
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

Creates, updates, deletes, gets or lists a <code>frontend_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="frontend_endpoints" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.frontdoor.frontend_endpoints" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_front_door', value: 'list_by_front_door' }
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration specifying how to enable HTTPS.</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsProvisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of Custom Https of the frontendEndpoint. Known values are: "Enabling", "Enabled", "Disabling", "Disabled", and "Failed". (Enabling, Enabled, Disabling, Disabled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsProvisioningSubstate" /></td>
    <td><code>string</code></td>
    <td>Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. Known values are: "SubmittingDomainControlValidationRequest", "PendingDomainControlValidationREquestApproval", "DomainControlValidationRequestApproved", "DomainControlValidationRequestRejected", "DomainControlValidationRequestTimedOut", "IssuingCertificate", "DeployingCertificate", "CertificateDeployed", "DeletingCertificate", and "CertificateDeleted". (SubmittingDomainControlValidationRequest, PendingDomainControlValidationREquestApproval, DomainControlValidationRequestApproved, DomainControlValidationRequestRejected, DomainControlValidationRequestTimedOut, IssuingCertificate, DeployingCertificate, CertificateDeployed, DeletingCertificate, CertificateDeleted)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the frontendEndpoint. Must be a domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the Front Door or Front Door SubResource. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", "Deleting", "Migrating", and "Migrated". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting, Migrating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="sessionAffinityEnabledState" /></td>
    <td><code>string</code></td>
    <td>Whether to allow session affinity on this host. Valid options are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="sessionAffinityTtlSeconds" /></td>
    <td><code>integer</code></td>
    <td>UNUSED. This field will be ignored. The TTL to use in seconds for session affinity, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallPolicyLink" /></td>
    <td><code>object</code></td>
    <td>Defines the Web Application Firewall policy for each host (if applicable).</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_front_door">

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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsConfiguration" /></td>
    <td><code>object</code></td>
    <td>The configuration specifying how to enable HTTPS.</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsProvisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning status of Custom Https of the frontendEndpoint. Known values are: "Enabling", "Enabled", "Disabling", "Disabled", and "Failed". (Enabling, Enabled, Disabling, Disabled, Failed)</td>
</tr>
<tr>
    <td><CopyableCode code="customHttpsProvisioningSubstate" /></td>
    <td><code>string</code></td>
    <td>Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. Known values are: "SubmittingDomainControlValidationRequest", "PendingDomainControlValidationREquestApproval", "DomainControlValidationRequestApproved", "DomainControlValidationRequestRejected", "DomainControlValidationRequestTimedOut", "IssuingCertificate", "DeployingCertificate", "CertificateDeployed", "DeletingCertificate", and "CertificateDeleted". (SubmittingDomainControlValidationRequest, PendingDomainControlValidationREquestApproval, DomainControlValidationRequestApproved, DomainControlValidationRequestRejected, DomainControlValidationRequestTimedOut, IssuingCertificate, DeployingCertificate, CertificateDeployed, DeletingCertificate, CertificateDeleted)</td>
</tr>
<tr>
    <td><CopyableCode code="hostName" /></td>
    <td><code>string</code></td>
    <td>The host name of the frontendEndpoint. Must be a domain name.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceState" /></td>
    <td><code>string</code></td>
    <td>Resource status of the Front Door or Front Door SubResource. Known values are: "Creating", "Enabling", "Enabled", "Disabling", "Disabled", "Deleting", "Migrating", and "Migrated". (Creating, Enabling, Enabled, Disabling, Disabled, Deleting, Migrating, Migrated)</td>
</tr>
<tr>
    <td><CopyableCode code="sessionAffinityEnabledState" /></td>
    <td><code>string</code></td>
    <td>Whether to allow session affinity on this host. Valid options are 'Enabled' or 'Disabled'. Known values are: "Enabled" and "Disabled". (Enabled, Disabled)</td>
</tr>
<tr>
    <td><CopyableCode code="sessionAffinityTtlSeconds" /></td>
    <td><code>integer</code></td>
    <td>UNUSED. This field will be ignored. The TTL to use in seconds for session affinity, if applicable.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="webApplicationFirewallPolicyLink" /></td>
    <td><code>object</code></td>
    <td>Defines the Web Application Firewall policy for each host (if applicable).</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-frontend_endpoint_name"><code>frontend_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a Frontend endpoint with the specified name within the specified Front Door.</td>
</tr>
<tr>
    <td><a href="#list_by_front_door"><CopyableCode code="list_by_front_door" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists all of the frontend endpoints within a Front Door.</td>
</tr>
<tr>
    <td><a href="#enable_https"><CopyableCode code="enable_https" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-frontend_endpoint_name"><code>frontend_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-certificateSource"><code>certificateSource</code></a>, <a href="#parameter-protocolType"><code>protocolType</code></a>, <a href="#parameter-minimumTlsVersion"><code>minimumTlsVersion</code></a></td>
    <td></td>
    <td>Enables a frontendEndpoint for HTTPS traffic.</td>
</tr>
<tr>
    <td><a href="#disable_https"><CopyableCode code="disable_https" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-front_door_name"><code>front_door_name</code></a>, <a href="#parameter-frontend_endpoint_name"><code>frontend_endpoint_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Disables a frontendEndpoint for HTTPS traffic.</td>
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
<tr id="parameter-front_door_name">
    <td><CopyableCode code="front_door_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Front Door which is globally unique. Required.</td>
</tr>
<tr id="parameter-frontend_endpoint_name">
    <td><CopyableCode code="frontend_endpoint_name" /></td>
    <td><code>string</code></td>
    <td>Name of the Frontend endpoint which is unique within the Front Door. Required.</td>
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
        { label: 'list_by_front_door', value: 'list_by_front_door' }
    ]}
>
<TabItem value="get">

Gets a Frontend endpoint with the specified name within the specified Front Door.

```sql
SELECT
id,
name,
customHttpsConfiguration,
customHttpsProvisioningState,
customHttpsProvisioningSubstate,
hostName,
resourceState,
sessionAffinityEnabledState,
sessionAffinityTtlSeconds,
type,
webApplicationFirewallPolicyLink
FROM azure.frontdoor.frontend_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND front_door_name = '{{ front_door_name }}' -- required
AND frontend_endpoint_name = '{{ frontend_endpoint_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_front_door">

Lists all of the frontend endpoints within a Front Door.

```sql
SELECT
id,
name,
customHttpsConfiguration,
customHttpsProvisioningState,
customHttpsProvisioningSubstate,
hostName,
resourceState,
sessionAffinityEnabledState,
sessionAffinityTtlSeconds,
type,
webApplicationFirewallPolicyLink
FROM azure.frontdoor.frontend_endpoints
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND front_door_name = '{{ front_door_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="enable_https"
    values={[
        { label: 'enable_https', value: 'enable_https' },
        { label: 'disable_https', value: 'disable_https' }
    ]}
>
<TabItem value="enable_https">

Enables a frontendEndpoint for HTTPS traffic.

```sql
EXEC azure.frontdoor.frontend_endpoints.enable_https 
@resource_group_name='{{ resource_group_name }}' --required, 
@front_door_name='{{ front_door_name }}' --required, 
@frontend_endpoint_name='{{ frontend_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"certificateSource": "{{ certificateSource }}", 
"protocolType": "{{ protocolType }}", 
"minimumTlsVersion": "{{ minimumTlsVersion }}", 
"keyVaultCertificateSourceParameters": "{{ keyVaultCertificateSourceParameters }}", 
"frontDoorCertificateSourceParameters": "{{ frontDoorCertificateSourceParameters }}"
}'
;
```
</TabItem>
<TabItem value="disable_https">

Disables a frontendEndpoint for HTTPS traffic.

```sql
EXEC azure.frontdoor.frontend_endpoints.disable_https 
@resource_group_name='{{ resource_group_name }}' --required, 
@front_door_name='{{ front_door_name }}' --required, 
@frontend_endpoint_name='{{ frontend_endpoint_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
