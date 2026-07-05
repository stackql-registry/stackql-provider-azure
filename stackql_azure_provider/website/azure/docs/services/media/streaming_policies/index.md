--- 
title: streaming_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_policies
  - media
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

Creates, updates, deletes, gets or lists a <code>streaming_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="streaming_policies" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media.streaming_policies" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;.</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="commonEncryptionCbcs" /></td>
    <td><code>object</code></td>
    <td>Configuration of CommonEncryptionCbcs.</td>
</tr>
<tr>
    <td><CopyableCode code="commonEncryptionCenc" /></td>
    <td><code>object</code></td>
    <td>Configuration of CommonEncryptionCenc.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of Streaming Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultContentKeyPolicyName" /></td>
    <td><code>string</code></td>
    <td>Default ContentKey used by current Streaming Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="envelopeEncryption" /></td>
    <td><code>object</code></td>
    <td>Configuration of EnvelopeEncryption.</td>
</tr>
<tr>
    <td><CopyableCode code="noEncryption" /></td>
    <td><code>object</code></td>
    <td>Configurations of NoEncryption.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><CopyableCode code="commonEncryptionCbcs" /></td>
    <td><code>object</code></td>
    <td>Configuration of CommonEncryptionCbcs.</td>
</tr>
<tr>
    <td><CopyableCode code="commonEncryptionCenc" /></td>
    <td><code>object</code></td>
    <td>Configuration of CommonEncryptionCenc.</td>
</tr>
<tr>
    <td><CopyableCode code="created" /></td>
    <td><code>string (date-time)</code></td>
    <td>Creation time of Streaming Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="defaultContentKeyPolicyName" /></td>
    <td><code>string</code></td>
    <td>Default ContentKey used by current Streaming Policy.</td>
</tr>
<tr>
    <td><CopyableCode code="envelopeEncryption" /></td>
    <td><code>object</code></td>
    <td>Configuration of EnvelopeEncryption.</td>
</tr>
<tr>
    <td><CopyableCode code="noEncryption" /></td>
    <td><code>object</code></td>
    <td>Configurations of NoEncryption.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>The system metadata relating to this resource.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_policy_name"><code>streaming_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get a Streaming Policy. Get the details of a Streaming Policy in the Media Services account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a></td>
    <td>List Streaming Policies. Lists the Streaming Policies in the account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_policy_name"><code>streaming_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Create a Streaming Policy. Create a Streaming Policy in the Media Services account.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-account_name"><code>account_name</code></a>, <a href="#parameter-streaming_policy_name"><code>streaming_policy_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Delete a Streaming Policy. Deletes a Streaming Policy in the Media Services account.</td>
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
<tr id="parameter-account_name">
    <td><CopyableCode code="account_name" /></td>
    <td><code>string</code></td>
    <td>The Media Services account name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group within the Azure subscription. Required.</td>
</tr>
<tr id="parameter-streaming_policy_name">
    <td><CopyableCode code="streaming_policy_name" /></td>
    <td><code>string</code></td>
    <td>The Streaming Policy name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>Restricts the set of items returned. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>Specifies the key by which the result collection should be ordered. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. Default value is None.</td>
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

Get a Streaming Policy. Get the details of a Streaming Policy in the Media Services account.

