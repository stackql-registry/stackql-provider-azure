--- 
title: sql_virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machines
  - sqlvirtualmachine
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

Creates, updates, deletes, gets or lists a <code>sql_virtual_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="sql_virtual_machines" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sqlvirtualmachine.sql_virtual_machines" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sql_vm_group', value: 'list_by_sql_vm_group' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentSettings" /></td>
    <td><code>object</code></td>
    <td>SQL best practices Assessment Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="autoBackupSettings" /></td>
    <td><code>object</code></td>
    <td>Auto backup settings for SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="autoPatchingSettings" /></td>
    <td><code>object</code></td>
    <td>Auto patching settings for applying critical security updates to SQL virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticUpgrade" /></td>
    <td><code>boolean</code></td>
    <td>Enable automatic upgrade of Sql IaaS extension Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultCredentialSettings" /></td>
    <td><code>object</code></td>
    <td>Key vault credential settings.</td>
</tr>
<tr>
    <td><CopyableCode code="leastPrivilegeMode" /></td>
    <td><code>string</code></td>
    <td>SQL IaaS Agent least privilege mode. Known values are: "Enabled" and "NotSet".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="serverConfigurationsManagementSettings" /></td>
    <td><code>object</code></td>
    <td>SQL Server configuration management settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageOffer" /></td>
    <td><code>string</code></td>
    <td>SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageSku" /></td>
    <td><code>string</code></td>
    <td>SQL Server edition type. Known values are: "Developer", "Express", "Standard", "Enterprise", and "Web".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlManagement" /></td>
    <td><code>string</code></td>
    <td>SQL Server Management type. Known values are: "Full", "LightWeight", and "NoAgent".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlServerLicenseType" /></td>
    <td><code>string</code></td>
    <td>SQL Server license type. Known values are: "PAYG", "AHUB", and "DR".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlVirtualMachineGroupResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of.</td>
</tr>
<tr>
    <td><CopyableCode code="storageConfigurationSettings" /></td>
    <td><code>object</code></td>
    <td>Storage Configuration Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="troubleshootingStatus" /></td>
    <td><code>object</code></td>
    <td>Troubleshooting status.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource id of underlying virtual machine created from SQL marketplace image.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcDomainCredentials" /></td>
    <td><code>object</code></td>
    <td>Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcStaticIp" /></td>
    <td><code>string</code></td>
    <td>Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_by_sql_vm_group">

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
    <td><CopyableCode code="assessmentSettings" /></td>
    <td><code>object</code></td>
    <td>SQL best practices Assessment Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="autoBackupSettings" /></td>
    <td><code>object</code></td>
    <td>Auto backup settings for SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="autoPatchingSettings" /></td>
    <td><code>object</code></td>
    <td>Auto patching settings for applying critical security updates to SQL virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticUpgrade" /></td>
    <td><code>boolean</code></td>
    <td>Enable automatic upgrade of Sql IaaS extension Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultCredentialSettings" /></td>
    <td><code>object</code></td>
    <td>Key vault credential settings.</td>
</tr>
<tr>
    <td><CopyableCode code="leastPrivilegeMode" /></td>
    <td><code>string</code></td>
    <td>SQL IaaS Agent least privilege mode. Known values are: "Enabled" and "NotSet".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="serverConfigurationsManagementSettings" /></td>
    <td><code>object</code></td>
    <td>SQL Server configuration management settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageOffer" /></td>
    <td><code>string</code></td>
    <td>SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageSku" /></td>
    <td><code>string</code></td>
    <td>SQL Server edition type. Known values are: "Developer", "Express", "Standard", "Enterprise", and "Web".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlManagement" /></td>
    <td><code>string</code></td>
    <td>SQL Server Management type. Known values are: "Full", "LightWeight", and "NoAgent".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlServerLicenseType" /></td>
    <td><code>string</code></td>
    <td>SQL Server license type. Known values are: "PAYG", "AHUB", and "DR".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlVirtualMachineGroupResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of.</td>
