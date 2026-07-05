--- 
title: cg_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - cg_profile
  - containerinstance
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

Creates, updates, deletes, gets or lists a <code>cg_profile</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="cg_profile" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.containerinstance.cg_profile" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_by_revision_number"
    values={[
        { label: 'get_by_revision_number', value: 'get_by_revision_number' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_by_revision_number">

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
    <td><CopyableCode code="confidentialComputeProperties" /></td>
    <td><code>object</code></td>
    <td>The properties for confidential container group.</td>
</tr>
<tr>
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>The containers within the container group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>The diagnostic information for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProperties" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>extensions used by virtual kubelet.</td>
</tr>
<tr>
    <td><CopyableCode code="imageRegistryCredentials" /></td>
    <td><code>array</code></td>
    <td>The image registry credentials by which the container group is created from.</td>
</tr>
<tr>
    <td><CopyableCode code="initContainers" /></td>
    <td><code>array</code></td>
    <td>The init containers for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>object</code></td>
    <td>The IP address type of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type required by the containers in the container group. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the container group. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="registeredRevisions" /></td>
    <td><code>array</code></td>
    <td>Registered revisions are calculated at request time based off the records in the table logs.</td>
</tr>
<tr>
    <td><CopyableCode code="restartPolicy" /></td>
    <td><code>string</code></td>
    <td>Restart policy for all containers within the container group. * `Always` Always restart * `OnFailure` Restart on failure * `Never` Never restart. Known values are: "Always", "OnFailure", and "Never". (Always, OnFailure, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>Container group profile current revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="securityContext" /></td>
    <td><code>object</code></td>
    <td>The container security properties.</td>
</tr>
<tr>
    <td><CopyableCode code="shutdownGracePeriod" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shutdown grace period for containers in a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU for a container group. Known values are: "NotSpecified", "Standard", "Dedicated", and "Confidential". (NotSpecified, Standard, Dedicated, Confidential)</td>
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
    <td><CopyableCode code="timeToLive" /></td>
    <td><code>string (date-time)</code></td>
    <td>Post completion time to live for containers of a CG.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useKrypton" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets Krypton use property.</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>The list of volumes that can be mounted by containers in this container group.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><CopyableCode code="confidentialComputeProperties" /></td>
    <td><code>object</code></td>
    <td>The properties for confidential container group.</td>
</tr>
<tr>
    <td><CopyableCode code="containers" /></td>
    <td><code>array</code></td>
    <td>The containers within the container group. Required.</td>
</tr>
<tr>
    <td><CopyableCode code="diagnostics" /></td>
    <td><code>object</code></td>
    <td>The diagnostic information for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="encryptionProperties" /></td>
    <td><code>object</code></td>
    <td>The encryption properties for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="extensions" /></td>
    <td><code>array</code></td>
    <td>extensions used by virtual kubelet.</td>
</tr>
<tr>
    <td><CopyableCode code="imageRegistryCredentials" /></td>
    <td><code>array</code></td>
    <td>The image registry credentials by which the container group is created from.</td>
</tr>
<tr>
    <td><CopyableCode code="initContainers" /></td>
    <td><code>array</code></td>
    <td>The init containers for a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="ipAddress" /></td>
    <td><code>object</code></td>
    <td>The IP address type of the container group.</td>
</tr>
<tr>
    <td><CopyableCode code="location" /></td>
    <td><code>string</code></td>
    <td>The geo-location where the resource lives.</td>
</tr>
<tr>
    <td><CopyableCode code="osType" /></td>
    <td><code>string</code></td>
    <td>The operating system type required by the containers in the container group. Required. Known values are: "Windows" and "Linux". (Windows, Linux)</td>
</tr>
<tr>
    <td><CopyableCode code="priority" /></td>
    <td><code>string</code></td>
    <td>The priority of the container group. Known values are: "Regular" and "Spot". (Regular, Spot)</td>
</tr>
<tr>
    <td><CopyableCode code="registeredRevisions" /></td>
    <td><code>array</code></td>
    <td>Registered revisions are calculated at request time based off the records in the table logs.</td>
</tr>
<tr>
    <td><CopyableCode code="restartPolicy" /></td>
    <td><code>string</code></td>
    <td>Restart policy for all containers within the container group. * `Always` Always restart * `OnFailure` Restart on failure * `Never` Never restart. Known values are: "Always", "OnFailure", and "Never". (Always, OnFailure, Never)</td>
</tr>
<tr>
    <td><CopyableCode code="revision" /></td>
    <td><code>integer</code></td>
    <td>Container group profile current revision number.</td>
</tr>
<tr>
    <td><CopyableCode code="securityContext" /></td>
    <td><code>object</code></td>
    <td>The container security properties.</td>
</tr>
<tr>
    <td><CopyableCode code="shutdownGracePeriod" /></td>
    <td><code>string (date-time)</code></td>
    <td>Shutdown grace period for containers in a container group.</td>
</tr>
<tr>
    <td><CopyableCode code="sku" /></td>
    <td><code>string</code></td>
    <td>The SKU for a container group. Known values are: "NotSpecified", "Standard", "Dedicated", and "Confidential". (NotSpecified, Standard, Dedicated, Confidential)</td>
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
    <td><CopyableCode code="timeToLive" /></td>
    <td><code>string (date-time)</code></td>
    <td>Post completion time to live for containers of a CG.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="useKrypton" /></td>
    <td><code>boolean</code></td>
    <td>Gets or sets Krypton use property.</td>
</tr>
<tr>
    <td><CopyableCode code="volumes" /></td>
    <td><code>array</code></td>
    <td>The list of volumes that can be mounted by containers in this container group.</td>
</tr>
<tr>
    <td><CopyableCode code="zones" /></td>
    <td><code>array</code></td>
    <td>The availability zones.</td>
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
    <td><a href="#get_by_revision_number"><CopyableCode code="get_by_revision_number" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_profile_name"><code>container_group_profile_name</code></a>, <a href="#parameter-revision_number"><code>revision_number</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get the properties of the specified revision of the container group profile. Gets the properties of the specified revision of the container group profile in the given subscription and resource group. The operation returns the properties of container group profile including containers, image registry credentials, restart policy, IP address type, OS type, volumes, current revision number, etc.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_profile_name"><code>container_group_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Display information about a specified ContainerGroupProfile. Get the properties of the specified container group profile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_profile_name"><code>container_group_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update a ContainerGroupProfile. Create a CGProfile if it doesn't exist or update an existing CGProfile.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_profile_name"><code>container_group_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Container group profile PATCH REST API. Update a specified container group profile.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_profile_name"><code>container_group_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create or Update a ContainerGroupProfile. Create a CGProfile if it doesn't exist or update an existing CGProfile.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_profile_name"><code>container_group_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Container group profile DELETE REST API. Deletes a container group profile.</td>
</tr>
<tr>
    <td><a href="#list_all_revisions"><CopyableCode code="list_all_revisions" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-container_group_profile_name"><code>container_group_profile_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a list of all the revisions of the specified container group profile in the given subscription and resource group. Get a list of all the revisions of the specified container group profile in the given subscription and resource group. This operation returns properties of each revision of the specified container group profile including containers, image registry credentials, restart policy, IP address type, OS type volumes, revision number, etc.</td>
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
<tr id="parameter-container_group_profile_name">
    <td><CopyableCode code="container_group_profile_name" /></td>
    <td><code>string</code></td>
    <td>ContainerGroupProfile name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-revision_number">
    <td><CopyableCode code="revision_number" /></td>
    <td><code>string</code></td>
    <td>The revision number of the container group profile. Required.</td>
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
    defaultValue="get_by_revision_number"
    values={[
        { label: 'get_by_revision_number', value: 'get_by_revision_number' },
        { label: 'get', value: 'get' }
    ]}
>
<TabItem value="get_by_revision_number">

Get the properties of the specified revision of the container group profile. Gets the properties of the specified revision of the container group profile in the given subscription and resource group. The operation returns the properties of container group profile including containers, image registry credentials, restart policy, IP address type, OS type, volumes, current revision number, etc.

```sql
SELECT
id,
name,
confidentialComputeProperties,
containers,
diagnostics,
encryptionProperties,
extensions,
imageRegistryCredentials,
initContainers,
ipAddress,
location,
osType,
priority,
registeredRevisions,
restartPolicy,
revision,
securityContext,
shutdownGracePeriod,
sku,
systemData,
tags,
timeToLive,
type,
useKrypton,
volumes,
zones
FROM azure.containerinstance.cg_profile
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_group_profile_name = '{{ container_group_profile_name }}' -- required
AND revision_number = '{{ revision_number }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Display information about a specified ContainerGroupProfile. Get the properties of the specified container group profile.

```sql
SELECT
id,
name,
confidentialComputeProperties,
containers,
diagnostics,
encryptionProperties,
extensions,
imageRegistryCredentials,
initContainers,
ipAddress,
location,
osType,
priority,
registeredRevisions,
restartPolicy,
revision,
securityContext,
shutdownGracePeriod,
sku,
systemData,
tags,
timeToLive,
type,
useKrypton,
volumes,
zones
FROM azure.containerinstance.cg_profile
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND container_group_profile_name = '{{ container_group_profile_name }}' -- required
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

Create or Update a ContainerGroupProfile. Create a CGProfile if it doesn't exist or update an existing CGProfile.

```sql
INSERT INTO azure.containerinstance.cg_profile (
properties,
tags,
location,
zones,
resource_group_name,
container_group_profile_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ tags }}',
'{{ location }}',
'{{ zones }}',
'{{ resource_group_name }}',
'{{ container_group_profile_name }}',
'{{ subscription_id }}'
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones
;
```
</TabItem>
<TabItem value="manifest">

<CodeBlock language="yaml">{`# Description fields are for documentation purposes
- name: cg_profile
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the cg_profile resource.
    - name: container_group_profile_name
      value: "{{ container_group_profile_name }}"
      description: Required parameter for the cg_profile resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the cg_profile resource.
    - name: properties
      description: |
        The container group profile properties.
      value:
        sku: "{{ sku }}"
        encryptionProperties:
          vaultBaseUrl: "{{ vaultBaseUrl }}"
          keyName: "{{ keyName }}"
          keyVersion: "{{ keyVersion }}"
          identity: "{{ identity }}"
        containers:
          - name: "{{ name }}"
            properties:
              image: "{{ image }}"
              command:
                - "{{ command }}"
              ports:
                - protocol: "{{ protocol }}"
                  port: {{ port }}
              environmentVariables:
                - name: "{{ name }}"
                  value: "{{ value }}"
                  secureValue: "{{ secureValue }}"
                  secureValueReference: "{{ secureValueReference }}"
              instanceView:
                restartCount: {{ restartCount }}
                currentState:
                  state: "{{ state }}"
                  startTime: "{{ startTime }}"
                  exitCode: {{ exitCode }}
                  finishTime: "{{ finishTime }}"
                  detailStatus: "{{ detailStatus }}"
                previousState:
                  state: "{{ state }}"
                  startTime: "{{ startTime }}"
                  exitCode: {{ exitCode }}
                  finishTime: "{{ finishTime }}"
                  detailStatus: "{{ detailStatus }}"
                events:
                  - count: {{ count }}
                    firstTimestamp: "{{ firstTimestamp }}"
                    lastTimestamp: "{{ lastTimestamp }}"
                    name: "{{ name }}"
                    message: "{{ message }}"
                    type: "{{ type }}"
              resources:
                requests:
                  memoryInGB: {{ memoryInGB }}
                  cpu: {{ cpu }}
                  gpu: "{{ gpu }}"
                limits:
                  memoryInGB: {{ memoryInGB }}
                  cpu: {{ cpu }}
                  gpu: "{{ gpu }}"
              volumeMounts:
                - name: "{{ name }}"
                  mountPath: "{{ mountPath }}"
                  readOnly: {{ readOnly }}
              livenessProbe:
                exec:
                  command: "{{ command }}"
                httpGet:
                  path: "{{ path }}"
                  port: {{ port }}
                  scheme: "{{ scheme }}"
                  httpHeaders: "{{ httpHeaders }}"
                initialDelaySeconds: {{ initialDelaySeconds }}
                periodSeconds: {{ periodSeconds }}
                failureThreshold: {{ failureThreshold }}
                successThreshold: {{ successThreshold }}
                timeoutSeconds: {{ timeoutSeconds }}
              readinessProbe:
                exec:
                  command: "{{ command }}"
                httpGet:
                  path: "{{ path }}"
                  port: {{ port }}
                  scheme: "{{ scheme }}"
                  httpHeaders: "{{ httpHeaders }}"
                initialDelaySeconds: {{ initialDelaySeconds }}
                periodSeconds: {{ periodSeconds }}
                failureThreshold: {{ failureThreshold }}
                successThreshold: {{ successThreshold }}
                timeoutSeconds: {{ timeoutSeconds }}
              securityContext:
                privileged: {{ privileged }}
                allowPrivilegeEscalation: {{ allowPrivilegeEscalation }}
                capabilities:
                  add: "{{ add }}"
                  drop: "{{ drop }}"
                runAsGroup: {{ runAsGroup }}
                runAsUser: {{ runAsUser }}
                seccompProfile: "{{ seccompProfile }}"
              configMap:
                keyValuePairs: "{{ keyValuePairs }}"
        initContainers:
          - name: "{{ name }}"
            properties:
              image: "{{ image }}"
              command:
                - "{{ command }}"
              environmentVariables:
                - name: "{{ name }}"
                  value: "{{ value }}"
                  secureValue: "{{ secureValue }}"
                  secureValueReference: "{{ secureValueReference }}"
              instanceView:
                restartCount: {{ restartCount }}
                currentState:
                  state: "{{ state }}"
                  startTime: "{{ startTime }}"
                  exitCode: {{ exitCode }}
                  finishTime: "{{ finishTime }}"
                  detailStatus: "{{ detailStatus }}"
                previousState:
                  state: "{{ state }}"
                  startTime: "{{ startTime }}"
                  exitCode: {{ exitCode }}
                  finishTime: "{{ finishTime }}"
                  detailStatus: "{{ detailStatus }}"
                events:
                  - count: {{ count }}
                    firstTimestamp: "{{ firstTimestamp }}"
                    lastTimestamp: "{{ lastTimestamp }}"
                    name: "{{ name }}"
                    message: "{{ message }}"
                    type: "{{ type }}"
              volumeMounts:
                - name: "{{ name }}"
                  mountPath: "{{ mountPath }}"
                  readOnly: {{ readOnly }}
              securityContext:
                privileged: {{ privileged }}
                allowPrivilegeEscalation: {{ allowPrivilegeEscalation }}
                capabilities:
                  add: "{{ add }}"
                  drop: "{{ drop }}"
                runAsGroup: {{ runAsGroup }}
                runAsUser: {{ runAsUser }}
                seccompProfile: "{{ seccompProfile }}"
        extensions:
          - name: "{{ name }}"
            properties:
              extensionType: "{{ extensionType }}"
              version: "{{ version }}"
              settings: "{{ settings }}"
              protectedSettings: "{{ protectedSettings }}"
        imageRegistryCredentials:
          - server: "{{ server }}"
            username: "{{ username }}"
            password: "{{ password }}"
            passwordReference: "{{ passwordReference }}"
            identity: "{{ identity }}"
            identityUrl: "{{ identityUrl }}"
        restartPolicy: "{{ restartPolicy }}"
        shutdownGracePeriod: "{{ shutdownGracePeriod }}"
        ipAddress:
          ports:
            - protocol: "{{ protocol }}"
              port: {{ port }}
          type: "{{ type }}"
          ip: "{{ ip }}"
          dnsNameLabel: "{{ dnsNameLabel }}"
          autoGeneratedDomainNameLabelScope: "{{ autoGeneratedDomainNameLabelScope }}"
          fqdn: "{{ fqdn }}"
        timeToLive: "{{ timeToLive }}"
        osType: "{{ osType }}"
        volumes:
          - name: "{{ name }}"
            azureFile:
              shareName: "{{ shareName }}"
              readOnly: {{ readOnly }}
              storageAccountName: "{{ storageAccountName }}"
              storageAccountKey: "{{ storageAccountKey }}"
              storageAccountKeyReference: "{{ storageAccountKeyReference }}"
            emptyDir: "{{ emptyDir }}"
            secret: "{{ secret }}"
            secretReference: "{{ secretReference }}"
            gitRepo:
              directory: "{{ directory }}"
              repository: "{{ repository }}"
              revision: "{{ revision }}"
        diagnostics:
          logAnalytics:
            workspaceId: "{{ workspaceId }}"
            workspaceKey: "{{ workspaceKey }}"
            logType: "{{ logType }}"
            metadata: "{{ metadata }}"
            workspaceResourceId: "{{ workspaceResourceId }}"
        priority: "{{ priority }}"
        confidentialComputeProperties:
          ccePolicy: "{{ ccePolicy }}"
        securityContext:
          privileged: {{ privileged }}
          allowPrivilegeEscalation: {{ allowPrivilegeEscalation }}
          capabilities:
            add:
              - "{{ add }}"
            drop:
              - "{{ drop }}"
          runAsGroup: {{ runAsGroup }}
          runAsUser: {{ runAsUser }}
          seccompProfile: "{{ seccompProfile }}"
        revision: {{ revision }}
        registeredRevisions:
          - {{ registeredRevisions }}
        useKrypton: {{ useKrypton }}
    - name: tags
      value: "{{ tags }}"
      description: |
        Resource tags.
    - name: location
      value: "{{ location }}"
      description: |
        The geo-location where the resource lives.
    - name: zones
      value:
        - "{{ zones }}"
      description: |
        The availability zones.
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

Container group profile PATCH REST API. Update a specified container group profile.

```sql
UPDATE azure.containerinstance.cg_profile
SET 
tags = '{{ tags }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_group_profile_name = '{{ container_group_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones;
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

Create or Update a ContainerGroupProfile. Create a CGProfile if it doesn't exist or update an existing CGProfile.

```sql
REPLACE azure.containerinstance.cg_profile
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}',
zones = '{{ zones }}'
WHERE 
resource_group_name = '{{ resource_group_name }}' --required
AND container_group_profile_name = '{{ container_group_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
RETURNING
id,
name,
location,
properties,
systemData,
tags,
type,
zones;
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

Container group profile DELETE REST API. Deletes a container group profile.

```sql
DELETE FROM azure.containerinstance.cg_profile
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND container_group_profile_name = '{{ container_group_profile_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_all_revisions"
    values={[
        { label: 'list_all_revisions', value: 'list_all_revisions' }
    ]}
>
<TabItem value="list_all_revisions">

Get a list of all the revisions of the specified container group profile in the given subscription and resource group. Get a list of all the revisions of the specified container group profile in the given subscription and resource group. This operation returns properties of each revision of the specified container group profile including containers, image registry credentials, restart policy, IP address type, OS type volumes, revision number, etc.

```sql
EXEC azure.containerinstance.cg_profile.list_all_revisions 
@resource_group_name='{{ resource_group_name }}' --required, 
@container_group_profile_name='{{ container_group_profile_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
