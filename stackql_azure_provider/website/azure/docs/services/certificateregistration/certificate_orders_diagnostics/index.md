--- 
title: certificate_orders_diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_orders_diagnostics
  - certificateregistration
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

Creates, updates, deletes, gets or lists a <code>certificate_orders_diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="certificate_orders_diagnostics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.certificateregistration.certificate_orders_diagnostics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_app_service_certificate_order_detector_response"
    values={[
        { label: 'get_app_service_certificate_order_detector_response', value: 'get_app_service_certificate_order_detector_response' },
        { label: 'list_app_service_certificate_order_detector_response', value: 'list_app_service_certificate_order_detector_response' }
    ]}
>
<TabItem value="get_app_service_certificate_order_detector_response">

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
    <td><CopyableCode code="dataProvidersMetadata" /></td>
    <td><code>array</code></td>
    <td>Additional configuration for different data providers to be used by the UI.</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>array</code></td>
    <td>Data Set.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>metadata for the detector.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Indicates status of the most severe insight.</td>
</tr>
<tr>
    <td><CopyableCode code="suggestedUtterances" /></td>
    <td><code>object</code></td>
    <td>Suggested utterances where the detector can be applicable.</td>
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
<TabItem value="list_app_service_certificate_order_detector_response">

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
    <td><CopyableCode code="dataProvidersMetadata" /></td>
    <td><code>array</code></td>
    <td>Additional configuration for different data providers to be used by the UI.</td>
</tr>
<tr>
    <td><CopyableCode code="dataset" /></td>
    <td><code>array</code></td>
    <td>Data Set.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="metadata" /></td>
    <td><code>object</code></td>
    <td>metadata for the detector.</td>
</tr>
<tr>
    <td><CopyableCode code="status" /></td>
    <td><code>object</code></td>
    <td>Indicates status of the most severe insight.</td>
</tr>
<tr>
    <td><CopyableCode code="suggestedUtterances" /></td>
    <td><code>object</code></td>
    <td>Suggested utterances where the detector can be applicable.</td>
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
    <td><a href="#get_app_service_certificate_order_detector_response"><CopyableCode code="get_app_service_certificate_order_detector_response" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-timeGrain"><code>timeGrain</code></a></td>
    <td>Microsoft.CertificateRegistration call to get a detector response from App Lens. Description for Microsoft.CertificateRegistration call to get a detector response from App Lens.</td>
</tr>
<tr>
    <td><a href="#list_app_service_certificate_order_detector_response"><CopyableCode code="list_app_service_certificate_order_detector_response" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-certificate_order_name"><code>certificate_order_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Microsoft.CertificateRegistration to get the list of detectors for this RP. Description for Microsoft.CertificateRegistration to get the list of detectors for this RP.</td>
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
<tr id="parameter-certificate_order_name">
    <td><CopyableCode code="certificate_order_name" /></td>
    <td><code>string</code></td>
    <td>Name of the certificate order.. Required.</td>
</tr>
<tr id="parameter-detector_name">
    <td><CopyableCode code="detector_name" /></td>
    <td><code>string</code></td>
    <td>The detector name which needs to be run. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-endTime">
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The end time for the detector response. Default value is None.</td>
</tr>
<tr id="parameter-startTime">
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>The start time for detector response. Default value is None.</td>
</tr>
<tr id="parameter-timeGrain">
    <td><CopyableCode code="timeGrain" /></td>
    <td><code>string</code></td>
    <td>The time grain for the detector response. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_app_service_certificate_order_detector_response"
    values={[
        { label: 'get_app_service_certificate_order_detector_response', value: 'get_app_service_certificate_order_detector_response' },
        { label: 'list_app_service_certificate_order_detector_response', value: 'list_app_service_certificate_order_detector_response' }
    ]}
>
<TabItem value="get_app_service_certificate_order_detector_response">

Microsoft.CertificateRegistration call to get a detector response from App Lens. Description for Microsoft.CertificateRegistration call to get a detector response from App Lens.

```sql
SELECT
id,
name,
dataProvidersMetadata,
dataset,
kind,
metadata,
status,
suggestedUtterances,
systemData,
type
FROM azure.certificateregistration.certificate_orders_diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND certificate_order_name = '{{ certificate_order_name }}' -- required
AND detector_name = '{{ detector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND startTime = '{{ startTime }}'
AND endTime = '{{ endTime }}'
AND timeGrain = '{{ timeGrain }}'
;
```
</TabItem>
<TabItem value="list_app_service_certificate_order_detector_response">

Microsoft.CertificateRegistration to get the list of detectors for this RP. Description for Microsoft.CertificateRegistration to get the list of detectors for this RP.

```sql
SELECT
id,
name,
dataProvidersMetadata,
dataset,
kind,
metadata,
status,
suggestedUtterances,
systemData,
type
FROM azure.certificateregistration.certificate_orders_diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND certificate_order_name = '{{ certificate_order_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>
