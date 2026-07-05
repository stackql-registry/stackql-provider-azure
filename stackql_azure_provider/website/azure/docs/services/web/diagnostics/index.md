--- 
title: diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics
  - web
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

Creates, updates, deletes, gets or lists a <code>diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="diagnostics" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web.diagnostics" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get_site_analysis_slot"
    values={[
        { label: 'get_site_analysis_slot', value: 'get_site_analysis_slot' },
        { label: 'get_site_detector_slot', value: 'get_site_detector_slot' },
        { label: 'list_site_analyses_slot', value: 'list_site_analyses_slot' },
        { label: 'get_site_detector_response_slot', value: 'get_site_detector_response_slot' },
        { label: 'get_site_analysis', value: 'get_site_analysis' },
        { label: 'get_site_detector', value: 'get_site_detector' },
        { label: 'list_site_detector_responses_slot', value: 'list_site_detector_responses_slot' },
        { label: 'list_site_analyses', value: 'list_site_analyses' },
        { label: 'get_site_detector_response', value: 'get_site_detector_response' },
        { label: 'get_hosting_environment_detector_response', value: 'get_hosting_environment_detector_response' },
        { label: 'list_site_detector_responses', value: 'list_site_detector_responses' },
        { label: 'list_hosting_environment_detector_responses', value: 'list_hosting_environment_detector_responses' }
    ]}
>
<TabItem value="get_site_analysis_slot">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the Analysis.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<TabItem value="get_site_detector_slot">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the detector.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the detector.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag representing whether detector is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="rank" /></td>
    <td><code>number</code></td>
    <td>Detector Rank.</td>
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
<TabItem value="list_site_analyses_slot">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the Analysis.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<TabItem value="get_site_detector_response_slot">

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
<TabItem value="get_site_analysis">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the Analysis.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<TabItem value="get_site_detector">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the detector.</td>
</tr>
<tr>
    <td><CopyableCode code="displayName" /></td>
    <td><code>string</code></td>
    <td>Display name of the detector.</td>
</tr>
<tr>
    <td><CopyableCode code="isEnabled" /></td>
    <td><code>boolean</code></td>
    <td>Flag representing whether detector is enabled or not.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
</tr>
<tr>
    <td><CopyableCode code="rank" /></td>
    <td><code>number</code></td>
    <td>Detector Rank.</td>
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
<TabItem value="list_site_detector_responses_slot">

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
<TabItem value="list_site_analyses">

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
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Description of the Analysis.</td>
</tr>
<tr>
    <td><CopyableCode code="kind" /></td>
    <td><code>string</code></td>
    <td>Kind of resource.</td>
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
<TabItem value="get_site_detector_response">

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
<TabItem value="get_hosting_environment_detector_response">

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
<TabItem value="list_site_detector_responses">

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
<TabItem value="list_hosting_environment_detector_responses">

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
    <td><a href="#get_site_analysis_slot"><CopyableCode code="get_site_analysis_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-analysis_name"><code>analysis_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Site Analysis. Description for Get Site Analysis.</td>
</tr>
<tr>
    <td><a href="#get_site_detector_slot"><CopyableCode code="get_site_detector_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Detector. Description for Get Detector.</td>
</tr>
<tr>
    <td><a href="#list_site_analyses_slot"><CopyableCode code="list_site_analyses_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Site Analyses. Description for Get Site Analyses.</td>
</tr>
<tr>
    <td><a href="#get_site_detector_response_slot"><CopyableCode code="get_site_detector_response_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-timeGrain"><code>timeGrain</code></a></td>
    <td>Get site detector response. Description for Get site detector response.</td>
</tr>
<tr>
    <td><a href="#get_site_analysis"><CopyableCode code="get_site_analysis" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-analysis_name"><code>analysis_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Site Analysis. Description for Get Site Analysis.</td>
</tr>
<tr>
    <td><a href="#get_site_detector"><CopyableCode code="get_site_detector" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Detector. Description for Get Detector.</td>
</tr>
<tr>
    <td><a href="#list_site_detector_responses_slot"><CopyableCode code="list_site_detector_responses_slot" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Site Detector Responses. Description for List Site Detector Responses.</td>
</tr>
<tr>
    <td><a href="#list_site_analyses"><CopyableCode code="list_site_analyses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Site Analyses. Description for Get Site Analyses.</td>