</tr>
<tr>
    <td><CopyableCode code="storageConfigurationSettings" /></td>
    <td><code>object</code></td>
    <td>Storage Configuration Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="troubleshootingStatus" /></td>
    <td><code>object</code></td>
    <td>Troubleshooting status.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource id of underlying virtual machine created from SQL marketplace image.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcDomainCredentials" /></td>
    <td><code>object</code></td>
    <td>Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcStaticIp" /></td>
    <td><code>string</code></td>
    <td>Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentSettings" /></td>
    <td><code>object</code></td>
    <td>SQL best practices Assessment Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="autoBackupSettings" /></td>
    <td><code>object</code></td>
    <td>Auto backup settings for SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="autoPatchingSettings" /></td>
    <td><code>object</code></td>
    <td>Auto patching settings for applying critical security updates to SQL virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticUpgrade" /></td>
    <td><code>boolean</code></td>
    <td>Enable automatic upgrade of Sql IaaS extension Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultCredentialSettings" /></td>
    <td><code>object</code></td>
    <td>Key vault credential settings.</td>
</tr>
<tr>
    <td><CopyableCode code="leastPrivilegeMode" /></td>
    <td><code>string</code></td>
    <td>SQL IaaS Agent least privilege mode. Known values are: "Enabled" and "NotSet".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="serverConfigurationsManagementSettings" /></td>
    <td><code>object</code></td>
    <td>SQL Server configuration management settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageOffer" /></td>
    <td><code>string</code></td>
    <td>SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageSku" /></td>
    <td><code>string</code></td>
    <td>SQL Server edition type. Known values are: "Developer", "Express", "Standard", "Enterprise", and "Web".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlManagement" /></td>
    <td><code>string</code></td>
    <td>SQL Server Management type. Known values are: "Full", "LightWeight", and "NoAgent".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlServerLicenseType" /></td>
    <td><code>string</code></td>
    <td>SQL Server license type. Known values are: "PAYG", "AHUB", and "DR".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlVirtualMachineGroupResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of.</td>
</tr>
<tr>
    <td><CopyableCode code="storageConfigurationSettings" /></td>
    <td><code>object</code></td>
    <td>Storage Configuration Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="troubleshootingStatus" /></td>
    <td><code>object</code></td>
    <td>Troubleshooting status.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource id of underlying virtual machine created from SQL marketplace image.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcDomainCredentials" /></td>
    <td><code>object</code></td>
    <td>Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcStaticIp" /></td>
    <td><code>string</code></td>
    <td>Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.</td>
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
    <td>Resource ID.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Resource name.</td>
</tr>
<tr>
    <td><CopyableCode code="assessmentSettings" /></td>
    <td><code>object</code></td>
    <td>SQL best practices Assessment Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="autoBackupSettings" /></td>
    <td><code>object</code></td>
    <td>Auto backup settings for SQL Server.</td>
</tr>
<tr>
    <td><CopyableCode code="autoPatchingSettings" /></td>
    <td><code>object</code></td>
    <td>Auto patching settings for applying critical security updates to SQL virtual machine.</td>
</tr>
<tr>
    <td><CopyableCode code="enableAutomaticUpgrade" /></td>
    <td><code>boolean</code></td>
    <td>Enable automatic upgrade of Sql IaaS extension Agent.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>Azure Active Directory identity of the server.</td>
</tr>
<tr>
    <td><CopyableCode code="keyVaultCredentialSettings" /></td>
    <td><code>object</code></td>
    <td>Key vault credential settings.</td>
</tr>
<tr>
    <td><CopyableCode code="leastPrivilegeMode" /></td>
    <td><code>string</code></td>
    <td>SQL IaaS Agent least privilege mode. Known values are: "Enabled" and "NotSet".</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>Resource location. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state to track the async operation status.</td>
</tr>
<tr>
    <td><CopyableCode code="serverConfigurationsManagementSettings" /></td>
    <td><code>object</code></td>
    <td>SQL Server configuration management settings.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageOffer" /></td>
    <td><code>string</code></td>
    <td>SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.</td>
</tr>
<tr>
    <td><CopyableCode code="sqlImageSku" /></td>
    <td><code>string</code></td>
    <td>SQL Server edition type. Known values are: "Developer", "Express", "Standard", "Enterprise", and "Web".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlManagement" /></td>
    <td><code>string</code></td>
    <td>SQL Server Management type. Known values are: "Full", "LightWeight", and "NoAgent".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlServerLicenseType" /></td>
    <td><code>string</code></td>
    <td>SQL Server license type. Known values are: "PAYG", "AHUB", and "DR".</td>
</tr>
<tr>
    <td><CopyableCode code="sqlVirtualMachineGroupResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of.</td>
</tr>
<tr>
    <td><CopyableCode code="storageConfigurationSettings" /></td>
    <td><code>object</code></td>
    <td>Storage Configuration Settings.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="tags" /></td>
    <td><code>object</code></td>
    <td>Resource tags.</td>
