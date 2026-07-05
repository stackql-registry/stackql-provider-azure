--- 
title: defender_for_storage
hide_title: false
hide_table_of_contents: false
keywords:
  - defender_for_storage
  - security
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

Creates, updates, deletes, gets or lists a <code>defender_for_storage</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="defender_for_storage" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.defender_for_storage" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_malware_scan"
    values={[
        { label: 'get_malware_scan', value: 'get_malware_scan' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_malware_scan">

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
    <td><CopyableCode code="scanEndTime" /></td>
    <td><code>string</code></td>
    <td>The time at which the scan has ended. Only available for a scan which has terminated.</td>
</tr>
<tr>
    <td><CopyableCode code="scanId" /></td>
    <td><code>string</code></td>
    <td>The identifier of the scan.</td>
</tr>
<tr>
    <td><CopyableCode code="scanStartTime" /></td>
    <td><code>string</code></td>
    <td>The time at which the scan had been initiated.</td>
</tr>
<tr>
    <td><CopyableCode code="scanStatus" /></td>
    <td><code>string</code></td>
    <td>A status code of the scan operation.</td>
</tr>
<tr>
    <td><CopyableCode code="scanStatusMessage" /></td>
    <td><code>string</code></td>
    <td>A description of the status of the scan.</td>
</tr>
<tr>
    <td><CopyableCode code="scanSummary" /></td>
    <td><code>object</code></td>
    <td>A summary of the scan results.</td>
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
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether Defender for Storage is enabled on this storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="malwareScanning" /></td>
    <td><code>object</code></td>
    <td>Properties of Malware Scanning.</td>
</tr>
<tr>
    <td><CopyableCode code="overrideSubscriptionLevelSettings" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the settings defined for this storage account should override the settings defined for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="sensitiveDataDiscovery" /></td>
    <td><code>object</code></td>
    <td>Properties of Sensitive Data Discovery.</td>
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
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether Defender for Storage is enabled on this storage account.</td>
</tr>
<tr>
    <td><CopyableCode code="malwareScanning" /></td>
    <td><code>object</code></td>
    <td>Properties of Malware Scanning.</td>
</tr>
<tr>
    <td><CopyableCode code="overrideSubscriptionLevelSettings" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the settings defined for this storage account should override the settings defined for the subscription.</td>
</tr>
<tr>
    <td><CopyableCode code="sensitiveDataDiscovery" /></td>
    <td><code>object</code></td>
    <td>Properties of Sensitive Data Discovery.</td>
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
    <td><a href="#get_malware_scan"><CopyableCode code="get_malware_scan" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-setting_name"><code>setting_name</code></a>, <a href="#parameter-scan_id"><code>scan_id</code></a></td>
    <td></td>
    <td>Gets the Defender for Storage malware scan for the specified storage resource.</td>
</tr>
<tr>
    <td><a href="#get"><CopyableCode code="get" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-setting_name"><code>setting_name</code></a></td>
    <td></td>
    <td>Gets the Defender for Storage settings for the specified storage account.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a></td>
    <td></td>
    <td>Lists the Defender for Storage settings for the specified storage account.</td>
</tr>
<tr>
    <td><a href="#create"><CopyableCode code="create" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-setting_name"><code>setting_name</code></a></td>
    <td></td>
    <td>Creates or updates the Defender for Storage settings on a specified storage account.</td>
</tr>
<tr>
    <td><a href="#start_malware_scan"><CopyableCode code="start_malware_scan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-setting_name"><code>setting_name</code></a></td>
    <td></td>
    <td>Initiate a Defender for Storage malware scan for the specified storage account. Blobs and Files will be scanned for malware.</td>
</tr>
<tr>
    <td><a href="#cancel_malware_scan"><CopyableCode code="cancel_malware_scan" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_id"><code>resource_id</code></a>, <a href="#parameter-setting_name"><code>setting_name</code></a>, <a href="#parameter-scan_id"><code>scan_id</code></a></td>
    <td></td>
    <td>Cancels a Defender for Storage malware scan for the specified storage account.</td>
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
<tr id="parameter-resource_id">
    <td><CopyableCode code="resource_id" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-scan_id">
    <td><CopyableCode code="scan_id" /></td>
    <td><code>string</code></td>
    <td>The identifier of the scan. Can be either 'latest' or a GUID. Required.</td>
</tr>
<tr id="parameter-setting_name">
    <td><CopyableCode code="setting_name" /></td>
    <td><code>string</code></td>
    <td>The defender for storage setting name. Known values are: "MCAS", "WDATP", "WDATP_EXCLUDE_LINUX_PUBLIC_PREVIEW", "WDATP_UNIFIED_SOLUTION", "Sentinel", and "current". Required.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_malware_scan"
    values={[
        { label: 'get_malware_scan', value: 'get_malware_scan' },
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' }
    ]}
>
<TabItem value="get_malware_scan">

Gets the Defender for Storage malware scan for the specified storage resource.

```sql
SELECT
scanEndTime,
scanId,
scanStartTime,
scanStatus,
scanStatusMessage,
scanSummary
FROM azure.security.defender_for_storage
WHERE resource_id = '{{ resource_id }}' -- required
AND setting_name = '{{ setting_name }}' -- required
AND scan_id = '{{ scan_id }}' -- required
;
```
</TabItem>
<TabItem value="get">

Gets the Defender for Storage settings for the specified storage account.

```sql
SELECT
id,
name,
isEnabled,
malwareScanning,
overrideSubscriptionLevelSettings,
sensitiveDataDiscovery,
systemData,
type
FROM azure.security.defender_for_storage
WHERE resource_id = '{{ resource_id }}' -- required
AND setting_name = '{{ setting_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Lists the Defender for Storage settings for the specified storage account.

```sql
SELECT
id,
name,
isEnabled,
malwareScanning,
overrideSubscriptionLevelSettings,
sensitiveDataDiscovery,
systemData,
type
FROM azure.security.defender_for_storage
WHERE resource_id = '{{ resource_id }}' -- required
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

Creates or updates the Defender for Storage settings on a specified storage account.

```sql
INSERT INTO azure.security.defender_for_storage (
properties,
resource_id,
setting_name
)
SELECT 
'{{ properties }}',
'{{ resource_id }}',
'{{ setting_name }}'
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
- name: defender_for_storage
  props:
    - name: resource_id
      value: "{{ resource_id }}"
      description: Required parameter for the defender_for_storage resource.
    - name: setting_name
      value: "{{ setting_name }}"
      description: Required parameter for the defender_for_storage resource.
    - name: properties
      description: |
        Defender for Storage resource properties.
      value:
        isEnabled: {{ isEnabled }}
        malwareScanning:
          onUpload:
            isEnabled: {{ isEnabled }}
            capGBPerMonth: {{ capGBPerMonth }}
            filters:
              excludeBlobsWithPrefix:
                - "{{ excludeBlobsWithPrefix }}"
              excludeBlobsWithSuffix:
                - "{{ excludeBlobsWithSuffix }}"
              excludeBlobsLargerThan: "{{ excludeBlobsLargerThan }}"
          scanResultsEventGridTopicResourceId: "{{ scanResultsEventGridTopicResourceId }}"
          blobScanResultsOptions: "{{ blobScanResultsOptions }}"
          automatedResponse: "{{ automatedResponse }}"
          operationStatus:
            code: "{{ code }}"
            message: "{{ message }}"
        sensitiveDataDiscovery:
          isEnabled: {{ isEnabled }}
          operationStatus:
            code: "{{ code }}"
            message: "{{ message }}"
        overrideSubscriptionLevelSettings: {{ overrideSubscriptionLevelSettings }}
`}</CodeBlock>

</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="start_malware_scan"
    values={[
        { label: 'start_malware_scan', value: 'start_malware_scan' },
        { label: 'cancel_malware_scan', value: 'cancel_malware_scan' }
    ]}
>
<TabItem value="start_malware_scan">

Initiate a Defender for Storage malware scan for the specified storage account. Blobs and Files will be scanned for malware.

```sql
EXEC azure.security.defender_for_storage.start_malware_scan 
@resource_id='{{ resource_id }}' --required, 
@setting_name='{{ setting_name }}' --required
;
```
</TabItem>
<TabItem value="cancel_malware_scan">

Cancels a Defender for Storage malware scan for the specified storage account.

```sql
EXEC azure.security.defender_for_storage.cancel_malware_scan 
@resource_id='{{ resource_id }}' --required, 
@setting_name='{{ setting_name }}' --required, 
@scan_id='{{ scan_id }}' --required
;
```
</TabItem>
</Tabs>
