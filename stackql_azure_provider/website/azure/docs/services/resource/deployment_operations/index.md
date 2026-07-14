--- 
title: deployment_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_operations
  - resource
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

Creates, updates, deletes, gets or lists a <code>deployment_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><CopyableCode code="deployment_operations" /></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource.deployment_operations" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_at_scope', value: 'get_at_scope' },
        { label: 'get_at_management_group_scope', value: 'get_at_management_group_scope' },
        { label: 'get_at_subscription_scope', value: 'get_at_subscription_scope' },
        { label: 'list_at_scope', value: 'list_at_scope' },
        { label: 'list_at_management_group_scope', value: 'list_at_management_group_scope' },
        { label: 'list_at_subscription_scope', value: 'list_at_subscription_scope' },
        { label: 'get_at_tenant_scope', value: 'get_at_tenant_scope' },
        { label: 'list_at_tenant_scope', value: 'list_at_tenant_scope' }
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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_scope">

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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_management_group_scope">

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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_subscription_scope">

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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_scope">

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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_management_group_scope">

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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_subscription_scope">

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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="get_at_tenant_scope">

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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="list_at_tenant_scope">

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
    <td>Full deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="duration" /></td>
    <td><code>string</code></td>
    <td>The duration of the operation.</td>
</tr>
<tr>
    <td><CopyableCode code="operationId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation ID.</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningOperation" /></td>
    <td><code>string</code></td>
    <td>The name of the current provisioning operation. Known values are: "NotSpecified", "Create", "Delete", "Waiting", "AzureAsyncOperationWaiting", "ResourceCacheWaiting", "Action", "Read", "EvaluateDeploymentOutput", and "DeploymentCleanup". (NotSpecified, Create, Delete, Waiting, AzureAsyncOperationWaiting, ResourceCacheWaiting, Action, Read, EvaluateDeploymentOutput, DeploymentCleanup)</td>
</tr>
<tr>
    <td><CopyableCode code="provisioningState" /></td>
    <td><code>string</code></td>
    <td>The state of the provisioning.</td>
</tr>
<tr>
    <td><CopyableCode code="request" /></td>
    <td><code>object</code></td>
    <td>The HTTP request message.</td>
</tr>
<tr>
    <td><CopyableCode code="response" /></td>
    <td><code>object</code></td>
    <td>The HTTP response message.</td>
</tr>
<tr>
    <td><CopyableCode code="serviceRequestId" /></td>
    <td><code>string</code></td>
    <td>Deployment operation service request id.</td>
</tr>
<tr>
    <td><CopyableCode code="statusCode" /></td>
    <td><code>string</code></td>
    <td>Operation status code from the resource provider. This property may not be set if a response has not yet been received.</td>
</tr>
<tr>
    <td><CopyableCode code="statusMessage" /></td>
    <td><code>object</code></td>
    <td>Operation status message from the resource provider. This property is optional. It will only be provided if an error was received from the resource provider.</td>
</tr>
<tr>
    <td><CopyableCode code="targetResource" /></td>
    <td><code>object</code></td>
    <td>The target resource.</td>
</tr>
<tr>
    <td><CopyableCode code="timestamp" /></td>
    <td><code>string (date-time)</code></td>
    <td>The date and time of the operation.</td>
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
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a deployments operation.</td>
</tr>
<tr>
    <td><a href="#list"><CopyableCode code="list" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-resource_group_name"><code>resource_group_name</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments operations for a deployment.</td>
</tr>
<tr>
    <td><a href="#get_at_scope"><CopyableCode code="get_at_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Gets a deployments operation.</td>
</tr>
<tr>
    <td><a href="#get_at_management_group_scope"><CopyableCode code="get_at_management_group_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Gets a deployments operation.</td>
</tr>
<tr>
    <td><a href="#get_at_subscription_scope"><CopyableCode code="get_at_subscription_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td></td>
    <td>Gets a deployments operation.</td>
</tr>
<tr>
    <td><a href="#list_at_scope"><CopyableCode code="list_at_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-scope"><code>scope</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments operations for a deployment.</td>
</tr>
<tr>
    <td><a href="#list_at_management_group_scope"><CopyableCode code="list_at_management_group_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-group_id"><code>group_id</code></a>, <a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments operations for a deployment.</td>