</tr>
<tr>
    <td><CopyableCode code="troubleshootingStatus" /></td>
    <td><code>object</code></td>
    <td>Troubleshooting status.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Resource type.</td>
</tr>
<tr>
    <td><CopyableCode code="virtualMachineResourceId" /></td>
    <td><code>string</code></td>
    <td>ARM Resource id of underlying virtual machine created from SQL marketplace image.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcDomainCredentials" /></td>
    <td><code>object</code></td>
    <td>Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.</td>
</tr>
<tr>
    <td><CopyableCode code="wsfcStaticIp" /></td>
    <td><code>string</code></td>
    <td>Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_name"><code>sql_virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$expand"><code>$expand</code></a></td>
    <td>Gets a SQL virtual machine.</td>
</tr>
<tr>
    <td><a href="#list_by_sql_vm_group"><CopyableCode code="list_by_sql_vm_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_group_name"><code>sql_virtual_machine_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets the list of sql virtual machines in a SQL virtual machine group.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all SQL virtual machines in a resource group.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets all SQL virtual machines in a subscription.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_name"><code>sql_virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a SQL virtual machine.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_name"><code>sql_virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Updates a SQL virtual machine.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_name"><code>sql_virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-location"><code>location</code></a></td>
    <td></td>
    <td>Creates or updates a SQL virtual machine.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_name"><code>sql_virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Deletes a SQL virtual machine.</td>
</tr>
<tr>
    <td><a href="#start_assessment"><CopyableCode code="start_assessment" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_name"><code>sql_virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Starts SQL best practices Assessment on SQL virtual machine.</td>
</tr>
<tr>
    <td><a href="#redeploy"><CopyableCode code="redeploy" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-sql_virtual_machine_name"><code>sql_virtual_machine_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Uninstalls and reinstalls the SQL IaaS Extension.</td>
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
    <td>Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-sql_virtual_machine_group_name">
    <td><CopyableCode code="sql_virtual_machine_group_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SQL virtual machine group. Required.</td>
</tr>
<tr id="parameter-sql_virtual_machine_name">
    <td><CopyableCode code="sql_virtual_machine_name" /></td>
    <td><code>string</code></td>
    <td>Name of the SQL virtual machine. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$expand">
    <td><CopyableCode code="$expand" /></td>
    <td><code>string</code></td>
    <td>The child resources to include in the response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_sql_vm_group', value: 'list_by_sql_vm_group' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Gets a SQL virtual machine.

```sql
SELECT
id,
name,
assessmentSettings,
autoBackupSettings,
autoPatchingSettings,
enableAutomaticUpgrade,
identity,
keyVaultCredentialSettings,
leastPrivilegeMode,
location,
provisioningState,
serverConfigurationsManagementSettings,
sqlImageOffer,
sqlImageSku,
sqlManagement,
sqlServerLicenseType,
sqlVirtualMachineGroupResourceId,
storageConfigurationSettings,
systemData,
tags,
troubleshootingStatus,
type,
virtualMachineResourceId,
wsfcDomainCredentials,
wsfcStaticIp
FROM azure.sqlvirtualmachine.sql_virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sql_virtual_machine_name = '{{ sql_virtual_machine_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $expand = '{{ $expand }}'
;
```
</TabItem>
<TabItem value="list_by_sql_vm_group">

Gets the list of sql virtual machines in a SQL virtual machine group.

```sql
SELECT
id,
name,
assessmentSettings,
autoBackupSettings,
autoPatchingSettings,
enableAutomaticUpgrade,
identity,
keyVaultCredentialSettings,
leastPrivilegeMode,
location,
provisioningState,
serverConfigurationsManagementSettings,
sqlImageOffer,
sqlImageSku,
sqlManagement,
sqlServerLicenseType,
sqlVirtualMachineGroupResourceId,
storageConfigurationSettings,
systemData,
tags,
troubleshootingStatus,
type,
virtualMachineResourceId,
wsfcDomainCredentials,
wsfcStaticIp
FROM azure.sqlvirtualmachine.sql_virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND sql_virtual_machine_group_name = '{{ sql_virtual_machine_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

Gets all SQL virtual machines in a resource group.

```sql
SELECT
id,
name,
assessmentSettings,
autoBackupSettings,
autoPatchingSettings,
enableAutomaticUpgrade,
identity,
keyVaultCredentialSettings,
leastPrivilegeMode,
location,
provisioningState,
serverConfigurationsManagementSettings,
sqlImageOffer,
sqlImageSku,
sqlManagement,
sqlServerLicenseType,
sqlVirtualMachineGroupResourceId,
storageConfigurationSettings,
systemData,
tags,
troubleshootingStatus,
type,
virtualMachineResourceId,
wsfcDomainCredentials,
wsfcStaticIp
FROM azure.sqlvirtualmachine.sql_virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all SQL virtual machines in a subscription.

