--- 
title: service_from_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - service_from_templates
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

Creates, updates, deletes, gets or lists a <code>service_from_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="service_from_templates" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.servicefabric_dataplane.service_from_templates" /></td></tr>
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
    <td><a href="#create_service_from_template"><CopyableCode code="create_service_from_template" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-application_id"><code>application_id</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a>, <a href="#parameter-ApplicationName"><code>ApplicationName</code></a>, <a href="#parameter-ServiceName"><code>ServiceName</code></a>, <a href="#parameter-ServiceTypeName"><code>ServiceTypeName</code></a></td>
    <td><a href="#parameter-timeout"><code>timeout</code></a></td>
    <td>Creates a Service Fabric service from the service template. Creates a Service Fabric service from the service template defined in the application manifest. A service template contains the properties that will be same for the service instance of the same type. The API allows overriding the properties that are usually different for different services of the same service type.</td>
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
<tr id="parameter-application_id">
    <td><CopyableCode code="application_id" /></td>
    <td><code>string</code></td>
    <td>The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the "~" character. For example, if the application name is "fabric:/myapp/app1", the application identity would be "myapp~app1" in 6.0+ and "myapp/app1" in previous versions.</td>
</tr>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>The service endpoint. (default: )</td>
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
    defaultValue="create_service_from_template"
    values={[
        { label: 'create_service_from_template', value: 'create_service_from_template' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_service_from_template">

Creates a Service Fabric service from the service template. Creates a Service Fabric service from the service template defined in the application manifest. A service template contains the properties that will be same for the service instance of the same type. The API allows overriding the properties that are usually different for different services of the same service type.

```sql
INSERT INTO azure.servicefabric_dataplane.service_from_templates (
ApplicationName,
ServiceName,
ServiceTypeName,
InitializationData,
ServicePackageActivationMode,
ServiceDnsName,
application_id,
endpoint,
timeout
)
SELECT 
'{{ ApplicationName }}' /* required */,
'{{ ServiceName }}' /* required */,
'{{ ServiceTypeName }}' /* required */,
'{{ InitializationData }}',
'{{ ServicePackageActivationMode }}',
'{{ ServiceDnsName }}',
'{{ application_id }}',
'{{ endpoint }}',
'{{ timeout }}'
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: service_from_templates
  props:
    - name: application_id
      value: "{{ application_id }}"
      description: Required parameter for the service_from_templates resource.
    - name: endpoint
      value: "{{ endpoint }}"
      description: Required parameter for the service_from_templates resource.
    - name: ApplicationName
      value: "{{ ApplicationName }}"
    - name: ServiceName
      value: "{{ ServiceName }}"
    - name: ServiceTypeName
      value: "{{ ServiceTypeName }}"
    - name: InitializationData
      value:
        - {{ InitializationData }}
    - name: ServicePackageActivationMode
      value: "{{ ServicePackageActivationMode }}"
    - name: ServiceDnsName
      value: "{{ ServiceDnsName }}"
    - name: timeout
      value: "{{ timeout }}"
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
      description: The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
`}</CodeBlock>

</TabItem>
</Tabs>
