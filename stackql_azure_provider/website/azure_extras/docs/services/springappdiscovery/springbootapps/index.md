--- 
title: springbootapps
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootapps
  - springappdiscovery
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

Creates, updates, deletes, gets or lists a <code>springbootapps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="springbootapps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.springappdiscovery.springbootapps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list_by_resource_group', value: 'list_by_resource_group' },
        { label: 'list_by_subscription', value: 'list_by_subscription' }
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
    <td><CopyableCode code="appName" /></td>
    <td><code>string</code></td>
    <td>The name of SpringBootApp.</td>
</tr>
<tr>
    <td><CopyableCode code="appPort" /></td>
    <td><code>integer</code></td>
    <td>The application port.</td>
</tr>
<tr>
    <td><CopyableCode code="appType" /></td>
    <td><code>string</code></td>
    <td>The application type, whether it is a SpringBoot app.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationConfigurations" /></td>
    <td><code>array</code></td>
    <td>The application configuration file list.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactName" /></td>
    <td><code>string</code></td>
    <td>The artifact name of SpringBootApp.</td>
</tr>
<tr>
    <td><CopyableCode code="bindingPorts" /></td>
    <td><code>array</code></td>
    <td>The application binding port list.</td>
</tr>
<tr>
    <td><CopyableCode code="buildJdkVersion" /></td>
    <td><code>string</code></td>
    <td>The jdk version in build.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>The certificate file list.</td>
</tr>
<tr>
    <td><CopyableCode code="checksum" /></td>
    <td><code>string</code></td>
    <td>The checksum of jar file.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStrings" /></td>
    <td><code>array</code></td>
    <td>The connection string list.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The dependency list.</td>
</tr>
<tr>
    <td><CopyableCode code="environments" /></td>
    <td><code>array</code></td>
    <td>The environment variable list.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceCount" /></td>
    <td><code>integer</code></td>
    <td>The total instance count the app deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>The breakdown info for app instances on all the servers.</td>
</tr>
<tr>
    <td><CopyableCode code="jarFileLocation" /></td>
    <td><code>string</code></td>
    <td>The jar file location on the server.</td>
</tr>
<tr>
    <td><CopyableCode code="jvmMemoryInMB" /></td>
    <td><code>integer</code></td>
    <td>The jvm heap memory allocated.</td>
</tr>
<tr>
    <td><CopyableCode code="jvmOptions" /></td>
    <td><code>array</code></td>
    <td>The jvm options.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this springbootapps jar file was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this springbootapps instance was last refreshed.</td>
</tr>
<tr>
    <td><CopyableCode code="machineArmIds" /></td>
    <td><code>array</code></td>
    <td>The machine ARM id list the app belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="miscs" /></td>
    <td><code>array</code></td>
    <td>The other types of date collected.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeJdkVersion" /></td>
    <td><code>string</code></td>
    <td>The jdk version installed on server.</td>
</tr>
<tr>
    <td><CopyableCode code="servers" /></td>
    <td><code>array</code></td>
    <td>The server list the app installed.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>The site name.</td>
</tr>
<tr>
    <td><CopyableCode code="springBootVersion" /></td>
    <td><code>string</code></td>
    <td>The spring boot version.</td>
</tr>
<tr>
    <td><CopyableCode code="staticContentLocations" /></td>
    <td><code>array</code></td>
    <td>The static content location list.</td>
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
    <td><CopyableCode code="appName" /></td>
    <td><code>string</code></td>
    <td>The name of SpringBootApp.</td>
</tr>
<tr>
    <td><CopyableCode code="appPort" /></td>
    <td><code>integer</code></td>
    <td>The application port.</td>
</tr>
<tr>
    <td><CopyableCode code="appType" /></td>
    <td><code>string</code></td>
    <td>The application type, whether it is a SpringBoot app.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationConfigurations" /></td>
    <td><code>array</code></td>
    <td>The application configuration file list.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactName" /></td>
    <td><code>string</code></td>
    <td>The artifact name of SpringBootApp.</td>
</tr>
<tr>
    <td><CopyableCode code="bindingPorts" /></td>
    <td><code>array</code></td>
    <td>The application binding port list.</td>
</tr>
<tr>
    <td><CopyableCode code="buildJdkVersion" /></td>
    <td><code>string</code></td>
    <td>The jdk version in build.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>The certificate file list.</td>
</tr>
<tr>
    <td><CopyableCode code="checksum" /></td>
    <td><code>string</code></td>
    <td>The checksum of jar file.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStrings" /></td>
    <td><code>array</code></td>
    <td>The connection string list.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The dependency list.</td>
