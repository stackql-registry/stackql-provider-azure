--- 
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - domainregistration
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

Creates, updates, deletes, gets or lists a <code>domains</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="domains" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.domainregistration.domains" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_ownership_identifier"
    values={[
        { label: 'get_ownership_identifier', value: 'get_ownership_identifier' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_ownership_identifier">

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
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ownershipId" /></td>
    <td><code>string</code></td>
    <td>Ownership Id.</td>
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
    <td><CopyableCode code="authCode" /></td>
    <td><code>string</code></td>
    <td>Authorization code for the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>true if the domain should be automatically renewed; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="consent" /></td>
    <td><code>object</code></td>
    <td>Legal agreement consent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactAdmin" /></td>
    <td><code>object</code></td>
    <td>Administrative contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactBilling" /></td>
    <td><code>object</code></td>
    <td>Billing contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactRegistrant" /></td>
    <td><code>object</code></td>
    <td>Registrant contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactTech" /></td>
    <td><code>object</code></td>
    <td>Technical contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Domain creation timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsType" /></td>
    <td><code>string</code></td>
    <td>Current DNS type. Known values are: "AzureDns" and "DefaultDomainRegistrarDns". (AzureDns, DefaultDomainRegistrarDns)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZoneId" /></td>
    <td><code>string</code></td>
    <td>Azure DNS Zone to use.</td>
</tr>
<tr>
    <td><CopyableCode code="domainNotRenewableReasons" /></td>
    <td><code>array</code></td>
    <td>Reasons why domain is not renewable.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Domain expiration timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRenewedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the domain was renewed last time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedHostNames" /></td>
    <td><code>array</code></td>
    <td>All hostnames derived from the domain and assigned to Azure resources.</td>
</tr>
<tr>
    <td><CopyableCode code="nameServers" /></td>
    <td><code>array</code></td>
    <td>Name servers.</td>
</tr>
<tr>
    <td><CopyableCode code="privacy" /></td>
    <td><code>boolean</code></td>
    <td>true if domain privacy is enabled for this domain; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Domain provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="readyForDnsRecordManagement" /></td>
    <td><code>boolean</code></td>
    <td>true if Azure can assign this domain to App Service apps; otherwise, false. This value will be true if domain registration status is active and \n it is hosted on name servers Azure has programmatic access to.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>Domain registration status. Known values are: "Active", "Awaiting", "Cancelled", "Confiscated", "Disabled", "Excluded", "Expired", "Failed", "Held", "Locked", "Parked", "Pending", "Reserved", "Reverted", "Suspended", "Transferred", "Unknown", "Unlocked", "Unparked", "Updated", and "JsonConverterFailed". (Active, Awaiting, Cancelled, Confiscated, Disabled, Excluded, Expired, Failed, Held, Locked, Parked, Pending, Reserved, Reverted, Suspended, Transferred, Unknown, Unlocked, Unparked, Updated, JsonConverterFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDnsType" /></td>
    <td><code>string</code></td>
    <td>Target DNS type (would be used for migration). Known values are: "AzureDns" and "DefaultDomainRegistrarDns". (AzureDns, DefaultDomainRegistrarDns)</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="authCode" /></td>
    <td><code>string</code></td>
    <td>Authorization code for the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>true if the domain should be automatically renewed; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="consent" /></td>
    <td><code>object</code></td>
    <td>Legal agreement consent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactAdmin" /></td>
    <td><code>object</code></td>
    <td>Administrative contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactBilling" /></td>
    <td><code>object</code></td>
    <td>Billing contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactRegistrant" /></td>
    <td><code>object</code></td>
    <td>Registrant contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactTech" /></td>
    <td><code>object</code></td>
    <td>Technical contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Domain creation timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsType" /></td>
    <td><code>string</code></td>
    <td>Current DNS type. Known values are: "AzureDns" and "DefaultDomainRegistrarDns". (AzureDns, DefaultDomainRegistrarDns)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZoneId" /></td>
    <td><code>string</code></td>
    <td>Azure DNS Zone to use.</td>
</tr>
<tr>
    <td><CopyableCode code="domainNotRenewableReasons" /></td>
    <td><code>array</code></td>
    <td>Reasons why domain is not renewable.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Domain expiration timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRenewedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the domain was renewed last time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedHostNames" /></td>
    <td><code>array</code></td>
    <td>All hostnames derived from the domain and assigned to Azure resources.</td>
</tr>
<tr>
    <td><CopyableCode code="nameServers" /></td>
    <td><code>array</code></td>
    <td>Name servers.</td>
</tr>
<tr>
    <td><CopyableCode code="privacy" /></td>
    <td><code>boolean</code></td>
    <td>true if domain privacy is enabled for this domain; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Domain provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="readyForDnsRecordManagement" /></td>
    <td><code>boolean</code></td>
    <td>true if Azure can assign this domain to App Service apps; otherwise, false. This value will be true if domain registration status is active and \n it is hosted on name servers Azure has programmatic access to.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>Domain registration status. Known values are: "Active", "Awaiting", "Cancelled", "Confiscated", "Disabled", "Excluded", "Expired", "Failed", "Held", "Locked", "Parked", "Pending", "Reserved", "Reverted", "Suspended", "Transferred", "Unknown", "Unlocked", "Unparked", "Updated", and "JsonConverterFailed". (Active, Awaiting, Cancelled, Confiscated, Disabled, Excluded, Expired, Failed, Held, Locked, Parked, Pending, Reserved, Reverted, Suspended, Transferred, Unknown, Unlocked, Unparked, Updated, JsonConverterFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDnsType" /></td>
    <td><code>string</code></td>
    <td>Target DNS type (would be used for migration). Known values are: "AzureDns" and "DefaultDomainRegistrarDns". (AzureDns, DefaultDomainRegistrarDns)</td>
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
    <td><CopyableCode code="authCode" /></td>
    <td><code>string</code></td>
    <td>Authorization code for the domain.</td>
</tr>
<tr>
    <td><CopyableCode code="autoRenew" /></td>
    <td><code>boolean</code></td>
    <td>true if the domain should be automatically renewed; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="consent" /></td>
    <td><code>object</code></td>
    <td>Legal agreement consent. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactAdmin" /></td>
    <td><code>object</code></td>
    <td>Administrative contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactBilling" /></td>
    <td><code>object</code></td>
    <td>Billing contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactRegistrant" /></td>
    <td><code>object</code></td>
    <td>Registrant contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="contactTech" /></td>
    <td><code>object</code></td>
    <td>Technical contact. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="createdTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Domain creation timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="dnsType" /></td>
    <td><code>string</code></td>
    <td>Current DNS type. Known values are: "AzureDns" and "DefaultDomainRegistrarDns". (AzureDns, DefaultDomainRegistrarDns)</td>
</tr>
<tr>
    <td><CopyableCode code="dnsZoneId" /></td>
    <td><code>string</code></td>
    <td>Azure DNS Zone to use.</td>
</tr>
<tr>
    <td><CopyableCode code="domainNotRenewableReasons" /></td>
    <td><code>array</code></td>
    <td>Reasons why domain is not renewable.</td>
</tr>
<tr>
    <td><CopyableCode code="expirationTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Domain expiration timestamp.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="lastRenewedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Timestamp when the domain was renewed last time.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="managedHostNames" /></td>
    <td><code>array</code></td>
    <td>All hostnames derived from the domain and assigned to Azure resources.</td>
</tr>
<tr>
    <td><CopyableCode code="nameServers" /></td>
    <td><code>array</code></td>
    <td>Name servers.</td>
</tr>
<tr>
    <td><CopyableCode code="privacy" /></td>
    <td><code>boolean</code></td>
    <td>true if domain privacy is enabled for this domain; otherwise, false.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Domain provisioning state. Known values are: "Succeeded", "Failed", "Canceled", "InProgress", and "Deleting". (Succeeded, Failed, Canceled, InProgress, Deleting)</td>
</tr>
<tr>
    <td><CopyableCode code="readyForDnsRecordManagement" /></td>
    <td><code>boolean</code></td>
    <td>true if Azure can assign this domain to App Service apps; otherwise, false. This value will be true if domain registration status is active and \n it is hosted on name servers Azure has programmatic access to.</td>
</tr>
<tr>
    <td><CopyableCode code="registrationStatus" /></td>
    <td><code>string</code></td>
    <td>Domain registration status. Known values are: "Active", "Awaiting", "Cancelled", "Confiscated", "Disabled", "Excluded", "Expired", "Failed", "Held", "Locked", "Parked", "Pending", "Reserved", "Reverted", "Suspended", "Transferred", "Unknown", "Unlocked", "Unparked", "Updated", and "JsonConverterFailed". (Active, Awaiting, Cancelled, Confiscated, Disabled, Excluded, Expired, Failed, Held, Locked, Parked, Pending, Reserved, Reverted, Suspended, Transferred, Unknown, Unlocked, Unparked, Updated, JsonConverterFailed)</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="targetDnsType" /></td>
    <td><code>string</code></td>
    <td>Target DNS type (would be used for migration). Known values are: "AzureDns" and "DefaultDomainRegistrarDns". (AzureDns, DefaultDomainRegistrarDns)</td>
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
    <td><a href="#get_ownership_identifier"><CopyableCode code="get_ownership_identifier" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get ownership identifier for domain. Description for Get ownership identifier for domain.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a domain. Description for Get a domain.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all domains in a resource group. Description for Get all domains in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all domains in a subscription. Description for Get all domains in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a domain. Description for Creates or updates a domain.</td>
</tr>
<tr>
    <td><a href="#create_or_update_ownership_identifier"><CopyableCode code="create_or_update_ownership_identifier" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an ownership identifier for a domain or updates identifier details for an existing identifier. Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier.</td>
</tr>
<tr>
    <td><a href="#update_ownership_identifier"><CopyableCode code="update_ownership_identifier" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an ownership identifier for a domain or updates identifier details for an existing identifier. Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates or updates a domain. Description for Creates or updates a domain.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a domain. Description for Creates or updates a domain.</td>
</tr>
<tr>
    <td><a href="#create_or_update_ownership_identifier"><CopyableCode code="create_or_update_ownership_identifier" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Creates an ownership identifier for a domain or updates identifier details for an existing identifier. Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier.</td>
</tr>
<tr>
    <td><a href="#delete_ownership_identifier"><CopyableCode code="delete_ownership_identifier" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete ownership identifier for domain. Description for Delete ownership identifier for domain.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-forceHardDeleteDomain"><code>forceHardDeleteDomain</code></a></td>
    <td>Delete a domain. Description for Delete a domain.</td>
</tr>
<tr>
    <td><a href="#list_ownership_identifiers"><CopyableCode code="list_ownership_identifiers" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Lists domain ownership identifiers. Description for Lists domain ownership identifiers.</td>
</tr>
<tr>
    <td><a href="#list_recommendations"><CopyableCode code="list_recommendations" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get domain name recommendations based on keywords. Description for Get domain name recommendations based on keywords.</td>
</tr>
<tr>
    <td><a href="#get_control_center_sso_request"><CopyableCode code="get_control_center_sso_request" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Generate a single sign-on request for the domain management portal. Description for Generate a single sign-on request for the domain management portal.</td>
</tr>
<tr>
    <td><a href="#renew"><CopyableCode code="renew" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Renew a domain. Description for Renew a domain.</td>
</tr>
<tr>
    <td><a href="#transfer_out"><CopyableCode code="transfer_out" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-domain_name"><code>domain_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Transfer out domain to another registrar. Transfer out domain to another registrar.</td>
</tr>
<tr>
    <td><a href="#check_availability"><CopyableCode code="check_availability" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Check if a domain is available for registration. Description for Check if a domain is available for registration.</td>
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
<tr id="parameter-domain_name">
    <td><CopyableCode code="domain_name" /></td>
    <td><code>string</code></td>
    <td>Name of the domain. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Name of identifier. Required.</td>
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
<tr id="parameter-forceHardDeleteDomain">
    <td><CopyableCode code="forceHardDeleteDomain" /></td>
    <td><code>boolean</code></td>
    <td>Specify true to delete the domain immediately. The default is false which deletes the domain after 24 hours. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_ownership_identifier"
    values={[
        { label: 'get_ownership_identifier', value: 'get_ownership_identifier' },
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_ownership_identifier">

Get ownership identifier for domain. Description for Get ownership identifier for domain.

```sql
SELECT
id,
name,
kind,
ownershipId,
systemData,
type
FROM azure.domainregistration.domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND domain_name = '{{ domain_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Get a domain. Description for Get a domain.

```sql
SELECT
id,
name,
authCode,
autoRenew,
consent,
contactAdmin,
contactBilling,
contactRegistrant,
contactTech,
createdTime,
dnsType,
dnsZoneId,
domainNotRenewableReasons,
expirationTime,
kind,
lastRenewedTime,
location,
managedHostNames,
nameServers,
privacy,
provisioningState,
readyForDnsRecordManagement,
registrationStatus,
systemData,
tags,
targetDnsType,
type
FROM azure.domainregistration.domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND domain_name = '{{ domain_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Get all domains in a resource group. Description for Get all domains in a resource group.

```sql
SELECT
id,
name,
authCode,
autoRenew,
consent,
contactAdmin,
contactBilling,
contactRegistrant,
contactTech,
createdTime,
dnsType,
dnsZoneId,
domainNotRenewableReasons,
expirationTime,
kind,
lastRenewedTime,
location,
managedHostNames,
nameServers,
privacy,
provisioningState,
readyForDnsRecordManagement,
registrationStatus,
systemData,
tags,
targetDnsType,
type
FROM azure.domainregistration.domains
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get all domains in a subscription. Description for Get all domains in a subscription.

```sql
SELECT
id,
name,
authCode,
autoRenew,
consent,
contactAdmin,
contactBilling,
contactRegistrant,
contactTech,
createdTime,
dnsType,
dnsZoneId,
domainNotRenewableReasons,
expirationTime,
kind,
lastRenewedTime,
location,
managedHostNames,
nameServers,
privacy,
provisioningState,
readyForDnsRecordManagement,
registrationStatus,
systemData,
tags,
targetDnsType,
type
FROM azure.domainregistration.domains
WHERE subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_ownership_identifier', value: 'create_or_update_ownership_identifier' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a domain. Description for Creates or updates a domain.

```sql
INSERT INTO azure.domainregistration.domains (
tags,
location,
properties,
kind,
resource_group_name,
domain_name,
subscription_id
)
SELECT 
'{{ tags }}',
'{{ location }}' /* required */,
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ domain_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
location,
properties,
systemData,
tags,
type
;
```
</TabItem>
<TabItem value="create_or_update_ownership_identifier">

Creates an ownership identifier for a domain or updates identifier details for an existing identifier. Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier.

```sql
INSERT INTO azure.domainregistration.domains (
properties,
kind,
resource_group_name,
domain_name,
name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ kind }}',
'{{ resource_group_name }}',
'{{ domain_name }}',
'{{ name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
kind,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: domains
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the domains resource.
    - name: domain_name
      value: "{{ domain_name }}"
      description: Required parameter for the domains resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the domains resource.
    - name: name
      value: "{{ name }}"
      description: Required parameter for the domains resource.
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
        DomainOwnershipIdentifier resource specific properties.
      value:
        ownershipId: "{{ ownershipId }}"
    - name: kind
      value: "{{ kind }}"
      description: |
        Kind of resource.
`}</CodeBlock>

</TabItem>
</Tabs>


## `UPDATE` examples

<Tabs
    defaultValue="update_ownership_identifier"
    values={[
        { label: 'update_ownership_identifier', value: 'update_ownership_identifier' },
        { label: 'update', value: 'update' }
    ]}
>
<TabItem value="update_ownership_identifier">

Creates an ownership identifier for a domain or updates identifier details for an existing identifier. Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier.

```sql
UPDATE azure.domainregistration.domains
SET 
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="update">

Creates or updates a domain. Description for Creates or updates a domain.

```sql
UPDATE azure.domainregistration.domains
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update"
    values={[
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'create_or_update_ownership_identifier', value: 'create_or_update_ownership_identifier' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a domain. Description for Creates or updates a domain.

```sql
REPLACE azure.domainregistration.domains
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
kind,
location,
properties,
systemData,
tags,
type;
```
</TabItem>
<TabItem value="create_or_update_ownership_identifier">

Creates an ownership identifier for a domain or updates identifier details for an existing identifier. Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier.

```sql
REPLACE azure.domainregistration.domains
SET 
properties = '{{ properties }}',
kind = '{{ kind }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
kind,
properties,
systemData,
type;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_ownership_identifier"
    values={[
        { label: 'delete_ownership_identifier', value: 'delete_ownership_identifier' },
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete_ownership_identifier">

Delete ownership identifier for domain. Description for Delete ownership identifier for domain.

```sql
DELETE FROM azure.domainregistration.domains
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND name = '{{ name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="delete">

Delete a domain. Description for Delete a domain.

```sql
DELETE FROM azure.domainregistration.domains
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND domain_name = '{{ domain_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND forceHardDeleteDomain = '{{ forceHardDeleteDomain }}'
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_ownership_identifiers"
    values={[
        { label: 'list_ownership_identifiers', value: 'list_ownership_identifiers' },
        { label: 'list_recommendations', value: 'list_recommendations' },
        { label: 'get_control_center_sso_request', value: 'get_control_center_sso_request' },
        { label: 'renew', value: 'renew' },
        { label: 'transfer_out', value: 'transfer_out' },
        { label: 'check_availability', value: 'check_availability' }
    ]}
>
<TabItem value="list_ownership_identifiers">

Lists domain ownership identifiers. Description for Lists domain ownership identifiers.

```sql
EXEC azure.domainregistration.domains.list_ownership_identifiers 
@resource_group_name='{{ resource_group_name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_recommendations">

Get domain name recommendations based on keywords. Description for Get domain name recommendations based on keywords.

```sql
EXEC azure.domainregistration.domains.list_recommendations 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"keywords": "{{ keywords }}", 
"maxDomainRecommendations": {{ maxDomainRecommendations }}
}'
;
```
</TabItem>
<TabItem value="get_control_center_sso_request">

Generate a single sign-on request for the domain management portal. Description for Generate a single sign-on request for the domain management portal.

```sql
EXEC azure.domainregistration.domains.get_control_center_sso_request 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="renew">

Renew a domain. Description for Renew a domain.

```sql
EXEC azure.domainregistration.domains.renew 
@resource_group_name='{{ resource_group_name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="transfer_out">

Transfer out domain to another registrar. Transfer out domain to another registrar.

```sql
EXEC azure.domainregistration.domains.transfer_out 
@resource_group_name='{{ resource_group_name }}' --required, 
@domain_name='{{ domain_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="check_availability">

Check if a domain is available for registration. Description for Check if a domain is available for registration.

```sql
EXEC azure.domainregistration.domains.check_availability 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}"
}'
;
```
</TabItem>
</Tabs>
