--- 
title: deploy_service_package_to_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - deploy_service_package_to_nodes
  - service_fabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>deploy_service_package_to_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deploy_service_package_to_nodes" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_dataplane.deploy_service_package_to_nodes" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


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
    <td><a href="#deploy_service_package_to_node"><CopyableCode code="deploy_service_package_to_node" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-node_name"><code>node_name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-ServiceManifestName"><code>ServiceManifestName</code></a>, <a href="#parameter-ApplicationTypeName"><code>ApplicationTypeName</code></a>, <a href="#parameter-ApplicationTypeVersion"><code>ApplicationTypeVersion</code></a>, <a href="#parameter-NodeName"><code>NodeName</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Downloads all of the code packages associated with specified service manifest on the specified node. This API provides a way to download code packages including the container images on a specific node outside of the normal application deployment and upgrade path. This is useful for the large code packages and container images to be present on the node before the actual application deployment and upgrade, thus significantly reducing the total time required for the deployment or upgrade.</td>
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
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint host (no scheme). (default: )</td>
</tr>
<tr id="parameter-node_name">
    <td><CopyableCode code="node_name" /></td>
    <td><code>string</code></td>
    <td>The name of the node.</td>
</tr>
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## Lifecycle Methods

<Tabs
    defaultValue="deploy_service_package_to_node"
    values={[
        { label: 'deploy_service_package_to_node', value: 'deploy_service_package_to_node' }
    ]}
>
<TabItem value="deploy_service_package_to_node">

Downloads all of the code packages associated with specified service manifest on the specified node. This API provides a way to download code packages including the container images on a specific node outside of the normal application deployment and upgrade path. This is useful for the large code packages and container images to be present on the node before the actual application deployment and upgrade, thus significantly reducing the total time required for the deployment or upgrade.

```sql
EXEC azure.service_fabric_dataplane.deploy_service_package_to_nodes.deploy_service_package_to_node 
@node_name='{{ node_name }}' --required, 
@endpoint='{{ endpoint }}' --required, 
@timeout='{{ timeout }}' 
@@json=
'{
"ServiceManifestName": "{{ ServiceManifestName }}", 
"ApplicationTypeName": "{{ ApplicationTypeName }}", 
"ApplicationTypeVersion": "{{ ApplicationTypeVersion }}", 
"NodeName": "{{ NodeName }}", 
"PackageSharingPolicy": "{{ PackageSharingPolicy }}"
}'
;
```
</TabItem>
</Tabs>
