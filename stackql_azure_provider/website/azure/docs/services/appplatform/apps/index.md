--- 
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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

Creates, updates, deletes, gets or lists an <code>apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="apps" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.appplatform.apps" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addonConfigs" /></td>
    <td><code>object</code></td>
    <td>Collection of addons.</td>
</tr>
<tr>
    <td><CopyableCode code="customPersistentDisks" /></td>
    <td><code>array</code></td>
    <td>List of custom persistent disks.</td>
</tr>
<tr>
    <td><CopyableCode code="enableEndToEndTLS" /></td>
    <td><code>boolean</code></td>
    <td>Indicate if end to end TLS is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified dns Name.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsOnly" /></td>
    <td><code>boolean</code></td>
    <td>Indicate if only https is allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Managed Identity type of the app resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressSettings" /></td>
    <td><code>object</code></td>
    <td>App ingress settings payload.</td>
</tr>
<tr>
    <td><CopyableCode code="loadedCertificates" /></td>
    <td><code>array</code></td>
    <td>Collection of loaded certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The GEO location of the application, always the same with its parent resource.</td>
</tr>
<tr>
    <td><CopyableCode code="persistentDisk" /></td>
    <td><code>object</code></td>
    <td>Persistent disk settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the App. Known values are: "Succeeded", "Failed", "Creating", "Updating", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="public" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the App exposes public endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="temporaryDisk" /></td>
    <td><code>object</code></td>
    <td>Temporary disk settings.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>URL of the App.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetAddons" /></td>
    <td><code>object</code></td>
    <td>Additional App settings in vnet injection instance.</td>
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
    <td>Fully qualified resource Id for the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="addonConfigs" /></td>
    <td><code>object</code></td>
    <td>Collection of addons.</td>
</tr>
<tr>
    <td><CopyableCode code="customPersistentDisks" /></td>
    <td><code>array</code></td>
    <td>List of custom persistent disks.</td>
</tr>
<tr>
    <td><CopyableCode code="enableEndToEndTLS" /></td>
    <td><code>boolean</code></td>
    <td>Indicate if end to end TLS is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="fqdn" /></td>
    <td><code>string</code></td>
    <td>Fully qualified dns Name.</td>
</tr>
<tr>
    <td><CopyableCode code="httpsOnly" /></td>
    <td><code>boolean</code></td>
    <td>Indicate if only https is allowed.</td>
</tr>
<tr>
    <td><CopyableCode code="identity" /></td>
    <td><code>object</code></td>
    <td>The Managed Identity type of the app resource.</td>
</tr>
<tr>
    <td><CopyableCode code="ingressSettings" /></td>
    <td><code>object</code></td>
    <td>App ingress settings payload.</td>
</tr>
<tr>
    <td><CopyableCode code="loadedCertificates" /></td>
    <td><code>array</code></td>
    <td>Collection of loaded certificates.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The GEO location of the application, always the same with its parent resource.</td>
</tr>
<tr>
    <td><CopyableCode code="persistentDisk" /></td>
    <td><code>object</code></td>
    <td>Persistent disk settings.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Provisioning state of the App. Known values are: "Succeeded", "Failed", "Creating", "Updating", and "Deleting".</td>
</tr>
<tr>
    <td><CopyableCode code="public" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the App exposes public endpoint.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Metadata pertaining to creation and last modification of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="temporaryDisk" /></td>
    <td><code>object</code></td>
    <td>Temporary disk settings.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>URL of the App.</td>
</tr>
<tr>
    <td><CopyableCode code="vnetAddons" /></td>
    <td><code>object</code></td>
    <td>Additional App settings in vnet injection instance.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-syncStatus"><code>syncStatus</code></a></td>
    <td>Get an App and its properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Handles requests to list all resources in a Service.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new App or update an exiting App.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to update an exiting App.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a new App or update an exiting App.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Operation to delete an App.</td>
</tr>
<tr>
    <td><a href="#get_resource_upload_url"><CopyableCode code="get_resource_upload_url" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get an resource upload URL for an App, which may be artifacts or source archive.</td>
</tr>
<tr>
    <td><a href="#set_active_deployments"><CopyableCode code="set_active_deployments" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Set existing Deployment under the app as active.</td>
</tr>
<tr>
    <td><a href="#validate_domain"><CopyableCode code="validate_domain" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-service_name"><code>service_name</code></a>, <a href="#parameter-app_name"><code>app_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a>, <a href="#parameter-name"><code>name</code></a></td>
    <td></td>
    <td>Check the resource name is valid as well as not in use.</td>
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
<tr id="parameter-app_name">
    <td><CopyableCode code="app_name" /></td>
    <td><code>string</code></td>
    <td>The name of the App resource. Required.</td>
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
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-syncStatus">
    <td><CopyableCode code="syncStatus" /></td>
    <td><code>string</code></td>
    <td>Indicates whether sync status. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get">

Get an App and its properties.

