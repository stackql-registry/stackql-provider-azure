--- 
title: build_service
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service
  - appplatform
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

Creates, updates, deletes, gets or lists a <code>build_service</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="build_service" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appplatform.build_service" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_build_result"
    values={[
        { label: 'get_build_result', value: 'get_build_result' },
        { label: 'list_build_results', value: 'list_build_results' },
        { label: 'get_supported_buildpack', value: 'get_supported_buildpack' },
        { label: 'get_supported_stack', value: 'get_supported_stack' },
        { label: 'list_builds', value: 'list_builds' },
        { label: 'list_build_services', value: 'list_build_services' }
    ]}
>
<TabItem value="get_build_result">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="buildPodName" /></td>
    <td><code>string</code></td>
    <td>The build pod name which can be used to get the build log streaming.</td>
</tr>
<tr>
    <td><CopyableCode code="buildStages" /></td>
    <td><code>array</code></td>
    <td>All of the build stage (init-container and container) resources in build pod.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error when build is failed.</td>
</tr>
<tr>
    <td><CopyableCode code="image" /></td>
    <td><code>string</code></td>
    <td>The container registry image of this build result.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the KPack build result. Known values are: "Queuing", "Building", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_build_results">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="buildPodName" /></td>
    <td><code>string</code></td>
    <td>The build pod name which can be used to get the build log streaming.</td>
</tr>
<tr>
    <td><CopyableCode code="buildStages" /></td>
    <td><code>array</code></td>
    <td>All of the build stage (init-container and container) resources in build pod.</td>
</tr>
<tr>
    <td><CopyableCode code="error" /></td>
    <td><code>object</code></td>
    <td>Error when build is failed.</td>
</tr>
<tr>
    <td><CopyableCode code="image" /></td>
    <td><code>string</code></td>
    <td>The container registry image of this build result.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the KPack build result. Known values are: "Queuing", "Building", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_supported_buildpack">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="buildpackId" /></td>
    <td><code>string</code></td>
    <td>The id of supported buildpack.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_supported_stack">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="stackId" /></td>
    <td><code>string</code></td>
    <td>The id of supported stack.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="version" /></td>
    <td><code>string</code></td>
    <td>The version of supported stack.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_builds">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="agentPool" /></td>
    <td><code>string</code></td>
    <td>The resource id of agent pool.</td>
</tr>
<tr>
    <td><CopyableCode code="apms" /></td>
    <td><code>array</code></td>
    <td>The APMs for this build.</td>
</tr>
<tr>
    <td><CopyableCode code="builder" /></td>
    <td><code>string</code></td>
    <td>The resource id of builder to build the source code.</td>
</tr>
<tr>
    <td><CopyableCode code="certificates" /></td>
    <td><code>array</code></td>
    <td>The CA Certificates for this build.</td>
</tr>
<tr>
    <td><CopyableCode code="env" /></td>
    <td><code>object</code></td>
    <td>The environment variables for this build.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the KPack build result. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="relativePath" /></td>
    <td><code>string</code></td>
    <td>The relative path of source code.</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRequests" /></td>
    <td><code>object</code></td>
    <td>The customized build resource for this build.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="triggeredBuildResult" /></td>
    <td><code>object</code></td>
    <td>The build result triggered by this build.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_build_services">

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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="containerRegistry" /></td>
    <td><code>string</code></td>
    <td>The resource id of the container registry used in this build service.</td>
</tr>
<tr>
    <td><CopyableCode code="kPackVersion" /></td>
    <td><code>string</code></td>
    <td>The installed KPack version in this build service.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the KPack build service. Known values are: "Creating", "Updating", "Succeeded", "Failed", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="resourceRequests" /></td>
    <td><code>object</code></td>
    <td>The runtime resource configuration of this build service.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
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
    <td><a href="#get_build_result"><CopyableCode code="get_build_result" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-build_name"><code>build_name</code></a>, <a href="#parameter-build_result_name"><code>build_result_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a KPack build result.</td>
</tr>
<tr>
    <td><a href="#list_build_results"><CopyableCode code="list_build_results" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-build_name"><code>build_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List KPack build results.</td>
</tr>
<tr>
    <td><a href="#get_supported_buildpack"><CopyableCode code="get_supported_buildpack" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-buildpack_name"><code>buildpack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the supported buildpack resource.</td>
</tr>
<tr>
    <td><a href="#get_supported_stack"><CopyableCode code="get_supported_stack" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-stack_name"><code>stack_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the supported stack resource.</td>