</tr>
<tr>
    <td><a href="#get_site_detector_response"><CopyableCode code="get_site_detector_response" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-timeGrain"><code>timeGrain</code></a></td>
    <td>Get site detector response. Description for Get site detector response.</td>
</tr>
<tr>
    <td><a href="#get_hosting_environment_detector_response"><CopyableCode code="get_hosting_environment_detector_response" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-timeGrain"><code>timeGrain</code></a></td>
    <td>Get Hosting Environment Detector Response. Description for Get Hosting Environment Detector Response.</td>
</tr>
<tr>
    <td><a href="#list_site_detector_responses"><CopyableCode code="list_site_detector_responses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Site Detector Responses. Description for List Site Detector Responses.</td>
</tr>
<tr>
    <td><a href="#list_hosting_environment_detector_responses"><CopyableCode code="list_hosting_environment_detector_responses" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-name"><code>name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>List Hosting Environment Detector Responses. Description for List Hosting Environment Detector Responses.</td>
</tr>
<tr>
    <td><a href="#list_site_diagnostic_categories"><CopyableCode code="list_site_diagnostic_categories" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Diagnostics Categories. Description for Get Diagnostics Categories.</td>
</tr>
<tr>
    <td><a href="#list_site_diagnostic_categories_slot"><CopyableCode code="list_site_diagnostic_categories_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Diagnostics Categories. Description for Get Diagnostics Categories.</td>
</tr>
<tr>
    <td><a href="#list_site_detectors"><CopyableCode code="list_site_detectors" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Detectors. Description for Get Detectors.</td>
</tr>
<tr>
    <td><a href="#list_site_detectors_slot"><CopyableCode code="list_site_detectors_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Detectors. Description for Get Detectors.</td>
</tr>
<tr>
    <td><a href="#get_site_diagnostic_category"><CopyableCode code="get_site_diagnostic_category" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Diagnostics Category. Description for Get Diagnostics Category.</td>
</tr>
<tr>
    <td><a href="#get_site_diagnostic_category_slot"><CopyableCode code="get_site_diagnostic_category_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Get Diagnostics Category. Description for Get Diagnostics Category.</td>
</tr>
<tr>
    <td><a href="#execute_site_analysis"><CopyableCode code="execute_site_analysis" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-analysis_name"><code>analysis_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-timeGrain"><code>timeGrain</code></a></td>
    <td>Execute Analysis. Description for Execute Analysis.</td>
</tr>
<tr>
    <td><a href="#execute_site_analysis_slot"><CopyableCode code="execute_site_analysis_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-analysis_name"><code>analysis_name</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-timeGrain"><code>timeGrain</code></a></td>
    <td>Execute Analysis. Description for Execute Analysis.</td>
</tr>
<tr>
    <td><a href="#execute_site_detector"><CopyableCode code="execute_site_detector" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-timeGrain"><code>timeGrain</code></a></td>
    <td>Execute Detector. Description for Execute Detector.</td>
</tr>
<tr>
    <td><a href="#execute_site_detector_slot"><CopyableCode code="execute_site_detector_slot" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-site_name"><code>site_name</code></a>, <a href="#parameter-detector_name"><code>detector_name</code></a>, <a href="#parameter-diagnostic_category"><code>diagnostic_category</code></a>, <a href="#parameter-slot"><code>slot</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-startTime"><code>startTime</code></a>, <a href="#parameter-endTime"><code>endTime</code></a>, <a href="#parameter-timeGrain"><code>timeGrain</code></a></td>
    <td>Execute Detector. Description for Execute Detector.</td>
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
<tr id="parameter-analysis_name">
    <td><CopyableCode code="analysis_name" /></td>
    <td><code>string</code></td>
    <td>Analysis Name. Required.</td>
</tr>
<tr id="parameter-detector_name">
    <td><CopyableCode code="detector_name" /></td>
    <td><code>string</code></td>
    <td>Detector Name. Required.</td>
</tr>
<tr id="parameter-diagnostic_category">
    <td><CopyableCode code="diagnostic_category" /></td>
    <td><code>string</code></td>
    <td>Diagnostic Category. Required.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>App Service Environment Name. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-site_name">
    <td><CopyableCode code="site_name" /></td>
    <td><code>string</code></td>
    <td>Site Name. Required.</td>