```sql
SELECT
id,
name,
addonConfigs,
customPersistentDisks,
enableEndToEndTLS,
fqdn,
httpsOnly,
identity,
ingressSettings,
loadedCertificates,
location,
persistentDisk,
provisioningState,
public,
systemData,
temporaryDisk,
type,
url,
vnetAddons
FROM azure.appplatform.apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND app_name = '{{ app_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND syncStatus = '{{ syncStatus }}'
;
```
</TabItem>
<TabItem value="list">

Handles requests to list all resources in a Service.

```sql
SELECT
id,
name,
addonConfigs,
customPersistentDisks,
enableEndToEndTLS,
fqdn,
httpsOnly,
identity,
ingressSettings,
loadedCertificates,
location,
persistentDisk,
provisioningState,
public,
systemData,
temporaryDisk,
type,
url,
vnetAddons
FROM azure.appplatform.apps
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND service_name = '{{ service_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
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

Create a new App or update an exiting App.

```sql
INSERT INTO azure.appplatform.apps (
properties,
identity,
location,
resource_group_name,
service_name,
app_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ identity }}',
'{{ location }}',
'{{ resource_group_name }}',
'{{ service_name }}',
'{{ app_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
identity,
location,
properties,
systemData,
type
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: apps
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the apps resource.
    - name: service_name
      value: "{{ service_name }}"
      description: Required parameter for the apps resource.
    - name: app_name
      value: "{{ app_name }}"
      description: Required parameter for the apps resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the apps resource.
    - name: properties
      description: |
        Properties of the App resource.
      value:
        public: {{ public }}
        url: "{{ url }}"
        addonConfigs: "{{ addonConfigs }}"
        provisioningState: "{{ provisioningState }}"
        fqdn: "{{ fqdn }}"
        httpsOnly: {{ httpsOnly }}
        temporaryDisk:
          sizeInGB: {{ sizeInGB }}
          mountPath: "{{ mountPath }}"
        persistentDisk:
          sizeInGB: {{ sizeInGB }}
          usedInGB: {{ usedInGB }}
          mountPath: "{{ mountPath }}"
        customPersistentDisks:
          - customPersistentDiskProperties:
              type: "{{ type }}"
              mountPath: "{{ mountPath }}"
              readOnly: {{ readOnly }}
              enableSubPath: {{ enableSubPath }}
              mountOptions:
                - "{{ mountOptions }}"
            storageId: "{{ storageId }}"
        enableEndToEndTLS: {{ enableEndToEndTLS }}
        loadedCertificates:
          - resourceId: "{{ resourceId }}"
            loadTrustStore: {{ loadTrustStore }}
        vnetAddons:
          publicEndpoint: {{ publicEndpoint }}
          publicEndpointUrl: "{{ publicEndpointUrl }}"
        ingressSettings:
          readTimeoutInSeconds: {{ readTimeoutInSeconds }}
          sendTimeoutInSeconds: {{ sendTimeoutInSeconds }}
          sessionAffinity: "{{ sessionAffinity }}"
          sessionCookieMaxAge: {{ sessionCookieMaxAge }}
          backendProtocol: "{{ backendProtocol }}"
          clientAuth:
            certificates:
              - "{{ certificates }}"
    - name: identity
      description: |
        The Managed Identity type of the app resource.
      value:
        type: "{{ type }}"
        principalId: "{{ principalId }}"
        tenantId: "{{ tenantId }}"
        userAssignedIdentities: "{{ userAssignedIdentities }}"
    - name: location
      value: "{{ location }}"
      description: |
        The GEO location of the application, always the same with its parent resource.
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

Operation to update an exiting App.

```sql
UPDATE azure.appplatform.apps
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
properties,
systemData,
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

Create a new App or update an exiting App.

```sql
REPLACE azure.appplatform.apps
SET 
properties = '{{ properties }}',
identity = '{{ identity }}',
location = '{{ location }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
identity,
location,
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

Operation to delete an App.

```sql
DELETE FROM azure.appplatform.apps
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND service_name = '{{ service_name }}' --required
AND app_name = '{{ app_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="get_resource_upload_url"
    values={[
        { label: 'get_resource_upload_url', value: 'get_resource_upload_url' },
        { label: 'set_active_deployments', value: 'set_active_deployments' },
        { label: 'validate_domain', value: 'validate_domain' }
    ]}
>
<TabItem value="get_resource_upload_url">

Get an resource upload URL for an App, which may be artifacts or source archive.

```sql
EXEC azure.appplatform.apps.get_resource_upload_url 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="set_active_deployments">

Set existing Deployment under the app as active.

```sql
EXEC azure.appplatform.apps.set_active_deployments 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"activeDeploymentNames": "{{ activeDeploymentNames }}"
}'
;
```
</TabItem>
<TabItem value="validate_domain">

Check the resource name is valid as well as not in use.

```sql
EXEC azure.appplatform.apps.validate_domain 
@resource_group_name='{{ resource_group_name }}' --required, 
@service_name='{{ service_name }}' --required, 
@app_name='{{ app_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required 
@@json=
'{
"name": "{{ name }}"
}'
;
```
</TabItem>
</Tabs>