```sql
SELECT
id,
name,
commonEncryptionCbcs,
commonEncryptionCenc,
created,
defaultContentKeyPolicyName,
envelopeEncryption,
noEncryption,
systemData,
type
FROM azure.media.streaming_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND streaming_policy_name = '{{ streaming_policy_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

List Streaming Policies. Lists the Streaming Policies in the account.

```sql
SELECT
id,
name,
commonEncryptionCbcs,
commonEncryptionCenc,
created,
defaultContentKeyPolicyName,
envelopeEncryption,
noEncryption,
systemData,
type
FROM azure.media.streaming_policies
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND account_name = '{{ account_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $filter = '{{ $filter }}'
AND $top = '{{ $top }}'
AND $orderby = '{{ $orderby }}'
;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create"
    values={[
        { label: 'create', value: 'create' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create">

Create a Streaming Policy. Create a Streaming Policy in the Media Services account.

```sql
INSERT INTO azure.media.streaming_policies (
properties,
resource_group_name,
account_name,
streaming_policy_name,
subscription_id
)
SELECT 
'{{ properties }}',
'{{ resource_group_name }}',
'{{ account_name }}',
'{{ streaming_policy_name }}',
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
- name: streaming_policies
  props:
    - name: resource_group_name
      value: "{{ resource_group_name }}"
      description: Required parameter for the streaming_policies resource.
    - name: account_name
      value: "{{ account_name }}"
      description: Required parameter for the streaming_policies resource.
    - name: streaming_policy_name
      value: "{{ streaming_policy_name }}"
      description: Required parameter for the streaming_policies resource.
    - name: subscription_id
      value: "{{ subscription_id }}"
      description: Required parameter for the streaming_policies resource.
    - name: properties
      value:
        defaultContentKeyPolicyName: "{{ defaultContentKeyPolicyName }}"
        envelopeEncryption:
          enabledProtocols:
            download: {{ download }}
            dash: {{ dash }}
            hls: {{ hls }}
            smoothStreaming: {{ smoothStreaming }}
          clearTracks:
            - trackSelections: "{{ trackSelections }}"
          contentKeys:
            defaultKey:
              label: "{{ label }}"
              policyName: "{{ policyName }}"
            keyToTrackMappings:
              - label: "{{ label }}"
                policyName: "{{ policyName }}"
                tracks: "{{ tracks }}"
          customKeyAcquisitionUrlTemplate: "{{ customKeyAcquisitionUrlTemplate }}"
        commonEncryptionCenc:
          enabledProtocols:
            download: {{ download }}
            dash: {{ dash }}
            hls: {{ hls }}
            smoothStreaming: {{ smoothStreaming }}
          clearTracks:
            - trackSelections: "{{ trackSelections }}"
          contentKeys:
            defaultKey:
              label: "{{ label }}"
              policyName: "{{ policyName }}"
            keyToTrackMappings:
              - label: "{{ label }}"
                policyName: "{{ policyName }}"
                tracks: "{{ tracks }}"
          drm:
            playReady:
              customLicenseAcquisitionUrlTemplate: "{{ customLicenseAcquisitionUrlTemplate }}"
              playReadyCustomAttributes: "{{ playReadyCustomAttributes }}"
            widevine:
              customLicenseAcquisitionUrlTemplate: "{{ customLicenseAcquisitionUrlTemplate }}"
          clearKeyEncryptionConfiguration:
            customKeysAcquisitionUrlTemplate: "{{ customKeysAcquisitionUrlTemplate }}"
        commonEncryptionCbcs:
          enabledProtocols:
            download: {{ download }}
            dash: {{ dash }}
            hls: {{ hls }}
            smoothStreaming: {{ smoothStreaming }}
          clearTracks:
            - trackSelections: "{{ trackSelections }}"
          contentKeys:
            defaultKey:
              label: "{{ label }}"
              policyName: "{{ policyName }}"
            keyToTrackMappings:
              - label: "{{ label }}"
                policyName: "{{ policyName }}"
                tracks: "{{ tracks }}"
          drm:
            fairPlay:
              customLicenseAcquisitionUrlTemplate: "{{ customLicenseAcquisitionUrlTemplate }}"
              allowPersistentLicense: {{ allowPersistentLicense }}
            playReady:
              customLicenseAcquisitionUrlTemplate: "{{ customLicenseAcquisitionUrlTemplate }}"
              playReadyCustomAttributes: "{{ playReadyCustomAttributes }}"
            widevine:
              customLicenseAcquisitionUrlTemplate: "{{ customLicenseAcquisitionUrlTemplate }}"
          clearKeyEncryptionConfiguration:
            customKeysAcquisitionUrlTemplate: "{{ customKeysAcquisitionUrlTemplate }}"
        noEncryption:
          enabledProtocols:
            download: {{ download }}
            dash: {{ dash }}
            hls: {{ hls }}
            smoothStreaming: {{ smoothStreaming }}
`}</CodeBlock>

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

Delete a Streaming Policy. Deletes a Streaming Policy in the Media Services account.

```sql
DELETE FROM azure.media.streaming_policies
WHERE resource_group_name = '{{ resource_group_name }}' --required
AND account_name = '{{ account_name }}' --required
AND streaming_policy_name = '{{ streaming_policy_name }}' --required
AND subscription_id = '{{ subscription_id }}' --required
;
```
</TabItem>
</Tabs>
