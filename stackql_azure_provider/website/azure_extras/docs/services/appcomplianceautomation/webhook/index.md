--- 
title: webhook
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook
  - appcomplianceautomation
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

Creates, updates, deletes, gets or lists a <code>webhook</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="webhook" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.appcomplianceautomation.webhook" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>content type. "application/json"</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryStatus" /></td>
    <td><code>string</code></td>
    <td>webhook deliveryStatus. Known values are: "Succeeded", "Failed", and "NotStarted".</td>
</tr>
<tr>
    <td><CopyableCode code="enableSslVerification" /></td>
    <td><code>string</code></td>
    <td>whether to enable ssl verification. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>under which event notification should be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="payloadUrl" /></td>
    <td><code>string</code></td>
    <td>webhook payload url.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Provisioning State. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Fixing", "Verifying", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="sendAllEvents" /></td>
    <td><code>string</code></td>
    <td>whether to send notification under any event. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Webhook status. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateWebhookKey" /></td>
    <td><code>string</code></td>
    <td>whether to update webhookKey. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="webhookId" /></td>
    <td><code>string</code></td>
    <td>Webhook id in database.</td>
</tr>
<tr>
    <td><CopyableCode code="webhookKey" /></td>
    <td><code>string</code></td>
    <td>webhook secret token. If not set, this field value is null; otherwise, please set a string value.</td>
</tr>
<tr>
    <td><CopyableCode code="webhookKeyEnabled" /></td>
    <td><code>string</code></td>
    <td>whether webhookKey is enabled. Known values are: "true" and "false".</td>
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
    <td>Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;. # pylint: disable=line-too-long</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="contentType" /></td>
    <td><code>string</code></td>
    <td>content type. "application/json"</td>
</tr>
<tr>
    <td><CopyableCode code="deliveryStatus" /></td>
    <td><code>string</code></td>
    <td>webhook deliveryStatus. Known values are: "Succeeded", "Failed", and "NotStarted".</td>
</tr>
<tr>
    <td><CopyableCode code="enableSslVerification" /></td>
    <td><code>string</code></td>
    <td>whether to enable ssl verification. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="events" /></td>
    <td><code>array</code></td>
    <td>under which event notification should be sent.</td>
</tr>
<tr>
    <td><CopyableCode code="payloadUrl" /></td>
    <td><code>string</code></td>
    <td>webhook payload url.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>Azure Resource Provisioning State. Known values are: "Succeeded", "Failed", "Canceled", "Creating", "Deleting", "Fixing", "Verifying", and "Updating".</td>
</tr>
<tr>
    <td><CopyableCode code="sendAllEvents" /></td>
    <td><code>string</code></td>
    <td>whether to send notification under any event. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>string</code></td>
    <td>Webhook status. Known values are: "Enabled" and "Disabled".</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="tenantId" /></td>
    <td><code>string</code></td>
    <td>Tenant id.</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts".</td>
</tr>
<tr>
    <td><CopyableCode code="updateWebhookKey" /></td>
    <td><code>string</code></td>
    <td>whether to update webhookKey. Known values are: "true" and "false".</td>
</tr>
<tr>
    <td><CopyableCode code="webhookId" /></td>
    <td><code>string</code></td>
    <td>Webhook id in database.</td>
</tr>
<tr>
    <td><CopyableCode code="webhookKey" /></td>
    <td><code>string</code></td>
    <td>webhook secret token. If not set, this field value is null; otherwise, please set a string value.</td>
</tr>
<tr>
    <td><CopyableCode code="webhookKeyEnabled" /></td>
    <td><code>string</code></td>
    <td>whether webhookKey is enabled. Known values are: "true" and "false".</td>
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
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-webhook_name"><code>webhook_name</code></a></td>
    <td></td>
    <td>Get the AppComplianceAutomation webhook and its properties.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a></td>
    <td><a href="#parameter-$skipToken"><code>$skipToken</code></a>, <a href="#parameter-$top"><code>$top</code></a>, <a href="#parameter-$select"><code>$select</code></a>, <a href="#parameter-$filter"><code>$filter</code></a>, <a href="#parameter-$orderby"><code>$orderby</code></a>, <a href="#parameter-offerGuid"><code>offerGuid</code></a>, <a href="#parameter-reportCreatorTenantId"><code>reportCreatorTenantId</code></a></td>
    <td>Get the AppComplianceAutomation webhook list.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-webhook_name"><code>webhook_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation webhook.</td>
</tr>
<tr>
    <td><a href="#update"><CopyableCode code="update" /></a></td>
    <td><CopyableCode code="update" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-webhook_name"><code>webhook_name</code></a></td>
    <td></td>
    <td>Update an exiting AppComplianceAutomation webhook.</td>
</tr>
<tr>
    <td><a href="#create_or_update"><CopyableCode code="create_or_update" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-webhook_name"><code>webhook_name</code></a>, <a href="#parameter-properties"><code>properties</code></a></td>
    <td></td>
    <td>Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation webhook.</td>
</tr>
<tr>
    <td><a href="#delete"><CopyableCode code="delete" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-report_name"><code>report_name</code></a>, <a href="#parameter-webhook_name"><code>webhook_name</code></a></td>
    <td></td>
    <td>Delete an AppComplianceAutomation webhook.</td>
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
<tr id="parameter-report_name">
    <td><CopyableCode code="report_name" /></td>
    <td><code>string</code></td>
    <td>Report Name. Required.</td>