</tr>
<tr id="parameter-slot">
    <td><CopyableCode code="slot" /></td>
    <td><code>string</code></td>
    <td>Slot Name. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-endTime">
    <td><CopyableCode code="endTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>End Time. Default value is None.</td>
</tr>
<tr id="parameter-startTime">
    <td><CopyableCode code="startTime" /></td>
    <td><code>string (date-time)</code></td>
    <td>Start Time. Default value is None.</td>
</tr>
<tr id="parameter-timeGrain">
    <td><CopyableCode code="timeGrain" /></td>
    <td><code>string</code></td>
    <td>Time Grain. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get_site_analysis_slot"
    values={[
        { label: 'get_site_analysis_slot', value: 'get_site_analysis_slot' },
        { label: 'get_site_detector_slot', value: 'get_site_detector_slot' },
        { label: 'list_site_analyses_slot', value: 'list_site_analyses_slot' },
        { label: 'get_site_detector_response_slot', value: 'get_site_detector_response_slot' },
        { label: 'get_site_analysis', value: 'get_site_analysis' },
        { label: 'get_site_detector', value: 'get_site_detector' },
        { label: 'list_site_detector_responses_slot', value: 'list_site_detector_responses_slot' },
        { label: 'list_site_analyses', value: 'list_site_analyses' },
        { label: 'get_site_detector_response', value: 'get_site_detector_response' },
        { label: 'get_hosting_environment_detector_response', value: 'get_hosting_environment_detector_response' },
        { label: 'list_site_detector_responses', value: 'list_site_detector_responses' },
        { label: 'list_hosting_environment_detector_responses', value: 'list_hosting_environment_detector_responses' }
    ]}
>
<TabItem value="get_site_analysis_slot">

Get Site Analysis. Description for Get Site Analysis.

```sql
SELECT
id,
name,
description,
kind,
systemData,
type
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND diagnostic_category = '{{ diagnostic_category }}' -- required
AND analysis_name = '{{ analysis_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_detector_slot">

Get Detector. Description for Get Detector.

```sql
SELECT
id,
name,
description,
displayName,
isEnabled,
kind,
rank,
systemData,
type
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND diagnostic_category = '{{ diagnostic_category }}' -- required
AND detector_name = '{{ detector_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_site_analyses_slot">

Get Site Analyses. Description for Get Site Analyses.

```sql
SELECT
id,
name,
description,
kind,
systemData,
type
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND diagnostic_category = '{{ diagnostic_category }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_detector_response_slot">

Get site detector response. Description for Get site detector response.

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
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND detector_name = '{{ detector_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND startTime = '{{ startTime }}'
AND endTime = '{{ endTime }}'
AND timeGrain = '{{ timeGrain }}'
;
```
</TabItem>
<TabItem value="get_site_analysis">

Get Site Analysis. Description for Get Site Analysis.

```sql
SELECT
id,
name,
description,
kind,
systemData,
type
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND diagnostic_category = '{{ diagnostic_category }}' -- required
AND analysis_name = '{{ analysis_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_detector">

Get Detector. Description for Get Detector.

```sql
SELECT
id,
name,
description,
displayName,
isEnabled,
kind,
rank,
systemData,
type
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND diagnostic_category = '{{ diagnostic_category }}' -- required
AND detector_name = '{{ detector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_site_detector_responses_slot">

List Site Detector Responses. Description for List Site Detector Responses.

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
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND slot = '{{ slot }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_site_analyses">

Get Site Analyses. Description for Get Site Analyses.

```sql
SELECT
id,
name,
description,
kind,
systemData,
type
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND diagnostic_category = '{{ diagnostic_category }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="get_site_detector_response">

Get site detector response. Description for Get site detector response.

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
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND detector_name = '{{ detector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND startTime = '{{ startTime }}'
AND endTime = '{{ endTime }}'
AND timeGrain = '{{ timeGrain }}'
;
```
</TabItem>
<TabItem value="get_hosting_environment_detector_response">