</tr>
<tr>
    <td><a href="#list_at_subscription_scope"><CopyableCode code="list_at_subscription_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-subscription_id"><code>subscription_id</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments operations for a deployment.</td>
</tr>
<tr>
    <td><a href="#get_at_tenant_scope"><CopyableCode code="get_at_tenant_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a>, <a href="#parameter-operation_id"><code>operation_id</code></a></td>
    <td></td>
    <td>Gets a deployments operation.</td>
</tr>
<tr>
    <td><a href="#list_at_tenant_scope"><CopyableCode code="list_at_tenant_scope" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-deployment_name"><code>deployment_name</code></a></td>
    <td><a href="#parameter-$top"><code>$top</code></a></td>
    <td>Gets all deployments operations for a deployment.</td>
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
<tr id="parameter-deployment_name">
    <td><CopyableCode code="deployment_name" /></td>
    <td><code>string</code></td>
    <td>The name of the deployment. Required.</td>
</tr>
<tr id="parameter-group_id">
    <td><CopyableCode code="group_id" /></td>
    <td><code>string</code></td>
    <td>The management group ID. Required.</td>
</tr>
<tr id="parameter-operation_id">
    <td><CopyableCode code="operation_id" /></td>
    <td><code>string</code></td>
    <td>The ID of the operation to get. Required.</td>
</tr>
<tr id="parameter-resource_group_name">
    <td><CopyableCode code="resource_group_name" /></td>
    <td><code>string</code></td>
    <td>The name of the resource group. The name is case insensitive. Required.</td>
</tr>
<tr id="parameter-scope">
    <td><CopyableCode code="scope" /></td>
    <td><code>string</code></td>
    <td>The fully qualified Azure Resource manager identifier of the resource. Required.</td>
</tr>
<tr id="parameter-subscription_id">
    <td><CopyableCode code="subscription_id" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr id="parameter-$top">
    <td><CopyableCode code="$top" /></td>
    <td><code>integer</code></td>
    <td>The number of results to return. Default value is None.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="get"
    values={[
        { label: 'get', value: 'get' },
        { label: 'list', value: 'list' },
        { label: 'get_at_scope', value: 'get_at_scope' },
        { label: 'get_at_management_group_scope', value: 'get_at_management_group_scope' },
        { label: 'get_at_subscription_scope', value: 'get_at_subscription_scope' },
        { label: 'list_at_scope', value: 'list_at_scope' },
        { label: 'list_at_management_group_scope', value: 'list_at_management_group_scope' },
        { label: 'list_at_subscription_scope', value: 'list_at_subscription_scope' },
        { label: 'get_at_tenant_scope', value: 'get_at_tenant_scope' },
        { label: 'list_at_tenant_scope', value: 'list_at_tenant_scope' }
    ]}
>
<TabItem value="get">

Gets a deployments operation.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list">

Gets all deployments operations for a deployment.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE resource_group_name = '{{ resource_group_name }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get_at_scope">

Gets a deployments operation.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE scope = '{{ scope }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_management_group_scope">

Gets a deployments operation.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE group_id = '{{ group_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
;
```
</TabItem>
<TabItem value="get_at_subscription_scope">

Gets a deployments operation.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE deployment_name = '{{ deployment_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
;
```
</TabItem>
<TabItem value="list_at_scope">

Gets all deployments operations for a deployment.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE scope = '{{ scope }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_at_management_group_scope">

Gets all deployments operations for a deployment.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE group_id = '{{ group_id }}' -- required
AND deployment_name = '{{ deployment_name }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="list_at_subscription_scope">

Gets all deployments operations for a deployment.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE deployment_name = '{{ deployment_name }}' -- required
AND subscription_id = '{{ subscription_id }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
<TabItem value="get_at_tenant_scope">

Gets a deployments operation.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE deployment_name = '{{ deployment_name }}' -- required
AND operation_id = '{{ operation_id }}' -- required
;
```
</TabItem>
<TabItem value="list_at_tenant_scope">

Gets all deployments operations for a deployment.

```sql
SELECT
id,
duration,
operationId,
provisioningOperation,
provisioningState,
request,
response,
serviceRequestId,
statusCode,
statusMessage,
targetResource,
timestamp
FROM azure.resource.deployment_operations
WHERE deployment_name = '{{ deployment_name }}' -- required
AND $top = '{{ $top }}'
;
```
</TabItem>
</Tabs>