</tr>
<tr>
    <td><CopyableCode code="environments" /></td>
    <td><code>array</code></td>
    <td>The environment variable list.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceCount" /></td>
    <td><code>integer</code></td>
    <td>The total instance count the app deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>The breakdown info for app instances on all the servers.</td>
</tr>
<tr>
    <td><CopyableCode code="jarFileLocation" /></td>
    <td><code>string</code></td>
    <td>The jar file location on the server.</td>
</tr>
<tr>
    <td><CopyableCode code="jvmMemoryInMB" /></td>
    <td><code>integer</code></td>
    <td>The jvm heap memory allocated.</td>
</tr>
<tr>
    <td><CopyableCode code="jvmOptions" /></td>
    <td><code>array</code></td>
    <td>The jvm options.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this springbootapps jar file was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this springbootapps instance was last refreshed.</td>
</tr>
<tr>
    <td><CopyableCode code="machineArmIds" /></td>
    <td><code>array</code></td>
    <td>The machine ARM id list the app belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="miscs" /></td>
    <td><code>array</code></td>
    <td>The other types of date collected.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeJdkVersion" /></td>
    <td><code>string</code></td>
    <td>The jdk version installed on server.</td>
</tr>
<tr>
    <td><CopyableCode code="servers" /></td>
    <td><code>array</code></td>
    <td>The server list the app installed.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>The site name.</td>
</tr>
<tr>
    <td><CopyableCode code="springBootVersion" /></td>
    <td><code>string</code></td>
    <td>The spring boot version.</td>
</tr>
<tr>
    <td><CopyableCode code="staticContentLocations" /></td>
    <td><code>array</code></td>
    <td>The static content location list.</td>
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
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="appName" /></td>
    <td><code>string</code></td>
    <td>The name of SpringBootApp.</td>
</tr>
<tr>
    <td><CopyableCode code="appPort" /></td>
    <td><code>integer</code></td>
    <td>The application port.</td>
</tr>
<tr>
    <td><CopyableCode code="appType" /></td>
    <td><code>string</code></td>
    <td>The application type, whether it is a SpringBoot app.</td>
</tr>
<tr>
    <td><CopyableCode code="applicationConfigurations" /></td>
    <td><code>array</code></td>
    <td>The application configuration file list.</td>
</tr>
<tr>
    <td><CopyableCode code="artifactName" /></td>
    <td><code>string</code></td>
    <td>The artifact name of SpringBootApp.</td>
</tr>
<tr>
    <td><CopyableCode code="bindingPorts" /></td>
    <td><code>array</code></td>
    <td>The application binding port list.</td>
</tr>
<tr>
    <td><CopyableCode code="buildJdkVersion" /></td>
    <td><code>string</code></td>
    <td>The jdk version in build.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>The certificate file list.</td>
</tr>
<tr>
    <td><CopyableCode code="checksum" /></td>
    <td><code>string</code></td>
    <td>The checksum of jar file.</td>
</tr>
<tr>
    <td><CopyableCode code="connectionStrings" /></td>
    <td><code>array</code></td>
    <td>The connection string list.</td>
</tr>
<tr>
    <td><CopyableCode code="dependencies" /></td>
    <td><code>array</code></td>
    <td>The dependency list.</td>
</tr>
<tr>
    <td><CopyableCode code="environments" /></td>
    <td><code>array</code></td>
    <td>The environment variable list.</td>
</tr>
<tr>
    <td><CopyableCode code="errors" /></td>
    <td><code>array</code></td>
    <td>The list of errors.</td>
</tr>
<tr>
    <td><CopyableCode code="instanceCount" /></td>
    <td><code>integer</code></td>
    <td>The total instance count the app deployed.</td>
</tr>
<tr>
    <td><CopyableCode code="instances" /></td>
    <td><code>array</code></td>
    <td>The breakdown info for app instances on all the servers.</td>
</tr>
<tr>
    <td><CopyableCode code="jarFileLocation" /></td>
    <td><code>string</code></td>
    <td>The jar file location on the server.</td>
</tr>
<tr>
    <td><CopyableCode code="jvmMemoryInMB" /></td>
    <td><code>integer</code></td>
    <td>The jvm heap memory allocated.</td>
</tr>
<tr>
    <td><CopyableCode code="jvmOptions" /></td>
    <td><code>array</code></td>
    <td>The jvm options.</td>
</tr>
<tr>
    <td><CopyableCode code="lastModifiedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this springbootapps jar file was last modified.</td>