</tr>
<tr id="parameter-webhook_name">
    <td><CopyableCode code="webhook_name" /></td>
    <td><code>string</code></td>
    <td>Webhook Name. Required.</td>
</tr>
<tr id="parameter-$filter">
    <td><CopyableCode code="$filter" /></td>
    <td><code>string</code></td>
    <td>The filter to apply on the operation. Default value is None.</td>
</tr>
<tr id="parameter-$orderby">
    <td><CopyableCode code="$orderby" /></td>
    <td><code>string</code></td>
    <td>OData order by query option. Default value is None.</td>
</tr>
<tr id="parameter-$select">
    <td><CopyableCode code="$select" /></td>
    <td><code>string</code></td>
    <td>OData Select statement. Limits the properties on each entry to just those requested, e.g. ?$select=reportName,id. Default value is None.</td>
</tr>
<tr id="parameter-$skipToken">
    <td><CopyableCode code="$skipToken" /></td>
    <td><code>string</code></td>
    <td>Skip over when retrieving results. Default value is None.</td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>Number of elements to return when retrieving results. Default value is None.</td>
</tr>
<tr id="parameter-offerGuid">
    <td><CopyableCode code="offerGuid" /></td>
    <td><code>string</code></td>
    <td>The offerGuid which mapping to the reports. Default value is None.</td>
</tr>
<tr id="parameter-reportCreatorTenantId">
    <td><CopyableCode code="reportCreatorTenantId" /></td>
    <td><code>string</code></td>
    <td>The tenant id of the report creator. Default value is None.</td>
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

Get the AppComplianceAutomation webhook and its properties.

```sql
SELECT
id,
name,
contentType,
deliveryStatus,
enableSslVerification,
events,
payloadUrl,
provisioningState,
sendAllEvents,
status,
systemData,
tenantId,
type,
updateWebhookKey,
webhookId,
webhookKey,
webhookKeyEnabled
FROM azure_extras.appcomplianceautomation.webhook
WHERE report_name = '{{ report_name }}' -- required
AND webhook_name = '{{ webhook_name }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get the AppComplianceAutomation webhook list.

```sql
SELECT
id,
name,
contentType,
deliveryStatus,
enableSslVerification,
events,
payloadUrl,
provisioningState,
sendAllEvents,
status,
systemData,
tenantId,
type,
updateWebhookKey,
webhookId,
webhookKey,
webhookKeyEnabled
FROM azure_extras.appcomplianceautomation.webhook
WHERE report_name = '{{ report_name }}' -- required
AND $skipToken = '{{ $skipToken }}'
AND $top = '{{ $top }}'
AND $select = '{{ $select }}'
AND $filter = '{{ $filter }}'
AND $orderby = '{{ $orderby }}'
AND offerGuid = '{{ offerGuid }}'
AND reportCreatorTenantId = '{{ reportCreatorTenantId }}'
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

Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation webhook.

```sql
INSERT INTO azure_extras.appcomplianceautomation.webhook (
properties,
report_name,
webhook_name
)
SELECT 
'{{ properties }}' /* required */,
'{{ report_name }}',
'{{ webhook_name }}'
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
- name: webhook
  props:
    - name: report_name
      value: "{{ report_name }}"
      description: Required parameter for the webhook resource.
    - name: webhook_name
      value: "{{ webhook_name }}"
      description: Required parameter for the webhook resource.
    - name: properties
      description: |
        Webhook property. Required.
      value:
        webhookId: "{{ webhookId }}"
        status: "{{ status }}"
        tenantId: "{{ tenantId }}"
        sendAllEvents: "{{ sendAllEvents }}"
        events:
          - "{{ events }}"
        payloadUrl: "{{ payloadUrl }}"
        contentType: "{{ contentType }}"
        webhookKey: "{{ webhookKey }}"
        updateWebhookKey: "{{ updateWebhookKey }}"
        webhookKeyEnabled: "{{ webhookKeyEnabled }}"
        enableSslVerification: "{{ enableSslVerification }}"
        deliveryStatus: "{{ deliveryStatus }}"
        provisioningState: "{{ provisioningState }}"
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

Update an exiting AppComplianceAutomation webhook.

```sql
UPDATE azure_extras.appcomplianceautomation.webhook
SET 
properties = '{{ properties }}'
WHERE 
report_name = '{{ report_name }}' --required
AND webhook_name = '{{ webhook_name }}' --required
RETURNING
id,
name,
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

Create a new AppComplianceAutomation webhook or update an exiting AppComplianceAutomation webhook.

```sql
REPLACE azure_extras.appcomplianceautomation.webhook
SET 
properties = '{{ properties }}'
WHERE 
report_name = '{{ report_name }}' --required
AND webhook_name = '{{ webhook_name }}' --required
AND properties = '{{ properties }}' --required
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
    defaultValue="delete"
    values={[
        { label: 'delete', value: 'delete' }
    ]}
>
<TabItem value="delete">

Delete an AppComplianceAutomation webhook.

```sql
DELETE FROM azure_extras.appcomplianceautomation.webhook
WHERE report_name = '{{ report_name }}' --required
AND webhook_name = '{{ webhook_name }}' --required
;
```
</TabItem>
</Tabs>
