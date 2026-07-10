--- 
title: compose_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - compose_deployments
  - servicefabric_dataplane
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

Creates, updates, deletes, gets or lists a <code>compose_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="compose_deployments" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.compose_deployments" /></td></tr>
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
    <td><a href="#create_compose_deployment"><CopyableCode code="create_compose_deployment" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-DeploymentName"><code>DeploymentName</code></a>, <a href="#parameter-ComposeFileContent"><code>ComposeFileContent</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Creates a Service Fabric compose deployment. Compose is a file format that describes multi-container applications. This API allows deploying container based applications defined in compose format in a Service Fabric cluster. Once the deployment is created, its status can be tracked via the `GetComposeDeploymentStatus` API.</td>
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
<tr id="parameter-timeout">
    <td><CopyableCode code="timeout" /></td>
    <td><code>integer (int64)</code></td>
    <td>The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.</td>
</tr>
</tbody>
</table>

## `INSERT` examples

<Tabs
    defaultValue="create_compose_deployment"
    values={[
        { label: 'create_compose_deployment', value: 'create_compose_deployment' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_compose_deployment">

Creates a Service Fabric compose deployment. Compose is a file format that describes multi-container applications. This API allows deploying container based applications defined in compose format in a Service Fabric cluster. Once the deployment is created, its status can be tracked via the `GetComposeDeploymentStatus` API.

```sql
INSERT INTO azure.servicefabric_dataplane.compose_deployments (
DeploymentName,
ComposeFileContent,
RegistryCredential,
endpoint,
timeout
)
SELECT 
'{{ DeploymentName }}' /* required */,
'{{ ComposeFileContent }}' /* required */,
'{{ RegistryCredential }}',
'{{ endpoint }}',
'{{ timeout }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: compose_deployments
  props:
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the compose_deployments resource.
    - name: DeploymentName
      value: "{{ DeploymentName }}"
    - name: ComposeFileContent
      value: "{{ ComposeFileContent }}"
    - name: RegistryCredential
      description: |
        Credential information to connect to container registry.
      value:
        RegistryUserName: "{{ RegistryUserName }}"
        RegistryPassword: "{{ RegistryPassword }}"
        PasswordEncrypted: {{ PasswordEncrypted }}
    - name: timeout
      value: "{{ timeout }}"
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
`}</CodeBlock>

</TabItem>
</Tabs>
