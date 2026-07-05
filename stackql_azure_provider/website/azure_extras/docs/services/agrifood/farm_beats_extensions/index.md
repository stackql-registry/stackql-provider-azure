--- 
title: farm_beats_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - farm_beats_extensions
  - agrifood
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

Creates, updates, deletes, gets or lists a <code>farm_beats_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="farm_beats_extensions" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.agrifood.farm_beats_extensions" /></td></tr>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Textual description.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedInformation" /></td>
    <td><code>array</code></td>
    <td>Detailed information which shows summary of requested data. Used in descriptive get extension metadata call. Information for weather category per api included are apisSupported, customParameters, PlatformParameters and Units supported.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionApiDocsLink" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension api docs link.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionAuthLink" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension auth link.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionCategory" /></td>
    <td><code>string</code></td>
    <td>Category of the extension. e.g. weather/sensor/satellite.</td>
</tr>
<tr>
    <td><CopyableCode code="farmBeatsExtensionId" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension ID.</td>
</tr>
<tr>
    <td><CopyableCode code="farmBeatsExtensionName" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension name.</td>
</tr>
<tr>
    <td><CopyableCode code="farmBeatsExtensionVersion" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension version.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherId" /></td>
    <td><code>string</code></td>
    <td>Publisher ID.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceType" /></td>
    <td><code>string</code></td>
    <td>Target ResourceType of the farmBeatsExtension.</td>
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
    <td>Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;".</td>
</tr>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource.</td>
</tr>
<tr>
    <td><CopyableCode code="description" /></td>
    <td><code>string</code></td>
    <td>Textual description.</td>
</tr>
<tr>
    <td><CopyableCode code="detailedInformation" /></td>
    <td><code>array</code></td>
    <td>Detailed information which shows summary of requested data. Used in descriptive get extension metadata call. Information for weather category per api included are apisSupported, customParameters, PlatformParameters and Units supported.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionApiDocsLink" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension api docs link.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionAuthLink" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension auth link.</td>
</tr>
<tr>
    <td><CopyableCode code="extensionCategory" /></td>
    <td><code>string</code></td>
    <td>Category of the extension. e.g. weather/sensor/satellite.</td>
</tr>
<tr>
    <td><CopyableCode code="farmBeatsExtensionId" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension ID.</td>
</tr>
<tr>
    <td><CopyableCode code="farmBeatsExtensionName" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension name.</td>
</tr>
<tr>
    <td><CopyableCode code="farmBeatsExtensionVersion" /></td>
    <td><code>string</code></td>
    <td>FarmBeatsExtension version.</td>
</tr>
<tr>
    <td><CopyableCode code="publisherId" /></td>
    <td><code>string</code></td>
    <td>Publisher ID.</td>
</tr>
<tr>
    <td><CopyableCode code="systemData" /></td>
    <td><code>object</code></td>
    <td>Azure Resource Manager metadata containing createdBy and modifiedBy information.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResourceType" /></td>
    <td><code>string</code></td>
    <td>Target ResourceType of the farmBeatsExtension.</td>
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
    <td><a href="#parameter-farm_beats_extension_id"><code>farm_beats_extension_id</code></a></td>
    <td></td>
    <td>Get farmBeats extension.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td></td>
    <td><a href="#parameter-$maxPageSize"><code>$maxPageSize</code></a></td>
    <td>Get list of farmBeats extension.</td>
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
<tr id="parameter-farm_beats_extension_id">
    <td><CopyableCode code="farm_beats_extension_id" /></td>
    <td><code>string</code></td>
    <td>farmBeatsExtensionId to be queried. Required.</td>
</tr>
<tr id="parameter-$maxPageSize">
    <td><CopyableCode code="$maxPageSize" /></td>
    <td><code>integer</code></td>
    <td>Maximum number of items needed (inclusive). Minimum = 10, Maximum = 1000, Default value = 50. Default value is 50.</td>
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

Get farmBeats extension.

```sql
SELECT
id,
name,
description,
detailedInformation,
extensionApiDocsLink,
extensionAuthLink,
extensionCategory,
farmBeatsExtensionId,
farmBeatsExtensionName,
farmBeatsExtensionVersion,
publisherId,
systemData,
targetResourceType,
type
FROM azure_extras.agrifood.farm_beats_extensions
WHERE farm_beats_extension_id = '{{ farm_beats_extension_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Get list of farmBeats extension.

```sql
SELECT
id,
name,
description,
detailedInformation,
extensionApiDocsLink,
extensionAuthLink,
extensionCategory,
farmBeatsExtensionId,
farmBeatsExtensionName,
farmBeatsExtensionVersion,
publisherId,
systemData,
targetResourceType,
type
FROM azure_extras.agrifood.farm_beats_extensions
WHERE $maxPageSize = '{{ $maxPageSize }}'
;
```
</TabItem>
</Tabs>