```sql
SELECT
id,
name,
assessmentSettings,
autoBackupSettings,
autoPatchingSettings,
enableAutomaticUpgrade,
identity,
keyVaultCredentialSettings,
leastPrivilegeMode,
location,
provisioningState,
serverConfigurationsManagementSettings,
sqlImageOffer,
sqlImageSku,
sqlManagement,
sqlServerLicenseType,
sqlVirtualMachineGroupResourceId,
storageConfigurationSettings,
systemData,
tags,
troubleshootingStatus,
type,
virtualMachineResourceId,
wsfcDomainCredentials,
wsfcStaticIp
FROM azure.sqlvirtualmachine.sql_virtual_machines
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
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a SQL virtual machine.

```sql
INSERT INTO azure.sqlvirtualmachine.sql_virtual_machines (
location,
tags,
identity,
properties,
resource_group_name,
sql_virtual_machine_name,
subscription_id
)
SELECT 
'{{ location }}' /* required */,
'{{ tags }}',
'{{ identity }}',
'{{ properties }}',
'{{ resource_group_name }}',
'{{ sql_virtual_machine_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
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
- name: sql_virtual_machines
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the sql_virtual_machines resource.
    - name: sql_virtual_machine_name
      value: "{{ sql_virtual_machine_name }}"
      description: Required parameter for the sql_virtual_machines resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the sql_virtual_machines resource.
    - name: location
      value: "{{ location }}"
      description: |
        Resource location. Required.
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: identity
      description: |
        Azure Active Directory identity of the server.
      value:
        principalId: "{{ principalId }}"
        type: "{{ type }}"
        tenantId: "{{ tenantId }}"
    - name: properties
      value:
        virtualMachineResourceId: "{{ virtualMachineResourceId }}"
        sqlImageOffer: "{{ sqlImageOffer }}"
        sqlServerLicenseType: "{{ sqlServerLicenseType }}"
        sqlManagement: "{{ sqlManagement }}"
        leastPrivilegeMode: "{{ leastPrivilegeMode }}"
        sqlImageSku: "{{ sqlImageSku }}"
        sqlVirtualMachineGroupResourceId: "{{ sqlVirtualMachineGroupResourceId }}"
        wsfcDomainCredentials:
          clusterBootstrapAccountPassword: "{{ clusterBootstrapAccountPassword }}"
          clusterOperatorAccountPassword: "{{ clusterOperatorAccountPassword }}"
          sqlServiceAccountPassword: "{{ sqlServiceAccountPassword }}"
        wsfcStaticIp: "{{ wsfcStaticIp }}"
        autoPatchingSettings:
          enable: {{ enable }}
          dayOfWeek: "{{ dayOfWeek }}"
          maintenanceWindowStartingHour: {{ maintenanceWindowStartingHour }}
          maintenanceWindowDuration: {{ maintenanceWindowDuration }}
        autoBackupSettings:
          enable: {{ enable }}
          enableEncryption: {{ enableEncryption }}
          retentionPeriod: {{ retentionPeriod }}
          storageAccountUrl: "{{ storageAccountUrl }}"
          storageContainerName: "{{ storageContainerName }}"
          storageAccessKey: "{{ storageAccessKey }}"
          password: "{{ password }}"
          backupSystemDbs: {{ backupSystemDbs }}
          backupScheduleType: "{{ backupScheduleType }}"
          fullBackupFrequency: "{{ fullBackupFrequency }}"
          daysOfWeek:
            - "{{ daysOfWeek }}"
          fullBackupStartTime: {{ fullBackupStartTime }}
          fullBackupWindowHours: {{ fullBackupWindowHours }}
          logBackupFrequency: {{ logBackupFrequency }}
        keyVaultCredentialSettings:
          enable: {{ enable }}
          credentialName: "{{ credentialName }}"
          azureKeyVaultUrl: "{{ azureKeyVaultUrl }}"
          servicePrincipalName: "{{ servicePrincipalName }}"
          servicePrincipalSecret: "{{ servicePrincipalSecret }}"
        serverConfigurationsManagementSettings:
          sqlConnectivityUpdateSettings:
            connectivityType: "{{ connectivityType }}"
            port: {{ port }}
            sqlAuthUpdateUserName: "{{ sqlAuthUpdateUserName }}"
            sqlAuthUpdatePassword: "{{ sqlAuthUpdatePassword }}"
          sqlWorkloadTypeUpdateSettings:
            sqlWorkloadType: "{{ sqlWorkloadType }}"
          sqlStorageUpdateSettings:
            diskCount: {{ diskCount }}
            startingDeviceId: {{ startingDeviceId }}
            diskConfigurationType: "{{ diskConfigurationType }}"
          additionalFeaturesServerConfigurations:
            isRServicesEnabled: {{ isRServicesEnabled }}
          sqlInstanceSettings:
            collation: "{{ collation }}"
            maxDop: {{ maxDop }}
            isOptimizeForAdHocWorkloadsEnabled: {{ isOptimizeForAdHocWorkloadsEnabled }}
            minServerMemoryMB: {{ minServerMemoryMB }}
            maxServerMemoryMB: {{ maxServerMemoryMB }}
            isLpimEnabled: {{ isLpimEnabled }}
            isIfiEnabled: {{ isIfiEnabled }}
          azureAdAuthenticationSettings:
            clientId: "{{ clientId }}"
        storageConfigurationSettings:
          sqlDataSettings:
            luns:
              - {{ luns }}
            defaultFilePath: "{{ defaultFilePath }}"
          sqlLogSettings:
            luns:
              - {{ luns }}
            defaultFilePath: "{{ defaultFilePath }}"
          sqlTempDbSettings:
            dataFileSize: {{ dataFileSize }}
            dataGrowth: {{ dataGrowth }}
            logFileSize: {{ logFileSize }}
            logGrowth: {{ logGrowth }}
            dataFileCount: {{ dataFileCount }}
            persistFolder: {{ persistFolder }}
            persistFolderPath: "{{ persistFolderPath }}"
            luns:
              - {{ luns }}
            defaultFilePath: "{{ defaultFilePath }}"
          sqlSystemDbOnDataDisk: {{ sqlSystemDbOnDataDisk }}
          diskConfigurationType: "{{ diskConfigurationType }}"
          storageWorkloadType: "{{ storageWorkloadType }}"
        assessmentSettings:
          enable: {{ enable }}
          runImmediately: {{ runImmediately }}
          schedule:
            enable: {{ enable }}
            weeklyInterval: {{ weeklyInterval }}
            monthlyOccurrence: {{ monthlyOccurrence }}
            dayOfWeek: "{{ dayOfWeek }}"
            startTime: "{{ startTime }}"
        enableAutomaticUpgrade: {{ enableAutomaticUpgrade }}
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