</tr>
<tr>
    <td><a href="#list_builds"><CopyableCode code="list_builds" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List KPack builds.</td>
</tr>
<tr>
    <td><a href="#list_build_services"><CopyableCode code="list_build_services" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List build services resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update_build"><CopyableCode code="create_or_update_build" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-build_name"><code>build_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a KPack build.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a build service resource.</td>
</tr>
<tr>
    <td><a href="#create_or_update_build"><CopyableCode code="create_or_update_build" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-build_name"><code>build_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or update a KPack build.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a build service resource.</td>
</tr>
<tr>
    <td><a href="#delete_build"><CopyableCode code="delete_build" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-build_name"><code>build_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>delete a KPack build.</td>
</tr>
<tr>
    <td><a href="#get_build_service"><CopyableCode code="get_build_service" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a build service resource.</td>
</tr>
<tr>
    <td><a href="#list_supported_buildpacks"><CopyableCode code="list_supported_buildpacks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all supported buildpacks.</td>
</tr>
<tr>
    <td><a href="#list_supported_stacks"><CopyableCode code="list_supported_stacks" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get all supported stacks.</td>
</tr>
<tr>
    <td><a href="#get_build"><CopyableCode code="get_build" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-build_name"><code>build_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a KPack build.</td>
</tr>
<tr>
    <td><a href="#get_build_result_log"><CopyableCode code="get_build_result_log" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-build_name"><code>build_name</code></a>, <a href="#parameter-build_result_name"><code>build_result_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a KPack build result log download URL.</td>
</tr>
<tr>
    <td><a href="#get_resource_upload_url"><CopyableCode code="get_resource_upload_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-build_service_name"><code>build_service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an resource upload URL for build service, which may be artifacts or source archive.</td>
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
<tr id="parameter-build_name">
    <td><CopyableCode code="build_name" /></td>
    <td><code>string</code></td>
    <td>The name of the build resource. Required.</td>
</tr>
<tr id="parameter-build_result_name">
    <td><CopyableCode code="build_result_name" /></td>
    <td><code>string</code></td>
    <td>The name of the build result resource. Required.</td>
</tr>
<tr id="parameter-build_service_name">
    <td><CopyableCode code="build_service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the build service resource. Required.</td>
</tr>
<tr id="parameter-buildpack_name">
    <td><CopyableCode code="buildpack_name" /></td>
    <td><code>string</code></td>
    <td>The name of the buildpack resource. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. Required.</td>
</tr>
<tr id="parameter-service_name">
    <td><CopyableCode code="service_name" /></td>
    <td><code>string</code></td>
    <td>The name of the Service resource. Required.</td>
</tr>
<tr id="parameter-stack_name">
    <td><CopyableCode code="stack_name" /></td>
    <td><code>string</code></td>
    <td>The name of the stack resource. Required.</td>
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
    defaultValue="get_build_result"
    values={[
        { label: 'get_build_result', value: 'get_build_result' },
        { label: 'list_build_results', value: 'list_build_results' },
        { label: 'get_supported_buildpack', value: 'get_supported_buildpack' },
        { label: 'get_supported_stack', value: 'get_supported_stack' },
        { label: 'list_builds', value: 'list_builds' },
        { label: 'list_build_services', value: 'list_build_services' }
    ]}
>
<TabItem value="get_build_result">

Get a KPack build result.

```sql
SELECT
id,
name,
buildPodName,
buildStages,
error,
image,
provisioningState,
systemData,
type
FROM azure.appplatform.build_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND build_service_name = '{{ build_service_name }}' -- required
AND build_name = '{{ build_name }}' -- required
AND build_result_name = '{{ build_result_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_build_results">

List KPack build results.

```sql
SELECT
id,
name,
buildPodName,
buildStages,
error,
image,
provisioningState,
systemData,
type
FROM azure.appplatform.build_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND build_service_name = '{{ build_service_name }}' -- required
AND build_name = '{{ build_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_supported_buildpack">

Get the supported buildpack resource.

```sql
SELECT
id,
name,
buildpackId,
systemData,
type
FROM azure.appplatform.build_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND build_service_name = '{{ build_service_name }}' -- required
AND buildpack_name = '{{ buildpack_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_supported_stack">

Get the supported stack resource.

```sql
SELECT
id,
name,
stackId,
systemData,
type,
version
FROM azure.appplatform.build_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND build_service_name = '{{ build_service_name }}' -- required
AND stack_name = '{{ stack_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_builds">