Get Hosting Environment Detector Response. Description for Get Hosting Environment Detector Response.

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
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND detector_name = '{{ detector_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND startTime = '{{ startTime }}'
AND endTime = '{{ endTime }}'
AND timeGrain = '{{ timeGrain }}'
;
```
</TabItem>
<TabItem value="list_site_detector_responses">

List Site Detector Responses. Description for List Site Detector Responses.

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
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND site_name = '{{ site_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_hosting_environment_detector_responses">

List Hosting Environment Detector Responses. Description for List Hosting Environment Detector Responses.

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
FROM azure.web.diagnostics
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND name = '{{ name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="list_site_diagnostic_categories"
    values={[
        { label: 'list_site_diagnostic_categories', value: 'list_site_diagnostic_categories' },
        { label: 'list_site_diagnostic_categories_slot', value: 'list_site_diagnostic_categories_slot' },
        { label: 'list_site_detectors', value: 'list_site_detectors' },
        { label: 'list_site_detectors_slot', value: 'list_site_detectors_slot' },
        { label: 'get_site_diagnostic_category', value: 'get_site_diagnostic_category' },
        { label: 'get_site_diagnostic_category_slot', value: 'get_site_diagnostic_category_slot' },
        { label: 'execute_site_analysis', value: 'execute_site_analysis' },
        { label: 'execute_site_analysis_slot', value: 'execute_site_analysis_slot' },
        { label: 'execute_site_detector', value: 'execute_site_detector' },
        { label: 'execute_site_detector_slot', value: 'execute_site_detector_slot' }
    ]}
>
<TabItem value="list_site_diagnostic_categories">

Get Diagnostics Categories. Description for Get Diagnostics Categories.

```sql
EXEC azure.web.diagnostics.list_site_diagnostic_categories 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_diagnostic_categories_slot">

Get Diagnostics Categories. Description for Get Diagnostics Categories.

```sql
EXEC azure.web.diagnostics.list_site_diagnostic_categories_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_detectors">

Get Detectors. Description for Get Detectors.

```sql
EXEC azure.web.diagnostics.list_site_detectors 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@diagnostic_category='{{ diagnostic_category }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="list_site_detectors_slot">

Get Detectors. Description for Get Detectors.

```sql
EXEC azure.web.diagnostics.list_site_detectors_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@diagnostic_category='{{ diagnostic_category }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_site_diagnostic_category">

Get Diagnostics Category. Description for Get Diagnostics Category.

```sql
EXEC azure.web.diagnostics.get_site_diagnostic_category 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@diagnostic_category='{{ diagnostic_category }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="get_site_diagnostic_category_slot">

Get Diagnostics Category. Description for Get Diagnostics Category.

```sql
EXEC azure.web.diagnostics.get_site_diagnostic_category_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@diagnostic_category='{{ diagnostic_category }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required
;
```
</TabItem>
<TabItem value="execute_site_analysis">

Execute Analysis. Description for Execute Analysis.

```sql
EXEC azure.web.diagnostics.execute_site_analysis 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@diagnostic_category='{{ diagnostic_category }}' --required, 
@analysis_name='{{ analysis_name }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@startTime='{{ startTime }}', 
@endTime='{{ endTime }}', 
@timeGrain='{{ timeGrain }}'
;
```
</TabItem>
<TabItem value="execute_site_analysis_slot">

Execute Analysis. Description for Execute Analysis.

```sql
EXEC azure.web.diagnostics.execute_site_analysis_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@diagnostic_category='{{ diagnostic_category }}' --required, 
@analysis_name='{{ analysis_name }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@startTime='{{ startTime }}', 
@endTime='{{ endTime }}', 
@timeGrain='{{ timeGrain }}'
;
```
</TabItem>
<TabItem value="execute_site_detector">

Execute Detector. Description for Execute Detector.

```sql
EXEC azure.web.diagnostics.execute_site_detector 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@detector_name='{{ detector_name }}' --required, 
@diagnostic_category='{{ diagnostic_category }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@startTime='{{ startTime }}', 
@endTime='{{ endTime }}', 
@timeGrain='{{ timeGrain }}'
;
```
</TabItem>
<TabItem value="execute_site_detector_slot">

Execute Detector. Description for Execute Detector.

```sql
EXEC azure.web.diagnostics.execute_site_detector_slot 
@resource_group_name='{{ resource_group_name }}' --required, 
@site_name='{{ site_name }}' --required, 
@detector_name='{{ detector_name }}' --required, 
@diagnostic_category='{{ diagnostic_category }}' --required, 
@slot='{{ slot }}' --required, 
@subscription_id='{{ subscription_id }}' --required, 
@startTime='{{ startTime }}', 
@endTime='{{ endTime }}', 
@timeGrain='{{ timeGrain }}'
;
```
</TabItem>
</Tabs>