Updates a SQL virtual machine.

```sql
UPDATE azure.sqlvirtualmachine.sql_virtual_machines
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_virtual_machine_name = '{{ sql_virtual_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
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
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update">

Creates or updates a SQL virtual machine.

```sql
REPLACE azure.sqlvirtualmachine.sql_virtual_machines
SET 
location = '{{ location }}',
tags = '{{ tags }}',
identity = '{{ identity }}',
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND sql_virtual_machine_name = '{{ sql_virtual_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
AND location = '{{ location }}' --required
RETURNING
id,
name,
identity,
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

Deletes a SQL virtual machine.

```sql
DELETE FROM azure.sqlvirtualmachine.sql_virtual_machines
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND sql_virtual_machine_name = '{{ sql_virtual_machine_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start_assessment"
    values={[
        { label: 'start_assessment', value: 'start_assessment' },
        { label: 'redeploy', value: 'redeploy' }
    ]}
>
<TabItem value="start_assessment">

Starts SQL best practices Assessment on SQL virtual machine.

```sql
EXEC azure.sqlvirtualmachine.sql_virtual_machines.start_assessment 
@resource_group_name='{{ resource_group_name }}' --required, 
@sql_virtual_machine_name='{{ sql_virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="redeploy">

Uninstalls and reinstalls the SQL IaaS Extension.

```sql
EXEC azure.sqlvirtualmachine.sql_virtual_machines.redeploy 
@resource_group_name='{{ resource_group_name }}' --required, 
@sql_virtual_machine_name='{{ sql_virtual_machine_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