List KPack builds.

```sql
SELECT
id,
name,
agentPool,
apms,
builder,
certificates,
env,
provisioningState,
relativePath,
resourceRequests,
systemData,
triggeredBuildResult,
type
FROM azure.appplatform.build_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND build_service_name = '{{ build_service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_build_services">

List build services resource.

```sql
SELECT
id,
name,
containerRegistry,
kPackVersion,
provisioningState,
resourceRequests,
systemData,
type
FROM azure.appplatform.build_service
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_or_update_build"
    values={[
        { label: 'create_or_update_build', value: 'create_or_update_build' },
        { label: 'create_or_update', value: 'create_or_update' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_or_update_build">

Create or update a KPack build.

```sql
INSERT INTO azure.appplatform.build_service (
properties,
resource_group_name,
service_name,
build_service_name,
build_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ build_service_name }}',
'{{ build_name }}',
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
<TabItem value="create_or_update">

Create a build service resource.

```sql
INSERT INTO azure.appplatform.build_service (
properties,
resource_group_name,
service_name,
build_service_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ build_service_name }}',
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
- name: build_service
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the build_service resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the build_service resource.
    - name: build_service_name
      value: "{{ build_service_name }}"
      description: Required parameter for the build_service resource.
    - name: build_name
      value: "{{ build_name }}"
      description: Required parameter for the build_service resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the build_service resource.
    - name: properties
      description: |
        Properties of the build resource.
      value:
        containerRegistry: "{{ containerRegistry }}"
        kPackVersion: "{{ kPackVersion }}"
        provisioningState: "{{ provisioningState }}"
        resourceRequests:
          cpu: "{{ cpu }}"
          memory: "{{ memory }}"
`}</CodeBlock>

</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_update_build"
    values={[
        { label: 'create_or_update_build', value: 'create_or_update_build' },
        { label: 'create_or_update', value: 'create_or_update' }
    ]}
>
<TabItem value="create_or_update_build">

Create or update a KPack build.

```sql
REPLACE azure.appplatform.build_service
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND build_service_name = '{{ build_service_name }}' --required
AND build_name = '{{ build_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
properties,
systemData,
type;
```
</TabItem>
<TabItem value="create_or_update">

Create a build service resource.

```sql
REPLACE azure.appplatform.build_service
SET 
properties = '{{ properties }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND build_service_name = '{{ build_service_name }}' --required
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
    defaultValue="delete_build"
    values={[
        { label: 'delete_build', value: 'delete_build' }
    ]}
>
<TabItem value="delete_build">

delete a KPack build.

```sql
DELETE FROM azure.appplatform.build_service
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND build_service_name = '{{ build_service_name }}' --required
AND build_name = '{{ build_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_build_service"
    values={[
        { label: 'get_build_service', value: 'get_build_service' },
        { label: 'list_supported_buildpacks', value: 'list_supported_buildpacks' },
        { label: 'list_supported_stacks', value: 'list_supported_stacks' },
        { label: 'get_build', value: 'get_build' },
        { label: 'get_build_result_log', value: 'get_build_result_log' },
        { label: 'get_resource_upload_url', value: 'get_resource_upload_url' }
    ]}
>
<TabItem value="get_build_service">

Get a build service resource.

```sql
EXEC azure.appplatform.build_service.get_build_service 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@build_service_name='{{ build_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_supported_buildpacks">

Get all supported buildpacks.

```sql
EXEC azure.appplatform.build_service.list_supported_buildpacks 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@build_service_name='{{ build_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_supported_stacks">

Get all supported stacks.

```sql
EXEC azure.appplatform.build_service.list_supported_stacks 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@build_service_name='{{ build_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_build">

Get a KPack build.

```sql
EXEC azure.appplatform.build_service.get_build 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@build_service_name='{{ build_service_name }}' --required, 
@build_name='{{ build_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_build_result_log">

Get a KPack build result log download URL.

```sql
EXEC azure.appplatform.build_service.get_build_result_log 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@build_service_name='{{ build_service_name }}' --required, 
@build_name='{{ build_name }}' --required, 
@build_result_name='{{ build_result_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_resource_upload_url">

Get an resource upload URL for build service, which may be artifacts or source archive.

```sql
EXEC azure.appplatform.build_service.get_resource_upload_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@build_service_name='{{ build_service_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