</tr>
<tr>
    <td><CopyableCode code="lastUpdatedTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Time when this springbootapps instance was last refreshed.</td>
</tr>
<tr>
    <td><CopyableCode code="machineArmIds" /></td>
    <td><code>array</code></td>
    <td>The machine ARM id list the app belongs to.</td>
</tr>
<tr>
    <td><CopyableCode code="miscs" /></td>
    <td><code>array</code></td>
    <td>The other types of date collected.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The resource provisioning state. Known values are: "Unknown", "Succeeded", "Failed", "Canceled", "Accepted", "Provisioning", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="runtimeJdkVersion" /></td>
    <td><code>string</code></td>
    <td>The jdk version installed on server.</td>
</tr>
<tr>
    <td><CopyableCode code="servers" /></td>
    <td><code>array</code></td>
    <td>The server list the app installed.</td>
</tr>
<tr>
    <td><CopyableCode code="siteName" /></td>
    <td><code>string</code></td>
    <td>The site name.</td>
</tr>
<tr>
    <td><CopyableCode code="springBootVersion" /></td>
    <td><code>string</code></td>
    <td>The spring boot version.</td>
</tr>
<tr>
    <td><CopyableCode code="staticContentLocations" /></td>
    <td><code>array</code></td>
    <td>The static content location list.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-springbootapps_name"><code>springbootapps_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a springbootapps resource.</td>
</tr>
<tr>
    <td><a href="#list_by_resource_group"><CopyableCode code="list_by_resource_group" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List springbootapps resource by resourceGroup.</td>
</tr>
<tr>
    <td><a href="#list_by_subscription"><CopyableCode code="list_by_subscription" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List springbootapps resource by subscription.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-springbootapps_name"><code>springbootapps_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Update a springbootapps resource.</td>
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
<tr id="parameter-site_name">
    <td><CopyableCode code="site_name" /></td>
    <td><code>string</code></td>
    <td>The springbootsites name. Required.</td>
</tr>
<tr id="parameter-springbootapps_name">
    <td><CopyableCode code="springbootapps_name" /></td>
    <td><code>string</code></td>
    <td>The springbootapps name. Required.</td>
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
        { label: 'list_by_subscription', value: 'list_by_subscription' }
    ]}
>
<TabItem value="get">

Get a springbootapps resource.

```sql
SELECT
id,
name,
appName,
appPort,
appType,
applicationConfigurations,
artifactName,
bindingPorts,
buildJdkVersion,
certificates,
checksum,
connectionStrings,
dependencies,
environments,
errors,
instanceCount,
instances,
jarFileLocation,
jvmMemoryInMB,
jvmOptions,
lastModifiedTime,
lastUpdatedTime,
machineArmIds,
miscs,
provisioningState,
runtimeJdkVersion,
servers,
siteName,
springBootVersion,
staticContentLocations,
systemData,
tags,
type
FROM azure_extras.springappdiscovery.springbootapps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND springbootapps_name = '{{ springbootapps_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_resource_group">

List springbootapps resource by resourceGroup.

```sql
SELECT
id,
name,
appName,
appPort,
appType,
applicationConfigurations,
artifactName,
bindingPorts,
buildJdkVersion,
certificates,
checksum,
connectionStrings,
dependencies,
environments,
errors,
instanceCount,
instances,
jarFileLocation,
jvmMemoryInMB,
jvmOptions,
lastModifiedTime,
lastUpdatedTime,
machineArmIds,
miscs,
provisioningState,
runtimeJdkVersion,
servers,
siteName,
springBootVersion,
staticContentLocations,
systemData,
tags,
type
FROM azure_extras.springappdiscovery.springbootapps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_by_subscription">

List springbootapps resource by subscription.

```sql
SELECT
id,
name,
appName,
appPort,
appType,
applicationConfigurations,
artifactName,
bindingPorts,
buildJdkVersion,
certificates,
checksum,
connectionStrings,
dependencies,
environments,
errors,
instanceCount,
instances,
jarFileLocation,
jvmMemoryInMB,
jvmOptions,
lastModifiedTime,
lastUpdatedTime,
machineArmIds,
miscs,
provisioningState,
runtimeJdkVersion,
servers,
siteName,
springBootVersion,
staticContentLocations,
systemData,
tags,
type
FROM azure_extras.springappdiscovery.springbootapps
WHERE site_name = '{{ site_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
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

Update a springbootapps resource.

```sql
UPDATE azure_extras.springappdiscovery.springbootapps
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND site_name = '{{ site_name }}' --required
AND springbootapps_name = '{{ springbootapps_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
tags,
type;
```
</TabItem>
</Tabs>
